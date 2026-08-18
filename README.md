<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/wordmark-dark.svg">
    <img src="assets/wordmark-light.svg" alt="Booster" width="560">
  </picture>
</p>

<p align="center">
  An anti-generic design system for AI agents.<br>
  Generated design collapses to a statistical mode.<br>
  The way out is not asking for creativity. It is naming the mode and banning it.
</p>

<p align="center">
  <img alt="form packs" src="https://img.shields.io/badge/form_packs-6-17131f">
  <img alt="sector packs" src="https://img.shields.io/badge/sector_packs-16-17131f">
  <img alt="distilled refs" src="https://img.shields.io/badge/distilled_refs-164-495e69">
  <img alt="sector modes" src="https://img.shields.io/badge/sector_modes-72-495e69">
  <img alt="bans" src="https://img.shields.io/badge/design_bans-18-8a2f40">
</p>

---

## Why this exists

Ask a model for a webpage and you get the same page everyone else gets: the gradient hero, the rounded card grid, the cream-and-terracotta palette, the headline with one italic accent word.
That output is not a lack of effort.
It is the statistical center of the training distribution, and more reasoning effort only polishes it.

Booster moves probability mass off the mode with three levers that testing bore out:

| Lever | Instead of |
|---|---|
| Bans with explicit provenance status | Aspirational adjectives ("make it unique") |
| A wide reference library, loaded narrow | A few examples pasted into every prompt |
| Outcome gates checked on screenshots | Process rules that template the result |

## Anatomy

```
DESIGN.md               the invariants: ban list, hard floors, derive step, judge step
packages/
  interface/            how a tool is built          PACK.md + refs/
  editorial/            how an idea page is built
  document/             how long-form reading is built
  personal/             how an identity page is built
  gallery/              how imagery-first pages are built
  showcase/             how objects are made desirable
  sectors/              what credibility means, per industry
    hospital/ retail/ law/ defense/ ...              PACK.md + refs/ + modes/
skills/
  booster/              scan a repo, recommend packs and refs
  booster-questions/    interview first, then recommend
  booster-audit/        inspect rendered evidence and report blocking failures
tools/
  booster.py            validate, index, search, observe, and surface candidates
evidence/
  bans.json             stable ban IDs and honest provenance status
  observations.json     explicit rejected-pattern evidence; never auto-promoted
```

Two axes.
Form packages answer "what kind of page is this"; sector packages answer "what does trust look like in this industry", and each sector documents its own mode as ban material, with real hex values pulled from the sites that ship it.

Refs are distilled from inspected site evidence and carry their source status and capture date when known. Full-CSS and archived Wayback evidence stay distinguishable. A ref records palettes with roles, type and motion evidence when verified, one signature element, and what goes wrong if the site is imitated naively.

## Quick start

In Codex:

```text
$booster Build a website for Seoul Garden BBQ, a family-owned Korean barbecue restaurant in Queens.
```

In Claude, use `/booster` instead. If no project is open, Booster asks whether to use an existing business folder or create a new one; the new folder name may be left blank. If no photos exist, it offers image generation only when the active agent provides it, otherwise it offers an imagery-light build, exact image spaces plus a saved generation brief, or a pause for uploads.

After the first build, invoke `$booster-audit` in Codex or `/booster-audit` in Claude for the rendered review.

## How a build runs

The default user experience is a one- or two-shot website build. Routing, search, and validation run behind the result instead of becoming a questionnaire.

1. **Establish the workspace.** If a project is open, Booster uses it. Otherwise it asks whether the user has an existing business folder or wants a new website folder. A new folder name is optional: Booster derives it from the business name when possible and uses a clearly named draft when neither is known. It scans documents, menus, logos, copy, code, and images before asking for information already on disk.
2. **Resolve imagery.** Existing business photography wins. When no usable images exist and the active agent actually provides the `imagegen` capability, Booster offers an art-directed generated image set, art-directed placeholders, or an imagery-light direction. When generation is unavailable, Booster says so plainly and offers an intentionally complete imagery-light build, exact image spaces plus a saved generation brief for later handoff, or a pause for uploads. The missing tool never blocks the first shot or pressures the user to switch agents. Generated assets are project-local concept imagery and never masquerade as documentary evidence of real premises, people, products, dishes, credentials, or events.
3. **Route.** The `booster` skill (`$booster` in Codex, `/booster` in Claude) picks one form pack, one sector pack if the brief belongs to an industry, and four candidate refs spanning different poles. Search ranks the shortlist; a diversity pass prevents ranking from becoming a preset. For an implementation request, the agent chooses and names two, opens no more than 2-3 ref files total, and continues without making the user operate the routing machinery.
4. **Derive.** Ground the design in the subject, record three materially different directions with compact ASCII wireframes, and discard family collisions and counterfactual-generic plans. Ask the user to choose only when the directions imply materially different business outcomes.
5. **Gate.** Four checks before building: could this plan ship for a different subject; does it clone a ref; can a visitor tell what kind of organization this is; would the organization actually ship it.
6. **Judge.** The `booster-audit` skill (`$booster-audit` in Codex, `/booster-audit` in Claude) reviews mobile, laptop, and wide screenshots plus applicable states and interactions. It separates hard-floor failures from aesthetic mode findings and reports severity, confidence, locations, and bounded corrections. Green builds are not evidence; the rendered result is.

## The ban list, briefly

New rules enter only when a failure is observed and logged, never speculatively.
A motif becomes a candidate after repeat sightings. The structured registry distinguishes complete evidence from entries that predate the ledger:

> **B011** Em dashes in copy. *Appeared throughout the recorded A/B runs before the ban.*
>
> **B012** The accent-colored italic serif word inside a roman headline. *7 sightings; survived soft discouragement in every run.*
>
> **B015** Deep forest green as the anchor palette. *7 consecutive builds across three unrelated subjects, with and without the spec.*
>
> **B018** Aphorism headlines ("Forty tanks. Plenty to ask."). *When a plain label does the job, the plain label wins: "Contact" beats "Tell us what the tank needs to do."*

The full list and stable IDs live in [DESIGN.md](DESIGN.md). Evidence status lives in `evidence/bans.json`; missing historical details stay marked `legacy-unstructured` instead of being reconstructed as fact.

## Rules of growth

- References enter by propose-and-veto: the library is a record of taste, not a scrape.
- Rejections enter `evidence/observations.json` with subject, model, artifact, date, screenshot when available, and the user's exact wording.
- Tooling groups repeated observations into candidates but never promotes them. A structured ban binds one repeated pattern key to at least two independent observation IDs plus explicit library-owner confirmation and date; it enters DESIGN.md only after that review.
- Positive prescriptions are avoided on principle. Bans carve out negative space and leave the rest free; prescriptions become the next template. When the system itself started prescribing (a palette hint in a sector pack, a shot count in a brief), every build converged, and the prescriptions were removed.

## Search and evidence tools

```sh
python3 tools/booster.py validate --root .
python3 tools/booster.py index --root . --write evidence/reference-index.json
python3 tools/booster.py search "family-owned Korean barbecue restaurant" --form gallery --limit 4
python3 tools/booster.py observe --pattern "generic centered restaurant hero" --subject "Korean barbecue website" --model "model-name" --artifact "path-or-url" --note "user's exact rejection"
python3 tools/booster.py candidates --min-count 2
```

Search retrieves; it does not decide. Read the returned packs, open only the 2-3 most relevant ref files, keep candidates from different visual families, and let the builder choose two.

## Install

Requirements: macOS or Linux with Zsh, Git, rsync, and Python 3.11 or newer.

```sh
git clone https://github.com/dklKevin/booster && cd booster
./install.sh
```

The default installs the canonical library and skills for Claude. Other agent skill homes can share the same canonical library:

```sh
./install.sh --agent codex
./install.sh --agent claude --agent codex
./install.sh --agent universal
```

Codex and `universal` target the current user skill directory, `~/.agents/skills`; `all` installs both Claude and universal skill locations. The installer validates the repository first, recognizes only Booster-owned or legacy Booster files, replaces stale files inside Booster-owned directories, and leaves agent instruction files untouched.
Reinstalling merges repository observations into the live evidence ledger and preserves live-only observations instead of resetting them.
Wire it in with one line in the relevant `CLAUDE.md` or `AGENTS.md` telling the agent to read `~/.claude/DESIGN.md` before designing any UI or page.

## Sync (maintainer direction)

`./sync.sh --dry-run` validates a staged export and shows its managed-file changes without touching the repository.
`./sync.sh` also requires a clean worktree, a cooperative export lock, a complete ownership-marked live install, and a passing staged validation before it changes tracked files. It rechecks the Git snapshot and applies one preimage-checked patch, so an empty, partial, or concurrently changed live package tree cannot silently erase the repository.
Managed file, package, reference, mode, ban, or observation removals are refused by default. So is a managed document shrinking below 60% of its tracked size. A maintainer making an intentional removal or major reduction must review the dry-run diff and pass `--allow-removals` explicitly.

## Verify

```sh
python3 -m unittest discover -s tests -p 'test_*.py'
zsh tests/test_install.zsh
```

## License

[MIT](LICENSE) © 2026 Dongkyu Lee

<p align="center">
  <sub>Grown one observed failure at a time.</sub>
</p>
