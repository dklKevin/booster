# https://www.chainguard.dev (sector: cybersecurity, sweep: excellence, fetched 2026-08-06)
status: full-css

## Token block (~10 lines)
- Palette / base: white `#FFFFFF` canvas, neutral ink `#0D161C`, neutral borders `#EDEDED`.
- Palette / primary action: blurple `#6226FB`; deep-blurple hover/text `#3200AF`; light-blurple surface `#F1ECFE`.
- Palette / supporting accents: aqua `#2BBAFD`, fuchsia `#FD2BF2`, lime `#44FD2B`, solar `#FD3964`.
- Type pairing: Gellix Regular/Bold/SemiBold/Medium for interface and display; Roobert Semi Mono (regular/semibold/bold) and Source Code Pro 400 for technical/terminal language; each custom face falls back to its supplied Arial metric-adjusted face.
- Display scale: `32/40px` (mobile), `40/48px` (tablet), `64/64px` (desktop hero); section display steps include `18/24`, `24/32`, `30/38`, `32/48`, `40/48`, and `48/48px`.
- Body/control scale: primary body is `18/24px`; extracted supporting sizes include `14px`, `16px`, and `20px`; display tracking is `-3%`, control tracking `-1%`, body tracking `0`.
- Spacing rhythm: a 4/8px-derived scale visibly concentrates at `16`, `24`, `32`, `40`, `48`, `64`, `72`, `80`, and `96px`; the section-end token is `80px`.
- Layout widths: centered `.container` is `1512px` with `32px` side padding; site max-width tokens are `1402px` and `1444px`; hero copy caps at `729px` and its body copy at `662px`.
- Layout intent: wide, centered editorial bands switch between bordered split columns, card grids, and narrow reading columns (the article container is `945px`) while retaining 16px mobile and 24-32px desktop gutters.
- Signature element: a blueprint-like hero frame made from exact `50.4px` outlined square cells (`#EDEDED` strokes) with sparse `#F8F6FE` and `#F1ECFE` fills, pairing software-system precision with a light, approachable surface.

## Lessons (3-5 bullets)
- Make security feel engineered rather than ominous: near-black copy and hairline grid borders carry authority, while restrained violet tiles and a single saturated action color keep the page optimistic.
- Encode technical credibility in structure as well as copy: the 50.4px modular hero grid, mono accents, bordered regions, and metric/stat blocks all resemble a legible system without turning the whole interface into a terminal.
- Keep one responsive headline recipe across homepage and product pages (`32/40` to `64/64px`), then let editorial pages top out at `48/48px`; this preserves brand recognition while respecting reading context.
- Use generous fixed section intervals (`64-96px`, with an `80px` section token) and controlled copy widths (`662-729px`) to make dense cybersecurity claims scan as a sequence of proofs.
- Separate text-safe and decorative accent roles: the source distinguishes deep/text variants from brighter non-text aqua, fuchsia, lime, and solar colors, protecting hierarchy while allowing vivid diagrams and states.

## Avoid (1-2 bullets)
- Do not copy every bright accent at equal strength; the live system reserves most saturated hues for non-text roles and relies mainly on `#6226FB`, ink, white, and pale violet in primary flows.
- Do not reproduce the grid as generic cyber decoration everywhere; its effect depends on sparse filled cells, exact hairlines, and large quiet areas around the content.
