#!/bin/zsh
# Pull the live design system from ~/.claude into this repo (maintainer direction).
# For first-time setup from a fresh clone, run ./install.sh instead; this script
# refuses to run against a machine that does not have a full Booster install.
set -e
cd "$(dirname "$0")"

if [ ! -s "$HOME/.claude/DESIGN.md" ] || ! grep -q "Design invariants" "$HOME/.claude/DESIGN.md"; then
  echo "No Booster install found at ~/.claude (DESIGN.md missing or not Booster's)."
  echo "This script syncs live -> repo and would overwrite the repo with nothing."
  echo "You probably want ./install.sh. Nothing was changed."
  exit 1
fi
if [ ! -d "$HOME/.claude/design/packages/sectors" ] || [ -z "$(ls "$HOME/.claude/design/packages" 2>/dev/null)" ]; then
  echo "~/.claude/design/packages is missing or empty; refusing to sync. Nothing was changed."
  exit 1
fi

cp "$HOME/.claude/DESIGN.md" .
rsync -a --delete "$HOME/.claude/design/packages/" packages/
rsync -a --delete "$HOME/.claude/design/notes/" notes/
cp "$HOME/.claude/skills/booster/SKILL.md" skills/booster/
cp "$HOME/.claude/skills/booster-questions/SKILL.md" skills/booster-questions/
echo "synced $(find packages -name '*.md' | wc -l | tr -d ' ') package files"
