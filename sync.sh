#!/bin/zsh
# Export a complete, validated live Booster install back into this repository.
# The repository stays untouched until a staged copy passes validation.
set -euo pipefail
cd "${0:A:h}"

VERSION="0.1.0"

dry_run=0
allow_removals=0
initial_head=""
initial_index_tree=""
sync_lock=""
lock_acquired=0
workspace=""

cleanup() {
  if [[ -n "$workspace" && -d "$workspace" ]]; then
    rm -rf "$workspace"
  fi
  if (( lock_acquired )) && [[ -n "$sync_lock" && -d "$sync_lock" ]]; then
    rmdir "$sync_lock" 2>/dev/null || true
  fi
}
trap cleanup EXIT INT TERM

trees_match() {
  python3 - "$1" "$2" <<'PY'
import hashlib
import os
import stat
import subprocess
import sys
from pathlib import Path


def snapshot(root_value):
    root = Path(root_value).resolve()
    entries = {}
    for current, directories, files in os.walk(root, followlinks=False):
        current_path = Path(current)
        if current_path == root and ".git" in directories:
            directories.remove(".git")
        for name in list(directories):
            path = current_path / name
            if name == "__pycache__":
                directories.remove(name)
                continue
            if path.is_symlink():
                entries[path.relative_to(root).as_posix()] = ("symlink", os.readlink(path))
                directories.remove(name)
        for name in files:
            if current_path == root and name == ".git":
                continue
            if name.endswith((".pyc", ".pyo")):
                continue
            path = current_path / name
            relative = path.relative_to(root).as_posix()
            if path.is_symlink():
                entries[relative] = ("symlink", os.readlink(path))
                continue
            mode = path.lstat().st_mode
            if not stat.S_ISREG(mode):
                entries[relative] = ("special", stat.S_IFMT(mode))
                continue
            digest = hashlib.sha256()
            with path.open("rb") as handle:
                for chunk in iter(lambda: handle.read(1024 * 1024), b""):
                    digest.update(chunk)
            executable = bool(stat.S_IMODE(path.stat().st_mode) & 0o111)
            entries[relative] = ("file", digest.hexdigest(), executable)
    return entries


try:
    left = snapshot(sys.argv[1])
    right = snapshot(sys.argv[2])
    right_root = Path(sys.argv[2]).resolve()
    tracked_result = subprocess.run(
        ["git", "-C", right_root.as_posix(), "ls-files", "-z"],
        capture_output=True,
        check=True,
    )
    untracked_result = subprocess.run(
        ["git", "-C", right_root.as_posix(), "ls-files", "--others", "--exclude-standard", "-z"],
        capture_output=True,
        check=True,
    )
    tracked = {value.decode() for value in tracked_result.stdout.split(b"\0") if value}
    untracked = {value.decode() for value in untracked_result.stdout.split(b"\0") if value}
except OSError as exc:
    print(f"tree verification error: {exc}", file=sys.stderr)
    raise SystemExit(2)

except subprocess.SubprocessError as exc:
    print(f"tree Git verification error: {exc}", file=sys.stderr)
    raise SystemExit(2)

changed = []
for key in set(left) | set(right):
    if left.get(key) == right.get(key):
        continue
    if key not in left and key in right and key not in tracked and key not in untracked:
        # Preserve ignored, untracked support files that are outside the export patch.
        continue
    changed.append(key)
if changed:
    changed.sort()
    for key in changed[:10]:
        print(f"tree mismatch: {key}", file=sys.stderr)
    raise SystemExit(1)
PY
}
usage() {
  print -r -- "usage: ./sync.sh [--dry-run] [--allow-removals]"
  print -r -- ""
  print -r -- "options:"
  print -r -- "  --dry-run         stage, validate, and preview without changing the repository"
  print -r -- "  --allow-removals  allow explicitly reviewed removals or major shrinkage"
  print -r -- "  -h, --help        show this help"
  print -r -- "  -v, -V, --version  print the Booster version"
  print -r -- ""
  print -r -- "example: ./sync.sh --dry-run"
}

if (( $# == 1 )) && [[ "$1" == -v || "$1" == -V || "$1" == --version ]]; then
  echo "$VERSION"
  exit 0
fi
while (( $# > 0 )); do
  case "$1" in
    --dry-run) dry_run=1 ;;
    --allow-removals) allow_removals=1 ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      usage
      exit 2
      ;;
  esac
  shift
done

for dependency in python3 rsync cp git cmp find grep mkdir mktemp rm rmdir wc tr; do
  if ! command -v "$dependency" >/dev/null 2>&1; then
    echo "Missing required command: $dependency. Nothing was changed."
    exit 1
  fi
done

if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "Cannot locate repository state; refusing a live-to-repo export. Nothing was changed."
  exit 1
fi

if (( ! dry_run )); then
  if ! sync_lock="$(git rev-parse --git-path booster-sync.lock 2>/dev/null)" || \
     [[ -z "$sync_lock" ]]; then
    echo "Cannot locate repository state; refusing a live-to-repo export. Nothing was changed."
    exit 1
  fi
  if ! mkdir "$sync_lock" 2>/dev/null; then
    echo "Another Booster export holds $sync_lock. Nothing was changed."
    exit 1
  fi
  lock_acquired=1
  if ! repository_status="$(git status --porcelain --untracked-files=all 2>/dev/null)"; then
    echo "Cannot read repository status; refusing a live-to-repo export. Nothing was changed."
    exit 1
  fi
  if [[ -n "$repository_status" ]]; then
    echo "Repository has uncommitted changes; refusing a live-to-repo export."
    echo "Commit or move them first, then retry. Nothing was changed."
    exit 1
  fi
  if ! initial_head="$(git rev-parse --verify HEAD 2>/dev/null)" || \
     ! initial_index_tree="$(git write-tree 2>/dev/null)"; then
    echo "Cannot fingerprint repository state; refusing a live-to-repo export. Nothing was changed."
    exit 1
  fi
fi

canonical="$HOME/.claude"
design_root="$canonical/design"
marker="$design_root/booster.json"
receipt="$design_root/.booster-installed.json"

if [[ -L "$design_root" ]] || [[ ! -d "$design_root" ]]; then
  echo "$design_root is missing or unsafe. Nothing was changed."
  exit 1
fi

typeset -a required_files
required_files=(
  "$canonical/DESIGN.md"
  "$marker"
  "$receipt"
  "$design_root/tools/booster.py"
  "$design_root/evidence/bans.json"
  "$design_root/evidence/observations.json"
  "$canonical/skills/booster/SKILL.md"
  "$canonical/skills/booster-questions/SKILL.md"
  "$canonical/skills/booster-audit/SKILL.md"
)
for required_path in "${required_files[@]}"; do
  if [[ -L "$required_path" ]] || [[ ! -s "$required_path" ]] || [[ ! -f "$required_path" ]]; then
    echo "Incomplete Booster install: missing or empty $required_path"
    echo "Run ./install.sh --agent claude first. Nothing was changed."
    exit 1
  fi
done
if ! grep -q '"name": "booster"' "$marker"; then
  echo "The live library has no valid Booster ownership marker. Nothing was changed."
  exit 1
fi
if ! cmp -s "$marker" booster.json; then
  echo "The live Booster ownership marker uses a different schema."
  echo "Run ./install.sh --agent claude first. Nothing was changed."
  exit 1
fi
for required_dir in \
  "$design_root/packages" \
  "$design_root/notes" \
  "$design_root/evidence" \
  "$design_root/tools" \
  "$canonical/skills/booster" \
  "$canonical/skills/booster-questions" \
  "$canonical/skills/booster-audit"; do
  if [[ -L "$required_dir" ]] || [[ ! -d "$required_dir" ]]; then
    echo "Incomplete Booster install: missing $required_dir. Nothing was changed."
    exit 1
  fi
  if [[ -n "$(find "$required_dir" -type l -print -quit 2>/dev/null)" ]]; then
    echo "Incomplete Booster install: symlink found under $required_dir. Nothing was changed."
    exit 1
  fi
done

python3 tools/booster.py validate --root "$design_root" >/dev/null

workspace="$(mktemp -d "${TMPDIR:-/tmp}/booster-sync.XXXXXX")"
baseline="$workspace/before"
stage="$workspace/after"
mkdir "$baseline" "$stage"

if (( dry_run )); then
  rsync -a --checksum --exclude '.git' ./ "$baseline/"
else
  if ! git checkout-index --all --prefix="$baseline/" 2>/dev/null; then
    echo "Could not materialize the tracked repository baseline. Nothing was changed."
    exit 1
  fi
fi
rsync -a --checksum "$baseline/" "$stage/"
cp "$canonical/DESIGN.md" "$stage/DESIGN.md"
rsync -a --checksum --delete "$design_root/packages/" "$stage/packages/"
rsync -a --checksum --delete "$design_root/notes/" "$stage/notes/"
# Executable tooling is repo-authoritative and is never imported from the live install.
rsync -a --checksum --delete --delete-excluded --exclude '*.lock' "$design_root/evidence/" "$stage/evidence/"
for skill in booster booster-questions booster-audit; do
  rsync -a --checksum --delete "$canonical/skills/$skill/" "$stage/skills/$skill/"
done

typeset -a inventory_args
inventory_args=(inventory-diff --baseline . --candidate "$stage")
(( allow_removals )) && inventory_args+=(--allow-removals)
python3 tools/booster.py "${inventory_args[@]}"
python3 tools/booster.py index --root "$stage" --write evidence/reference-index.json --update-readme
python3 tools/booster.py validate --root "$stage"

export_patch="$workspace/export.patch"
if (cd "$workspace" && git -c diff.noprefix=false diff --no-index --binary \
    --no-ext-diff --no-textconv --src-prefix=a/ --dst-prefix=b/ \
    -- before after > "$export_patch" 2>/dev/null); then
  patch_status=0
else
  patch_status=$?
fi
if (( patch_status != 0 && patch_status != 1 )); then
  echo "Could not construct the validated export patch. Nothing was changed."
  exit 1
fi

echo "Validated export changes:"
if [[ -s "$export_patch" ]]; then
  git apply --stat --summary -p2 "$export_patch"
else
  echo "No managed content changes."
fi

if (( dry_run )); then
  echo "Dry run only; repository unchanged."
  exit 0
fi

if ! current_status="$(git status --porcelain --untracked-files=all 2>/dev/null)" || \
   ! current_head="$(git rev-parse --verify HEAD 2>/dev/null)" || \
   ! current_index_tree="$(git write-tree 2>/dev/null)"; then
  echo "Cannot recheck repository state; refusing the export. Nothing was changed."
  exit 1
fi
if [[ -n "$current_status" ]] || [[ "$current_head" != "$initial_head" ]] || \
   [[ "$current_index_tree" != "$initial_index_tree" ]]; then
  echo "Repository changed while the export was staged; refusing to overwrite it. Nothing was changed."
  exit 1
fi

if [[ -s "$export_patch" ]]; then
  if ! git -c apply.whitespace=nowarn -c apply.ignoreWhitespace=false \
      apply --binary --whitespace=nowarn -p2 \
      "$export_patch" 2>/dev/null; then
    echo "Repository content changed before the atomic patch could apply. Nothing was changed."
    exit 1
  fi
fi
if ! trees_match "$stage" .; then
  rollback_ok=0
  if [[ -s "$export_patch" ]] && \
     git -c apply.whitespace=nowarn -c apply.ignoreWhitespace=false \
       apply --reverse --binary --whitespace=nowarn \
       -p2 "$export_patch" >/dev/null 2>&1 && trees_match "$baseline" .; then
    rollback_ok=1
  fi
  if (( rollback_ok )); then
    echo "Applied export differed from its validated stage and was rolled back safely."
  else
    echo "Applied export verification failed; concurrent changes were preserved for manual recovery."
  fi
  exit 1
fi
python3 tools/booster.py validate --root .
echo "Exported and validated $(find packages -name '*.md' | wc -l | tr -d ' ') package files."
