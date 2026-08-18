#!/usr/bin/env python3
"""Dependency-free catalog, search, validation, and evidence tooling for Booster."""

from __future__ import annotations

import argparse
import ast
import datetime as dt
import fcntl
import hashlib
import json
import os
import re
import shlex
import subprocess
import sys
import tempfile
from collections import defaultdict
from contextlib import contextmanager
from pathlib import Path
from typing import Any, Iterable, Sequence


VERSION = "0.1.0"
SCHEMA_VERSION = 1
TOOL_RELEASE_SHA256 = "e49d894c002b53a00dcb813f878ba855d6fccd775394927f8d4c7ebc619333e5"
DEFAULT_INDEX_PATH = Path("evidence/reference-index.json")
DEFAULT_BANS_PATH = Path("evidence/bans.json")
DEFAULT_OBSERVATIONS_PATH = Path("evidence/observations.json")
INSTALL_RECEIPT_PATH = Path(".booster-installed.json")
DATE_RE = re.compile(r"\b(20\d{2}-\d{2}-\d{2})\b")
TOKEN_RE = re.compile(r"[^\W_]+", flags=re.UNICODE)
BAN_RE = re.compile(r"^- \*\*(B\d{3})\*\*\s+(.+)$")
EVIDENCE_RE = re.compile(r"\s+\(Observed failure:\s*(.+)\)\s*$")
VALID_SOURCE_STATUSES = {"full-css", "wayback", "legacy-unstructured"}
VALID_BAN_STATUSES = {"legacy-unstructured", "structured"}
MIN_RELEVANCE_SCORE = 3.0
UNCOVERED_INDUSTRY_TOKENS = {
    "bakery": "food/hospitality",
    "barbeque": "food/hospitality",
    "barbecue": "food/hospitality",
    "bbq": "food/hospitality",
    "bistro": "food/hospitality",
    "cafe": "food/hospitality",
    "cafes": "food/hospitality",
    "church": "religion",
    "college": "education",
    "diner": "food/hospitality",
    "eatery": "food/hospitality",
    "government": "civic",
    "gym": "sports",
    "hotel": "hospitality",
    "hotels": "hospitality",
    "motel": "hospitality",
    "mosque": "religion",
    "restaurant": "food/hospitality",
    "restaurants": "food/hospitality",
    "school": "education",
    "schools": "education",
    "synagogue": "religion",
    "temple": "religion",
    "university": "education",
}
CANONICAL_HOME = "~/.claude"
VALID_LIBRARY_HOMES = ("~/.claude", "~/.grok")
MANAGED_LIBRARY_PATHS = [
    "DESIGN.md",
    "design/packages",
    "design/notes",
    "design/tools",
    "design/evidence",
]
REQUIRED_SKILLS = ["booster", "booster-questions", "booster-audit"]
REQUIRED_MANAGED_PATHS = [
    "notes/gwern.md",
    "notes/comparables-2026-08.md",
    "tools/booster.py",
    "evidence/bans.json",
    "evidence/observations.json",
    "evidence/reference-index.json",
    "skills/booster/SKILL.md",
    "skills/booster/booster-skill.json",
    "skills/booster/agents/openai.yaml",
    "skills/booster/references/direction-record.md",
    "skills/booster-questions/SKILL.md",
    "skills/booster-questions/booster-skill.json",
    "skills/booster-questions/agents/openai.yaml",
    "skills/booster-audit/SKILL.md",
    "skills/booster-audit/booster-skill.json",
    "skills/booster-audit/agents/openai.yaml",
]
DESIGN_SECTIONS = [
    "## Ban list (the mode, excised by name)",
    "## Hard floors (non-negotiable)",
    "## Design packages",
    "## Evidence lifecycle",
    "## Derive step (per artifact, before building)",
    "## Photography integration (when the page carries photos)",
    "## Judge step (after building)",
]


class BoosterError(Exception):
    """A user-actionable Booster error."""


class BoosterUsageError(Exception):
    """A command-line usage error with generated help text."""

    def __init__(self, message: str, help_text: str) -> None:
        super().__init__(message)
        self.help_text = help_text


class AxiArgumentParser(argparse.ArgumentParser):
    """Argparse that lets the caller render usage errors as TOON or JSON."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs.setdefault("allow_abbrev", False)
        super().__init__(*args, **kwargs)

    def error(self, message: str) -> None:
        raise BoosterUsageError(message, self.format_help().rstrip())


def uses_current_schema(value: Any) -> bool:
    """Accept the integer schema version exactly; JSON booleans are not versions."""

    return (
        isinstance(value, dict)
        and type(value.get("schema_version")) is int
        and value["schema_version"] == SCHEMA_VERSION
    )


def is_valid_library_home(value: Any) -> bool:
    return (
        isinstance(value, str)
        and value.strip() != ""
        and (
            value in VALID_LIBRARY_HOMES
            or value.startswith("~/")
            or value.startswith("/")
        )
    )


def is_booster_ownership_marker(value: Any) -> bool:
    """Recognize a compatible marker without freezing release-specific inventory."""

    return (
        uses_current_schema(value)
        and value.get("name") == "booster"
        and is_valid_library_home(value.get("canonical_home"))
        and value.get("managed_library_paths") == MANAGED_LIBRARY_PATHS
    )


def is_install_receipt(value: Any) -> bool:
    return uses_current_schema(value) and value.get("name") == "booster-installed-library"


def has_release_inventory(value: Any) -> bool:
    """Require the exact managed inventory shipped with this tool release."""

    return (
        is_booster_ownership_marker(value)
        and value.get("skills") == REQUIRED_SKILLS
        and value.get("required_managed_paths") == REQUIRED_MANAGED_PATHS
    )


def default_root() -> Path:
    """Return the library root paired with this script, independent of cwd."""

    return Path(__file__).resolve().parent.parent


def booster_design_path(root: Path) -> Path:
    local = root / "DESIGN.md"
    if local.exists() or local.is_symlink():
        return local
    return root.parent / "DESIGN.md" if is_installed_layout(root) else local


def resolve_root(value: str | Path | None) -> Path:
    root = Path(value).expanduser() if value is not None else default_root()
    return root.resolve()


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        raise BoosterError(f"cannot read {path}: {exc}") from exc


def normalized_tool_sha256(source: str) -> str:
    normalized, replacements = re.subn(
        r'^TOOL_RELEASE_SHA256 = "[0-9a-f]{64}"$',
        'TOOL_RELEASE_SHA256 = "<normalized-release-digest>"',
        source,
        count=1,
        flags=re.MULTILINE,
    )
    if replacements != 1:
        return ""
    return hashlib.sha256(normalized.encode("utf-8")).hexdigest()


def load_json(path: Path) -> Any:
    try:
        return json.loads(read_text(path))
    except json.JSONDecodeError as exc:
        raise BoosterError(
            f"invalid JSON in {path}: line {exc.lineno}, column {exc.colno}: {exc.msg}"
        ) from exc


def write_json(path: Path, value: Any) -> None:
    """Write deterministic JSON atomically."""

    path.parent.mkdir(parents=True, exist_ok=True)
    rendered = json.dumps(value, indent=2, ensure_ascii=False) + "\n"
    temporary = path.with_name(f".{path.name}.{os.getpid()}.tmp")
    try:
        temporary.write_text(rendered, encoding="utf-8", newline="\n")
        os.replace(temporary, path)
    except OSError as exc:
        try:
            temporary.unlink(missing_ok=True)
        except OSError:
            pass
        raise BoosterError(f"cannot write {path}: {exc}") from exc


def relative_path(path: Path, root: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return path.as_posix()


def package_paths(root: Path) -> tuple[list[Path], list[Path]]:
    forms = sorted((root / "packages").glob("*/PACK.md"))
    sectors = sorted((root / "packages" / "sectors").glob("*/PACK.md"))
    return forms, sectors


def reference_paths(root: Path) -> tuple[list[Path], list[Path]]:
    refs = sorted(root.glob("packages/**/refs/*.md"))
    modes = sorted(root.glob("packages/**/modes/*.md"))
    return refs, modes


def extract_section(text: str, heading: str) -> list[str]:
    """Return lines after an exact H2 until the next H2 or EOF."""

    lines = text.splitlines()
    try:
        start = lines.index(heading) + 1
    except ValueError:
        return []
    end = len(lines)
    for index in range(start, len(lines)):
        if lines[index].startswith("## "):
            end = index
            break
    return lines[start:end]


def _stem_occurs(stem: str, line: str) -> bool:
    pattern = rf"(?<![A-Za-z0-9_.-]){re.escape(stem)}(?![A-Za-z0-9_.-])"
    return re.search(pattern, line, flags=re.IGNORECASE) is not None


def _pole_from_range_line(line: str, target_text: str | None = None) -> str:
    cleaned = re.sub(r"^-\s+", "", line.strip())
    backtick = re.match(r"`[^`]+`\s*:\s*(.+)$", cleaned)
    if backtick:
        return backtick.group(1).strip()

    if " - " in cleaned:
        return cleaned.split(" - ", 1)[1].strip()

    represents = re.search(r"\s+represents\s+(.+)$", cleaned, flags=re.IGNORECASE)
    if represents:
        return represents.group(1).strip()

    if target_text:
        location = cleaned.lower().find(target_text.lower())
        if location >= 0:
            tail = cleaned[location + len(target_text) :].strip(" :;-")
            return tail.strip()
    return ""


def parse_range_map(pack_path: Path) -> dict[str, Any]:
    """Parse every live range-map grammar without treating aliases as files."""

    text = read_text(pack_path)
    lines = [line.strip() for line in extract_section(text, "## Range map") if line.strip()]
    ref_dir = pack_path.parent / "refs"
    ref_files = sorted(ref_dir.glob("*.md")) if ref_dir.is_dir() else []
    refs_by_stem = sorted(ref_files, key=lambda path: (-len(path.stem), path.name))
    mapped: dict[str, str] = {}
    unresolved: list[dict[str, Any]] = []
    duplicates: list[dict[str, Any]] = []

    for offset, line in enumerate(lines, start=1):
        target: Path | None = None
        target_text: str | None = None
        explicit = re.search(r"`(refs/[^`]+\.md)`", line)
        if explicit:
            target_text = explicit.group(1)
            target = pack_path.parent / target_text
        else:
            matches = [path for path in refs_by_stem if _stem_occurs(path.stem, line)]
            if matches:
                target = matches[0]
                target_text = target.stem
                if len(matches) > 1:
                    duplicates.append(
                        {
                            "line": line,
                            "line_number": offset,
                            "targets": [path.name for path in matches],
                        }
                    )

        if target is None or not target.is_file():
            unresolved.append(
                {"line": line, "line_number": offset, "target": target_text or "unknown"}
            )
            continue

        key = target.name
        pole = _pole_from_range_line(line, target_text)
        if key in mapped:
            duplicates.append(
                {"line": line, "line_number": offset, "targets": [key]}
            )
        else:
            mapped[key] = pole

    return {
        "mapped": mapped,
        "unresolved": unresolved,
        "duplicates": duplicates,
        "lines": lines,
    }


def parse_reference_metadata(path: Path, root: Path, pole: str | None) -> dict[str, Any]:
    text = read_text(path)
    lines = text.splitlines()
    heading = lines[0][2:].strip() if lines and lines[0].startswith("# ") else ""
    status_match = re.fullmatch(r"status:\s*([^\s]+)\s*", lines[1]) if len(lines) > 1 else None
    status = status_match.group(1) if status_match else "legacy-unstructured"
    date_match = DATE_RE.search(lines[0]) if lines else None
    date = date_match.group(1) if date_match else None

    parts = path.relative_to(root).parts
    if len(parts) >= 5 and parts[1] == "sectors":
        axis = "sector"
        package = parts[2]
    else:
        axis = "form"
        package = parts[1]
    kind = "mode" if path.parent.name == "modes" else "ref"
    stable_id = f"{axis}.{package}.{kind}.{path.stem}"
    title = heading.split(" (", 1)[0] if heading else path.stem
    return {
        "id": stable_id,
        "kind": kind,
        "axis": axis,
        "package": package,
        "title": title,
        "provenance": heading,
        "status": status,
        "date": date,
        "path": relative_path(path, root),
        "pole": pole if kind == "ref" else "mode to avoid",
        "content_sha256": hashlib.sha256(text.encode("utf-8")).hexdigest(),
    }


def build_reference_index(root: Path) -> dict[str, Any]:
    forms, sectors = package_paths(root)
    refs, modes = reference_paths(root)
    pole_by_path: dict[str, str] = {}

    for pack in [*forms, *sectors]:
        parsed = parse_range_map(pack)
        for filename, pole in parsed["mapped"].items():
            path = pack.parent / "refs" / filename
            pole_by_path[relative_path(path, root)] = pole

    entries: list[dict[str, Any]] = []
    for path in [*refs, *modes]:
        rel = relative_path(path, root)
        entries.append(parse_reference_metadata(path, root, pole_by_path.get(rel)))
    entries.sort(key=lambda entry: entry["id"])

    return {
        "schema_version": SCHEMA_VERSION,
        "counts": {
            "form_packs": len(forms),
            "sector_packs": len(sectors),
            "refs": len(refs),
            "modes": len(modes),
            "entries": len(entries),
        },
        "entries": entries,
    }


def tokenize(value: str | None) -> set[str]:
    if not value:
        return set()
    return set(TOKEN_RE.findall(value.lower()))


def uncovered_industry(query: str) -> str | None:
    """Return an uncovered industry label when the brief names one.

    Diagnosis only. Never used to retrieve or rewrite a shortlist.
    """

    labels = {
        UNCOVERED_INDUSTRY_TOKENS[token]
        for token in tokenize(query)
        if token in UNCOVERED_INDUSTRY_TOKENS
    }
    if not labels:
        return None
    return ",".join(sorted(labels))


def catalog_package_names(root: Path) -> tuple[list[str], list[str]]:
    forms, sectors = package_paths(root)
    return [path.parent.name for path in forms], [path.parent.name for path in sectors]


def _jaccard(left: set[str], right: set[str]) -> float:
    if not left and not right:
        return 1.0
    union = left | right
    return len(left & right) / len(union) if union else 0.0


def _relevance(root: Path, entry: dict[str, Any], query: str) -> float:
    query_tokens = tokenize(query)
    if not query_tokens:
        return 1.0

    pole = str(entry.get("pole") or "")
    identity = " ".join(
        [
            str(entry.get("title") or ""),
            str(entry.get("package") or ""),
            str(entry.get("path") or ""),
        ]
    )
    body_path = root / str(entry["path"])
    body = read_text(body_path)
    pole_tokens = tokenize(pole)
    identity_tokens = tokenize(identity)
    body_tokens = tokenize(body)
    score = (
        5.0 * len(query_tokens & pole_tokens)
        + 3.0 * len(query_tokens & identity_tokens)
        + 1.0 * len(query_tokens & body_tokens)
    )
    lowered = query.strip().lower()
    if lowered and lowered in pole.lower():
        score += 7.0
    if lowered and lowered in identity.lower():
        score += 5.0
    return score


def search_references(
    root: Path,
    query: str,
    *,
    form: str | None = None,
    sector: str | None = None,
    limit: int = 4,
    min_score: float = MIN_RELEVANCE_SCORE,
) -> list[dict[str, Any]]:
    """Rank lexical relevance, then use MMR-style pole and package diversity."""

    if limit < 1:
        raise BoosterError("--limit must be at least 1")
    if min_score < 0:
        raise BoosterError("min_score must be at least 0")
    index = build_reference_index(root)
    entries = [entry for entry in index["entries"] if entry["kind"] == "ref"]
    form_names = {entry["package"] for entry in entries if entry["axis"] == "form"}
    sector_names = {entry["package"] for entry in entries if entry["axis"] == "sector"}
    if form and form not in form_names:
        raise BoosterError(
            f"unknown form {form!r}; available forms: {', '.join(sorted(form_names))}"
        )
    if sector and sector not in sector_names:
        raise BoosterError(
            f"unknown sector {sector!r}; available sectors: {', '.join(sorted(sector_names))}"
        )
    if uncovered_industry(query) and not sector:
        return []

    if form or sector:
        entries = [
            entry
            for entry in entries
            if (form and entry["axis"] == "form" and entry["package"] == form)
            or (sector and entry["axis"] == "sector" and entry["package"] == sector)
        ]

    scored: list[dict[str, Any]] = []
    for entry in entries:
        candidate = dict(entry)
        candidate["score"] = _relevance(root, entry, query)
        if candidate["score"] < min_score:
            continue
        candidate["_pole_tokens"] = tokenize(str(entry.get("pole") or ""))
        scored.append(candidate)
    scored.sort(key=lambda item: (-item["score"], item["id"]))
    if not scored:
        return []

    selected: list[dict[str, Any]] = []
    remaining = list(scored)
    maximum = max(item["score"] for item in scored) or 1.0

    while remaining and len(selected) < min(limit, len(scored)):
        best: dict[str, Any] | None = None
        best_value = float("-inf")
        for candidate in remaining:
            relevance = candidate["score"] / maximum
            if selected:
                novelty = min(
                    1.0 - _jaccard(candidate["_pole_tokens"], item["_pole_tokens"])
                    for item in selected
                )
            else:
                novelty = 1.0
            package_novelty = (
                1.0
                if all(candidate["package"] != item["package"] for item in selected)
                else 0.0
            )
            axis_novelty = (
                1.0
                if all(candidate["axis"] != item["axis"] for item in selected)
                else 0.0
            )
            selection_score = (
                0.55 * relevance
                + 0.25 * novelty
                + 0.15 * package_novelty
                + 0.05 * axis_novelty
            )
            if selection_score > best_value or (
                selection_score == best_value
                and best is not None
                and candidate["id"] < best["id"]
            ):
                best = candidate
                best_value = selection_score
        assert best is not None
        best["selection_score"] = round(best_value, 4)
        selected.append(best)
        remaining.remove(best)

    result: list[dict[str, Any]] = []
    for candidate in selected:
        result.append(
            {
                key: value
                for key, value in candidate.items()
                if not key.startswith("_")
            }
        )
    return result


def diagnose_empty_search(
    root: Path,
    query: str,
    *,
    form: str | None = None,
    sector: str | None = None,
    min_score: float = MIN_RELEVANCE_SCORE,
) -> dict[str, Any]:
    """Explain a zero-hit search without suggesting the query be broadened."""

    forms, sectors = catalog_package_names(root)
    uncovered = uncovered_industry(query)
    diagnosis: dict[str, Any] = {
        "reason": "no-lexical-hit",
        "query": query,
        "form": form,
        "sector": sector,
        "available_forms": forms,
        "available_sectors": sectors,
    }
    if uncovered:
        diagnosis["uncovered"] = uncovered
    if uncovered and not sector:
        diagnosis["reason"] = "no-sector"
        return diagnosis
    if form or sector:
        unfiltered = search_references(root, query, min_score=min_score)
        if unfiltered:
            diagnosis["reason"] = "filter-too-narrow"
            return diagnosis
    return diagnosis


def empty_search_help(diagnosis: dict[str, Any]) -> list[str]:
    reason = str(diagnosis.get("reason") or "no-lexical-hit")
    if reason == "no-sector":
        label = str(diagnosis.get("uncovered") or "an uncovered industry")
        return [
            f"This brief names {label}, which has no sector pack. Set sector to none.",
            "Open a form PACK.md range map. Do not search the catalog. Never retry unfiltered.",
        ]
    if reason == "filter-too-narrow":
        return [
            "Hits exist outside the current --form/--sector filter. Add the matching sector or open that PACK.md range map.",
            "Never retry unfiltered. Never broaden the query to force a hit.",
        ]
    return [
        "No ref in the current filter contains these terms. Open the chosen PACK.md range map.",
        "Never retry unfiltered. Never broaden the query to force a hit.",
    ]


def parse_design_bans(path: Path) -> list[dict[str, Any]]:
    section = extract_section(read_text(path), "## Ban list (the mode, excised by name)")
    bans: list[dict[str, Any]] = []
    for line in section:
        match = BAN_RE.match(line)
        if not match:
            continue
        ban_id, body = match.groups()
        evidence_match = EVIDENCE_RE.search(body)
        evidence_summary = evidence_match.group(1) if evidence_match else None
        pattern = body[: evidence_match.start()].rstrip() if evidence_match else body.strip()
        bans.append(
            {
                "id": ban_id,
                "pattern": pattern,
                "evidence_summary": evidence_summary,
            }
        )
    return bans


def issue(severity: str, code: str, path: str, message: str) -> dict[str, str]:
    return {"severity": severity, "code": code, "path": path, "message": message}


def _valid_date(value: str) -> bool:
    if not isinstance(value, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        return False
    try:
        dt.date.fromisoformat(value)
    except (TypeError, ValueError):
        return False
    return True


def _validate_readme_counts(root: Path, issues: list[dict[str, str]]) -> None:
    readme = read_text(root / "README.md")
    forms, sectors = package_paths(root)
    refs, modes = reference_paths(root)
    design_bans = parse_design_bans(root / "DESIGN.md")
    expected = {
        "form_packs": len(forms),
        "sector_packs": len(sectors),
        "distilled_refs": len(refs),
        "sector_modes": len(modes),
        "design_bans": len(design_bans),
    }
    for label, actual in expected.items():
        matches = re.findall(rf"{re.escape(label)}-(\d+)-", readme)
        if len(matches) != 1:
            issues.append(
                issue(
                    "error",
                    "readme-count-missing",
                    "README.md",
                    f"{label} badge must appear exactly once",
                )
            )
        elif int(matches[0]) != actual:
            issues.append(
                issue(
                    "error",
                    "readme-count-mismatch",
                    "README.md",
                    f"{label} says {matches[0]}, filesystem has {actual}",
                )
            )


def _frontmatter_fields(text: str) -> dict[str, str] | None:
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        return None
    try:
        end = lines.index("---", 1)
    except ValueError:
        return None
    body = lines[1:end]
    if len(body) != 2:
        return None
    fields: dict[str, str] = {}
    for line in body:
        direct = re.fullmatch(r"(name|description): ([^\r\n]+)", line)
        if not direct or direct.group(1) in fields:
            return None
        value = direct.group(2)
        implicit_scalar = value.lower() in {
            "null",
            "~",
            "true",
            "false",
            "yes",
            "no",
            "on",
            "off",
        } or re.fullmatch(r"[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:e[-+]?\d+)?", value, re.I)
        if (
            not value.strip()
            or value != value.strip()
            or not value[0].isalnum()
            or any(
                ord(character) < 0x20 or 0x7F <= ord(character) <= 0x9F
                for character in value
            )
            or implicit_scalar
            or ": " in value
            or " #" in value
        ):
            return None
        key = direct.group(1)
        if key == "name" and (
            len(value) > 64 or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", value)
        ):
            return None
        if key == "description" and (
            len(value) > 1024 or not re.search(r"\s", value) or "<" in value or ">" in value
        ):
            return None
        fields[key] = value
    return fields if set(fields) == {"name", "description"} else None


def _validate_markdown_contract(
    root: Path,
    issues: list[dict[str, str]],
    relative: str,
    h1: str,
    sections: Sequence[str],
    *,
    frontmatter: bool = False,
    source_path: Path | None = None,
    minimum_bytes: int = 400,
    required_anchors: Sequence[str] = (),
) -> None:
    path = source_path if source_path is not None else root / relative
    if not path.is_file():
        return
    text = read_text(path)
    lines = text.splitlines()
    if len(text.encode("utf-8")) < minimum_bytes:
        issues.append(
            issue(
                "error",
                "document-content",
                relative,
                f"managed document must retain at least {minimum_bytes} bytes of substantive content",
            )
        )
    for anchor in required_anchors:
        if anchor not in text:
            issues.append(
                issue(
                    "error",
                    "document-anchor",
                    relative,
                    f"managed workflow anchor is missing: {anchor!r}",
                )
            )
    heading_index = 0
    if frontmatter and lines and lines[0] == "---":
        try:
            heading_index = lines.index("---", 1) + 1
        except ValueError:
            heading_index = len(lines)
        while heading_index < len(lines) and not lines[heading_index].strip():
            heading_index += 1
    if heading_index >= len(lines) or lines[heading_index] != h1:
        location = "first body heading" if frontmatter else "first line"
        issues.append(issue("error", "document-heading", relative, f"{location} must be {h1!r}"))
    positions: list[int] = []
    for heading in sections:
        matches = [index for index, line in enumerate(lines) if line == heading]
        if len(matches) != 1:
            issues.append(
                issue(
                    "error",
                    "document-section",
                    relative,
                    f"required section {heading!r} must appear exactly once",
                )
            )
            continue
        positions.append(matches[0])
        body = extract_section(text, heading)
        body_text = " ".join(line.strip().lstrip("-*0123456789. ") for line in body if line.strip())
        if len(body_text) < 12 or len(TOKEN_RE.findall(body_text.lower())) < 3:
            issues.append(
                issue(
                    "error",
                    "document-section-empty",
                    relative,
                    f"section {heading!r} needs substantive content",
                )
            )
    if len(positions) == len(sections) and positions != sorted(positions):
        issues.append(issue("error", "document-section-order", relative, "required sections are out of order"))


def _validate_owned_documents(root: Path, issues: list[dict[str, str]]) -> None:
    contracts = [
        (
            "DESIGN.md",
            "# Design invariants",
            DESIGN_SECTIONS,
            [
                "2-3 refs total",
                "evidence/observations.json",
                "compact ASCII wireframe",
                "prefers-reduced-motion",
            ],
        ),
        (
            "notes/gwern.md",
            "# Gwern design reference",
            [
                "## Documented decisions and their reasoning",
                "## Graveyard (abandoned, with cause)",
                "## Meta-lessons",
            ],
            [
                "Sidenotes in both margins",
                "A/B showed no improvement",
                "Every ornament needs an off-switch",
            ],
        ),
        (
            "notes/comparables-2026-08.md",
            "# Comparable systems scan, 2026-08-17",
            [
                "## Ten closest systems",
                "## Implemented synthesis",
                "## Deliberately not adopted",
            ],
            ["Anthropic Frontend Design", "Superdesign Skill", "structured evidence registry"],
        ),
        (
            "skills/booster/references/direction-record.md",
            "# Direction record",
            [
                "## Context fingerprint",
                "## Direction A: <subject-specific name>",
                "## Direction B: <subject-specific name>",
                "## Direction C: <subject-specific name>",
                "## Rejection checks",
                "## Selection",
            ],
            [
                "Two selected refs, named by the builder",
                "<compact ASCII wireframe>",
                "Family collisions found and discarded",
                "Believability gate",
            ],
        ),
    ]
    for relative, h1, sections, anchors in contracts:
        _validate_markdown_contract(
            root, issues, relative, h1, sections, required_anchors=anchors
        )


def _validate_readme_contract(root: Path, issues: list[dict[str, str]]) -> None:
    path = root / "README.md"
    if path.is_symlink() or not path.is_file():
        return
    text = read_text(path)
    rel = "README.md"
    if len(text.encode("utf-8")) < 2_000:
        issues.append(
            issue(
                "error",
                "readme-content",
                rel,
                "README must retain the product, workflow, install, sync, and verification contracts",
            )
        )
    headings = [
        "## Why this exists",
        "## Anatomy",
        "## How a build runs",
        "## The ban list, briefly",
        "## Rules of growth",
        "## Search and evidence tools",
        "## Install",
        "## Sync (maintainer direction)",
        "## Verify",
    ]
    section_anchors = {
        "## Why this exists": ["statistical center", "three levers"],
        "## Anatomy": ["tools/", "evidence/"],
        "## How a build runs": ["$booster", "ASCII wireframes"],
        "## The ban list, briefly": ["legacy-unstructured", "DESIGN.md"],
        "## Rules of growth": ["evidence/observations.json", "never promotes them"],
        "## Search and evidence tools": ["python3 tools/booster.py validate"],
        "## Install": ["./install.sh --agent codex", "~/.agents/skills"],
        "## Sync (maintainer direction)": ["./sync.sh --dry-run", "--allow-removals"],
        "## Verify": ["unittest discover", "tests/test_install.zsh"],
    }
    for heading in headings:
        if text.splitlines().count(heading) != 1:
            issues.append(
                issue("error", "readme-section", rel, f"required section {heading!r} is missing")
            )
            continue
        body = " ".join(line.strip() for line in extract_section(text, heading) if line.strip())
        if len(body) < 24 or len(TOKEN_RE.findall(body.lower())) < 4:
            issues.append(
                issue("error", "readme-section", rel, f"section {heading!r} is not substantive")
            )
        for anchor in section_anchors[heading]:
            if anchor not in body:
                issues.append(
                    issue(
                        "error",
                        "readme-anchor",
                        rel,
                        f"section {heading!r} is missing workflow anchor {anchor!r}",
                    )
                )


def _validate_tool_contract(root: Path, issues: list[dict[str, str]]) -> None:
    path = root / "tools/booster.py"
    rel = relative_path(path, root)
    if path.is_symlink() or not path.is_file():
        issues.append(issue("error", "tool-structure", rel, "tool must be a regular file"))
        return
    source = read_text(path)
    if normalized_tool_sha256(source) != TOOL_RELEASE_SHA256:
        issues.append(
            issue(
                "error",
                "tool-digest",
                rel,
                "tool content does not match this release's normalized digest",
            )
        )
        return
    if len(source.encode("utf-8")) < 10_000 or not source.startswith("#!/usr/bin/env python3\n"):
        issues.append(
            issue(
                "error",
                "tool-content",
                rel,
                "tool is truncated or missing its validation and CLI contracts",
            )
        )
        return
    try:
        tree = ast.parse(source, path.as_posix())
    except SyntaxError as exc:
        issues.append(
            issue(
                "error",
                "tool-syntax",
                rel,
                f"tool does not compile: line {exc.lineno}: {exc.msg}",
            )
        )
        return
    definitions = {
        node.name for node in tree.body if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    }
    required_definitions = {"validate_repository", "build_parser", "main"}

    def is_main_guard(node: ast.stmt) -> bool:
        if not isinstance(node, ast.If) or not isinstance(node.test, ast.Compare):
            return False
        compare = node.test
        guard = (
            isinstance(compare.left, ast.Name)
            and compare.left.id == "__name__"
            and len(compare.ops) == 1
            and isinstance(compare.ops[0], ast.Eq)
            and len(compare.comparators) == 1
            and isinstance(compare.comparators[0], ast.Constant)
            and compare.comparators[0].value == "__main__"
        )
        return guard and any(
            isinstance(descendant, ast.Call)
            and isinstance(descendant.func, ast.Name)
            and descendant.func.id == "main"
            for statement in node.body
            for descendant in ast.walk(statement)
        )

    if not required_definitions.issubset(definitions) or not any(
        is_main_guard(node) for node in tree.body
    ):
        issues.append(
            issue(
                "error",
                "tool-content",
                rel,
                "tool AST is missing required validation, parser, or executable entry points",
            )
        )
        return
    environment = dict(os.environ)
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    smoke_cases = [
        ([sys.executable, path.as_posix(), "--version"], VERSION),
        ([sys.executable, path.as_posix(), "--help"], "validate"),
    ]
    for command, expected in smoke_cases:
        try:
            completed = subprocess.run(
                command,
                cwd=root,
                env=environment,
                capture_output=True,
                text=True,
                timeout=10,
                check=False,
            )
        except (OSError, subprocess.SubprocessError) as exc:
            issues.append(issue("error", "tool-smoke", rel, f"tool smoke check failed: {exc}"))
            return
        if completed.returncode != 0 or completed.stderr or expected not in completed.stdout:
            issues.append(
                issue(
                    "error",
                    "tool-smoke",
                    rel,
                    f"tool did not satisfy the {command[-1]} executable contract",
                )
            )
            return
    try:
        with tempfile.TemporaryDirectory(prefix="booster-tool-smoke.") as invalid_root:
            completed = subprocess.run(
                [
                    sys.executable,
                    path.as_posix(),
                    "validate",
                    "--root",
                    invalid_root,
                    "--json",
                ],
                cwd=root,
                env=environment,
                capture_output=True,
                text=True,
                timeout=10,
                check=False,
            )
            try:
                response = json.loads(completed.stdout)
            except json.JSONDecodeError:
                response = None
            if (
                completed.returncode != 1
                or completed.stderr
                or not isinstance(response, dict)
                or response.get("valid") is not False
                or type(response.get("errors")) is not int
                or response["errors"] < 1
            ):
                issues.append(
                    issue(
                        "error",
                        "tool-smoke",
                        rel,
                        "tool did not return a structured failure for an invalid repository",
                    )
                )
    except (OSError, subprocess.SubprocessError) as exc:
        issues.append(issue("error", "tool-smoke", rel, f"tool validation smoke failed: {exc}"))


def _validate_skills(root: Path, issues: list[dict[str, str]]) -> None:
    skill_files = sorted(root.glob("skills/*/SKILL.md"))
    if not skill_files:
        issues.append(issue("error", "skills-missing", "skills", "no SKILL.md files found"))
        return
    for path in skill_files:
        rel = relative_path(path, root)
        fields = _frontmatter_fields(read_text(path))
        if fields is None:
            issues.append(issue("error", "skill-frontmatter", rel, "missing or unclosed frontmatter"))
            continue
        if not fields.get("name"):
            issues.append(issue("error", "skill-name", rel, "frontmatter name is required"))
        elif fields["name"] != path.parent.name:
            issues.append(
                issue(
                    "error",
                    "skill-name-mismatch",
                    rel,
                    f"frontmatter name {fields['name']!r} does not match directory {path.parent.name!r}",
                )
            )
        if not fields.get("description"):
            issues.append(issue("error", "skill-description", rel, "frontmatter description is required"))
        skill_contracts = {
            "booster": (
                "# Booster: design-pack routing",
                [f"## Step {number}: {title}" for number, title in [
                    (1, "Scan for context"),
                    (2, "Pick the form package"),
                    (3, "Pick the sector package, if one applies"),
                    (4, "Choose refs"),
                    (5, "Deliver the recommendation"),
                    (6, "Derive when the build is proceeding"),
                ]],
                [
                    "existing visual language",
                    "page's job",
                    "Never force a sector fit",
                    "Never retry unfiltered",
                    "open no more than 2-3 ref files total",
                    "## Booster recommendation",
                    "compact ASCII wireframe",
                    "Counterfactual",
                    "one chosen direction",
                    "Screenshot mobile and laptop",
                ],
            ),
            "booster-questions": (
                "# Booster questions: interview, then route",
                ["## The interview", "## Then route"],
                [
                    "Ask ONE question at a time",
                    "Ask at most 5",
                    "~/.agents/skills/booster/SKILL.md",
                    "~/.claude/skills/booster/SKILL.md",
                    "~/.grok/skills/booster/SKILL.md",
                ],
            ),
            "booster-audit": (
                "# Booster audit",
                [
                    "## 1. Reconstruct intent",
                    "## 2. Capture rendered evidence",
                    "## 3. Classify findings",
                    "## 4. Report the verdict",
                    "## 5. Correct without converging",
                ],
                [
                    "mark the affected gates UNVERIFIED",
                    "test reduced motion at runtime",
                    "coverage matrix",
                    "Verdict: PASS | REVISE | FAIL | INCOMPLETE",
                    "report-only unless the user separately authorizes",
                ],
            ),
        }
        contract = skill_contracts.get(path.parent.name)
        if contract:
            _validate_markdown_contract(
                root,
                issues,
                rel,
                contract[0],
                contract[1],
                frontmatter=True,
                required_anchors=contract[2],
            )
        ownership_path = path.parent / "booster-skill.json"
        ownership_rel = relative_path(ownership_path, root)
        if not ownership_path.is_file():
            issues.append(issue("error", "skill-ownership", ownership_rel, "file is required"))
        else:
            try:
                ownership = load_json(ownership_path)
            except BoosterError as exc:
                issues.append(issue("error", "skill-ownership", ownership_rel, str(exc)))
            else:
                if not (
                    uses_current_schema(ownership)
                    and ownership.get("owner") == "booster"
                    and ownership.get("skill") == path.parent.name
                ):
                    issues.append(
                        issue(
                            "error",
                            "skill-ownership",
                            ownership_rel,
                            "owner, integer schema_version, and skill must match Booster",
                        )
                    )
        metadata_path = path.parent / "agents" / "openai.yaml"
        metadata_rel = relative_path(metadata_path, root)
        if not metadata_path.is_file():
            issues.append(issue("error", "skill-openai-metadata", metadata_rel, "file is required"))
            continue
        metadata = read_text(metadata_path)
        lines = [line for line in metadata.splitlines() if line.strip()]
        allowed_fields = ["display_name", "short_description", "default_prompt"]
        if "\t" in metadata or not lines or lines[0] != "interface:":
            issues.append(
                issue("error", "skill-openai-metadata", metadata_rel, "interface must be a YAML mapping")
            )
            continue
        parsed: dict[str, str] = {}
        malformed = False
        for line in lines[1:]:
            match = re.fullmatch(r"  ([a-z_]+):\s*(.+?)\s*", line)
            if not match or match.group(1) not in allowed_fields or match.group(1) in parsed:
                malformed = True
                break
            parsed[match.group(1)] = match.group(2)
        if malformed or len(lines) != 4:
            issues.append(
                issue(
                    "error",
                    "skill-openai-metadata",
                    metadata_rel,
                    "metadata must contain only interface and its three supported fields",
                )
            )
            continue
        decoded_metadata: dict[str, str] = {}
        for field in allowed_fields:
            raw = parsed.get(field, "")
            try:
                value = json.loads(raw)
            except json.JSONDecodeError:
                value = None
            if not isinstance(value, str) or not value.strip():
                issues.append(
                    issue(
                        "error",
                        "skill-openai-metadata",
                        metadata_rel,
                        f"interface.{field} must be a nonempty double-quoted string",
                    )
                )
            else:
                decoded_metadata[field] = value
        short_description = decoded_metadata.get("short_description", "")
        if short_description and not 25 <= len(short_description) <= 64:
            issues.append(
                issue(
                    "error",
                    "skill-openai-description",
                    metadata_rel,
                    "short_description must contain 25 to 64 characters",
                )
            )
        expected_display_name = path.parent.name.replace("-", " ").title()
        display_name = decoded_metadata.get("display_name", "")
        if display_name and display_name != expected_display_name:
            issues.append(
                issue(
                    "error",
                    "skill-openai-identity",
                    metadata_rel,
                    f"display_name must be {expected_display_name!r}",
                )
            )
        expected_token = f"${path.parent.name}"
        prompt = decoded_metadata.get("default_prompt", "")
        skill_tokens = set(re.findall(r"\$[a-z0-9]+(?:-[a-z0-9]+)*", prompt))
        if prompt and skill_tokens != {expected_token}:
            issues.append(
                issue(
                    "error",
                    "skill-openai-identity",
                    metadata_rel,
                    f"default_prompt must invoke exactly {expected_token}",
                )
            )


def _validate_reference_metadata(root: Path, issues: list[dict[str, str]]) -> None:
    refs, modes = reference_paths(root)
    for path in [*refs, *modes]:
        rel = relative_path(path, root)
        text = read_text(path)
        lines = text.splitlines()
        if not lines or not lines[0].startswith("# "):
            issues.append(issue("error", "reference-heading", rel, "first line must be an H1"))
            continue
        date_match = DATE_RE.search(lines[0])
        if not date_match or not _valid_date(date_match.group(1)):
            issues.append(issue("error", "reference-date", rel, "H1 must carry a valid YYYY-MM-DD date"))
        status_lines = [
            (index, line)
            for index, line in enumerate(lines)
            if re.match(r"^status:", line)
        ]
        status_match = re.fullmatch(r"status:\s*([^\s]+)\s*", lines[1]) if len(lines) > 1 else None
        if status_lines and (len(status_lines) != 1 or status_lines[0][0] != 1 or not status_match):
            issues.append(
                issue(
                    "error",
                    "reference-status-slot",
                    rel,
                    "status may appear once, immediately after the H1",
                )
            )
        if status_match:
            if status_match.group(1) not in VALID_SOURCE_STATUSES:
                issues.append(
                    issue(
                        "error",
                        "reference-status",
                        rel,
                        f"unsupported status {status_match.group(1)!r}",
                    )
                )
        else:
            issues.append(
                issue(
                    "warning",
                    "reference-legacy-status",
                    rel,
                    "status is absent; indexed as legacy-unstructured",
                )
            )

        parts = path.relative_to(root).parts
        is_sector = len(parts) >= 5 and parts[1] == "sectors"
        owning_pack = (
            root / "packages" / "sectors" / parts[2] / "PACK.md"
            if is_sector
            else root / "packages" / parts[1] / "PACK.md"
        )
        if not owning_pack.is_file() or owning_pack.is_symlink():
            issues.append(
                issue(
                    "error",
                    "reference-orphan",
                    rel,
                    "reference must belong to a package with a regular PACK.md",
                )
            )
        if not is_sector:
            avoid = re.search(r"^Avoid:\s*(\S.+)$", text, flags=re.MULTILINE)
            if not avoid or len(avoid.group(1).strip()) < 20:
                issues.append(
                    issue(
                        "error",
                        "reference-avoid",
                        rel,
                        "form ref must contain a substantive Avoid passage",
                    )
                )
            substantive_bullets = [
                line for line in lines if line.startswith("- ") and len(line[2:].strip()) >= 20
            ]
            if len(substantive_bullets) < 3 or len(text.encode("utf-8")) < 400:
                issues.append(
                    issue(
                        "error",
                        "reference-content",
                        rel,
                        "form ref must retain substantive distilled evidence, not placeholders",
                    )
                )
            continue

        sector = parts[2]
        expected_sweep = "mode" if path.parent.name == "modes" else "excellence"
        heading = lines[0]
        if f"sector: {sector}" not in heading:
            issues.append(issue("error", "reference-sector", rel, f"heading must declare sector: {sector}"))
        if f"sweep: {expected_sweep}" not in heading:
            issues.append(
                issue("error", "reference-sweep", rel, f"heading must declare sweep: {expected_sweep}")
            )
        required_sections = (
            ["## Default patterns observed", "## Tells"]
            if expected_sweep == "mode"
            else ["## Token block", "## Lessons", "## Avoid"]
        )
        substantive_bullets = [
            line
            for line in lines
            if line.startswith("- ") and len(line[2:].strip()) >= 20
        ]
        for section in required_sections:
            matching_heading = next((line for line in lines if line.startswith(section)), None)
            if matching_heading is None:
                issues.append(
                    issue("error", "reference-section", rel, f"missing section beginning {section!r}")
                )
                continue
            body = extract_section(text, matching_heading)
            if not any(
                line.startswith("- ") and len(line[2:].strip()) >= 20 for line in body
            ):
                issues.append(
                    issue(
                        "error",
                        "reference-section-empty",
                        rel,
                        f"section beginning {section!r} needs distilled evidence bullets",
                    )
                )
        if (
            len(text.encode("utf-8")) < 400
            or len(substantive_bullets) < len(required_sections)
        ):
            issues.append(
                issue(
                    "error",
                    "reference-content",
                    rel,
                    "sector ref must retain substantive distilled evidence, not placeholders",
                )
            )


def _validate_pack_contracts(root: Path, issues: list[dict[str, str]]) -> None:
    forms, sectors = package_paths(root)
    if not forms:
        issues.append(issue("error", "catalog-empty", "packages", "at least one form pack is required"))
    if not sectors:
        issues.append(
            issue("error", "catalog-empty", "packages/sectors", "at least one sector pack is required")
        )
    refs, _ = reference_paths(root)
    if not refs:
        issues.append(issue("error", "catalog-empty", "packages", "at least one reference is required"))
    for path in forms:
        relative = relative_path(path, root)
        _validate_markdown_contract(
            root,
            issues,
            relative,
            f"# {path.parent.name.capitalize()} package",
            ["## Range map", "## Lessons (cross-site)", "## Avoid (cross-site)"],
        )
    for path in sectors:
        relative = relative_path(path, root)
        sector = path.parent.name
        _validate_markdown_contract(
            root,
            issues,
            relative,
            f"# {sector} sector package",
            [
                f"## The {sector} mode (avoid)",
                "## Tells",
                "## Register",
                "## Range map",
            ],
        )
        pack_text = read_text(path)
        if "**Operational surface:**" not in pack_text:
            issues.append(
                issue(
                    "error",
                    "sector-operational-surface",
                    relative,
                    "Register must include an Operational surface bullet distilled from this sector's refs",
                )
            )


def _validate_range_maps(root: Path, issues: list[dict[str, str]]) -> None:
    forms, sectors = package_paths(root)
    for pack in [*forms, *sectors]:
        rel = relative_path(pack, root)
        parsed = parse_range_map(pack)
        if not parsed["lines"]:
            issues.append(issue("error", "range-map-missing", rel, "Range map is empty or missing"))
        for unresolved in parsed["unresolved"]:
            issues.append(
                issue(
                    "error",
                    "range-map-path",
                    rel,
                    f"unresolved range-map entry: {unresolved['line']}",
                )
            )
        for duplicate in parsed["duplicates"]:
            issues.append(
                issue(
                    "error",
                    "range-map-duplicate",
                    rel,
                    f"ambiguous or duplicate entry: {duplicate['line']}",
                )
            )
        expected = sorted(path.name for path in (pack.parent / "refs").glob("*.md"))
        for filename in expected:
            if filename not in parsed["mapped"]:
                issues.append(
                    issue(
                        "error",
                        "range-map-unmapped-ref",
                        rel,
                        f"refs/{filename} is not represented in the range map",
                    )
                )
            elif not parsed["mapped"][filename]:
                issues.append(
                    issue(
                        "error",
                        "range-map-pole",
                        rel,
                        f"refs/{filename} has no pole description",
                    )
                )


def _validate_bans(root: Path, issues: list[dict[str, str]]) -> None:
    path = root / DEFAULT_BANS_PATH
    rel = relative_path(path, root)
    if not path.is_file():
        issues.append(issue("error", "bans-missing", rel, "evidence bans file is required"))
        return
    try:
        data = load_json(path)
    except BoosterError as exc:
        issues.append(issue("error", "bans-json", rel, str(exc)))
        return
    if not uses_current_schema(data):
        issues.append(issue("error", "bans-schema", rel, f"schema_version must be {SCHEMA_VERSION}"))
        return
    if data.get("source") != "DESIGN.md":
        issues.append(issue("error", "bans-source", rel, "source must be DESIGN.md"))
    bans = data.get("bans")
    if not isinstance(bans, list):
        issues.append(issue("error", "bans-schema", rel, "bans must be an array"))
        return
    design_bans = parse_design_bans(booster_design_path(root))
    design_ids = [item["id"] for item in design_bans]
    duplicate_design_ids = sorted(
        {value for value in design_ids if design_ids.count(value) > 1}
    )
    if duplicate_design_ids:
        issues.append(
            issue(
                "error",
                "ban-design-id-duplicate",
                booster_design_path(root).as_posix(),
                f"duplicate DESIGN IDs: {', '.join(duplicate_design_ids)}",
            )
        )
    expected = {item["id"]: item for item in design_bans}
    observations_by_id: dict[str, dict[str, Any]] = {}
    try:
        observation_data = load_json(root / DEFAULT_OBSERVATIONS_PATH)
        observation_entries = (
            observation_data.get("observations", []) if isinstance(observation_data, dict) else []
        )
        if isinstance(observation_entries, list):
            observations_by_id = {
                item["id"]: item
                for item in observation_entries
                if isinstance(item, dict) and isinstance(item.get("id"), str)
            }
    except BoosterError:
        pass
    seen: set[str] = set()
    for index, ban in enumerate(bans):
        location = f"{rel}#bans[{index}]"
        if not isinstance(ban, dict):
            issues.append(issue("error", "ban-entry", location, "ban must be an object"))
            continue
        ban_id = ban.get("id")
        if not isinstance(ban_id, str) or not re.fullmatch(r"B\d{3}", ban_id):
            issues.append(issue("error", "ban-id", location, "id must match BNNN"))
            continue
        if ban_id in seen:
            issues.append(issue("error", "ban-id-duplicate", location, f"duplicate id {ban_id}"))
        seen.add(ban_id)
        status = ban.get("status")
        if not isinstance(status, str) or status not in VALID_BAN_STATUSES:
            issues.append(issue("error", "ban-status", location, "invalid provenance status"))
        if not isinstance(ban.get("pattern"), str) or not ban["pattern"].strip():
            issues.append(issue("error", "ban-pattern", location, "pattern is required"))
        source = expected.get(ban_id)
        if source and ban.get("pattern") != source["pattern"]:
            issues.append(
                issue("error", "ban-drift", location, f"pattern does not match {ban_id} in DESIGN.md")
            )
        evidence_summary = ban.get("evidence_summary")
        if evidence_summary is not None and not isinstance(evidence_summary, str):
            issues.append(
                issue(
                    "error",
                    "ban-evidence-summary",
                    location,
                    "evidence_summary must be a string or null",
                )
            )
        if source and evidence_summary != source.get("evidence_summary"):
            issues.append(
                issue(
                    "error",
                    "ban-evidence-drift",
                    location,
                    "evidence_summary must match the DESIGN provenance note",
                )
            )
        if status == "structured":
            observation_ids = ban.get("observation_ids")
            if (
                not isinstance(observation_ids, list)
                or len(observation_ids) < 2
                or not all(isinstance(value, str) and value for value in observation_ids)
                or len(set(observation_ids)) != len(observation_ids)
            ):
                issues.append(
                    issue(
                        "error",
                        "ban-observations",
                        location,
                        "structured bans need at least two unique observation IDs",
                    )
                )
            else:
                linked = [observations_by_id.get(value) for value in observation_ids]
                missing_ids = [value for value, item in zip(observation_ids, linked) if item is None]
                if missing_ids:
                    issues.append(
                        issue(
                            "error",
                            "ban-observation-link",
                            location,
                            f"unknown observation IDs: {', '.join(missing_ids)}",
                        )
                    )
                artifacts = {
                    str(item.get("artifact"))
                    for item in linked
                    if isinstance(item, dict) and item.get("artifact")
                }
                if len(artifacts) < 2:
                    issues.append(
                        issue(
                            "error",
                            "ban-independent-evidence",
                            location,
                            "structured bans need evidence from at least two independent artifacts",
                        )
                    )
                pattern_keys = {
                    str(item.get("pattern_key"))
                    for item in linked
                    if isinstance(item, dict) and item.get("pattern_key")
                }
                if len(pattern_keys) != 1:
                    issues.append(
                        issue(
                            "error",
                            "ban-pattern-group",
                            location,
                            "structured bans must link one repeated pattern group",
                        )
                    )
                elif ban.get("pattern_key") != next(iter(pattern_keys)):
                    issues.append(
                        issue(
                            "error",
                            "ban-pattern-key",
                            location,
                            "structured ban pattern_key must bind the linked observation group",
                        )
                    )
                elif isinstance(ban.get("pattern"), str) and ban.get("pattern_key") != pattern_key(
                    ban["pattern"]
                ):
                    issues.append(
                        issue(
                            "error",
                            "ban-pattern-key",
                            location,
                            "structured ban pattern_key must match the normalized ban pattern",
                        )
                    )
            if not isinstance(ban.get("confirmed_by"), str) or not ban["confirmed_by"].strip():
                issues.append(
                    issue("error", "ban-confirmation", location, "confirmed_by is required")
                )
            if not isinstance(ban.get("confirmed_date"), str) or not _valid_date(
                ban.get("confirmed_date")
            ):
                issues.append(
                    issue(
                        "error",
                        "ban-confirmation",
                        location,
                        "confirmed_date must be YYYY-MM-DD",
                    )
                )
    missing = sorted(set(expected) - seen)
    extra = sorted(seen - set(expected))
    if missing:
        issues.append(issue("error", "ban-missing", rel, f"missing DESIGN IDs: {', '.join(missing)}"))
    if extra:
        issues.append(issue("error", "ban-extra", rel, f"unknown IDs: {', '.join(extra)}"))


def _validate_observations(root: Path, issues: list[dict[str, str]]) -> None:
    path = root / DEFAULT_OBSERVATIONS_PATH
    rel = relative_path(path, root)
    if not path.is_file():
        issues.append(issue("error", "observations-missing", rel, "observations file is required"))
        return
    try:
        data = load_json(path)
    except BoosterError as exc:
        issues.append(issue("error", "observations-json", rel, str(exc)))
        return
    if not uses_current_schema(data):
        issues.append(
            issue("error", "observations-schema", rel, f"schema_version must be {SCHEMA_VERSION}")
        )
        return
    observations = data.get("observations")
    if not isinstance(observations, list):
        issues.append(issue("error", "observations-schema", rel, "observations must be an array"))
        return
    seen: set[str] = set()
    for index, observation in enumerate(observations):
        location = f"{rel}#observations[{index}]"
        for code, message in observation_integrity_errors(observation):
            issues.append(issue("error", code, location, message))
        observation_id = observation.get("id") if isinstance(observation, dict) else None
        if isinstance(observation_id, str):
            if observation_id in seen:
                issues.append(
                    issue("error", "observation-id-duplicate", location, f"duplicate id {observation_id}")
                )
            seen.add(observation_id)


def _validate_generated_indexes(root: Path, issues: list[dict[str, str]]) -> None:
    evidence = root / "evidence"
    if not evidence.is_dir():
        return
    generated_index = build_reference_index(root)
    generated_by_path = {
        entry["path"]: entry for entry in generated_index["entries"]
    }
    for path in sorted(evidence.glob("*index*.json")):
        rel = relative_path(path, root)
        try:
            data = load_json(path)
        except BoosterError as exc:
            issues.append(issue("error", "index-json", rel, str(exc)))
            continue
        if not uses_current_schema(data):
            issues.append(issue("error", "index-schema", rel, f"schema_version must be {SCHEMA_VERSION}"))
            continue
        entries = data.get("entries")
        if not isinstance(entries, list):
            issues.append(issue("error", "index-schema", rel, "entries must be an array"))
            continue
        counts = data.get("counts")
        count_fields = ["form_packs", "sector_packs", "refs", "modes", "entries"]
        if not isinstance(counts, dict) or any(
            type(counts.get(field)) is not int or counts[field] < 0 for field in count_fields
        ):
            issues.append(
                issue("error", "index-schema", rel, "counts must contain nonnegative integer totals")
            )
        else:
            forms, sectors = package_paths(root)
            expected_counts = {
                "form_packs": len(forms),
                "sector_packs": len(sectors),
                "refs": sum(
                    isinstance(entry, dict) and entry.get("kind") == "ref" for entry in entries
                ),
                "modes": sum(
                    isinstance(entry, dict) and entry.get("kind") == "mode" for entry in entries
                ),
                "entries": len(entries),
            }
            if counts != expected_counts:
                issues.append(
                    issue(
                        "error",
                        "index-counts",
                        rel,
                        "counts must match the indexed entries and current package catalog",
                    )
                )
        ids: set[str] = set()
        for index, entry in enumerate(entries):
            location = f"{rel}#entries[{index}]"
            if not isinstance(entry, dict):
                issues.append(issue("error", "index-entry", location, "entry must be an object"))
                continue
            string_fields = [
                "id",
                "kind",
                "axis",
                "package",
                "title",
                "provenance",
                "date",
                "path",
                "pole",
                "content_sha256",
            ]
            for field in string_fields:
                value = entry.get(field)
                if not isinstance(value, str) or not value.strip():
                    issues.append(
                        issue("error", "index-field", location, f"{field} must be a nonempty string")
                    )
            kind = entry.get("kind")
            if not isinstance(kind, str) or kind not in {"ref", "mode"}:
                issues.append(issue("error", "index-field", location, "kind must be ref or mode"))
            axis = entry.get("axis")
            if not isinstance(axis, str) or axis not in {"form", "sector"}:
                issues.append(issue("error", "index-field", location, "axis must be form or sector"))
            status = entry.get("status")
            if not isinstance(status, str) or status not in VALID_SOURCE_STATUSES:
                issues.append(issue("error", "index-field", location, "status is invalid"))
            date = entry.get("date")
            if not isinstance(date, str) or not _valid_date(date):
                issues.append(issue("error", "index-field", location, "date must be YYYY-MM-DD"))
            entry_path = entry.get("path")
            if isinstance(entry_path, str) and entry_path.strip():
                lexical = Path(entry_path)
                target = root / lexical
                if (
                    lexical.is_absolute()
                    or ".." in lexical.parts
                    or target.is_symlink()
                    or not target.is_file()
                    or not entry_path.startswith("packages/")
                ):
                    issues.append(
                        issue(
                            "error",
                            "index-field",
                            location,
                            "path must identify a regular package reference",
                        )
                    )
                expected_entry = generated_by_path.get(entry_path)
                if expected_entry is None or entry != expected_entry:
                    issues.append(
                        issue(
                            "error",
                            "index-entry-drift",
                            location,
                            "entry metadata does not match the generated metadata for its path",
                        )
                    )
            content_digest = entry.get("content_sha256")
            if not isinstance(content_digest, str) or not re.fullmatch(
                r"[0-9a-f]{64}", content_digest
            ):
                issues.append(
                    issue("error", "index-field", location, "content_sha256 must be lowercase SHA-256")
                )
            elif isinstance(entry_path, str) and (root / entry_path).is_file():
                actual_digest = hashlib.sha256((root / entry_path).read_bytes()).hexdigest()
                if content_digest != actual_digest:
                    issues.append(
                        issue(
                            "error",
                            "index-field",
                            location,
                            "content_sha256 does not match the referenced file",
                        )
                    )
            entry_id = entry.get("id")
            if isinstance(entry_id, str):
                if entry_id in ids:
                    issues.append(issue("error", "index-id-duplicate", location, f"duplicate id {entry_id}"))
                ids.add(entry_id)
        if path.resolve() == (root / DEFAULT_INDEX_PATH).resolve():
            if data != generated_index:
                issues.append(
                    issue(
                        "error",
                        "index-stale",
                        rel,
                        "generated index does not match the current package library",
                    )
                )


def _validate_marker(root: Path, issues: list[dict[str, str]]) -> None:
    path = root / "booster.json"
    rel = relative_path(path, root)
    try:
        data = load_json(path)
    except BoosterError as exc:
        issues.append(issue("error", "marker-json", rel, str(exc)))
        return
    if not isinstance(data, dict):
        issues.append(issue("error", "marker-schema", rel, "marker must be an object"))
        return
    if not is_booster_ownership_marker(data):
        issues.append(
            issue(
                "error",
                "marker-schema",
                rel,
                f"marker ownership fields and schema_version {SCHEMA_VERSION} must be valid",
            )
        )
        return

    expected_skills = data.get("skills")
    if expected_skills != REQUIRED_SKILLS:
        issues.append(
            issue(
                "error",
                "marker-skills",
                rel,
                f"skills must equal the release inventory: {', '.join(REQUIRED_SKILLS)}",
            )
        )
    else:
        actual_skills = sorted(path.parent.name for path in root.glob("skills/*/SKILL.md"))
        if sorted(REQUIRED_SKILLS) != actual_skills:
            issues.append(
                issue(
                    "error",
                    "managed-skills-mismatch",
                    rel,
                    f"skills expected {', '.join(sorted(expected_skills))}; filesystem has {', '.join(actual_skills)}",
                )
            )

    required_paths = data.get("required_managed_paths")
    if required_paths != REQUIRED_MANAGED_PATHS:
        issues.append(
            issue(
                "error",
                "marker-paths",
                rel,
                "required_managed_paths must equal the validator's release inventory",
            )
        )
        return
    for value in required_paths:
        if not isinstance(value, str) or not value:
            issues.append(issue("error", "marker-paths", rel, "required paths must be strings"))
            continue
        candidate = Path(value)
        if candidate.is_absolute() or ".." in candidate.parts:
            issues.append(issue("error", "marker-paths", rel, f"unsafe required path {value!r}"))
            continue
        managed_path = root / candidate
        if not managed_path.is_file() or managed_path.stat().st_size == 0:
            issues.append(
                issue("error", "managed-path-missing", value, "required managed file is missing or empty")
            )


def _validate_managed_symlinks(root: Path, issues: list[dict[str, str]]) -> None:
    for relative in ["DESIGN.md", "README.md", "booster.json"]:
        if (root / relative).is_symlink():
            issues.append(
                issue("error", "managed-symlink", relative, "repository root file cannot be a symlink")
            )
    for relative in ["packages", "notes", "tools", "evidence", "skills"]:
        managed_root = root / relative
        if managed_root.is_symlink():
            issues.append(issue("error", "managed-symlink", relative, "managed root cannot be a symlink"))
            continue
        if not managed_root.is_dir():
            continue
        for path in managed_root.rglob("*"):
            if path.is_symlink():
                issues.append(
                    issue(
                        "error",
                        "managed-symlink",
                        relative_path(path, root),
                        "managed content cannot be a symlink",
                    )
                )
            elif not path.is_dir() and not path.is_file():
                issues.append(
                    issue(
                        "error",
                        "managed-special",
                        relative_path(path, root),
                        "managed content must be a regular file or directory",
                    )
                )


def validate_repository(root: Path) -> dict[str, Any]:
    issues: list[dict[str, str]] = []
    required_files = [
        "DESIGN.md",
        "README.md",
        "booster.json",
        *REQUIRED_MANAGED_PATHS,
    ]
    for rel in required_files:
        path = root / rel
        if path.is_symlink():
            issues.append(issue("error", "managed-symlink", rel, "required file cannot be a symlink"))
        elif not path.exists():
            issues.append(issue("error", "structure-missing", rel, "required path is missing"))
        elif not path.is_file():
            issues.append(issue("error", "structure-type", rel, "required path must be a file"))
    for rel in ["packages", "notes", "tools", "evidence", "skills"]:
        path = root / rel
        if path.is_symlink():
            issues.append(issue("error", "managed-symlink", rel, "required directory cannot be a symlink"))
        elif not path.exists():
            issues.append(issue("error", "structure-missing", rel, "required path is missing"))
        elif not path.is_dir():
            issues.append(issue("error", "structure-type", rel, "required path must be a directory"))
    if issues:
        return _validation_result(root, issues)

    _validate_readme_counts(root, issues)
    _validate_readme_contract(root, issues)
    _validate_marker(root, issues)
    _validate_managed_symlinks(root, issues)
    _validate_owned_documents(root, issues)
    _validate_tool_contract(root, issues)
    _validate_skills(root, issues)
    _validate_pack_contracts(root, issues)
    _validate_reference_metadata(root, issues)
    _validate_range_maps(root, issues)
    _validate_bans(root, issues)
    _validate_observations(root, issues)
    _validate_generated_indexes(root, issues)
    return _validation_result(root, issues)


def is_installed_layout(root: Path) -> bool:
    local_design = root / "DESIGN.md"
    receipt = root / INSTALL_RECEIPT_PATH
    return (
        root.name == "design"
        and not local_design.exists()
        and not local_design.is_symlink()
        and (receipt.exists() or receipt.is_symlink())
    )


def validate_installed_library(root: Path) -> dict[str, Any]:
    issues: list[dict[str, str]] = []
    design = booster_design_path(root)
    required_files = [
        design,
        root / "booster.json",
        root / INSTALL_RECEIPT_PATH,
        root / "notes/gwern.md",
        root / "notes/comparables-2026-08.md",
        root / "tools/booster.py",
        root / DEFAULT_BANS_PATH,
        root / DEFAULT_OBSERVATIONS_PATH,
        root / DEFAULT_INDEX_PATH,
    ]
    for path in required_files:
        if path.is_symlink() or not path.is_file():
            issues.append(
                issue(
                    "error",
                    "install-structure",
                    path.as_posix(),
                    "required installed path is missing or unsafe",
                )
            )
    for path in [root / "packages", root / "notes", root / "tools", root / "evidence"]:
        if path.is_symlink() or not path.is_dir():
            issues.append(
                issue(
                    "error",
                    "install-structure",
                    path.as_posix(),
                    "required installed directory is missing or unsafe",
                )
            )
    if issues:
        return _validation_result(root, issues)

    receipt_path = root / INSTALL_RECEIPT_PATH
    try:
        receipt = load_json(receipt_path)
    except BoosterError as exc:
        issues.append(issue("error", "install-receipt", receipt_path.as_posix(), str(exc)))
    else:
        if not (
            uses_current_schema(receipt)
            and receipt.get("name") == "booster-installed-library"
        ):
            issues.append(
                issue(
                    "error",
                    "install-receipt",
                    receipt_path.as_posix(),
                    "installed layout receipt is invalid",
                )
            )

    marker_path = root / "booster.json"
    try:
        marker = load_json(marker_path)
    except BoosterError as exc:
        issues.append(issue("error", "marker-json", marker_path.as_posix(), str(exc)))
    else:
        if not has_release_inventory(marker):
            issues.append(
                issue(
                    "error",
                    "marker-schema",
                    marker_path.as_posix(),
                    "installed library marker does not match this release inventory",
                )
            )

    _validate_markdown_contract(
        root,
        issues,
        design.as_posix(),
        "# Design invariants",
        DESIGN_SECTIONS,
        source_path=design,
    )
    _validate_managed_symlinks(root, issues)
    _validate_owned_documents(root, issues)
    _validate_tool_contract(root, issues)
    _validate_pack_contracts(root, issues)
    _validate_reference_metadata(root, issues)
    _validate_range_maps(root, issues)
    _validate_bans(root, issues)
    _validate_observations(root, issues)
    _validate_generated_indexes(root, issues)
    return _validation_result(root, issues)


def _validation_result(root: Path, issues: list[dict[str, str]]) -> dict[str, Any]:
    errors = sum(item["severity"] == "error" for item in issues)
    warnings = sum(item["severity"] == "warning" for item in issues)
    return {
        "valid": errors == 0,
        "root": root.as_posix(),
        "errors": errors,
        "warnings": warnings,
        "issues": issues,
    }


def normalize_pattern(pattern: str) -> str:
    return " ".join(TOKEN_RE.findall(pattern.lower()))


def pattern_key(pattern: str) -> str:
    normalized = normalize_pattern(pattern)
    return "pattern-" + hashlib.sha256(normalized.encode("utf-8")).hexdigest()[:12]


def make_observation(
    *,
    pattern: str,
    subject: str,
    model: str,
    artifact: str,
    note: str,
    date: str,
    screenshot: str | None = None,
) -> dict[str, Any]:
    values = {
        "pattern": pattern.strip(),
        "subject": subject.strip(),
        "model": model.strip(),
        "artifact": artifact.strip(),
        "note": note.strip(),
        "date": date.strip(),
    }
    missing = [key for key, value in values.items() if not value]
    if missing:
        raise BoosterError(f"observation fields cannot be empty: {', '.join(missing)}")
    if not _valid_date(values["date"]):
        raise BoosterError("--date must be a valid YYYY-MM-DD date")
    if not normalize_pattern(values["pattern"]):
        raise BoosterError("--pattern must contain at least one letter or number")
    normalized_screenshot = screenshot.strip() if screenshot and screenshot.strip() else None
    key = pattern_key(values["pattern"])
    identity = json.dumps(
        {**values, "screenshot": normalized_screenshot}, sort_keys=True, ensure_ascii=False
    )
    observation_id = "observation-" + hashlib.sha256(identity.encode("utf-8")).hexdigest()[:12]
    return {
        "id": observation_id,
        "pattern_key": key,
        "pattern": values["pattern"],
        "subject": values["subject"],
        "model": values["model"],
        "artifact": values["artifact"],
        "screenshot": normalized_screenshot,
        "date": values["date"],
        "note": values["note"],
        "outcome": "rejected",
    }


def observation_integrity_errors(value: Any) -> list[tuple[str, str]]:
    if not isinstance(value, dict):
        return [("observation-entry", "observation must be an object")]
    errors: list[tuple[str, str]] = []
    required = ["id", "pattern_key", "pattern", "subject", "model", "artifact", "date", "note"]
    for field in required:
        field_value = value.get(field)
        if not isinstance(field_value, str) or not field_value.strip():
            errors.append(("observation-field", f"{field} is required"))
        elif field_value != field_value.strip():
            errors.append(("observation-field", f"{field} must not have surrounding whitespace"))
    screenshot = value.get("screenshot")
    if screenshot is not None and (not isinstance(screenshot, str) or not screenshot.strip()):
        errors.append(("observation-screenshot", "screenshot must be a nonempty string or null"))
    elif isinstance(screenshot, str) and screenshot != screenshot.strip():
        errors.append(("observation-screenshot", "screenshot must not have surrounding whitespace"))
    if value.get("outcome") != "rejected":
        errors.append(("observation-outcome", "outcome must be rejected"))
    date = value.get("date")
    if isinstance(date, str) and date.strip() and not _valid_date(date):
        errors.append(("observation-date", "date must be YYYY-MM-DD"))
    base_fields_valid = all(
        isinstance(value.get(field), str) and value[field].strip()
        for field in ["pattern", "subject", "model", "artifact", "date", "note"]
    )
    if base_fields_valid and isinstance(screenshot, (str, type(None))):
        try:
            expected = make_observation(
                pattern=value["pattern"],
                subject=value["subject"],
                model=value["model"],
                artifact=value["artifact"],
                note=value["note"],
                date=value["date"],
                screenshot=screenshot,
            )
        except BoosterError as exc:
            errors.append(("observation-integrity", str(exc)))
        else:
            if value.get("pattern_key") != expected["pattern_key"]:
                errors.append(
                    ("observation-pattern-key", "pattern_key does not match the normalized pattern")
                )
            if value.get("id") != expected["id"]:
                errors.append(("observation-id", "id does not match the observation contents"))
    return errors


@contextmanager
def observation_lock(path: Path) -> Iterable[None]:
    if not path.parent.is_dir():
        raise BoosterError(f"observation directory does not exist: {path.parent}")
    lock_path = path.with_name(path.name + ".lock")
    flags = os.O_CREAT | os.O_RDWR
    if hasattr(os, "O_NOFOLLOW"):
        flags |= os.O_NOFOLLOW
    try:
        descriptor = os.open(lock_path, flags, 0o600)
        handle = os.fdopen(descriptor, "a+", encoding="utf-8")
    except OSError as exc:
        raise BoosterError(f"cannot open observation lock {lock_path}: {exc}") from exc
    try:
        fcntl.flock(handle.fileno(), fcntl.LOCK_EX)
        yield
    except OSError as exc:
        raise BoosterError(f"cannot lock observation registry {path}: {exc}") from exc
    finally:
        try:
            fcntl.flock(handle.fileno(), fcntl.LOCK_UN)
        finally:
            handle.close()


def record_observation(path: Path, observation: dict[str, Any]) -> bool:
    new_errors = observation_integrity_errors(observation)
    if new_errors:
        raise BoosterError(f"invalid observation: {new_errors[0][1]}")
    with observation_lock(path):
        data = load_json(path)
        if not uses_current_schema(data):
            raise BoosterError(f"{path} does not use observation schema version {SCHEMA_VERSION}")
        observations = data.get("observations")
        if not isinstance(observations, list):
            raise BoosterError(f"{path} field observations must be an array")
        for existing in observations:
            existing_errors = observation_integrity_errors(existing)
            if existing_errors:
                raise BoosterError(f"invalid existing observation: {existing_errors[0][1]}")
        if any(item["id"] == observation["id"] for item in observations):
            return False
        observations.append(observation)
        observations.sort(key=lambda item: (item["date"], item["id"]))
        write_json(path, data)
        return True


def merge_observations(target: Path, source: Path) -> dict[str, int]:
    if source.is_symlink() or not source.is_file():
        raise BoosterError(f"observation merge source is missing or unsafe: {source}")
    source_data = load_json(source)
    if not uses_current_schema(source_data):
        raise BoosterError(f"{source} does not use observation schema version {SCHEMA_VERSION}")
    source_entries = source_data.get("observations")
    if not isinstance(source_entries, list):
        raise BoosterError(f"{source} field observations must be an array")
    source_by_id: dict[str, dict[str, Any]] = {}
    for entry in source_entries:
        entry_errors = observation_integrity_errors(entry)
        if entry_errors:
            raise BoosterError(f"invalid source observation: {entry_errors[0][1]}")
        if entry["id"] in source_by_id:
            raise BoosterError(f"duplicate source observation ID: {entry['id']}")
        source_by_id[entry["id"]] = entry

    with observation_lock(target):
        target_data = load_json(target)
        if not uses_current_schema(target_data):
            raise BoosterError(f"{target} does not use observation schema version {SCHEMA_VERSION}")
        target_entries = target_data.get("observations")
        if not isinstance(target_entries, list):
            raise BoosterError(f"{target} field observations must be an array")
        target_by_id: dict[str, dict[str, Any]] = {}
        for entry in target_entries:
            entry_errors = observation_integrity_errors(entry)
            if entry_errors:
                raise BoosterError(f"invalid target observation: {entry_errors[0][1]}")
            if entry["id"] in target_by_id:
                raise BoosterError(f"duplicate target observation ID: {entry['id']}")
            target_by_id[entry["id"]] = entry
        added = 0
        for observation_id, entry in source_by_id.items():
            if observation_id not in target_by_id:
                target_entries.append(entry)
                target_by_id[observation_id] = entry
                added += 1
        if added:
            target_entries.sort(key=lambda item: (item["date"], item["id"]))
            write_json(target, target_data)
        return {"added": added, "total": len(target_entries)}


def aggregate_candidates(observations: Sequence[dict[str, Any]], min_count: int = 3) -> list[dict[str, Any]]:
    if min_count < 2:
        raise BoosterError("--min-count must be at least 2 for repeated evidence")
    groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for observation in observations:
        if not isinstance(observation, dict) or observation.get("outcome") != "rejected":
            continue
        key = observation.get("pattern_key")
        if isinstance(key, str):
            groups[key].append(observation)

    candidates: list[dict[str, Any]] = []
    for key, group in groups.items():
        artifacts = sorted({str(item.get("artifact")) for item in group if item.get("artifact")})
        if len(artifacts) < min_count:
            continue
        ordered = sorted(group, key=lambda item: (item.get("date", ""), item.get("id", "")))
        candidates.append(
            {
                "pattern_key": key,
                "pattern": ordered[0].get("pattern", ""),
                "independent_count": len(artifacts),
                "observation_count": len(group),
                "artifacts": artifacts,
                "first_seen": ordered[0].get("date"),
                "last_seen": ordered[-1].get("date"),
            }
        )
    candidates.sort(key=lambda item: (-item["independent_count"], item["pattern_key"]))
    return candidates


def toon_scalar(value: Any) -> str:
    if value is None:
        return "null"
    if value is True:
        return "true"
    if value is False:
        return "false"
    if isinstance(value, float) and value.is_integer():
        return str(int(value))
    if isinstance(value, (int, float)):
        return str(value).lower()
    string = str(value)
    primitive = string in {"true", "false", "null"} or re.fullmatch(
        r"[+-]?[0-9]+(?:\.[0-9]+)?(?:e[+-]?[0-9]+)?", string, flags=re.IGNORECASE
    )
    unsafe = (
        not string
        or string != string.strip()
        or primitive
        or string.startswith(("#", "-"))
        or any(ord(char) < 0x20 for char in string)
        or any(char in string for char in [",", ":", "[", "]", "{", "}", '"', "\\"])
    )
    if not unsafe:
        return string
    encoded = json.dumps(string, ensure_ascii=False)
    output: list[str] = []
    index = 0
    while index < len(encoded):
        character = encoded[index]
        if character == "\\" and index + 1 < len(encoded):
            escape = encoded[index + 1]
            if escape == "b":
                output.append("\\u0008")
            elif escape == "f":
                output.append("\\u000c")
            else:
                output.extend((character, escape))
            index += 2
            continue
        output.append(character)
        index += 1
    return "".join(output)


def toon_table(name: str, rows: Sequence[dict[str, Any]], fields: Sequence[str]) -> str:
    if not rows:
        return f"{name}: []"
    header = f"{name}[{len(rows)}]{{{','.join(fields)}}}:"
    body = [
        "  " + ",".join(toon_scalar(row.get(field)) for field in fields)
        for row in rows
    ]
    return "\n".join([header, *body])


def toon_list(name: str, values: Sequence[str]) -> str:
    if not values:
        return f"{name}: []"
    return f"{name}[{len(values)}]: " + ",".join(toon_scalar(value) for value in values)


def emit_json(value: Any) -> None:
    print(json.dumps(value, indent=2, ensure_ascii=False))


def executable_label() -> str:
    executable = Path(__file__).resolve().as_posix()
    home = Path.home().as_posix()
    if executable.startswith(home + "/"):
        return "~/" + executable[len(home) + 1 :]
    return executable


def executable_command() -> str:
    return f"python3 {shlex.quote(Path(__file__).resolve().as_posix())}"


def home_view(root: Path) -> str:
    executable = executable_label()
    command = executable_command()
    require_catalog_root(root)
    index = build_reference_index(root)
    counts = index["counts"]
    lines = [
            f"bin: {executable}",
            "description: Search, validate, and grow Booster's evidence-backed design library",
            "catalog:",
            f"  form_packs: {counts['form_packs']}",
            f"  sector_packs: {counts['sector_packs']}",
            f"  refs: {counts['refs']}",
            f"  modes: {counts['modes']}",
    ]
    lines.extend(
        toon_list(
            "help",
            [
            f'Run `{command} search "<brief>" --form <form> --sector <sector>` for four diverse refs',
            f"Run `{command} validate --root <repo>` to check the library",
            f"Run `{command} index --root <repo> --write evidence/reference-index.json` to write JSON",
            f"Run `{command} observe --help` to record an explicit rejection",
            f"Run `{command} candidates --min-count 2` to surface repeated patterns",
            ],
        ).splitlines()
    )
    return "\n".join(lines)


def evidence_output_path(root: Path, value: str | Path) -> Path:
    path = Path(value).expanduser()
    path = path if path.is_absolute() else root / path
    lexical = Path(os.path.abspath(path))
    expected = Path(os.path.abspath(root / DEFAULT_INDEX_PATH))
    if lexical != expected:
        raise BoosterError(f"generated index path must be {DEFAULT_INDEX_PATH.as_posix()}")
    if lexical.is_symlink() or (lexical.exists() and not lexical.is_file()):
        raise BoosterError(f"generated index destination is not a regular file: {lexical}")
    return lexical


def require_catalog_root(root: Path) -> None:
    if not root.is_dir():
        raise BoosterError(f"Booster root does not exist: {root}")
    marker = root / "booster.json"
    if marker.is_symlink() or not marker.is_file():
        raise BoosterError(f"Booster ownership marker is missing or unsafe: {marker}")
    data = load_json(marker)
    installed = is_installed_layout(root)
    if installed:
        receipt_path = root / INSTALL_RECEIPT_PATH
        if receipt_path.is_symlink() or not receipt_path.is_file():
            raise BoosterError(f"Booster install receipt is missing or unsafe: {receipt_path}")
        receipt = load_json(receipt_path)
        if not is_install_receipt(receipt):
            raise BoosterError(f"invalid Booster install receipt: {receipt_path}")
        if not is_booster_ownership_marker(data):
            raise BoosterError(f"invalid Booster ownership marker: {marker}")
    elif not has_release_inventory(data):
        raise BoosterError(f"Booster ownership marker does not match this release: {marker}")
    design = booster_design_path(root)
    packages = root / "packages"
    if design.is_symlink() or not design.is_file():
        raise BoosterError(f"Booster design doctrine is missing or unsafe: {design}")
    if packages.is_symlink() or not packages.is_dir():
        raise BoosterError(f"Booster package library is missing or unsafe: {packages}")
    forms, sectors = package_paths(root)
    if not forms or not sectors:
        raise BoosterError(f"Booster package library is incomplete: {packages}")


def require_managed_mutation_root(root: Path, registry: Path | None = None) -> None:
    require_catalog_root(root)
    evidence = root / "evidence"
    if evidence.is_symlink() or not evidence.is_dir():
        raise BoosterError(f"Booster evidence directory is missing or unsafe: {evidence}")
    if registry is not None:
        path = root / registry
        if path.is_symlink() or not path.is_file():
            raise BoosterError(f"required Booster registry is missing or unsafe: {path}")


def update_readme_counts(root: Path, index: dict[str, Any]) -> None:
    path = root / "README.md"
    text = read_text(path)
    counts = index["counts"]
    replacements = {
        "form_packs": counts["form_packs"],
        "sector_packs": counts["sector_packs"],
        "distilled_refs": counts["refs"],
        "sector_modes": counts["modes"],
        "design_bans": len(parse_design_bans(root / "DESIGN.md")),
    }
    for label, count in replacements.items():
        text, changed = re.subn(
            rf"(badge/{re.escape(label)}-)\d+(-)",
            rf"\g<1>{count}\g<2>",
            text,
        )
        if changed != 1:
            raise BoosterError(f"README.md must contain exactly one {label} badge")
    temporary = path.with_name(f".{path.name}.{os.getpid()}.tmp")
    try:
        temporary.write_text(text, encoding="utf-8", newline="\n")
        os.replace(temporary, path)
    except OSError as exc:
        temporary.unlink(missing_ok=True)
        raise BoosterError(f"cannot update {path}: {exc}") from exc


def managed_content_sizes(root: Path) -> dict[str, int]:
    paths = [root / "DESIGN.md", root / "README.md", root / "booster.json"]
    for directory in ["packages", "notes", "skills", "evidence", "tools"]:
        managed_root = root / directory
        if managed_root.is_dir() and not managed_root.is_symlink():
            paths.extend(managed_root.rglob("*"))
    sizes: dict[str, int] = {}
    for path in paths:
        if (
            path.is_symlink()
            or not path.is_file()
            or path.name.endswith(".lock")
            or "__pycache__" in path.parts
            or path.suffix in {".pyc", ".pyo"}
        ):
            continue
        sizes[relative_path(path, root)] = path.stat().st_size
    return sizes


def reference_inventory_diff(baseline: Path, candidate: Path) -> dict[str, Any]:
    def identities(root: Path) -> set[str]:
        forms, sectors = package_paths(root)
        index = build_reference_index(root)
        result = {
            *(f"form-pack.{path.parent.name}" for path in forms),
            *(f"sector-pack.{path.parent.name}" for path in sectors),
            *(entry["id"] for entry in index["entries"]),
            *(f"ban.{ban['id']}" for ban in parse_design_bans(root / "DESIGN.md")),
            *(f"managed-file.{path}" for path in managed_content_sizes(root)),
        }
        observation_data = load_json(root / DEFAULT_OBSERVATIONS_PATH)
        observations = (
            observation_data.get("observations") if isinstance(observation_data, dict) else None
        )
        if not isinstance(observations, list):
            raise BoosterError(
                f"{root / DEFAULT_OBSERVATIONS_PATH} field observations must be an array"
            )
        for observation in observations:
            if not isinstance(observation, dict) or not isinstance(observation.get("id"), str):
                raise BoosterError(f"invalid observation in {root / DEFAULT_OBSERVATIONS_PATH}")
            result.add(f"observation.{observation['id']}")
        return result

    baseline_entries = identities(baseline)
    candidate_entries = identities(candidate)
    baseline_sizes = managed_content_sizes(baseline)
    candidate_sizes = managed_content_sizes(candidate)
    shrunk = [
        {
            "path": path,
            "before_bytes": before,
            "after_bytes": candidate_sizes[path],
        }
        for path, before in baseline_sizes.items()
        if path in candidate_sizes
        and before >= 80
        and candidate_sizes[path] * 100 < before * 60
    ]
    shrunk.sort(key=lambda item: item["path"])
    return {
        "added": sorted(candidate_entries - baseline_entries),
        "removed": sorted(baseline_entries - candidate_entries),
        "shrunk": shrunk,
    }


def build_parser() -> AxiArgumentParser:
    parser = AxiArgumentParser(
        prog="booster.py",
        description="Search, validate, and grow Booster's design evidence.",
    )
    subparsers = parser.add_subparsers(dest="command")

    index = subparsers.add_parser("index", help="scan refs and modes into a stable index")
    index.add_argument("--root", help="Booster repository root (default: script library root)")
    index.add_argument("--write", help="write JSON under evidence/, for example evidence/reference-index.json")
    index.add_argument("--update-readme", action="store_true", help="refresh generated catalog badges")
    index.add_argument("--json", action="store_true", help="print the full index as JSON")

    search = subparsers.add_parser("search", help="return relevant, pole-diverse refs")
    search.add_argument("query", help="brief or design terms to retrieve")
    search.add_argument("--form", help="limit to one form package")
    search.add_argument("--sector", help="also search one sector package")
    search.add_argument("--limit", type=int, default=4, help="number of refs (default: 4)")
    search.add_argument("--root", help="Booster library root (default: script library root)")
    search.add_argument("--json", action="store_true", help="print JSON instead of TOON")

    validate = subparsers.add_parser("validate", help="validate repository and evidence integrity")
    validate.add_argument("--root", help="Booster repository root (default: script library root)")
    validate.add_argument("--json", action="store_true", help="print JSON instead of TOON")

    observe = subparsers.add_parser("observe", help="record an explicit rejected pattern")
    observe.add_argument("--pattern", required=True, help="rejected visual or copy pattern")
    observe.add_argument("--subject", required=True, help="brief subject where it appeared")
    observe.add_argument("--model", required=True, help="model or build surface that produced it")
    observe.add_argument("--artifact", required=True, help="independent build path or URL")
    observe.add_argument("--note", required=True, help="the user's exact rejection or faithful note")
    observe.add_argument("--screenshot", help="optional screenshot path or URL")
    observe.add_argument("--date", default=dt.date.today().isoformat(), help="YYYY-MM-DD (default: today)")
    observe.add_argument("--root", help="Booster library root (default: script library root)")
    observe.add_argument("--json", action="store_true", help="print JSON instead of TOON")

    candidates = subparsers.add_parser("candidates", help="list repeated rejection patterns")
    candidates.add_argument("--min-count", type=int, default=2, help="independent artifacts required (default: 2)")
    candidates.add_argument("--root", help="Booster library root (default: script library root)")
    candidates.add_argument("--json", action="store_true", help="print JSON instead of TOON")

    merge = subparsers.add_parser("observations-merge", help="merge a validated observation registry")
    merge.add_argument("--from", dest="source", required=True, help="source observations.json")
    merge.add_argument("--root", help="target Booster library root (default: script library root)")
    merge.add_argument("--json", action="store_true", help="print JSON instead of TOON")

    inventory = subparsers.add_parser("inventory-diff", help="compare managed package, ref, and mode identities")
    inventory.add_argument("--baseline", required=True, help="baseline Booster repository root")
    inventory.add_argument("--candidate", required=True, help="candidate Booster repository root")
    inventory.add_argument("--allow-removals", action="store_true", help="accept explicitly reviewed removals")
    inventory.add_argument("--json", action="store_true", help="print JSON instead of TOON")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args_list = list(sys.argv[1:] if argv is None else argv)
    if len(args_list) == 1 and args_list[0] in {"-v", "-V", "--version"}:
        print(VERSION)
        return 0
    parser = build_parser()
    if not args_list:
        try:
            print(home_view(default_root()))
            return 0
        except BoosterError as exc:
            print(f"error: {toon_scalar(str(exc))}")
            print(
                toon_list(
                    "help", [f"Run `{executable_command()} --help` for available commands"]
                )
            )
            return 1
    json_requested = "--json" in args_list
    try:
        args, unknown = parser.parse_known_args(args_list)
    except BoosterUsageError as exc:
        help_text = f"Run `{executable_command()} --help` for valid inputs"
        if json_requested:
            emit_json({"error": str(exc), "help": help_text})
        else:
            print(f"error: {toon_scalar(str(exc))}")
            print(toon_list("help", [help_text]))
        return 2
    if unknown:
        message = f"unrecognized arguments: {' '.join(unknown)}"
        command = f" {args.command}" if args.command else ""
        help_text = f"Run `{executable_command()}{command} --help` for valid inputs"
        if json_requested:
            emit_json({"error": message, "help": help_text})
        else:
            print(f"error: {toon_scalar(message)}")
            print(toon_list("help", [help_text]))
        return 2
    if not args.command:
        help_text = f"Run `{executable_command()} --help` for available commands"
        if json_requested:
            emit_json({"error": "a command is required", "help": help_text})
        else:
            print(f"error: {toon_scalar('a command is required')}")
            print(toon_list("help", [help_text]))
        return 2
    root = resolve_root(getattr(args, "root", None))

    try:
        if args.command == "index":
            require_catalog_root(root)
            index = build_reference_index(root)
            if args.update_readme and not args.write:
                raise BoosterError("--update-readme requires --write")
            if args.write:
                require_managed_mutation_root(root)
                destination = evidence_output_path(root, args.write)
                write_json(destination, index)
                if args.update_readme:
                    update_readme_counts(root, index)
                if args.json:
                    emit_json(index)
                else:
                    counts = index["counts"]
                    print("index:")
                    print(f"  path: {relative_path(destination, root)}")
                    print(f"  entries: {counts['entries']}")
                    print(f"  refs: {counts['refs']}")
                    print(f"  modes: {counts['modes']}")
            elif args.json:
                emit_json(index)
            else:
                counts = index["counts"]
                print("index:")
                print(f"  entries: {counts['entries']}")
                print(f"  refs: {counts['refs']}")
                print(f"  modes: {counts['modes']}")
                print(
                    toon_list(
                        "help",
                        [
                            f"Run `{executable_command()} index --json` to print every indexed entry",
                            f"Run `{executable_command()} index --write evidence/reference-index.json` to update the generated index",
                        ],
                    )
                )
            return 0

        if args.command == "inventory-diff":
            baseline = resolve_root(args.baseline)
            candidate = resolve_root(args.candidate)
            result = reference_inventory_diff(baseline, candidate)
            denied = bool((result["removed"] or result["shrunk"]) and not args.allow_removals)
            if args.json:
                response = dict(result)
                if denied:
                    response["error"] = (
                        "managed identity removals or major content shrinkage require --allow-removals"
                    )
                emit_json(response)
            else:
                print(toon_table("added", [{"id": value} for value in result["added"]], ["id"]))
                print(toon_table("removed", [{"id": value} for value in result["removed"]], ["id"]))
                print(
                    toon_table(
                        "shrunk",
                        result["shrunk"],
                        ["path", "before_bytes", "after_bytes"],
                    )
                )
                if denied:
                    print(
                        "error: managed identity removals or major content shrinkage require --allow-removals"
                    )
            if denied:
                return 1
            return 0

        if args.command == "search":
            require_catalog_root(root)
            results = search_references(
                root,
                args.query,
                form=args.form,
                sector=args.sector,
                limit=args.limit,
            )
            if not results:
                diagnosis = diagnose_empty_search(
                    root,
                    args.query,
                    form=args.form,
                    sector=args.sector,
                )
                help_text = empty_search_help(diagnosis)
                if args.json:
                    emit_json(
                        {
                            "count": 0,
                            "results": [],
                            "empty": diagnosis,
                            "help": help_text,
                        }
                    )
                else:
                    print(toon_table("refs", [], ["id", "path", "pole", "score"]))
                    print("empty:")
                    print(f"  reason: {toon_scalar(diagnosis['reason'])}")
                    print(f"  query: {toon_scalar(diagnosis['query'])}")
                    print(f"  form: {toon_scalar(diagnosis['form'])}")
                    print(f"  sector: {toon_scalar(diagnosis['sector'])}")
                    if diagnosis.get("uncovered"):
                        print(f"  uncovered: {toon_scalar(diagnosis['uncovered'])}")
                    print(toon_list("available_forms", diagnosis["available_forms"]))
                    print(toon_list("available_sectors", diagnosis["available_sectors"]))
                    print(toon_list("help", help_text))
                return 0
            if args.json:
                emit_json({"count": len(results), "results": results})
            else:
                print(toon_table("refs", results, ["id", "path", "pole", "score"]))
            return 0

        if args.command == "validate":
            result = validate_installed_library(root) if is_installed_layout(root) else validate_repository(root)
            if args.json:
                emit_json(result)
            else:
                print("validation:")
                print(f"  valid: {toon_scalar(result['valid'])}")
                print(f"  errors: {result['errors']}")
                print(f"  warnings: {result['warnings']}")
                print(
                    toon_table(
                        "issues",
                        result["issues"],
                        ["severity", "code", "path", "message"],
                    )
                )
            return 0 if result["valid"] else 1

        if args.command == "observe":
            require_managed_mutation_root(root, DEFAULT_OBSERVATIONS_PATH)
            observation_issues: list[dict[str, str]] = []
            _validate_observations(root, observation_issues)
            invalid_registry = next(
                (item for item in observation_issues if item["severity"] == "error"), None
            )
            if invalid_registry:
                raise BoosterError(
                    f"observation registry is invalid ({invalid_registry['code']}): {invalid_registry['message']}"
                )
            observation = make_observation(
                pattern=args.pattern,
                subject=args.subject,
                model=args.model,
                artifact=args.artifact,
                note=args.note,
                screenshot=args.screenshot,
                date=args.date,
            )
            path = root / DEFAULT_OBSERVATIONS_PATH
            created = record_observation(path, observation)
            response = {
                "id": observation["id"],
                "pattern_key": observation["pattern_key"],
                "status": "recorded" if created else "already-recorded",
                "path": relative_path(path, root),
            }
            if args.json:
                emit_json(response)
            else:
                print("observation:")
                for key, value in response.items():
                    print(f"  {key}: {toon_scalar(value)}")
            return 0

        if args.command == "observations-merge":
            require_managed_mutation_root(root, DEFAULT_OBSERVATIONS_PATH)
            source = Path(args.source).expanduser()
            source = source if source.is_absolute() else Path.cwd() / source
            result = merge_observations(root / DEFAULT_OBSERVATIONS_PATH, source)
            if args.json:
                emit_json(result)
            else:
                print("observation_merge:")
                print(f"  added: {result['added']}")
                print(f"  total: {result['total']}")
            return 0

        if args.command == "candidates":
            require_managed_mutation_root(root, DEFAULT_OBSERVATIONS_PATH)
            observation_issues = []
            _validate_observations(root, observation_issues)
            invalid_registry = next(
                (item for item in observation_issues if item["severity"] == "error"), None
            )
            if invalid_registry:
                raise BoosterError(
                    f"observation registry is invalid ({invalid_registry['code']}): {invalid_registry['message']}"
                )
            path = root / DEFAULT_OBSERVATIONS_PATH
            data = load_json(path)
            observations = data.get("observations", []) if isinstance(data, dict) else []
            if not isinstance(observations, list):
                raise BoosterError(f"{path} field observations must be an array")
            candidates = aggregate_candidates(observations, args.min_count)
            if args.json:
                emit_json({"count": len(candidates), "candidates": candidates})
            else:
                print(
                    toon_table(
                        "candidates",
                        candidates,
                        ["pattern_key", "pattern", "independent_count", "first_seen", "last_seen"],
                    )
                )
                if not candidates:
                    print(
                        toon_list(
                            "help",
                            [f"Run `{executable_command()} observe --help` to record explicit rejection evidence"],
                        )
                    )
            return 0
    except BoosterError as exc:
        if getattr(args, "json", False):
            if args.command == "validate":
                help_text = "fix the reported repository or evidence path, then rerun validate"
            else:
                help_text = f"run `{executable_command()} {args.command} --help` for valid inputs"
            emit_json({"error": str(exc), "help": help_text})
        else:
            print(f"error: {toon_scalar(str(exc))}")
            if args.command == "validate":
                print(
                    toon_list(
                        "help", ["Fix the reported repository or evidence path, then rerun validate"]
                    )
                )
            else:
                print(
                    toon_list(
                        "help",
                        [f"Run `{executable_command()} {args.command} --help` for valid inputs"],
                    )
                )
        return 1

    print(f"error: unsupported command {args.command}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
