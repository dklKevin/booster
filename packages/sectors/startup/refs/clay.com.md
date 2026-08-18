# https://www.clay.com (sector: startup, sweep: excellence, fetched 2026-08-06)
status: full-css

## Token block (~10 lines)
- Palette / canvas and text: white `#ffffff`; warm oat surfaces `#f9f8f6` and `#f3f2ed`; primary ink `#000000`; muted ink `#7b7974`; soft borders `#eee9df`.
- Palette / hero: deep green `#035d44`, with responsive overlay/gradient green `#006147`; hero copy uses warm white `#fefdfb`.
- Palette / accents: blueberry `#395afa`, slushie `#3bd3fd`, lime `#cbd810`, lemon `#fdbe11`, ube `#a17bf9`, pomegranate `#fb4450`, tangerine `#ff7614`, dragonfruit `#ff70d1`.
- Type pairing: primary `Roobertvf, Arial, sans-serif` (responsive fallback token uses `Roobert, Arial, sans-serif`); secondary labels/eyebrows `"Roobert mono", Arial, sans-serif`.
- Heading scale (desktop / tablet / mobile): H1 `5.5rem / 4rem / 3rem`, weight `575`, line-height `1`, tracking `-0.04em`; H2 `4.5rem / 3.5rem / 2.5rem`, weight `500`, line-height `1`, tracking `-0.03em`; H3 `3rem / 2.25rem / 2rem`.
- Body scale: large `1.5rem` (`1.25rem` mobile), medium `1.25rem` (`1.125rem` mobile), regular `1rem`, small `0.875rem`; line-heights `1.3 / 1.25 / 1.4 / 1.3`.
- Spacing rhythm: explicit `0.25, 0.5, 0.75, 0.875, 1, 1.25, 1.5, 1.75, 2, 2.5, 3, 4, 4.5, 5, 6, 7, 8, 11rem` scale; core gaps are `1 / 1.25 / 1.5 / 2rem`.
- Section/card rhythm: desktop vertical sections `3 / 4 / 6 / 9rem` (small/regular/medium/large); card padding `1 / 1.5 / 2 / 3rem`; both contract at `991px` and `479px`.
- Layout intent: centered percentage-width shells - standard `.container` is `90%` with `75rem` max, while current navigation/hero shells are `95%` with `125rem` max; global desktop gutters are `2.5rem`, reduced to `1.25rem` below `991px`.
- Signature element: a `120vh` (`52rem` min, `67rem` max) deep-green hero whose source contains a full-bleed video/poster of a colorful playful contraption with tubes, balls, magnets, and a funnel, staged behind oversized warm-white revenue copy.

## Lessons (3-5 bullets)
- Let one high-production metaphor carry the brand: Clay reserves the cinematic contraption for the opening hero, then returns to restrained warm-neutral product and proof sections.
- Use a variable grotesk for both expressive display and dense UI; the `575/530` heading settings, tight negative tracking, and mono eyebrow face create hierarchy without adding many font families.
- Encode density by breakpoint at the token level: typography, section padding, card padding, radius, and horizontal margins all contract together at `991px` and `479px`.
- Keep separate content templates on one visual chassis: the pricing grid and editorial customer story differ structurally, but reuse the same oat palette, type system, containers, utility spacing, and closing CTA.
- Pair a practical `75rem` reading/product container with a much wider `125rem` stage for navigation and cinematic media, so operational content stays legible while brand moments feel expansive.

## Avoid (1-2 bullets)
- Do not copy the oversized animated hero without equivalent compression, art direction, and responsive fallbacks; its source already needs explicit height caps, a poster image, gradient masking, and mobile overrides.
- Do not deploy the entire bright accent spectrum uniformly: the neutral oat field and black/green anchors are what keep blueberry, lime, lemon, ube, slushie, pomegranate, tangerine, and dragonfruit from becoming visual noise.
