#!/bin/zsh
# Install Booster's library into ~/.claude or ~/.grok and its skills into one
# or more agent homes. Safe to re-run; only Booster-owned directories are replaced.
set -euo pipefail
cd "${0:A:h}"

VERSION="0.1.0"

usage() {
  print -r -- "usage: ./install.sh [--agent claude|codex|grok|universal|all]..."
  print -r -- ""
  print -r -- "options:"
  print -r -- "  --agent TARGET   install skills for TARGET; repeatable (default: claude)"
  print -r -- "  -h, --help       show this help"
  print -r -- "  -v, -V, --version  print the Booster version"
  print -r -- ""
  print -r -- "example: ./install.sh --agent claude --agent codex"
}

if (( $# == 1 )) && [[ "$1" == -v || "$1" == -V || "$1" == --version ]]; then
  echo "$VERSION"
  exit 0
fi

typeset -a agents
agents=()
while (( $# > 0 )); do
  case "$1" in
    --agent)
      (( $# >= 2 )) || { usage; exit 2; }
      agents+=("$2")
      shift 2
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      usage
      exit 2
      ;;
  esac
done
(( ${#agents[@]} > 0 )) || agents=(claude)

typeset -a install_roots
install_roots=()
for agent in "${agents[@]}"; do
  case "$agent" in
    claude) install_roots+=("$HOME/.claude/skills") ;;
    codex) install_roots+=("$HOME/.agents/skills") ;;
    grok) install_roots+=("$HOME/.grok/skills") ;;
    universal) install_roots+=("$HOME/.agents/skills") ;;
    all)
      install_roots+=("$HOME/.claude/skills" "$HOME/.grok/skills" "$HOME/.agents/skills")
      ;;
    *)
      echo "unknown agent target: $agent"
      usage
      exit 2
      ;;
  esac
done

for dependency in python3 rsync cp mkdir find grep cmp wc tr; do
  if ! command -v "$dependency" >/dev/null 2>&1; then
    echo "Missing required command: $dependency. Nothing was changed."
    exit 1
  fi
done

python3 tools/booster.py validate --root .

typeset -A seen_roots
for root in "${install_roots[@]}"; do
  [[ -n "${seen_roots[$root]-}" ]] && continue
  seen_roots[$root]=1
  if [[ -L "$root" ]] || [[ -e "$root" && ! -d "$root" ]]; then
    echo "$root is not a regular skill directory. Nothing was changed."
    exit 1
  fi
  for skill in booster booster-questions booster-audit; do
    target="$root/$skill"
    if [[ -L "$target" ]]; then
      echo "$target is a symlink; refusing to replace its destination. Nothing was changed."
      exit 1
    fi
    if [[ -d "$target" ]]; then
      if [[ -f "$target/booster-skill.json" ]]; then
        if ! cmp -s "skills/$skill/booster-skill.json" "$target/booster-skill.json"; then
          echo "$target has an incompatible Booster ownership marker. Nothing was changed."
          exit 1
        fi
      else
        legacy_skill=0
        case "$skill" in
          booster)
            [[ -f "$target/SKILL.md" ]] && \
              grep -q "You are routing a brief to the right slice of Kevin's design library" "$target/SKILL.md" && \
              grep -q "a builder that picks its own range markers derives more and clones less" "$target/SKILL.md" && legacy_skill=1
            ;;
          booster-questions)
            [[ -f "$target/SKILL.md" ]] && \
              grep -q 'Same destination as `/booster`' "$target/SKILL.md" && \
              grep -q "Kevin works strictly this way" "$target/SKILL.md" && legacy_skill=1
            ;;
          booster-audit)
            [[ -f "$target/SKILL.md" ]] && \
              cmp -s "skills/$skill/SKILL.md" "$target/SKILL.md" && legacy_skill=1
            ;;
        esac
        if (( ! legacy_skill )); then
          echo "$target is not marked as a Booster-owned skill. Nothing was changed."
          exit 1
        fi
      fi
    elif [[ -e "$target" ]]; then
      echo "$target exists and is not a directory. Nothing was changed."
      exit 1
    fi
  done
done

wants_claude=0
wants_grok=0
for agent in "${agents[@]}"; do
  case "$agent" in
    claude) wants_claude=1 ;;
    grok) wants_grok=1 ;;
    all)
      wants_claude=1
      wants_grok=1
      ;;
  esac
done
if [[ -n "${BOOSTER_HOME:-}" ]]; then
  canonical="${BOOSTER_HOME/#\~/$HOME}"
elif (( wants_claude == 0 && wants_grok == 1 )); then
  canonical="$HOME/.grok"
else
  canonical="$HOME/.claude"
fi
if [[ "$canonical" == "$HOME/.grok" ]]; then
  home_label="~/.grok"
elif [[ "$canonical" == "$HOME/.claude" ]]; then
  home_label="~/.claude"
else
  home_label="$canonical"
fi
design_root="$canonical/design"
marker="$design_root/booster.json"
receipt="$design_root/.booster-installed.json"
live_observations="$design_root/evidence/observations.json"

if [[ -L "$design_root" ]]; then
  echo "$design_root is a symlink; refusing to replace its destination. Nothing was changed."
  exit 1
fi
if [[ -L "$canonical/DESIGN.md" ]] || [[ -e "$canonical/DESIGN.md" && ! -f "$canonical/DESIGN.md" ]]; then
  echo "$canonical/DESIGN.md is not a regular file. Nothing was changed."
  exit 1
fi
if [[ -L "$marker" ]] || [[ -e "$marker" && ! -f "$marker" ]]; then
  echo "$marker is not a regular file. Nothing was changed."
  exit 1
fi
if [[ -L "$receipt" ]] || [[ -e "$receipt" && ! -f "$receipt" ]]; then
  echo "$receipt is not a regular install receipt. Nothing was changed."
  exit 1
fi
if [[ -f "$receipt" ]] && ! python3 - "$receipt" <<'PY'
import json
import sys

try:
    value = json.load(open(sys.argv[1], encoding="utf-8"))
except (OSError, UnicodeError, json.JSONDecodeError):
    raise SystemExit(1)
valid = (
    isinstance(value, dict)
    and value.get("name") == "booster-installed-library"
    and type(value.get("schema_version")) is int
    and value["schema_version"] == 1
)
raise SystemExit(0 if valid else 1)
PY
then
  echo "$receipt is invalid. Nothing was changed."
  exit 1
fi
for managed_dir in packages notes tools evidence; do
  managed_path="$design_root/$managed_dir"
  if [[ -L "$managed_path" ]] || [[ -e "$managed_path" && ! -d "$managed_path" ]]; then
    echo "$managed_path is not a regular managed directory. Nothing was changed."
    exit 1
  fi
done
if [[ -L "$live_observations" ]] || [[ -e "$live_observations" && ! -f "$live_observations" ]]; then
  echo "$live_observations is not a regular evidence file. Nothing was changed."
  exit 1
fi

legacy_install=0
if [[ -f "$canonical/DESIGN.md" && ! -f "$marker" ]]; then
  if ! grep -q "the mode, excised by name" "$canonical/DESIGN.md" || \
     ! grep -q "Refs are range markers" "$canonical/DESIGN.md"; then
    echo "A non-Booster $canonical/DESIGN.md already exists."
    echo "Back it up or choose another home before installing. Nothing was changed."
    exit 1
  fi
  echo "Recognized a legacy Booster install; adding the ownership marker."
  legacy_install=1
fi

if [[ -f "$marker" ]]; then
  if ! python3 - "$marker" booster.json <<'PY'
import json
import sys

try:
    installed = json.load(open(sys.argv[1], encoding="utf-8"))
    source = json.load(open(sys.argv[2], encoding="utf-8"))
except (OSError, UnicodeError, json.JSONDecodeError):
    raise SystemExit(1)
compatible = (
    isinstance(installed, dict)
    and isinstance(source, dict)
    and installed.get("name") == source.get("name") == "booster"
    and type(installed.get("schema_version")) is int
    and type(source.get("schema_version")) is int
    and installed.get("schema_version") == source.get("schema_version")
    and isinstance(installed.get("canonical_home"), str)
    and installed["canonical_home"].strip() != ""
    and (
        installed["canonical_home"].startswith("~/")
        or installed["canonical_home"].startswith("/")
    )
    and installed.get("managed_library_paths") == source.get("managed_library_paths")
)
raise SystemExit(0 if compatible else 1)
PY
  then
    echo "$marker has an incompatible Booster ownership schema. Nothing was changed."
    exit 1
  fi
fi
if [[ ! -f "$marker" && $legacy_install -eq 0 && -d "$design_root" ]] && \
   [[ -n "$(find "$design_root" -mindepth 1 -print -quit 2>/dev/null)" ]]; then
  echo "$design_root already contains unowned files. Nothing was changed."
  exit 1
fi
if [[ -f "$live_observations" ]]; then
  if [[ ! -f "$marker" ]]; then
    echo "A live observation ledger exists without a Booster ownership marker. Nothing was changed."
    exit 1
  fi
  PYTHONDONTWRITEBYTECODE=1 python3 - "$PWD/tools/booster.py" "$design_root" <<'PY'
import importlib.util
import pathlib
import sys

spec = importlib.util.spec_from_file_location("booster_install_check", sys.argv[1])
if spec is None or spec.loader is None:
    raise SystemExit(1)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
issues = []
module._validate_observations(pathlib.Path(sys.argv[2]), issues)
raise SystemExit(1 if any(item["severity"] == "error" for item in issues) else 0)
PY
fi

mkdir -p "$design_root/packages" "$design_root/notes" "$design_root/tools" "$design_root/evidence"
if (( legacy_install )); then
  rsync -a --checksum packages/ "$design_root/packages/"
  rsync -a --checksum notes/ "$design_root/notes/"
  rsync -a --checksum --exclude '__pycache__/' --exclude '*.pyc' tools/ "$design_root/tools/"
  rsync -a --checksum --exclude 'observations.json' --exclude '*.lock' evidence/ "$design_root/evidence/"
else
  rsync -a --checksum --delete packages/ "$design_root/packages/"
  rsync -a --checksum --delete notes/ "$design_root/notes/"
  rsync -a --checksum --delete --delete-excluded --exclude '__pycache__/' --exclude '*.pyc' tools/ "$design_root/tools/"
  rsync -a --checksum --delete --exclude 'observations.json' --exclude '*.lock' evidence/ "$design_root/evidence/"
fi
[[ -f "$live_observations" ]] || cp evidence/observations.json "$live_observations"

seen_roots=()
for root in "${install_roots[@]}"; do
  [[ -n "${seen_roots[$root]-}" ]] && continue
  seen_roots[$root]=1
  mkdir -p "$root"
  for skill in booster booster-questions booster-audit; do
    target="$root/$skill"
    mkdir -p "$target"
    rsync -a --checksum --delete "skills/$skill/" "$target/"
  done
done

# Canonical single files use temp+replace so an existing hard link cannot
# transmit writes outside the Booster install.
python3 - DESIGN.md "$canonical/DESIGN.md" booster.json "$marker" "$receipt" "$home_label" <<'PY'
import json
import os
import shutil
import stat
import sys


def atomic_copy(source, target):
    temporary = f"{target}.booster-install.{os.getpid()}"
    descriptor = None
    try:
        flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL
        if hasattr(os, "O_NOFOLLOW"):
            flags |= os.O_NOFOLLOW
        descriptor = os.open(temporary, flags, 0o600)
        with os.fdopen(descriptor, "wb") as output, open(source, "rb") as input_file:
            descriptor = None
            shutil.copyfileobj(input_file, output)
            output.flush()
            os.fsync(output.fileno())
        os.chmod(temporary, stat.S_IMODE(os.stat(source).st_mode))
        os.replace(temporary, target)
    finally:
        if descriptor is not None:
            os.close(descriptor)
        try:
            os.unlink(temporary)
        except FileNotFoundError:
            pass


def atomic_write_json(target, value):
    temporary = f"{target}.booster-install.{os.getpid()}"
    with open(temporary, "x", encoding="utf-8") as handle:
        json.dump(value, handle, indent=2)
        handle.write("\n")
        handle.flush()
        os.fsync(handle.fileno())
    os.chmod(temporary, stat.S_IMODE(os.stat(sys.argv[3]).st_mode))
    os.replace(temporary, target)


atomic_copy(sys.argv[1], sys.argv[2])
marker = json.loads(open(sys.argv[3], encoding="utf-8").read())
marker["canonical_home"] = sys.argv[6]
atomic_write_json(sys.argv[4], marker)
receipt_path = sys.argv[5]
atomic_write_json(
    receipt_path,
    {"name": "booster-installed-library", "schema_version": 1},
)
PY

python3 tools/booster.py observations-merge \
  --root "$design_root" \
  --from "$PWD/evidence/observations.json" >/dev/null

echo "Installed: DESIGN.md, $(find packages -name '*.md' | wc -l | tr -d ' ') package files, tools, evidence, and 3 skills."
echo "Library home: $canonical"
echo "Wire it in: tell each agent to read $canonical/DESIGN.md before designing any UI or page."
echo "Verify the installed library: python3 $design_root/tools/booster.py validate"
