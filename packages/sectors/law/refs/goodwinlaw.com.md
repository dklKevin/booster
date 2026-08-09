# https://www.goodwinlaw.com (sector: law, sweep: excellence, fetched 2026-08-06)
status: full-css

## Token block (~10 lines)
- Palette — primary text/ink #2d3539; page canvas #ececec; content surfaces #fff.
- Palette — action accent #f7941d; structural rules/borders #82ceea; secondary border/icon gray #c4c4c4; subdued rule #868d91.
- Palette — pale supporting surfaces #eff0ed and #efefef; hero wash is a 180deg gradient from #fdfaf6 at 26.56% to #e6f5fb at 80.21%.
- Type pairing — Proxima Nova (`proxima-nova, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif`) for body/UI; Chaparral Pro and Chaparral Pro Display with `serif` fallbacks for editorial headings, names, and quotes.
- Type scale — H1 40px rising to 45px at 48em, serif H1 36px rising to 45px; H2 20px rising to 24px, 600 weight, uppercase, .0625em tracking.
- Type scale — H3/H4 20px rising to 24px; H5/H6 16px rising to 20px; eyebrow 16px, 700 weight, uppercase, .125em tracking; body line-height 1.45.
- Spacing rhythm — 16px small, 24px top, 32px standard section spacing, and 64px desktop section spacing; component grids use 16px, 20px, 24px, or 32px gaps.
- Container — max-width 85.05em (1360.8px) with 28px side padding, rising to 30.4px at 48em; long-form/read-more copy caps at 65em (1040px).
- Layout intent — fluid, centered shell with mobile-first stacked content; desktop shifts to two-column editorial/asides and repeat(2–4, 1fr) card grids, with key breakpoints at 48em, 53.75em, and 65em.
- Signature element — “leaf” panels/cards use only 15px top-left and bottom-right radii, a thin #82ceea outline, and an orange #f7941d underlay that reveals through a translated hover state; headings echo it with a short 5px orange rule (8px in a featured module).

## Lessons (3-5 bullets)
- Make the information architecture do visible work: the homepage pairs a large “How can we help you?” search-led brand panel with a narrower live-insights rail, letting expertise discovery and proof of currency share the first content row.
- Use a restrained institutional palette, then reserve one warm color for action and motion: #f7941d marks links, active states, arrows, heading rules, and hover underlays while #82ceea quietly structures cards and dividers.
- Pair a neutral sans serif for dense navigation and scanning with a humanist serif for editorial hierarchy; the 40–45px headline ceiling keeps authority without turning legal content into a luxury-brand billboard.
- Build responsiveness from reusable proportions: a 1360.8px shell, 40%/60% editorial splits, 2–4-column equal grids, and 32px-to-64px section spacing support both search-heavy indexes and long publications.
- Let interaction reinforce the brand shape: the repeated diagonal-corner card silhouette, orange offset reveal, and 0.3s cubic-bezier(.61,1,.88,1) transitions create recognition without decorative clutter.

## Avoid (1-2 bullets)
- Do not copy the clipped-corner card, orange underlay, short heading rule, and hexagonal graphics all at once without the site’s generous whitespace; stacking every motif would turn a controlled signature into visual noise.
- Do not reuse the light #82ceea or #c4c4c4 as text colors on white; the fetched CSS uses them chiefly for borders, rules, and icons while primary copy remains #2d3539.
