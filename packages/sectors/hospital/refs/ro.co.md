# https://ro.co (sector: hospital, sweep: excellence, fetched 2026-08-06)
status: full-css

## Token block (~10 lines)
- Core palette: light surface #ffffff, dark surface/primary text #1a1a1a, secondary text #444444, tertiary text #666666, subtle border #dddddd.
- Clinical/action accents: Kelly green #119555 (light-surface accent), #0d7744 (small accent text), bright green #20c86d (dark-surface accent), alert dark red #be4d40.
- Supporting brand surfaces: teal #add8d5, light teal #e5f2f2, orange #ffa674, bright red #ff6554, rich blue #356ab1, bright yellow #f8ffa1, warm neutral #eee9e4, cool grey #f3f5f6.
- Type pairing: custom "Ro Sans", with `Ro Sans, sans-serif` used globally; weights 200, 400, 600, and 700 are supplied (regular and italic files).
- Display scale: 72/79 or 72/86px desktop, 64/70 or 64/77px tablet portrait, 56/62 or 56/67px mobile (600/400 weights).
- Heading scale: desktop H1 36/36 or 36/43px, H2 32/38px, H3 29/29 or 29/35px, H4 26/26 or 26/31px, H5 23/23 or 23/28px; mobile H1 29px through H5 18px.
- Body/label scale: body 18/25, 16/22, 14/20, and 13/18px desktop; mobile steps to 16/22, 14/20, 13/18, and 12/17px; labels are 14/20px desktop and 12/17px mobile.
- Spacing rhythm: 4px base increments at the small end (.25, .5, .75, 1, 1.5rem), expanding to 2, 3, 4, 5, 8, 9, 10, 11, and 12rem for desktop section spacing; pill buttons use an 80px radius.
- Layout intent: 12-column, full-bleed marketing grid with 64px desktop padding/32px gutters, 48px/24px tablet-landscape, 32px/16px tablet-portrait, and 24px mobile padding; article content caps at 60rem.
- Signature element: an oversized, no-wrap branding word rendered at 9.4375rem, reduced to 8rem below 25rem viewport width and enlarged to 15.813rem at 960px+, with line-height 1 and negative top/bottom margins so it crops tightly into the composition.

## Lessons (3-5 bullets)
- Use one humane custom sans across clinical explanation and commerce, then create hierarchy through a disciplined 400/600 weight pairing and responsive line-height changes rather than introducing a decorative second face.
- Give healthcare actions a stable semantic green (#119555) while reserving a broader teal/orange/red/blue palette for editorial and product-section identity; this keeps conversion cues consistent without making the whole site visually clinical.
- Combine full-bleed storytelling sections with a fixed 12-column grid, but narrow evidence-heavy article reading to 60rem; the same system can support emotional marketing and credible long-form education.
- Scale section spacing much more aggressively than component spacing: 4-24px increments keep controls compact, while 48-192px intervals create calm, legible separation between healthcare topics.
- Let one brand gesture break the otherwise restrained system: the 128-253px tightly cropped branding word creates memorability while typography, grid, and semantic colors remain systematic.

## Avoid (1-2 bullets)
- Do not apply every supporting brand color equally to actions; copying the palette without its semantic green/action hierarchy would make clinical states and conversion paths ambiguous.
- Do not reuse the giant cropped brand treatment for ordinary headings: at up to 15.813rem with negative margins it depends on short, no-wrap brand text and would cause overflow or obscure content with longer copy.
