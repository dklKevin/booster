# https://www.recursion.com (sector: pharma, sweep: excellence, fetched 2026-08-06)
status: full-css

## Token block (~10 lines)
- Core palette: white #FFFFFF (canvas, hero/nav text), near-black #333333 (default text), charcoal #4E4E4E (paragraph text), light grey #F7F7F7 (section ground).
- Product-role palette: pipeline #8000FF, platform #F34A17, approach #2D65B0, impact #E82267; supporting aquamarine #33B894.
- Gradient accent: purple #A64CC4 to pink #E01C88 for section headings; the footer statement uses a seven-stop spectrum from #2131C5 through #EA005B and #FAA900 to #00DA7E.
- Type pairing: Messina Sans, sans-serif for display and editorial copy; Messina Sans Mono, sans-serif for links and controls (served weights 300, 400, 600, 700, 900).
- Display scale: hero 96px/101px at weight 400 with -2px tracking; tablet 80px, small tablet 71px, mobile 55px.
- Content scale: secondary heading 53px/59px at 600; section heading 32px/36px at 600; paragraph module 17px/23.8px; mono CTA 16px.
- Spacing rhythm: 20px base gutters and grid gaps, then 40px, 60px, 68px, and 100px for section-level breathing room.
- Layout intent: centered 1,160px max-width container with 20px side padding, nested two-column Webflow grids, and full-viewport media sections.
- Viewport pattern: homepage video hero is 80vh with 750px minimum and 1,300px maximum; supporting feature sections commonly use 60–100vh.
- Signature element: a full-bleed, autoplaying loop of automated laboratory machinery behind a white 96px headline, pairing literal scientific proof with cinematic scale.

## Lessons (3-5 bullets)
- Assign saturated colors to stable content roles (pipeline, platform, approach, impact), then reuse those roles in navigation, diagrams, and calls to action rather than applying color decoratively.
- Let one operational image carry the hero: the automated-lab loop makes the technology tangible while the short white headline supplies the ambition.
- Use a restrained editorial hierarchy after the dramatic hero: 32px gradient section labels, 17px body copy, and a fixed 1,160px reading frame keep dense scientific material scannable.
- Pair a humanist sans for claims and explanations with a mono face for actions and technical links; this signals computational rigor without turning body copy into an interface aesthetic.

## Avoid (1-2 bullets)
- Do not copy the 80vh/750px-minimum video hero without aggressive media optimization and a static fallback; its scale can delay the core message on smaller or slower devices.
- Do not reproduce every spectrum and role color on the same screen; without Recursion's semantic assignments, the purple-pink headings, rainbow footer, and product colors would compete.
