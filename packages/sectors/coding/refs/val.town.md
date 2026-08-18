# https://val.town (sector: coding, sweep: excellence, fetched 2026-08-06)
status: full-css

## Token block (~10 lines)
- Palette - core: #FFFFFF page/background, #000000 primary text, #F0F9FF soft sky-tinted surface.
- Palette - action: #00BCFF primary CTA, #00A6F4 CTA hover, #052F4A CTA text/dark sky.
- Palette - illustration: #F8F4F2 warm town-scene field, #FF7250 terminal character/caret accent, #4B3D35 terminal surface, #695E57 window controls.
- Display/marketing face: "Sprig Sans", -apple-system, sans-serif; supplied at 400 and 700.
- Product/UI face: IBM Plex Sans, -apple-system, sans-serif; supplied at 400, 600, and 700.
- Code face: "iA Writer Mono", "Menlo", "Consolas", "ui-monospace", monospace.
- Type scale: 12, 14, 16, 18, 20, 24, 30, 36, 48, 60px; homepage hero steps 24 → 32 → 36 → 48px with 1.2 line-height.
- Spacing rhythm: 4px base; recurring 8/12/16/20/24/32/48/64px gaps; marketing gutters are 24px, then 48px at md.
- Layout intent: 80rem homepage/pricing shell and 72rem feature sections; hero uses a 7fr/4fr grid, while prose is capped at 65ch.
- Signature element: a layered 3072×1792 town illustration scaled to 0.7/0.8, with 7–8.4s swaying trees framing a dark, code-like terminal card.

## Lessons (3-5 bullets)
- Pair a friendly custom display face with a conventional product UI face and a credible code font; the shift makes marketing feel warm without making the tool itself feel unserious.
- Let the product proof occupy the larger 7/11 share of the hero, then keep the promise and CTA in the narrower 4/11 column; this makes the interface demonstration the argument rather than decoration.
- Build responsiveness from explicit type and gutter steps: 24/32/36/48px headlines and 24/48px outer padding preserve hierarchy without relying on fluid values everywhere.
- Give a coding brand one memorable world-building device, then animate only small environmental details; Val Town's oversized scene stays recognizable while the 7–8.4s tree motion remains quiet.
- Reuse a restrained sky action family across buttons, links, focus states, and pale surfaces, while reserving coral and warm browns for the signature terminal illustration.

## Avoid (1-2 bullets)
- Do not imitate the large illustrated world without equally concrete product evidence; the terminal card is what keeps the scene connected to the coding task.
- Do not transplant the fixed 3072×1792 scene and `calc(1267px * var(--bg-scale))` offset unchanged; those values are tightly coupled to this artwork and its 0.7/0.8 responsive scale.
