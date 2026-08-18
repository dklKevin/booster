# https://colossal.com (sector: biosecurity, sweep: excellence, fetched 2026-08-06)
status: full-css

## Token block (~10 lines)
- Core palette: #000 backgrounds/type and #FFF surfaces/reversed type; the outer HTML canvas is #EEE.
- Neutral palette: #222 body copy/dark panels, #838383 secondary copy and borders, #444/#777 rules, #f1f1f1 pale section fields.
- Accent palette: #9940dd/#ad65d4 purple species/CTA states, #ff7b31 orange science panels, #91ed0d green status dots.
- Type pairing: Telegraf is the body face; NB Architekt Light is the display heading face; NB Architekt Std is used for labels, navigation, and emphatic display text.
- Base type scale: paragraphs clamp(14px, 1.5vw, 29px); medium clamp(10px, 1.9vw, 35px); large clamp(10px, 2.9vw, 55px).
- Display scale: section labels clamp(10px, 0.6vw, 12px); interior h4/h3/h2 reach 36px/80px/120px; technology and species heroes reach 230px and 210px.
- Controls: small buttons clamp(10px, 0.7vw, 14px) with 100px radius; large CTAs reach 29px with 60px vertical/120px right padding and 1000px radius.
- Spacing rhythm: named vertical spacers top out at 20/60/100/160/240/320px, driven by 1/3/5/8/12/16vw clamps.
- Layout intent: Bootstrap rows/12-column classes on a centered 2000px canvas; 40px fluid gutters or 120px narrow gutters; interior containers cap at 84vw/1680px (94vw mobile).
- Signature element: indexed lab-notebook navigation (for example 000-00) paired with 0.5-1px rules, 4-8px squares, 3-60px discs, and neon status dots over cinematic full-bleed imagery.

## Lessons (3-5 bullets)
- Make complex biotechnology feel navigable by numbering both pages and page sections, turning a sprawling narrative into an explicit scientific index.
- Pair cinematic organism imagery and very large 120-230px display type with tiny 10-15px technical labels; the contrast carries wonder and evidentiary precision at once.
- Reuse a small annotation grammar - hairlines, squares, discs, dots, rotated captions - across otherwise different species palettes so every page still belongs to one research system.
- Scale long-form storytelling with viewport-based clamps and a fixed spacer ladder, while keeping copy in constrained columns inside the 12-column frame.
- Reserve saturated purple, orange, and green for species identity, interactive state, or scientific notation against dominant black/white/gray fields.

## Avoid (1-2 bullets)
- Do not copy the 200px-plus headlines, overflow imagery up to 200% width, or negative viewport margins without the source's mobile overrides; they will collide or crop unpredictably.
- Do not reproduce every accent color and annotation at equal intensity; without the black/white field and strict indexed hierarchy, the lab language becomes visual noise.
