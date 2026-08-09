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
  <img alt="sector packs" src="https://img.shields.io/badge/sector_packs-15-17131f">
  <img alt="distilled refs" src="https://img.shields.io/badge/distilled_refs-140%2B-495e69">
  <img alt="bans" src="https://img.shields.io/badge/bans_from_observed_failures-18-8a2f40">
</p>

---

## Why this exists

Ask a model for a webpage and you get the same page everyone else gets: the gradient hero, the rounded card grid, the cream-and-terracotta palette, the headline with one italic accent word.
That output is not a lack of effort.
It is the statistical center of the training distribution, and more reasoning effort only polishes it.

Booster moves probability mass off the mode with three levers that testing bore out:

| Lever | Instead of |
|---|---|
| Bans, grown only from observed failures | Aspirational adjectives ("make it unique") |
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
```

Two axes.
Form packages answer "what kind of page is this"; sector packages answer "what does trust look like in this industry", and each sector documents its own mode as ban material, with real hex values pulled from the sites that ship it.

Every ref is distilled from a live site's actual CSS: real palettes with roles, real type scales, real motion values, one signature element, and a line on what goes wrong if the site is imitated naively.

## How a build runs

1. **Route.** `/booster` picks one form pack, one sector pack if the brief belongs to an industry, and offers four refs spanning different poles. The builder chooses two and must name its choices.
2. **Derive.** Ground the design in the subject, sketch three materially different directions, and discard the first instinct: the first direction that comes to mind is the mode.
3. **Gate.** Four checks before building: could this plan ship for a different subject; does it clone a ref; can a visitor tell what kind of organization this is; would the organization actually ship it.
4. **Judge.** Screenshot the result at multiple widths and evaluate the pixels against the ban list and the plan. Green builds are not evidence; the screenshot is.

## The ban list, briefly

Rules enter only when a failure is observed and logged, never speculatively.
A motif gets banned after repeat sightings, with the log kept in the entry:

> Em dashes in copy. *Appeared in 6 of 6 A/B runs before the ban; 0 after.*
>
> The accent-colored italic serif word inside a roman headline. *7 sightings; survived soft discouragement in every run, died on the day of the ban.*
>
> Deep forest green as the anchor palette. *7 consecutive builds across three unrelated subjects, with and without the spec.*
>
> Aphorism headlines ("Forty tanks. Plenty to ask."). *When a plain label does the job, the plain label wins: "Contact" beats "Tell us what the tank needs to do."*

The full list, with all 18 entries and their logs, lives in [DESIGN.md](DESIGN.md).

## Rules of growth

- References enter by propose-and-veto: the library is a record of taste, not a scrape.
- Bans enter from the observed-failure loop above.
- Positive prescriptions are avoided on principle. Bans carve out negative space and leave the rest free; prescriptions become the next template. When the system itself started prescribing (a palette hint in a sector pack, a shot count in a brief), every build converged, and the prescriptions were removed.

## Install

```sh
git clone https://github.com/dklKevin/booster && cd booster
./install.sh
```

This copies the system into `~/.claude/`, where agents read it, and refuses to touch a `DESIGN.md` it does not recognize.
Then wire it in: one line in your `~/.claude/CLAUDE.md` telling agents to read `~/.claude/DESIGN.md` before designing any UI or page.

## Sync (maintainer direction)

`./sync.sh` pulls the live `~/.claude/` state back into the repo before committing.
It refuses to run against a machine without a full Booster install, so a fresh clone cannot overwrite itself.

<p align="center">
  <sub>Grown one observed failure at a time.</sub>
</p>
