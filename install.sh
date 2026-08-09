#!/bin/zsh
# Install Booster from this repo into ~/.claude, where agents read it.
# Safe to re-run; existing Booster files are updated in place.
set -e
cd "$(dirname "$0")"

if [ -f "$HOME/.claude/DESIGN.md" ] && ! grep -q "Design invariants" "$HOME/.claude/DESIGN.md"; then
  echo "A ~/.claude/DESIGN.md exists that does not look like Booster's."
  echo "Back it up or remove it, then re-run. Nothing was changed."
  exit 1
fi

mkdir -p "$HOME/.claude/design" "$HOME/.claude/skills/booster" "$HOME/.claude/skills/booster-questions"
cp DESIGN.md "$HOME/.claude/DESIGN.md"
rsync -a packages/ "$HOME/.claude/design/packages/"
rsync -a notes/ "$HOME/.claude/design/notes/"
cp skills/booster/SKILL.md "$HOME/.claude/skills/booster/"
cp skills/booster-questions/SKILL.md "$HOME/.claude/skills/booster-questions/"

echo "Installed: DESIGN.md, $(find packages -name '*.md' | wc -l | tr -d ' ') package files, 2 skills."
echo "Wire it in: add a line to your ~/.claude/CLAUDE.md telling agents to read ~/.claude/DESIGN.md before designing any UI or page."
