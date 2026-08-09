# https://www.delta.com (sector: fortune500, sweep: excellence, fetched 2026-08-06)
status: full-css

## Token block (~10 lines)
- Palette / navigation: #012 (navy surface; source shorthand for #001122) with #fff inverse text and active-tab surface.
- Palette / content: #f2f3f5 page surface, #fff raised surface, #001e3c headings, #3e414f body copy, #6c718a subtle text.
- Palette / action: #e01933 primary CTA, #ad1834 hover, #661024 pressed; #06c links and #64affa focus stroke.
- Type pairing: Whitney, sans-serif for the interface; "Whitney Condensed", sans-serif for condensed display treatment.
- Type scale: .75, .875, 1, 1.125, 1.25, 1.5, 1.75, 2.25, 2.5, 3, 4, and 6rem (12, 14, 16, 18, 20, 24, 28, 36, 40, 48, 64, 96px).
- Type weights: 300 light, 400 book, 500 medium, 600 semibold, 700 bold, 900 black; heading tracking -.015em.
- Spacing rhythm: 4px base with 4, 8, 12, 16, 20, 24, 32, 40, 48, 72, and 96px tokens.
- Shape/elevation: radii 2, 4, 6, 8, 12, and 16px plus pill 9999px; cards use the extracted multi-layer shadow-03.
- Layout intent: full-bleed navy/imagery bands around centered responsive content widths of 704px tablet, 928px laptop, and 1152px/72rem ultrawide; cards switch from one column to wider grids.
- Signature element: the navy booking tab strip (Flights, Hotels, Cars, Vacations, Cruises) turns the active tab white and leads directly into the From/To travel-search workflow above the full-bleed marketing hero.

## Lessons (3-5 bullets)
- Put the sector's primary job at navigation level: Delta's booking tabs and airport fields precede promotional content, so task completion remains the visual anchor.
- Reserve saturated red for consequential CTAs and keep navigation, headings, and large framing surfaces in a deep navy family; this creates urgency without making the entire interface loud.
- Use one unusually broad type family across utility labels, body copy, headings, and condensed display text; hierarchy comes from weight, scale, and width rather than unrelated fonts.
- Let imagery bleed edge to edge while keeping copy and card edges on the same 704/928/1152px responsive rails; the page feels cinematic without losing operational clarity.
- Encode dense travel controls with a 4px spacing system and explicit semantic states, then allow marketing sections to jump to 48-96px spacing for a deliberate task/content tempo change.

## Avoid (1-2 bullets)
- Do not copy the dark booking band without the white active-tab inversion and strong focus states; the extracted design depends on state contrast to make a dense control set scannable.
- Do not blend the legacy interior-page palette and one-off component CSS (#0b1f66 and numerous fixed values) into the newer MACH homepage tokens; that would reproduce Delta's transitional inconsistency rather than its strongest system.
