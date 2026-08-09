# Teenage Engineering (teenage.engineering, extracted 2026-08-06)

- Palette: bg #fff, surface #f5f5f5, ink #0f0e12, hairlines #b2b2b2, muted #767676; saturated color (#0071bb action, #006837 success, #c0262c error, #f05a24, #fab413) bound to state roles only.
- Type: two custom faces (te-40 display, te-20 body), weights 100 and 300 ONLY; no bold token exists, so hierarchy can only come from size.
- Scale named by baseline rows: 9/10, 13/15, 18/20, 23/30, 27/30, 36/40 (size/line-height at 980 reference); every line-height a multiple of the 10px baseline, so mixed content self-aligns with no per-page correction.
- Spacing: five steps (5/10/15/22.5/45 at 980) tied to the grid's gutter and margin; mobile is the identical system at exactly 2x, not a second design.
- Layout: 12 columns / 980 reference / proportional vw canvas, no max-width; radius 0 on desktop; structure drawn only with 1px hairlines on grid cells.
- Per-page theming: one ~7-variable inline :root block per route (product pages adopt a gray pulled from the product itself); nothing else is page-specific.
- Signature: header nav is one inline SVG with ~11 theme-addressable color slots.

Avoid: their contrast is marginal by design (#767676 at ~4.0:1, hairlines 2.1:1) and their gray ramp is non-monotonic; our floors override. Unclamped vw type breaks at large viewports.
