# https://www.apple.com (sector: bigtech, sweep: excellence, fetched 2026-08-06)
status: full-css

## Token block (~10 lines)
- Palette, light: canvas #ffffff; alternate/product-tile surface #f5f5f7; primary text #1d1d1f; secondary text #6e6e73 and #86868b.
- Palette, dark: canvas #000000; primary text #f5f5f7; dark alternate surface #1d1d1f.
- Palette, action: text link #0066cc; filled CTA and focus #0071e3; CTA hover #0076df; active #006edb.
- Type pairing: `SF Pro Display, SF Pro Icons, Helvetica Neue, Helvetica, Arial, sans-serif` for display; `SF Pro Text, SF Pro Icons, Helvetica Neue, Helvetica, Arial, sans-serif` for body/UI.
- Display scale: 80/84px super headline (600, -0.015em), 56px section headline, 40/44px home promo headline, 28px card headline, 24px eyebrow, 21px subhead; super headline steps to 64px at 1068px and 48px at 734px.
- Text scale: 17/25px body (400, -0.022em), 19px tout, 14/18px home callout/button, 12/16px caption.
- Spacing rhythm: homepage tiles use 12px gaps; tile padding is 48px 0 56px desktop, 54px 0 61px at 1068px, and 39px 0 43px at 734px; CTA groups start 17px below copy.
- Section rhythm: iPhone content sections use 112px vertical padding, 96px at 1068px, and 56px at 734px; section headers end with 48px, reduced to 32px on phones.
- Layout intent: center an 87.5%-wide, max-1260px 12-column content frame (20px grid gap), allow hero media to 1680px, and cap the homepage canvas at 2560px; major breakpoints are 1068px and 734px.
- Signature element: centered, minimal copy floats above a full-tile product image inside edge-to-edge 580px hero/promo stages (500px on phones), alternating #f5f5f7 and #000000 themes with 12px seams.

## Lessons (3-5 bullets)
- Separate editorial scale from reading scale: SF Pro Display carries 21-80px product storytelling while SF Pro Text stays at 12-17px for dense UI, captions, and body copy.
- Make imagery the layout, not an attachment: each product tile gives its image wrapper the full hero height and positions concise copy above it, preserving a single visual idea per stage.
- Use a narrow neutral system with role-specific grays, then reserve #0066cc/#0071e3 for links, focus, and conversion actions so interactive hierarchy remains unmistakable.
- Keep responsive behavior systematic: the same 1068px/734px thresholds coordinate headline steps, section padding, tile height, and grid collapse rather than tuning each component independently.

## Avoid (1-2 bullets)
- Do not copy the 80px headlines and 580px stages without similarly sparse copy and dominant imagery; ordinary content would become slow and excessively scroll-heavy.
- Do not treat #f5f5f7, #1d1d1f, and large whitespace as the whole style; without the precisely art-directed full-tile media and strict type hierarchy, the result becomes generic.
