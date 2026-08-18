#!/bin/zsh
set -euo pipefail
setopt NO_BG_NICE
cd "$(dirname "$0")/.."

test_root="$(mktemp -d "${TMPDIR:-/tmp}/booster-install-test.XXXXXX")"
cleanup() { rm -rf "$test_root"; }
trap cleanup EXIT INT TERM

test_home="$test_root/home"
mkdir -p "$test_home"

test "$(zsh install.sh --version)" = "0.1.0"
test "$(zsh install.sh -V)" = "0.1.0"
test "$(zsh sync.sh --version)" = "0.1.0"
test "$(zsh sync.sh -V)" = "0.1.0"

set +e
zsh install.sh --agent invalid >/dev/null 2>&1
invalid_agent_status=$?
zsh install.sh --version --invalid >/dev/null 2>&1
invalid_install_version_status=$?
zsh sync.sh --version --invalid >/dev/null 2>&1
invalid_sync_version_status=$?
set -e
test "$invalid_agent_status" -eq 2
test "$invalid_install_version_status" -eq 2
test "$invalid_sync_version_status" -eq 2

collision_home="$test_root/collision-home"
mkdir -p "$collision_home/.agents/skills/booster"
cat > "$collision_home/.agents/skills/booster/SKILL.md" <<'EOF'
---
name: booster
description: An unrelated colliding skill.
---
EOF
touch "$collision_home/.agents/skills/booster/preserve-me"
if HOME="$collision_home" zsh install.sh --agent codex >/dev/null 2>&1; then
  echo "install accepted an unowned colliding skill"
  exit 1
fi
test -f "$collision_home/.agents/skills/booster/preserve-me"

symlink_home="$test_root/symlink-home"
symlink_target="$test_root/unrelated-packages"
mkdir -p "$symlink_home/.claude/design" "$symlink_target"
touch "$symlink_target/preserve-me"
ln -s "$symlink_target" "$symlink_home/.claude/design/packages"
if HOME="$symlink_home" zsh install.sh --agent claude >/dev/null 2>&1; then
  echo "install accepted a symlinked managed directory"
  exit 1
fi
test -f "$symlink_target/preserve-me"

marker_home="$test_root/marker-home"
mkdir -p "$marker_home/.claude/design/packages"
touch "$marker_home/.claude/design/packages/preserve-me"
printf '{"name":"booster","schema_version":999}\n' > "$marker_home/.claude/design/booster.json"
if HOME="$marker_home" zsh install.sh --agent claude >/dev/null 2>&1; then
  echo "install accepted an incompatible ownership marker"
  exit 1
fi
test -f "$marker_home/.claude/design/packages/preserve-me"

boolean_marker_home="$test_root/boolean-marker-home"
mkdir -p "$boolean_marker_home/.claude/design/packages"
touch "$boolean_marker_home/.claude/design/packages/preserve-me"
printf '%s\n' '{"name":"booster","schema_version":true,"canonical_home":"~/.claude","managed_library_paths":["DESIGN.md","design/packages","design/notes","design/tools","design/evidence"]}' > "$boolean_marker_home/.claude/design/booster.json"
if HOME="$boolean_marker_home" zsh install.sh --agent claude >/dev/null 2>&1; then
  echo "install accepted a boolean ownership schema"
  exit 1
fi
test -f "$boolean_marker_home/.claude/design/packages/preserve-me"

truncated_marker_home="$test_root/truncated-marker-home"
mkdir -p "$truncated_marker_home/.claude/design/packages"
touch "$truncated_marker_home/.claude/design/packages/preserve-me"
printf '{"name":"booster","schema_version":1}\n' > "$truncated_marker_home/.claude/design/booster.json"
if HOME="$truncated_marker_home" zsh install.sh --agent claude >/dev/null 2>&1; then
  echo "install accepted a truncated ownership marker"
  exit 1
fi
test -f "$truncated_marker_home/.claude/design/packages/preserve-me"

legacy_home="$test_root/legacy-home"
mkdir -p "$legacy_home/.claude/skills/booster" "$legacy_home/.claude/skills/booster-questions"
cat > "$legacy_home/.claude/DESIGN.md" <<'EOF'
# Design invariants
## Ban list (the mode, excised by name)
Refs are range markers selected narrowly for each brief.
EOF
cat > "$legacy_home/.claude/skills/booster/SKILL.md" <<'EOF'
You are routing a brief to the right slice of Kevin's design library.
a builder that picks its own range markers derives more and clones less.
EOF
cat > "$legacy_home/.claude/skills/booster-questions/SKILL.md" <<'EOF'
Same destination as `/booster`, reached through a short interview.
Kevin works strictly this way: ask one question at a time.
EOF
cp "$legacy_home/.claude/DESIGN.md" "$test_root/legacy-design-original"
ln "$legacy_home/.claude/DESIGN.md" "$test_root/legacy-design-outside"
HOME="$legacy_home" zsh install.sh --agent claude >/dev/null
test -f "$legacy_home/.claude/skills/booster/booster-skill.json"
cmp -s "$test_root/legacy-design-original" "$test_root/legacy-design-outside"

HOME="$test_home" zsh install.sh --agent claude --agent codex >/dev/null
test -f "$test_home/.claude/DESIGN.md"
test -f "$test_home/.claude/design/booster.json"
test -f "$test_home/.claude/design/.booster-installed.json"
test -f "$test_home/.claude/design/tools/booster.py"
test -f "$test_home/.claude/skills/booster-audit/SKILL.md"
test -f "$test_home/.agents/skills/booster/SKILL.md"
HOME="$test_home" python3 "$test_home/.claude/design/tools/booster.py" >/dev/null
HOME="$test_home" python3 "$test_home/.claude/design/tools/booster.py" index \
  --root "$test_home/.claude/design" >/dev/null
HOME="$test_home" python3 "$test_home/.claude/design/tools/booster.py" validate --json >/dev/null
HOME="$test_home" zsh sync.sh --dry-run > "$test_root/clean-preview.log"
grep -q '^No managed content changes\.$' "$test_root/clean-preview.log"
if grep -Eq '^[.<>ch*][^[:space:]]{8,}' "$test_root/clean-preview.log"; then
  echo "dry-run preview reported metadata-only rsync changes"
  exit 1
fi

# A second install must be idempotent.
HOME="$test_home" zsh install.sh --agent claude --agent codex >/dev/null

# A compatible prior marker may have release-specific inventory that differs.
python3 - "$test_home/.claude/design/booster.json" <<'PY'
import json
import sys

path = sys.argv[1]
with open(path, encoding="utf-8") as handle:
    marker = json.load(handle)
marker["skills"] = ["booster"]
marker["required_managed_paths"] = ["notes/gwern.md"]
with open(path, "w", encoding="utf-8") as handle:
    json.dump(marker, handle)
    handle.write("\n")
PY
HOME="$test_home" zsh install.sh --agent claude --agent codex >/dev/null

# A reinstall must merge and preserve live observation evidence.
baseline_observations="$(python3 -c 'import json,sys; print(len(json.load(open(sys.argv[1]))["observations"]))' "$test_home/.claude/design/evidence/observations.json")"
python3 "$test_home/.claude/design/tools/booster.py" observe \
  --root "$test_home/.claude/design" \
  --pattern "floating status cards" \
  --subject "clinic scheduling" \
  --model "test-model" \
  --artifact "$test_root/build-a" \
  --note "explicit rejection" \
  --date "2026-08-17" >/dev/null
HOME="$test_home" zsh install.sh --agent claude --agent codex >/dev/null
installed_observations="$(python3 -c 'import json,sys; print(len(json.load(open(sys.argv[1]))["observations"]))' "$test_home/.claude/design/evidence/observations.json")"
test "$installed_observations" -eq $(( baseline_observations + 1 ))
grep -q '"pattern": "floating status cards"' "$test_home/.claude/design/evidence/observations.json"

# Shell help is a successful universal capability.
zsh sync.sh --help >/dev/null

# A non-dry export must fail closed when repository state is unavailable.
no_git_repo="$test_root/no-git-repo"
mkdir -p "$no_git_repo"
rsync -a --exclude '.git' ./ "$no_git_repo/"
if HOME="$test_home" zsh "$no_git_repo/sync.sh" >/dev/null 2>&1; then
  echo "sync proceeded without a readable Git repository"
  exit 1
fi

# A failed lock acquisition must never remove another export's lock.
lock_repo="$test_root/lock-repo"
mkdir -p "$lock_repo"
rsync -a --exclude '.git' ./ "$lock_repo/"
git -C "$lock_repo" init -q
git -C "$lock_repo" add .
git -C "$lock_repo" -c user.name=Booster -c user.email=booster@example.invalid commit -qm baseline
mkdir "$lock_repo/.git/booster-sync.lock"
if HOME="$test_home" zsh "$lock_repo/sync.sh" >/dev/null 2>&1; then
  echo "sync ignored an existing export lock"
  exit 1
fi
test -d "$lock_repo/.git/booster-sync.lock"

# A validated non-dry export applies as one preimage-checked patch.
success_repo="$test_root/success-repo"
mkdir -p "$success_repo"
rsync -a --exclude '.git' ./ "$success_repo/"
git -C "$success_repo" init -q
git -C "$success_repo" add .
git -C "$success_repo" -c user.name=Booster -c user.email=booster@example.invalid commit -qm baseline
git -C "$success_repo" config diff.noprefix true
git -C "$success_repo" config apply.whitespace fix
git -C "$success_repo" config apply.ignoreWhitespace change
printf 'ambient whitespace   \n' >> "$test_home/.claude/design/notes/gwern.md"
python3 - "$test_home/.claude/design/notes/gwern.md" "$success_repo/notes/gwern.md" <<'PY'
import os
import pathlib
import sys

live = pathlib.Path(sys.argv[1])
repo = pathlib.Path(sys.argv[2])
text = live.read_text(encoding="utf-8")
if "Grayscale" not in text:
    raise SystemExit("fixture lacks Grayscale token")
live.write_text(text.replace("Grayscale", "Xrayscale", 1), encoding="utf-8")
stat = repo.stat()
os.utime(live, ns=(stat.st_atime_ns, stat.st_mtime_ns))
PY
if ! GIT_EXTERNAL_DIFF=/usr/bin/true HOME="$test_home" \
    zsh "$success_repo/sync.sh" > "$test_root/success-sync.log" 2>&1; then
  cat "$test_root/success-sync.log"
  exit 1
fi
python3 "$success_repo/tools/booster.py" validate --root "$success_repo" >/dev/null
grep -q '"pattern": "floating status cards"' "$success_repo/evidence/observations.json"
python3 -c 'import pathlib,sys; assert "ambient whitespace   \n" in pathlib.Path(sys.argv[1]).read_text()' "$success_repo/notes/gwern.md"
grep -q 'Xrayscale' "$success_repo/notes/gwern.md"
HOME="$test_home" zsh install.sh --agent claude --agent codex >/dev/null

# Ambient Git config cannot hide an untracked managed file from the clean guard.
status_repo="$test_root/status-repo"
mkdir -p "$status_repo"
rsync -a --exclude '.git' ./ "$status_repo/"
git -C "$status_repo" init -q
git -C "$status_repo" add .
git -C "$status_repo" -c user.name=Booster -c user.email=booster@example.invalid commit -qm baseline
git -C "$status_repo" config status.showUntrackedFiles no
touch "$status_repo/packages/interface/preserve-user-data.txt"
if HOME="$test_home" zsh "$status_repo/sync.sh" >/dev/null 2>&1; then
  echo "sync accepted a hidden untracked managed file"
  exit 1
fi
test -f "$status_repo/packages/interface/preserve-user-data.txt"

# Linked worktrees use a .git file and must verify without treating it as content.
linked_source="$test_root/linked-source"
linked_repo="$test_root/linked-repo"
mkdir -p "$linked_source"
rsync -a --exclude '.git' ./ "$linked_source/"
git -C "$linked_source" init -q
git -C "$linked_source" add .
git -C "$linked_source" -c user.name=Booster -c user.email=booster@example.invalid commit -qm baseline
git -C "$linked_source" worktree add -q "$linked_repo"
HOME="$test_home" zsh "$linked_repo/sync.sh" >/dev/null
python3 "$linked_repo/tools/booster.py" validate --root "$linked_repo" >/dev/null

# A concurrent tracked edit after staging starts must survive and abort export.
race_repo="$test_root/race-repo"
race_tmp="$test_root/race-tmp"
mkdir -p "$race_repo" "$race_tmp"
rsync -a --exclude '.git' ./ "$race_repo/"
git -C "$race_repo" init -q
git -C "$race_repo" add .
git -C "$race_repo" -c user.name=Booster -c user.email=booster@example.invalid commit -qm baseline
(
  while [[ -z "$(find "$race_tmp" -maxdepth 1 -type d -name 'booster-sync.*' -print -quit)" ]]; do
    sleep 0.01
  done
  print '\n<!-- concurrent edit -->' >> "$race_repo/packages/interface/PACK.md"
) &
race_writer=$!
if HOME="$test_home" TMPDIR="$race_tmp" zsh "$race_repo/sync.sh" >/dev/null 2>&1; then
  echo "sync overwrote a concurrent tracked edit"
  wait "$race_writer"
  exit 1
fi
wait "$race_writer"
grep -q 'concurrent edit' "$race_repo/packages/interface/PACK.md"

# A complete live install must pass the staged dry run.
HOME="$test_home" zsh sync.sh --dry-run >/dev/null

# A structurally truncated managed document must fail before export.
sed -n '1,4p' "$test_home/.claude/skills/booster/SKILL.md" > "$test_home/truncated-skill.md"
mv "$test_home/truncated-skill.md" "$test_home/.claude/skills/booster/SKILL.md"
if HOME="$test_home" zsh sync.sh --dry-run >/dev/null 2>&1; then
  echo "sync accepted a truncated managed skill"
  exit 1
fi
HOME="$test_home" zsh install.sh --agent claude --agent codex >/dev/null

# A partial skill directory must fail before an export can delete repo support files.
mv "$test_home/.claude/skills/booster/references/direction-record.md" "$test_home/direction-record.saved"
if HOME="$test_home" zsh sync.sh --dry-run >/dev/null 2>&1; then
  echo "sync accepted an incomplete Booster skill"
  exit 1
fi
HOME="$test_home" zsh install.sh --agent claude --agent codex >/dev/null

# An incomplete live library must fail before sync touches the repository.
mv "$test_home/.claude/design/packages/sectors" "$test_home/sectors.saved"
mkdir "$test_home/.claude/design/packages/sectors"
if HOME="$test_home" zsh sync.sh --dry-run >/dev/null 2>&1; then
  echo "sync accepted an empty sectors directory"
  exit 1
fi

echo "install and sync safety checks passed"
