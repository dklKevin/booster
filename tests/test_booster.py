from __future__ import annotations

import importlib.util
import io
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / "tools" / "booster.py"
SPEC = importlib.util.spec_from_file_location("booster_tool", MODULE_PATH)
assert SPEC and SPEC.loader
booster = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(booster)


class BoosterFixture:
    def __init__(self, root: Path) -> None:
        self.root = root

    def write(self, relative: str, content: str) -> None:
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    def build(self) -> None:
        self.write(
            "DESIGN.md",
            """# Design invariants

## Ban list (the mode, excised by name)

- **B001** Generic centered hero.

## Hard floors (non-negotiable)

- Text contrast and focus visibility pass before an artifact is considered ready.
- Animation respects prefers-reduced-motion at runtime.

## Design packages

- Read one form and one sector package, then choose only brief-specific evidence.
- Keep the context narrow at 2-3 refs total.
- Uncovered industries: civic, education, food/hospitality, hospitality, religion, sports.

## Evidence lifecycle

- Record repeated, independent evidence before any proposed ban can be promoted.
- Store explicit rejections in evidence/observations.json.

## Derive step (per artifact, before building)

- Derive three materially different directions grounded in the actual subject.
- Give each direction a compact ASCII wireframe.

## Photography integration (when the page carries photos)

- Plan crops deliberately and verify that subject placement survives responsive layouts.

## Judge step (after building)

- Review rendered evidence at mobile, laptop, and wide desktop sizes before release.
""",
        )
        readme = (MODULE_PATH.parents[1] / "README.md").read_text(encoding="utf-8")
        for label, count in {
            "form_packs": 1,
            "sector_packs": 1,
            "distilled_refs": 8,
            "sector_modes": 0,
            "design_bans": 1,
        }.items():
            readme = re.sub(
                rf"(badge/{label}-)\d+(-)", rf"\g<1>{count}\2", readme
            )
        self.write("README.md", readme)
        self.write(
            "skills/booster/SKILL.md",
            """---
name: booster
description: Route visual briefs to evidence-backed references when design work begins.
---

# Booster: design-pack routing

## Step 1: Scan for context
Scan the project for subject, audience, existing tokens, and brand constraints.
## Step 2: Pick the form package
Pick one form package by the page's actual job rather than its industry.
## Step 3: Pick the sector package, if one applies
Pick one sector only when industry credibility materially affects the design.
## Step 4: Choose refs
Choose a pole-spanning shortlist, then open no more than three reference files.
## Step 5: Deliver the recommendation
Deliver the form, optional sector, candidate paths, and brief-specific reasons.
## Step 6: Derive when the build is proceeding
Derive three materially different families and reject generic or cloned anatomy.
""",
        )
        self.write(
            "skills/booster-questions/SKILL.md",
            """---
name: booster-questions
description: Interview before routing an ambiguous visual brief.
---

# Booster questions: interview, then route

## The interview
Ask one focused question at a time and stop as soon as routing is unambiguous.
## Then route
Route the answers through the Booster form, sector, and reference selection steps.
Carry the stated poles and anchors into the shortlist instead of discarding interview evidence.
""",
        )
        self.write(
            "skills/booster-audit/SKILL.md",
            """---
name: booster-audit
description: Audit rendered design evidence against Booster gates.
---

# Booster audit

## 1. Reconstruct intent
Read the brief, selected direction, existing system, and subject-specific constraints.
## 2. Capture rendered evidence
Capture mobile, laptop, and wide viewports plus keyboard and reduced-motion evidence.
## 3. Classify findings
Classify each finding against hard floors, uniqueness, cloning, legibility, or believability.
## 4. Report the verdict
Report evidence, impact, and the smallest correction that preserves the chosen family.
## 5. Correct without converging
Return to derivation when a correction would collapse the work into a familiar mode.
""",
        )
        for skill in ["booster", "booster-questions", "booster-audit"]:
            display_name = skill.replace("-", " ").title()
            self.write(
                f"skills/{skill}/booster-skill.json",
                json.dumps(
                    {"owner": "booster", "schema_version": 1, "skill": skill}, indent=2
                )
                + "\n",
            )
            self.write(
                f"skills/{skill}/agents/openai.yaml",
                f'''interface:
  display_name: "{display_name}"
  short_description: "Fixture metadata for {skill}"
  default_prompt: "Use ${skill} for this fixture."
''',
            )
        self.write("notes/README.md", "# Notes\n")
        self.write(
            "notes/gwern.md",
            """# Gwern design reference

## Documented decisions and their reasoning
- Record the rejected alternatives and explain how the surviving decision serves the subject.
- Keep the underlying constraints beside each decision so later edits do not erase its cause.
## Graveyard (abandoned, with cause)
- Preserve abandoned approaches with the observed reason each one failed during review.
- Distinguish a subject mismatch from a technical failure or an inaccessible interaction.
## Meta-lessons
- Separate reusable evidence from visual details that belong only to one subject.
- Prefer a compact causal record over a gallery of unexplained screenshots and impressions.
""",
        )
        self.write(
            "notes/comparables-2026-08.md",
            """# Comparable systems scan, 2026-08-17

## Ten closest systems
- Compare ten adjacent systems by routing, derivation, evidence, audit, and distribution behavior.
## Implemented synthesis
- Adopt searchable references, direction receipts, and explicit outcome gates without presets.
## Deliberately not adopted
- Reject cloning, numeric taste scores, and automatic promotion of aesthetic prohibitions.
""",
        )
        self.write(
            "skills/booster/references/direction-record.md",
            """# Direction record

## Context fingerprint
- Record the subject, audience, job, existing design-system constraints, and evidence inspected.
## Direction A: <subject-specific name>
- Describe a subject-bound structure, signature element, hierarchy, and responsive behavior.
## Direction B: <subject-specific name>
- Describe a materially different family with its own content geometry and interaction grammar.
## Direction C: <subject-specific name>
- Describe a third family whose anatomy cannot be mistaken for either earlier direction.
## Rejection checks
- State whether the plan could ship for another subject or recognizably reproduces a reference.
## Selection
- Name the selected direction, the rejected alternatives, and the evidence behind the choice.
""",
        )
        for relative in [
            "notes/gwern.md",
            "notes/comparables-2026-08.md",
            "skills/booster/references/direction-record.md",
            "skills/booster/SKILL.md",
            "skills/booster-questions/SKILL.md",
            "skills/booster-audit/SKILL.md",
        ]:
            self.write(
                relative,
                (MODULE_PATH.parents[1] / relative).read_text(encoding="utf-8"),
            )
        self.write("tools/booster.py", MODULE_PATH.read_text(encoding="utf-8"))
        self.write(
            "packages/interface/PACK.md",
            """# Interface package

## Range map

- `refs/terminal.md`: dark operational utility; command output is the proof.
- `refs/quiet.md`: pale editorial workspace; reading structure leads.
- `refs/playful.md`: colorful consumer tool; restrained chrome holds character.
- `refs/dense.md`: dense product desktop; information grammar carries identity.

## Lessons (cross-site)

- Demonstrate real state.

## Avoid (cross-site)

- Do not copy the shell.
""",
        )
        form_refs = {
            "terminal": "terminal command dark operational dashboard",
            "quiet": "quiet pale editorial reading workspace",
            "playful": "playful colorful consumer illustration",
            "dense": "dense data desktop controls",
        }
        for name, body in form_refs.items():
            self.write(
                f"packages/interface/refs/{name}.md",
                f"# {name} ({name}.example, extracted 2026-08-01)\nstatus: full-css\n\n- {body} with measured foreground and background roles grounded in inspected output.\n- Type evidence records display, body, and monospace roles with verified sizes and leading.\n- Layout evidence records content rails, responsive gutters, density, and interaction geometry.\n- Motion evidence distinguishes verified timing from behavior that was not available to inspect.\n- Signature evidence names one subject-bound element and explains why it carries the identity.\n\nAvoid: Do not clone the measured shell without the subject and operational evidence that justify it.\n",
            )

        self.write(
            "packages/sectors/hospital/PACK.md",
            """# hospital sector package

## The hospital mode (avoid)

- Avoid portal sameness.

## Tells

- Blue card grids.

## Register

- Put care tasks first.
- **Operational surface:** keep scheduling, records access, and after-hours guidance on the owned site.

## Range map

care.example - patient scheduling utility with humane operational proof.
research.example - evidence-led clinical reading with sober hierarchy.
warm.example - neighborhood care with warm photography and direct access.
urgent.example - high-contrast triage navigation with calm action states.
""",
        )
        sector_refs = {
            "care.example": "patient scheduling dashboard and appointment proof",
            "research.example": "clinical research evidence and papers",
            "warm.example": "warm neighborhood care photography",
            "urgent.example": "urgent triage high contrast action",
        }
        for name, body in sector_refs.items():
            self.write(
                f"packages/sectors/hospital/refs/{name}.md",
                f"""# https://{name} (sector: hospital, sweep: excellence, fetched 2026-08-02)
status: full-css

## Token block (~10 lines)

- {body} with documented color, type, spacing, surface, and interaction roles from the source.

## Lessons (3-5 bullets)

- Put real tasks near claims and preserve the operational proof that makes the subject believable.

## Avoid (1-2 bullets)

- Do not clone the visual shell or detach its motifs from the care task that justified them.
""",
            )

        bans = {
            "schema_version": 1,
            "source": "DESIGN.md",
            "bans": [
                {
                    "id": "B001",
                    "pattern": "Generic centered hero.",
                    "status": "legacy-unstructured",
                    "evidence_summary": None,
                }
            ],
        }
        observations = {"schema_version": 1, "observations": []}
        self.write("evidence/bans.json", json.dumps(bans, indent=2) + "\n")
        self.write("evidence/observations.json", json.dumps(observations, indent=2) + "\n")
        self.write(
            "evidence/uncovered.json",
            json.dumps(
                {
                    "schema_version": 1,
                    "industries": [
                        {
                            "id": "food/hospitality",
                            "label": "restaurants",
                            "tokens": ["barbecue", "restaurant", "restaurants"],
                        },
                        {
                            "id": "civic",
                            "label": "government",
                            "tokens": ["government"],
                        },
                        {
                            "id": "education",
                            "label": "schools",
                            "tokens": ["school"],
                        },
                        {
                            "id": "hospitality",
                            "label": "hotels",
                            "tokens": ["hotel"],
                        },
                        {
                            "id": "religion",
                            "label": "worship",
                            "tokens": ["church"],
                        },
                        {
                            "id": "sports",
                            "label": "gyms",
                            "tokens": ["gym"],
                        },
                    ],
                },
                indent=2,
            )
            + "\n",
        )
        self.write(
            "evidence/reference-index.json",
            json.dumps(booster.build_reference_index(self.root), indent=2) + "\n",
        )
        marker = {
            "name": "booster",
            "schema_version": 1,
            "canonical_home": "~/.claude",
            "managed_library_paths": [
                "DESIGN.md",
                "design/packages",
                "design/notes",
                "design/tools",
                "design/evidence",
            ],
            "skills": list(booster.REQUIRED_SKILLS),
            "required_managed_paths": list(booster.REQUIRED_MANAGED_PATHS),
        }
        self.write("booster.json", json.dumps(marker, indent=2) + "\n")


class BoosterTests(unittest.TestCase):
    def make_repo(self) -> tuple[tempfile.TemporaryDirectory[str], Path]:
        temporary = tempfile.TemporaryDirectory()
        root = Path(temporary.name)
        BoosterFixture(root).build()
        return temporary, root

    def test_index_has_stable_ids_and_metadata(self) -> None:
        temporary, root = self.make_repo()
        self.addCleanup(temporary.cleanup)

        first = booster.build_reference_index(root)
        second = booster.build_reference_index(root)

        self.assertEqual(first, second)
        self.assertEqual(first["counts"]["refs"], 8)
        ids = [entry["id"] for entry in first["entries"]]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertTrue(all(entry["path"] for entry in first["entries"]))
        self.assertTrue(all(entry["date"] for entry in first["entries"]))
        self.assertTrue(all(entry["provenance"] for entry in first["entries"]))
        self.assertTrue(all(entry["pole"] for entry in first["entries"]))

    def test_search_balances_relevance_and_diversity_across_axes(self) -> None:
        temporary, root = self.make_repo()
        self.addCleanup(temporary.cleanup)

        results = booster.search_references(
            root,
            "patient scheduling operational dashboard",
            form="interface",
            sector="hospital",
            limit=4,
            min_score=1,
        )

        self.assertEqual(len(results), 4)
        self.assertEqual(results[0]["id"], "sector.hospital.ref.care.example")
        self.assertEqual({item["axis"] for item in results}, {"form", "sector"})
        self.assertEqual(len({item["pole"] for item in results}), 4)

    def test_search_returns_empty_when_nothing_is_relevant(self) -> None:
        temporary, root = self.make_repo()
        self.addCleanup(temporary.cleanup)

        results = booster.search_references(root, "zzzzzzzzzzzz", limit=4)

        self.assertEqual(results, [])

    def test_search_refuses_uncovered_industry_without_a_sector(self) -> None:
        temporary, root = self.make_repo()
        self.addCleanup(temporary.cleanup)

        results = booster.search_references(
            root, "family-owned Korean barbecue restaurant", limit=4
        )

        self.assertEqual(results, [])
        diagnosis = booster.diagnose_empty_search(
            root, "family-owned Korean barbecue restaurant"
        )
        self.assertEqual(diagnosis["reason"], "no-sector")
        self.assertEqual(diagnosis["uncovered"], "food/hospitality")
        help_text = " ".join(booster.empty_search_help(diagnosis))
        self.assertIn("Never retry unfiltered", help_text)
        self.assertNotIn("broader brief", help_text)

    def test_search_names_filter_too_narrow_instead_of_broadening(self) -> None:
        temporary, root = self.make_repo()
        self.addCleanup(temporary.cleanup)

        results = booster.search_references(
            root, "patient scheduling", form="interface", limit=4
        )

        self.assertEqual(results, [])
        diagnosis = booster.diagnose_empty_search(
            root, "patient scheduling", form="interface"
        )
        self.assertEqual(diagnosis["reason"], "filter-too-narrow")
        help_text = " ".join(booster.empty_search_help(diagnosis))
        self.assertIn("Never retry unfiltered", help_text)
        self.assertNotIn("broader brief", help_text)

    def test_empty_search_cli_does_not_suggest_broadening(self) -> None:
        temporary, root = self.make_repo()
        self.addCleanup(temporary.cleanup)
        output = io.StringIO()
        with redirect_stdout(output):
            result = booster.main(
                [
                    "search",
                    "family-owned Korean barbecue restaurant",
                    "--form",
                    "interface",
                    "--root",
                    str(root),
                    "--json",
                ]
            )

        self.assertEqual(result, 0)
        payload = json.loads(output.getvalue())
        self.assertEqual(payload["count"], 0)
        self.assertEqual(payload["empty"]["reason"], "no-sector")
        self.assertNotIn("broader brief", json.dumps(payload))

    def test_validation_accepts_complete_repository(self) -> None:
        temporary, root = self.make_repo()
        self.addCleanup(temporary.cleanup)

        result = booster.validate_repository(root)

        self.assertTrue(result["valid"], result["issues"])
        self.assertEqual(result["errors"], 0)

    def test_validation_reports_readme_and_range_map_drift(self) -> None:
        temporary, root = self.make_repo()
        self.addCleanup(temporary.cleanup)
        readme = (root / "README.md").read_text(encoding="utf-8")
        (root / "README.md").write_text(
            readme.replace("distilled_refs-8", "distilled_refs-99"), encoding="utf-8"
        )
        pack = root / "packages/interface/PACK.md"
        pack.write_text(
            pack.read_text(encoding="utf-8").replace(
                "- `refs/quiet.md`: pale editorial workspace; reading structure leads.\n", ""
            ),
            encoding="utf-8",
        )

        result = booster.validate_repository(root)
        codes = {item["code"] for item in result["issues"]}

        self.assertFalse(result["valid"])
        self.assertIn("readme-count-mismatch", codes)
        self.assertIn("range-map-unmapped-ref", codes)

    def test_validation_rejects_a_stale_generated_index(self) -> None:
        temporary, root = self.make_repo()
        self.addCleanup(temporary.cleanup)
        booster.write_json(root / "evidence/reference-index.json", booster.build_reference_index(root))
        ref = root / "packages/interface/refs/terminal.md"
        ref.write_text(
            ref.read_text(encoding="utf-8").replace("status: full-css", "status: wayback"),
            encoding="utf-8",
        )

        result = booster.validate_repository(root)
        codes = {item["code"] for item in result["issues"]}

        self.assertFalse(result["valid"])
        self.assertIn("index-stale", codes)

    def test_validation_rejects_malformed_skill_metadata_and_frontmatter(self) -> None:
        temporary, root = self.make_repo()
        self.addCleanup(temporary.cleanup)
        metadata = root / "skills/booster/agents/openai.yaml"
        original_metadata = metadata.read_text(encoding="utf-8")
        metadata.write_text(original_metadata + "broken: [\n", encoding="utf-8")

        result = booster.validate_repository(root)
        codes = {item["code"] for item in result["issues"]}
        self.assertIn("skill-openai-metadata", codes)

        metadata.write_text(
            original_metadata.replace('display_name: "Booster"', 'display_name: "Bad\\q"'),
            encoding="utf-8",
        )
        result = booster.validate_repository(root)
        codes = {item["code"] for item in result["issues"]}
        self.assertIn("skill-openai-metadata", codes)

        metadata.write_text(
            original_metadata.replace(
                'short_description: "Fixture metadata for booster"',
                'short_description: "too short"',
            ),
            encoding="utf-8",
        )
        result = booster.validate_repository(root)
        codes = {item["code"] for item in result["issues"]}
        self.assertIn("skill-openai-description", codes)

        metadata.write_text(original_metadata, encoding="utf-8")
        audit_metadata = root / "skills/booster-audit/agents/openai.yaml"
        audit_original = audit_metadata.read_text(encoding="utf-8")
        audit_metadata.write_text(original_metadata, encoding="utf-8")
        result = booster.validate_repository(root)
        codes = {item["code"] for item in result["issues"]}
        self.assertIn("skill-openai-identity", codes)
        audit_metadata.write_text(
            audit_original.replace('display_name: "Booster Audit"', 'display_name: "Wrong Skill"'),
            encoding="utf-8",
        )
        result = booster.validate_repository(root)
        codes = {item["code"] for item in result["issues"]}
        self.assertIn("skill-openai-identity", codes)
        audit_metadata.write_text(audit_original, encoding="utf-8")

        skill = root / "skills/booster/SKILL.md"
        original_skill = skill.read_text(encoding="utf-8")
        skill.write_text(
            re.sub(
                r"^description: (.+)$",
                r"description: \1\nbroken: [",
                original_skill,
                count=1,
                flags=re.MULTILINE,
            ),
            encoding="utf-8",
        )
        result = booster.validate_repository(root)
        codes = {item["code"] for item in result["issues"]}
        self.assertIn("skill-frontmatter", codes)

        skill.write_text(
            re.sub(
                r"^description: .+$",
                "description: true",
                original_skill,
                count=1,
                flags=re.MULTILINE,
            ),
            encoding="utf-8",
        )
        result = booster.validate_repository(root)
        codes = {item["code"] for item in result["issues"]}
        self.assertIn("skill-frontmatter", codes)

        for invalid in [
            "- broken scalar",
            "? broken scalar",
            "%directive",
            ",flow",
            "]flow",
            "}flow",
            "tab\tvalue",
            f"control{chr(0x7F)}value",
            "Route <unsafe> visual briefs",
            "A " + "x" * 1023,
        ]:
            skill.write_text(
                re.sub(
                    r"^description: .+$",
                    lambda _: f"description: {invalid}",
                    original_skill,
                    count=1,
                    flags=re.MULTILINE,
                ),
                encoding="utf-8",
            )
            result = booster.validate_repository(root)
            codes = {item["code"] for item in result["issues"]}
            self.assertIn("skill-frontmatter", codes, invalid)

    def test_schema_versions_reject_json_booleans(self) -> None:
        temporary, root = self.make_repo()
        self.addCleanup(temporary.cleanup)
        cases = [
            ("booster.json", "marker-schema"),
            ("evidence/bans.json", "bans-schema"),
            ("evidence/observations.json", "observations-schema"),
            ("evidence/reference-index.json", "index-schema"),
        ]
        for relative, expected_code in cases:
            path = root / relative
            original = path.read_text(encoding="utf-8")
            data = json.loads(original)
            data["schema_version"] = True
            path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
            result = booster.validate_repository(root)
            codes = {item["code"] for item in result["issues"]}
            self.assertIn(expected_code, codes, relative)
            path.write_text(original, encoding="utf-8")

    def test_release_inventory_cannot_be_removed_from_its_own_marker(self) -> None:
        temporary, root = self.make_repo()
        self.addCleanup(temporary.cleanup)
        (root / "notes/comparables-2026-08.md").unlink()
        marker_path = root / "booster.json"
        marker = json.loads(marker_path.read_text(encoding="utf-8"))
        marker["required_managed_paths"].remove("notes/comparables-2026-08.md")
        marker_path.write_text(json.dumps(marker, indent=2) + "\n", encoding="utf-8")

        result = booster.validate_repository(root)
        codes = {item["code"] for item in result["issues"]}

        self.assertFalse(result["valid"])
        self.assertIn("structure-missing", codes)

    def test_empty_package_catalog_is_invalid(self) -> None:
        temporary, root = self.make_repo()
        self.addCleanup(temporary.cleanup)
        shutil.rmtree(root / "packages")
        (root / "packages").mkdir()

        result = booster.validate_repository(root)
        codes = {item["code"] for item in result["issues"]}

        self.assertFalse(result["valid"])
        self.assertIn("catalog-empty", codes)

    def test_repository_named_design_is_not_misclassified_as_an_install(self) -> None:
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        root = Path(temporary.name) / "design"
        BoosterFixture(root).build()
        (root / "README.md").unlink()
        shutil.rmtree(root / "skills")

        self.assertFalse(booster.is_installed_layout(root))
        result = booster.validate_repository(root)
        self.assertFalse(result["valid"])
        self.assertIn("structure-missing", {item["code"] for item in result["issues"]})

    def test_installed_layout_survives_a_symlinked_claude_home(self) -> None:
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        outer = Path(temporary.name)
        target = outer / "custom-claude-root"
        root = target / "design"
        BoosterFixture(root).build()
        (root / "DESIGN.md").replace(target / "DESIGN.md")
        (root / booster.INSTALL_RECEIPT_PATH).write_text(
            json.dumps(
                {"name": "booster-installed-library", "schema_version": 1}, indent=2
            )
            + "\n",
            encoding="utf-8",
        )
        home = outer / "home"
        home.mkdir()
        (home / ".claude").symlink_to(target, target_is_directory=True)
        resolved = (home / ".claude/design").resolve()

        self.assertTrue(booster.is_installed_layout(resolved))
        self.assertTrue(booster.validate_installed_library(resolved)["valid"])

        (resolved / "booster.json").write_text("{invalid json\n", encoding="utf-8")
        self.assertTrue(booster.is_installed_layout(resolved))
        result = booster.validate_installed_library(resolved)
        self.assertFalse(result["valid"])
        self.assertIn("marker-json", {item["code"] for item in result["issues"]})

    def test_repository_root_contract_files_cannot_be_symlinks(self) -> None:
        temporary, root = self.make_repo()
        self.addCleanup(temporary.cleanup)
        marker = root / "booster.json"
        external = root.parent / f"{root.name}-booster.json"
        marker.replace(external)
        marker.symlink_to(external)

        result = booster.validate_repository(root)

        self.assertFalse(result["valid"])
        self.assertIn("managed-symlink", {item["code"] for item in result["issues"]})

    def test_ban_ids_and_evidence_summaries_are_reconciled(self) -> None:
        temporary, root = self.make_repo()
        self.addCleanup(temporary.cleanup)
        design = root / "DESIGN.md"
        original_design = design.read_text(encoding="utf-8")
        design.write_text(
            original_design.replace(
                "- **B001** Generic centered hero.\n",
                "- **B001** Generic centered hero.\n- **B001** Generic centered hero.\n",
            ),
            encoding="utf-8",
        )
        readme = root / "README.md"
        readme.write_text(
            readme.read_text(encoding="utf-8").replace("design_bans-1", "design_bans-2"),
            encoding="utf-8",
        )
        result = booster.validate_repository(root)
        self.assertIn(
            "ban-design-id-duplicate", {item["code"] for item in result["issues"]}
        )

        design.write_text(original_design, encoding="utf-8")
        readme.write_text(
            readme.read_text(encoding="utf-8").replace("design_bans-2", "design_bans-1"),
            encoding="utf-8",
        )
        bans_path = root / "evidence/bans.json"
        bans = json.loads(bans_path.read_text(encoding="utf-8"))
        bans["bans"][0]["evidence_summary"] = {"fabricated": True}
        bans_path.write_text(json.dumps(bans, indent=2) + "\n", encoding="utf-8")
        result = booster.validate_repository(root)
        codes = {item["code"] for item in result["issues"]}
        self.assertIn("ban-evidence-summary", codes)
        self.assertIn("ban-evidence-drift", codes)

        bans["bans"][0]["evidence_summary"] = None
        bans["source"] = "fabricated.md"
        bans_path.write_text(json.dumps(bans, indent=2) + "\n", encoding="utf-8")
        result = booster.validate_repository(root)
        self.assertIn("bans-source", {item["code"] for item in result["issues"]})

    def test_reference_status_must_use_the_metadata_slot(self) -> None:
        temporary, root = self.make_repo()
        self.addCleanup(temporary.cleanup)
        ref = root / "packages/interface/refs/terminal.md"
        lines = ref.read_text(encoding="utf-8").splitlines()
        ref.write_text("\n".join([lines[0], *lines[2:], "status: full-css"]) + "\n", encoding="utf-8")
        booster.write_json(root / "evidence/reference-index.json", booster.build_reference_index(root))

        result = booster.validate_repository(root)
        codes = {item["code"] for item in result["issues"]}

        self.assertIn("reference-status-slot", codes)

    def test_orphan_references_and_malformed_extra_indexes_are_invalid(self) -> None:
        temporary, root = self.make_repo()
        self.addCleanup(temporary.cleanup)
        orphan = root / "packages/orphan/refs/example.md"
        orphan.parent.mkdir(parents=True)
        orphan.write_text(
            "# Orphan (example.test, extracted 2026-08-17)\nstatus: full-css\n\n"
            + "- Substantive orphan evidence that should never enter an unowned package.\n" * 5
            + "\nAvoid: Do not accept evidence that has no package or range-map owner.\n",
            encoding="utf-8",
        )
        index = booster.build_reference_index(root)
        booster.write_json(root / "evidence/reference-index.json", index)
        booster.update_readme_counts(root, index)

        result = booster.validate_repository(root)
        self.assertIn("reference-orphan", {item["code"] for item in result["issues"]})

        orphan.unlink()
        orphan.parent.rmdir()
        orphan.parent.parent.rmdir()
        index = booster.build_reference_index(root)
        booster.write_json(root / "evidence/reference-index.json", index)
        booster.update_readme_counts(root, index)
        booster.write_json(
            root / "evidence/bogus-index.json",
            {
                "schema_version": 1,
                "counts": {"form_packs": 0, "sector_packs": 0, "refs": 0, "modes": 0, "entries": 1},
                "entries": [
                    {"id": None, "kind": [], "axis": False, "package": {}, "title": 1,
                     "provenance": False, "status": 42, "date": {}, "path": [], "pole": None}
                ],
            },
        )
        result = booster.validate_repository(root)
        self.assertIn("index-field", {item["code"] for item in result["issues"]})

        forged = booster.build_reference_index(root)
        forged["entries"][0].update(
            {
                "id": "form.fake.ref.forged",
                "package": "fake",
                "title": "Fabricated title",
                "provenance": "Fabricated provenance",
                "pole": "Fabricated pole",
            }
        )
        booster.write_json(root / "evidence/bogus-index.json", forged)
        result = booster.validate_repository(root)
        self.assertIn("index-entry-drift", {item["code"] for item in result["issues"]})

    def test_dates_require_the_documented_calendar_format(self) -> None:
        for value in ["20260817", "2026-W34-1", "2026-8-17", "2026-02-30"]:
            with self.assertRaises(booster.BoosterError, msg=value):
                booster.make_observation(
                    pattern="Generic centered hero",
                    subject="Fixture",
                    model="fixture-model",
                    artifact="fixture-a",
                    note="Rejected",
                    date=value,
                )

    def test_validation_rejects_truncated_owned_content(self) -> None:
        temporary, root = self.make_repo()
        self.addCleanup(temporary.cleanup)
        cases = [
            ("DESIGN.md", "# Design invariants\n", "document-section"),
            (
                "skills/booster/SKILL.md",
                "---\nname: booster\ndescription: Valid multiword description.\n---\n",
                "document-heading",
            ),
            (
                "packages/interface/PACK.md",
                "# Interface package\n\n## Range map\n\n- `refs/terminal.md`: one pole.\n",
                "document-section",
            ),
            ("notes/gwern.md", "# Gwern design reference\n", "document-section"),
            (
                "skills/booster/references/direction-record.md",
                """# Direction record

## Context fingerprint
x
## Direction A: <subject-specific name>
x
## Direction B: <subject-specific name>
x
## Direction C: <subject-specific name>
x
## Rejection checks
x
## Selection
x
""",
                "document-content",
            ),
            (
                "skills/booster/booster-skill.json",
                "x\n",
                "skill-ownership",
            ),
            ("tools/booster.py", "#\n", "tool-digest"),
            (
                "README.md",
                "\n".join(
                    [
                        "![x](https://img.shields.io/badge/form_packs-1-x)",
                        "![x](https://img.shields.io/badge/sector_packs-1-x)",
                        "![x](https://img.shields.io/badge/distilled_refs-8-x)",
                        "![x](https://img.shields.io/badge/sector_modes-0-x)",
                        "![x](https://img.shields.io/badge/design_bans-1-x)",
                    ]
                )
                + "\n",
                "readme-content",
            ),
            (
                "packages/interface/refs/terminal.md",
                "# terminal (terminal.example, extracted 2026-08-01)\nstatus: full-css\n\n- placeholder evidence one\n- placeholder evidence two\n- placeholder evidence three\n\nAvoid: placeholder warning that says little.\n",
                "reference-content",
            ),
            (
                "packages/sectors/hospital/refs/care.example.md",
                """# https://care.example (sector: hospital, sweep: excellence, fetched 2026-08-02)
status: full-css

## Token block
- placeholder evidence only
## Lessons
- placeholder evidence only
## Avoid
- placeholder evidence only
""",
                "reference-content",
            ),
        ]
        for relative, truncated, expected_code in cases:
            path = root / relative
            original = path.read_text(encoding="utf-8")
            path.write_text(truncated, encoding="utf-8")
            result = booster.validate_repository(root)
            codes = {item["code"] for item in result["issues"]}
            self.assertIn(expected_code, codes, relative)
            path.write_text(original, encoding="utf-8")

    def test_malformed_ban_status_stays_a_structured_validation_error(self) -> None:
        temporary, root = self.make_repo()
        self.addCleanup(temporary.cleanup)
        bans_path = root / "evidence/bans.json"
        bans = json.loads(bans_path.read_text(encoding="utf-8"))
        bans["bans"][0]["status"] = []
        bans_path.write_text(json.dumps(bans, indent=2) + "\n", encoding="utf-8")

        result = booster.validate_repository(root)

        self.assertFalse(result["valid"])
        self.assertIn("ban-status", {item["code"] for item in result["issues"]})

    def test_inventory_flags_major_managed_content_shrinkage(self) -> None:
        baseline_temporary, baseline = self.make_repo()
        candidate_temporary, candidate = self.make_repo()
        self.addCleanup(baseline_temporary.cleanup)
        self.addCleanup(candidate_temporary.cleanup)
        skill = candidate / "skills/booster/SKILL.md"
        skill.write_text(
            "---\nname: booster\ndescription: Valid multiword description.\n---\n",
            encoding="utf-8",
        )

        result = booster.reference_inventory_diff(baseline, candidate)

        self.assertFalse(result["removed"])
        self.assertEqual(
            [item["path"] for item in result["shrunk"]],
            ["skills/booster/SKILL.md"],
        )

        (baseline / "packages/interface/support.txt").write_text("managed support\n", encoding="utf-8")
        result = booster.reference_inventory_diff(baseline, candidate)
        self.assertIn("managed-file.packages/interface/support.txt", result["removed"])

    def test_special_managed_files_are_rejected(self) -> None:
        temporary, root = self.make_repo()
        self.addCleanup(temporary.cleanup)
        fifo = root / "notes/untrusted.pipe"
        os.mkfifo(fifo)

        result = booster.validate_repository(root)

        self.assertFalse(result["valid"])
        self.assertIn("managed-special", {item["code"] for item in result["issues"]})

    def test_toon_scalars_and_lists_use_current_canonical_shapes(self) -> None:
        self.assertEqual(booster.toon_scalar(12.0), "12")
        self.assertEqual(booster.toon_scalar("+1"), '"+1"')
        self.assertEqual(booster.toon_scalar("a\x01b"), '"a\\u0001b"')
        self.assertEqual(booster.toon_list("help", []), "help: []")
        rendered = booster.toon_list("help", ["first", "second, value"])
        self.assertEqual(rendered, 'help[2]: first,"second, value"')

    def test_optional_screenshot_is_canonicalized(self) -> None:
        observation = booster.make_observation(
            pattern="보라색 그라디언트",
            subject="Fixture",
            model="fixture-model",
            artifact="fixture-a",
            note="Rejected",
            screenshot="screenshot.png",
            date="2026-08-17",
        )
        observation["screenshot"] = " screenshot.png "
        codes = {code for code, _ in booster.observation_integrity_errors(observation)}
        self.assertIn("observation-screenshot", codes)

    def test_observation_recording_is_idempotent(self) -> None:
        temporary, root = self.make_repo()
        self.addCleanup(temporary.cleanup)
        observation = booster.make_observation(
            pattern="Floating cards around a device",
            subject="Clinic scheduling",
            model="test-model",
            artifact="build-a",
            note="The cards feel generic",
            date="2026-08-17",
        )
        path = root / "evidence/observations.json"

        self.assertTrue(booster.record_observation(path, observation))
        self.assertFalse(booster.record_observation(path, observation))
        data = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(len(data["observations"]), 1)
        self.assertEqual(data["observations"][0]["outcome"], "rejected")

    def test_observation_hashes_and_structured_ban_links_are_validated(self) -> None:
        temporary, root = self.make_repo()
        self.addCleanup(temporary.cleanup)
        observation = booster.make_observation(
            pattern="Floating cards around a device",
            subject="Clinic scheduling",
            model="test-model",
            artifact="build-a",
            note="Rejected",
            date="2026-08-17",
        )
        observation["pattern_key"] = "pattern-forged"
        observation["id"] = "observation-forged"
        (root / "evidence/observations.json").write_text(
            json.dumps({"schema_version": 1, "observations": [observation]}, indent=2) + "\n",
            encoding="utf-8",
        )
        bans_path = root / "evidence/bans.json"
        bans = json.loads(bans_path.read_text(encoding="utf-8"))
        bans["bans"][0].update(
            {
                "status": "structured",
                "observation_ids": ["observation-missing-a", "observation-missing-b"],
                "confirmed_by": "reviewer",
                "confirmed_date": "2026-08-17",
            }
        )
        bans_path.write_text(json.dumps(bans, indent=2) + "\n", encoding="utf-8")

        result = booster.validate_repository(root)
        codes = {item["code"] for item in result["issues"]}

        self.assertIn("observation-pattern-key", codes)
        self.assertIn("observation-id", codes)
        self.assertIn("ban-observation-link", codes)
        with redirect_stdout(io.StringIO()):
            self.assertEqual(booster.main(["candidates", "--root", str(root)]), 1)

    def test_structured_bans_bind_one_explicit_repeated_pattern(self) -> None:
        temporary, root = self.make_repo()
        self.addCleanup(temporary.cleanup)
        first = booster.make_observation(
            pattern="Floating status cards",
            subject="Clinic scheduling",
            model="test-model",
            artifact="build-a",
            note="Rejected",
            date="2026-08-16",
        )
        second = booster.make_observation(
            pattern="Floating status cards",
            subject="Retail scheduling",
            model="test-model",
            artifact="build-b",
            note="Rejected again",
            date="2026-08-17",
        )
        observations_path = root / "evidence/observations.json"
        observations_path.write_text(
            json.dumps({"schema_version": 1, "observations": [first, second]}, indent=2) + "\n",
            encoding="utf-8",
        )
        bans_path = root / "evidence/bans.json"
        bans = json.loads(bans_path.read_text(encoding="utf-8"))
        bans["bans"][0].update(
            {
                "status": "structured",
                "pattern_key": "pattern-wrong",
                "observation_ids": [first["id"], second["id"]],
                "confirmed_by": "reviewer",
                "confirmed_date": "2026-08-17",
            }
        )
        bans_path.write_text(json.dumps(bans, indent=2) + "\n", encoding="utf-8")

        result = booster.validate_repository(root)
        codes = {item["code"] for item in result["issues"]}
        self.assertIn("ban-pattern-key", codes)

        unrelated = booster.make_observation(
            pattern="Tiny gray text",
            subject="Retail scheduling",
            model="test-model",
            artifact="build-b",
            note="Rejected for legibility",
            date="2026-08-17",
        )
        observations_path.write_text(
            json.dumps({"schema_version": 1, "observations": [first, unrelated]}, indent=2) + "\n",
            encoding="utf-8",
        )
        bans["bans"][0]["pattern_key"] = first["pattern_key"]
        bans["bans"][0]["observation_ids"] = [first["id"], unrelated["id"]]
        bans_path.write_text(json.dumps(bans, indent=2) + "\n", encoding="utf-8")
        result = booster.validate_repository(root)
        codes = {item["code"] for item in result["issues"]}
        self.assertIn("ban-pattern-group", codes)

        second_unrelated = booster.make_observation(
            pattern="Entirely unrelated floating cards",
            subject="Retail scheduling",
            model="test-model",
            artifact="build-c",
            note="Rejected again",
            date="2026-08-17",
        )
        first_unrelated = booster.make_observation(
            pattern="Entirely unrelated floating cards",
            subject="Clinic scheduling",
            model="test-model",
            artifact="build-d",
            note="Rejected",
            date="2026-08-16",
        )
        observations_path.write_text(
            json.dumps(
                {"schema_version": 1, "observations": [first_unrelated, second_unrelated]},
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )
        bans["bans"][0]["pattern_key"] = first_unrelated["pattern_key"]
        bans["bans"][0]["observation_ids"] = [first_unrelated["id"], second_unrelated["id"]]
        bans_path.write_text(json.dumps(bans, indent=2) + "\n", encoding="utf-8")
        result = booster.validate_repository(root)
        self.assertIn("ban-pattern-key", {item["code"] for item in result["issues"]})

    def test_mutations_require_managed_roots_and_reserved_index_path(self) -> None:
        temporary, root = self.make_repo()
        self.addCleanup(temporary.cleanup)
        observations_path = root / "evidence/observations.json"
        before = observations_path.read_text(encoding="utf-8")
        with redirect_stdout(io.StringIO()):
            result = booster.main(
                ["index", "--root", str(root), "--write", "evidence/observations.json"]
            )
        self.assertEqual(result, 1)
        self.assertEqual(observations_path.read_text(encoding="utf-8"), before)

        missing = root / "missing-library"
        with redirect_stdout(io.StringIO()):
            result = booster.main(
                [
                    "observe",
                    "--root",
                    str(missing),
                    "--pattern",
                    "Floating cards",
                    "--subject",
                    "Clinic",
                    "--model",
                    "test-model",
                    "--artifact",
                    "build-a",
                    "--note",
                    "Rejected",
                ]
            )
        self.assertEqual(result, 1)
        self.assertFalse(missing.exists())

    def test_index_rejects_symlink_destinations(self) -> None:
        temporary, root = self.make_repo()
        self.addCleanup(temporary.cleanup)
        index_path = root / "evidence/reference-index.json"
        victim = root / "victim.json"
        victim.write_text("preserve me\n", encoding="utf-8")
        index_path.unlink()
        index_path.symlink_to(victim)

        with redirect_stdout(io.StringIO()):
            result = booster.main(
                ["index", "--root", str(root), "--write", "evidence/reference-index.json"]
            )

        self.assertEqual(result, 1)
        self.assertEqual(victim.read_text(encoding="utf-8"), "preserve me\n")

    def test_json_errors_are_single_parseable_documents(self) -> None:
        temporary, root = self.make_repo()
        self.addCleanup(temporary.cleanup)
        output = io.StringIO()
        with redirect_stdout(output):
            result = booster.main(
                ["search", "dashboard", "--root", str(root), "--limit", "0", "--json"]
            )
        self.assertEqual(result, 1)
        self.assertEqual(set(json.loads(output.getvalue())), {"error", "help"})

        output = io.StringIO()
        with redirect_stdout(output):
            result = booster.main(["search", "dashboard", "--limit", "bad", "--json"])
        self.assertEqual(result, 2)
        self.assertEqual(set(json.loads(output.getvalue())), {"error", "help"})

        for arguments in (["validate", "--bogus", "--json"], ["--json"]):
            output = io.StringIO()
            with redirect_stdout(output):
                result = booster.main(arguments)
            self.assertEqual(result, 2)
            self.assertEqual(set(json.loads(output.getvalue())), {"error", "help"})

    def test_toon_scalars_use_supported_control_character_escapes(self) -> None:
        self.assertEqual(booster.toon_scalar("\b\f"), r'"\u0008\u000c"')
        self.assertEqual(booster.toon_scalar(r"\b\f"), r'"\\b\\f"')

    def test_read_commands_reject_missing_roots(self) -> None:
        temporary, root = self.make_repo()
        self.addCleanup(temporary.cleanup)
        missing = root / "typo-library"
        for command in (["search", "dashboard"], ["index"]):
            output = io.StringIO()
            with redirect_stdout(output):
                result = booster.main([*command, "--root", str(missing), "--json"])
            self.assertEqual(result, 1)
            self.assertIn("does not exist", json.loads(output.getvalue())["error"])

    def test_inventory_json_removal_denial_is_parseable(self) -> None:
        baseline_temporary, baseline = self.make_repo()
        candidate_temporary, candidate = self.make_repo()
        self.addCleanup(baseline_temporary.cleanup)
        self.addCleanup(candidate_temporary.cleanup)
        (candidate / "packages/interface/refs/terminal.md").unlink()
        output = io.StringIO()
        with redirect_stdout(output):
            result = booster.main(
                [
                    "inventory-diff",
                    "--baseline",
                    str(baseline),
                    "--candidate",
                    str(candidate),
                    "--json",
                ]
            )
        self.assertEqual(result, 1)
        payload = json.loads(output.getvalue())
        self.assertTrue(payload["removed"])
        self.assertIn("error", payload)

    def test_flag_abbreviations_are_rejected(self) -> None:
        temporary, root = self.make_repo()
        self.addCleanup(temporary.cleanup)
        with redirect_stdout(io.StringIO()):
            result = booster.main(
                ["search", "dashboard", "--for", "interface", "--root", str(root)]
            )
        self.assertEqual(result, 2)

    def test_concurrent_observations_do_not_lose_updates(self) -> None:
        temporary, root = self.make_repo()
        self.addCleanup(temporary.cleanup)
        processes = []
        for index in range(8):
            command = [
                sys.executable,
                str(MODULE_PATH),
                "observe",
                "--root",
                str(root),
                "--pattern",
                f"Rejected pattern {index}",
                "--subject",
                "Clinic",
                "--model",
                "test-model",
                "--artifact",
                f"build-{index}",
                "--note",
                f"Rejected {index}",
                "--date",
                "2026-08-17",
            ]
            processes.append(
                subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            )
        for process in processes:
            stdout, stderr = process.communicate(timeout=20)
            self.assertEqual(process.returncode, 0, stdout + stderr)
        data = json.loads((root / "evidence/observations.json").read_text(encoding="utf-8"))
        self.assertEqual(len(data["observations"]), 8)

    def test_candidate_aggregation_requires_independent_artifacts(self) -> None:
        shared = {
            "pattern": "Floating cards around a device",
            "subject": "Scheduling",
            "model": "test-model",
        }
        observations = [
            booster.make_observation(
                **shared,
                artifact="build-a",
                note="Rejected once",
                date="2026-08-15",
            ),
            booster.make_observation(
                **shared,
                artifact="build-a",
                note="Rejected again in the same artifact",
                date="2026-08-16",
            ),
            booster.make_observation(
                **shared,
                artifact="build-b",
                note="Rejected independently",
                date="2026-08-17",
            ),
            booster.make_observation(
                pattern="Unrelated pattern",
                subject="Scheduling",
                model="test-model",
                artifact="build-c",
                note="Only one sighting",
                date="2026-08-17",
            ),
        ]

        candidates = booster.aggregate_candidates(observations, min_count=2)

        self.assertEqual(len(candidates), 1)
        self.assertEqual(candidates[0]["independent_count"], 2)
        self.assertEqual(candidates[0]["observation_count"], 3)
        self.assertEqual(candidates[0]["artifacts"], ["build-a", "build-b"])


class LiveCatalogTests(unittest.TestCase):
    root = Path(__file__).resolve().parents[1]

    def test_documented_readme_search_returns_covered_refs(self) -> None:
        readme = (self.root / "README.md").read_text(encoding="utf-8")
        self.assertNotIn("barbecue", readme.lower())
        self.assertNotIn("seoul garden", readme.lower())
        match = re.search(
            r'python3 tools/booster.py search "([^"]+)" --form (\S+) --sector (\S+) --limit 4',
            readme,
        )
        self.assertIsNotNone(match)
        assert match is not None
        query, form, sector = match.group(1), match.group(2), match.group(3)
        results = booster.search_references(
            self.root, query, form=form, sector=sector, limit=4
        )
        self.assertEqual(len(results), 4)
        packages = {item["package"] for item in results}
        self.assertTrue(packages <= {form, sector})
        self.assertIn(sector, packages)

    def test_previous_barbecue_demo_fails_closed(self) -> None:
        results = booster.search_references(
            self.root,
            "family-owned Korean barbecue restaurant",
            form="gallery",
            limit=4,
        )
        self.assertEqual(results, [])
        diagnosis = booster.diagnose_empty_search(
            self.root,
            "family-owned Korean barbecue restaurant",
            form="gallery",
        )
        self.assertEqual(diagnosis["reason"], "no-sector")


if __name__ == "__main__":
    unittest.main()
