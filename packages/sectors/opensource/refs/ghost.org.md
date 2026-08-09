# https://ghost.org (sector: opensource, sweep: excellence, fetched 2026-08-06)
status: full-css

## Token block (~10 lines)
- Palette — core ink `#15171a`, black `#000000`, white `#ffffff`; ink is the declared base and the dashboard frame color.
- Palette — section surfaces use slate `#0f172a` (dark), `#e2e8f0` (light), with secondary text `#cbd5e1`, `#64748b`, and `#334155`.
- Palette — restrained accents are lime `#d1ff19`, yellow `#fec137`, plus declared blue `#3eb0ef`, green `#5dcf1f`, and pink `#ff247d`.
- Type pairing — marketing headings use `"InterDisplay", sans-serif`; UI/body uses `"InterVariable", sans-serif` (fallback declaration `"Inter", sans-serif`); Resources pairs `"Inter var", sans-serif` with `"STIX Two Text", serif`.
- Type scale — `12/14/15/18/20/24/36/48/96px`; homepage hero is fluid `6.5vmin` and becomes `96px` at the large breakpoint, at line-height `1` and letter-spacing `-0.025em`.
- Type roles — `12px`, uppercase, `0.1em` tracking for section eyebrows; `20–24px` supporting copy; `36–48px` feature headings; Resources article copy is `20px/1.6`.
- Spacing rhythm — rem utilities follow a 4px step (`0.4rem`): recurring gaps/margins include `12, 16, 24, 32, 40, 48, 80px`; page gutters are `16px`, rising to `24px`.
- Section rhythm — major vertical padding is fluid, chiefly `8vmin`, with `10vmin`, `12vmin`, and `14vmin` variants; feature grids use `4vmin`, `6vmin`, or `8vmin` gaps.
- Layout intent — center content in a 12-column grid capped at `140rem` (with `128rem` media frames), alternate full-width white/slate sections, and use `1.6rem` large card radii; Resources narrows prose to a `720px` named grid track.
- Signature element — a minimal, centered two-line `96px` hero flows directly into a nearly full-width, rounded `140rem` product-dashboard video, then repeated oversized product UI demonstrations alternate across dark and light bands.

## Lessons (3-5 bullets)
- Let the product interface carry the visual proof: Ghost gives real dashboard/editor footage the widest container and keeps the surrounding claim short.
- Pair a stable 4px component rhythm with viewport-relative section spacing; controls remain orderly while long marketing pages retain cinematic pacing.
- Use one grid across navigation, hero media, feature copy, pricing, and CTAs; vary background bands and column spans instead of inventing a new composition for every section.
- Give documentation its own reading geometry and serif body face while retaining the shared base palette and sans-serif UI, so the content mode changes without losing brand continuity.

## Avoid (1-2 bullets)
- Do not copy the `96px`/`6.5vmin` hero or `8–14vmin` section spacing without the same short copy and strong product imagery; ordinary content would become sparse and over-scaled.
- Do not treat every declared accent as equally prominent: the homepage is mostly black, white, and slate, with lime/yellow used as small signals rather than broad rainbow branding.
