# https://www.twistbioscience.com (sector: biosecurity, sweep: excellence, fetched 2026-08-06)
status: full-css

## Token block (~10 lines)
- Palette / canvas: white `#ffffff`; cool section surface `#eef2f6`; light gray section surface `#f5f5f5`.
- Palette / copy: heading and dark-button ink `#232e35`; body copy `#354652`; secondary labels, metadata, and tabs `#627684`.
- Palette / action: vivid green `#2ad39b` for CTA fills and the navigation underline; darker green link/hover colors `#04a973` / `#04ad75`.
- Type pairing: headings use `"proxima-nova", "Helvetica Neue", Helvetica, Arial, sans-serif`; the page, labels, and controls use `din-2014, "Helvetica Neue", Helvetica, Arial, sans-serif`.
- Heading scale: h1 `48px/56px`, h2 `36px/48px`, h3 `30px/40px`, h4 `24px/32px`, all weight 800; h5 `18px/23px` and h6 `16px/20px`, weight 700.
- Body/detail scale: core copy `16px/28px` with `.02em` tracking; hero copy `18px/32px`; compact uppercase labels and buttons commonly `12–13px` with `.14em` tracking.
- Spacing rhythm: recurring `8px`, `16px`, `24px`, `32px`, `40px`, and `48px`; card grids use `24px` gaps, while major sections commonly use `60px` vertical padding.
- Layout: AEM 12-column percentage grid inside a repeated `1170px` max-width container with `15px` side padding; primary breakpoints include `1169px`, `1024px`, `768/767px`, and `576px`.
- Controls: dark CTAs are `#232e35`, typically 12–16px uppercase text with `.14em` tracking, `14–18px` vertical padding, and `2–4px` corner radii.
- Signature element: a fixed, two-column vertical carousel pairs 554px-tall images (asymmetric `8px 8px 8px 80px` radius) with 48px uppercase titles tracked at `9px`; image and title translate together in 400ms every 2500ms.

## Lessons (3-5 bullets)
- Use two typographic voices to separate scientific hierarchy from operating detail: heavy Proxima Nova headlines carry the proposition, while DIN handles dense copy, metadata, tabs, and controls.
- Keep technical pages calm with a narrow semantic palette: dark blue-gray copy and cool neutral fields make the single fluorescent green action signal unmistakable.
- Standardize complex product and resource layouts on one `1170px` container and a 12-column grid, then collapse purposefully at the explicit `768/767px` boundary rather than inventing component-specific widths.
- Give a broad platform one memorable narrative device: the synchronized vertical carousel cycles application areas while its supporting claim and CTA remain stable.
- Encode hierarchy through repeatable micro-patterns—13px uppercase tabs, `.14em` tracking, 2px active rules, and 24px gaps—so dense scientific navigation remains scannable.

## Avoid (1-2 bullets)
- Do not reuse the carousel's fixed positioning, 554px media height, or extreme title tracking without the mobile fallback; the source hides the image column below `768px` and reduces title size/tracking below `1200px`.
- Do not spread `#2ad39b` across decorative surfaces: its effectiveness here depends on being concentrated in CTAs, active/navigation cues, and small category accents.
