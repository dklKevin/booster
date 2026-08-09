---
name: booster
description: Scan the current repo/brief and recommend which design packs and refs from Kevin's design library (~/.claude/design/packages/) to load before building any UI or page. Use whenever the user invokes /booster, asks "which pack should I use", "what design direction fits this project", or wants a design recommendation grounded in the library instead of picking packs by hand. This is the manual routing entry point for the design system.
---

# Booster: design-pack routing

You are routing a brief to the right slice of Kevin's design library so the build derives from evidence instead of the mode.
The library is two-axis: form packages (how a page is built) and sector packages (what credibility means in an industry).
Loading narrow matters: 2-3 refs total, chosen for the brief, so no single site can dominate the generation.

## Step 1: Scan for context

Gather only what identifies the subject, audience, and job of the page. Usual sources, cheapest first:
- The conversation itself: if the user already described what they're building, that outranks everything on disk.
- README.md, package.json (name/description/dependencies), site copy in src/pages or app/ routes, marketing strings.
- Domain keywords that signal a sector (patients/clinical, flights/fleet, contributors/license, reps/scoops, funds/portfolio...).

Do not deep-read the codebase; this is a routing decision, not a review. A minute of scanning is the budget.

## Step 2: Pick the form package

One of `~/.claude/design/packages/`: interface (tool/app UI with controls), editorial (idea-led presentation and landing pages), document (long-form reading), personal (Kevin's own identity/portfolio), gallery (imagery-first, interface recedes), showcase (a physical object that must be desired).
Pick by the page's job, not its industry.

## Step 3: Pick the sector package, if one applies

`ls ~/.claude/design/packages/sectors/` for the current list; match the brief's industry.
Many briefs have no sector: that is a normal outcome, not a failure. Never force a sector fit.

## Step 4: Choose refs

Read the chosen packages' PACK.md range maps, then pick refs that SPAN a range relevant to the brief (two different poles beat two similar sites).
Cross-package borrowing is legitimate: a hospital dashboard might take one interface ref and one hospital ref.
Prefer offering FOUR pole-spanning refs with the instruction to choose two and name the choices; a builder that picks its own range markers derives more and clones less.
Rotate refs between builds on the same subject; feeding the same trio every time re-converges the results.

## Step 5: Deliver the recommendation

ALWAYS use this exact shape:

```
## Booster recommendation

Form: packages/<name> - [one line: why this is the page's job]
Sector: packages/sectors/<name> - [one line] (or "none: [reason]")
Refs (offer these; builder chooses two and names them):
- <path> - [the pole it covers for this brief]
- <path> - [the pole it covers for this brief]
- <path> - [the pole it covers for this brief]
- <path> - [the pole it covers for this brief]

Reminders: DESIGN.md ban list + hard floors apply; sketch three directions before committing;
all four gates are live (uniqueness including page outline, no cloning, category legibility,
believability: would this organization actually ship it?).
```

Then offer to load the recommended files into context and start the derive step immediately; if the user declines, they have the file list to use manually or to hand to another agent.

If the scan leaves you genuinely unsure between two form packs or two sectors, say so in one line and recommend `/booster-questions` instead of guessing.
