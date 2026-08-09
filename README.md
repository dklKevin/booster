# Booster

An anti-generic design system for AI agents.
It exists because model-generated design collapses to a statistical mode, and the reliable way out is naming the mode and banning it, not asking for creativity.

## How it works

- `DESIGN.md` is the core: a ban list grown only from observed failures, hard floors, a derive step with four gates (uniqueness, no cloning, category legibility, believability), and a screenshot-then-judge loop.
- `packages/` is a two-axis reference library distilled from live sites' real CSS.
  Form packages (interface, editorial, document, personal, gallery, showcase) say how a page is built.
  Sector packages (`packages/sectors/`, 15 industries) say what credibility means in an industry, including each sector's own mode to avoid.
- `skills/` holds the routing skills: `/booster` scans a repo and recommends which packs and refs to load; `/booster-questions` interviews first.

## Loading rule

Read the matching form PACK.md, the sector PACK.md when the brief belongs to an industry, plus a small set of refs chosen to span a range.
Never load a whole refs folder; the library is wide so no single ref can dominate.
Builders choose two refs from four offered and must name their choices.

## Rules of growth

New bans enter only from observed failures, with the sighting log kept in the ban entry.
Refs enter by propose-and-veto; the library is a record of taste, not a scrape.
Positive prescriptions are avoided on principle: bans preserve freedom, prescriptions collapse it.

## Sync

The canonical copies live in `~/.claude/`.
Run `./sync.sh` to pull the current state into this repo before committing.
