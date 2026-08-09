# https://www.gosh.org (sector: hospital, sweep: excellence, fetched 2026-08-06)
status: full-css

## Token block (~10 lines)
- Palette / brand: `#0AD7FF` cyan for the header, footer, cards, CTAs and selected donation states; `#E3F30C` acid yellow for donate/submit actions.
- Palette / text and surfaces: `#212121` primary text, `#FFFFFF` page/card surface, `#E7E6E5` secondary panels, navigation and story cards.
- Palette / interaction: `#3333FA` links, `#6300CC` visited links, `#0078EB` active controls/focus accents, `#B00020` errors.
- Type family: custom `GOSH Brave, Arial, Helvetica, sans-serif`, supplied in 400/500/600/700 normal and italic faces; headings commonly use 600–800.
- Body type: root `16px` with `1.5625` line-height (25px); supporting sizes include 12, 14, 17, 18, 19, 20, 21 and 22px.
- Heading scale: base h1/h2/h3/h4–h6 = 28/30/26/20px; content page title = 36px/1.0 at weight 800; donation hero title = 30px mobile and 50px from 650px.
- Spacing rhythm: 10/15/20/24/30/40/50/60/80px recur; standard section separation is 60px, cards use 20–30px gaps, and desktop story cards use 50px padding.
- Layout widths: `1180px` large shell, `804px` small/reading column, `1455px` campaign banner; horizontal shell padding is 24px mobile and 50px from 900px.
- Responsive layout: breakpoints at 450, 650, 900 and 1180px; card grids step from one column to two at 650px and three/four-column rules at 900px, with flex sidebars/content on desktop.
- Signature element: a white donation amount/frequency selector embedded over a photographic hero (320px max on desktop), pulled upward by `margin:-100px auto 0` on mobile, with cyan selected amounts and an acid-yellow submit.

## Lessons (3-5 bullets)
- Put the highest-value hospital action inside the emotional story image: the homepage does not separate patient photography from giving, but overlays a compact, immediately usable donation control.
- Reserve the brightest colors by role: cyan carries institutional identity and selected states, while acid yellow is narrowly assigned to donation conversion actions, preserving a clear hierarchy.
- Pair a friendly proprietary typeface with restrained geometry and high-contrast `#212121` text; personality comes from type and color while reading pages remain conventional and accessible.
- Use one shell system across templates, then selectively break it for campaigns: 1180px supports ordinary navigation/content, 804px controls reading measure, and only hero campaigns extend to 1455px.
- Let components reflow rather than merely shrink: cards change column count, story cards become alternating image/text rows at 900px, and the donation form changes from an overlap to an in-image panel.

## Avoid (1-2 bullets)
- Do not spread `#0AD7FF` and `#E3F30C` across every component; copying the palette without its role discipline would erase the donation CTA's priority.
- Do not copy the full 12–100px stylesheet type range as a general scale; many sizes belong to campaign/event variants, while core pages use a much tighter 16–36px range.
