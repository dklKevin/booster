#!/bin/zsh
# Pull the live design system from ~/.claude into this repo.
set -e
cd "$(dirname "$0")"
cp ~/.claude/DESIGN.md .
rsync -a --delete ~/.claude/design/packages/ packages/
rsync -a --delete ~/.claude/design/notes/ notes/
cp ~/.claude/skills/booster/SKILL.md skills/booster/
cp ~/.claude/skills/booster-questions/SKILL.md skills/booster-questions/
echo "synced $(find packages -name '*.md' | wc -l | tr -d ' ') package files"
