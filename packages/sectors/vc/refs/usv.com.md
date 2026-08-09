# https://www.usv.com (sector: vc, sweep: excellence, fetched 2026-08-06)
status: full-css

## Token block (~10 lines)
- Palette — surface #fff; primary navigation/brand text #000; headings and SVG icons #0d0d0d.
- Palette — action/link accent #28a055 with hover #187f3e; metadata #999; hairline dividers #e6e6e6.
- Palette — optional thesis/category accents #161c74 (indigo) and #f9b44f (amber), paired with #28a055 (green); tag text #fff.
- Type pairing — a deliberate single-family system: "Graphik Web", sans-serif, self-hosted in weights 100–900; body uses 400 and strong text 500.
- Type scale — body 16px/1.9 mobile and 18px/1.7 from 783px; h1 30→60px, h2 36→46px, h3 24→36px, h4 20→30px.
- Editorial scale — homepage thesis 18/30→24/36px; article title 30/40→36/36px; article copy 18/30px; metadata 20/24→24/36px.
- Spacing rhythm — 20px mobile side gutters; 30–32px common section/column gaps; 60–67px editorial transitions; 90–100px major desktop section spacing.
- Layout — fluid mobile canvas resolves to a centered 1128px content frame; long-form reading blocks narrow to 744px.
- Responsive system — primary shifts occur at 783px, 992px, and 1200px; columns stack below roughly 785px and use a 32px desktop gutter.
- Signature element — the homepage's equal-column editorial split: a compact thesis at left and ruled recent-post stream at right, divided by a 1px #e6e6e6 vertical line on desktop.

## Lessons (3-5 bullets)
- Treat the investment thesis as the homepage's primary content, not a slogan over decorative imagery: USV gives it 24/36px desktop type and an entire column.
- Use one type family across navigation, thesis, lists, and essays, then create hierarchy through weight, size, and line-height; this makes a content-heavy VC site feel coherent rather than templated.
- Constrain institutional pages to 1128px but narrow sustained reading to 744px, preserving a consistent shell while optimizing each content mode.
- Make the firm's publishing cadence visible beside its positioning; the thesis/recent split connects what the firm believes with what its people are discussing now.
- Let a single green (#28a055) carry links, underlines, buttons, and blockquotes while neutral #e6e6e6 rules organize dense information without card chrome.

## Avoid (1-2 bullets)
- Do not copy the very light divider-and-whitespace structure without equally strong typography and content hierarchy; dense lists would otherwise lose boundaries and scanability.
- Do not deploy all three thesis accents (#161c74, #f9b44f, #28a055) as general brand colors; the CSS scopes them to thesis/category dividers and tags, while the live homepage remains predominantly monochrome with green links.
