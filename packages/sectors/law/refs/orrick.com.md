# https://www.orrick.com (sector: law, sweep: excellence, fetched 2026-08-06)
status: full-css

## Token block (~10 lines)
- Palette/base: body text `#292938`; headings and dark section background `#333447`; deepest black `#1b1c1c`; white `#fff`.
- Palette/neutrals: muted text `#717271`, warm muted text `#b1a99f`, borders `#e2ddd7` / `#e8e4df`, pale surfaces `#f5f3f2` / `#ebe8e4`.
- Palette/accents: link blue `#0077c7` (hover `#00497b`), brand green `#7a9c49` (light `#acc37e`), teal `#008c95`, light blue `#558ed5`.
- Type pairing: no second text face is declared; `"Azo Sans", sans-serif` carries body and headings, with the custom `orrick` font reserved for icons.
- Azo Sans weights: 300, 400, 600, 700, 800 plus italic 300/400/600/700; base body is 13px and editorial copy is 14px.
- Type scale: h1 24px; h2 24px; h3/h4 15px; homepage h2 30px rising to 40px at desktop; hero titles 31px rising to 37px; line-height 1.3 (hero-carousel headings 1.2).
- Spacing rhythm: recurring 10/15/20/30px increments; editorial paragraphs use 20px bottom margin, cards use 15px 14px 5px padding, and major sections move from 20px 0 30px to 60px 0 30px 30px at 768px+.
- Layout width: Bootstrap-derived containers are 740/960/1030px at 768/992/1200px, but the current stylesheet overrides `.container` at 769px+ to `width:100%` with 150px horizontal padding.
- Layout intent: a 12-column responsive grid supports full-bleed homepage experiences; the article interior uses an 8-column reading area paired with a 4-column author/sidebar rail.
- Signature element: stacked full-width Ceros experiences form an interactive cinematic hero and alternating story bands—source aspect ratios 2.80898876, 4.19463087, and 8.38926174—with `margin-bottom:-45px` joining the bands tightly.

## Lessons (3-5 bullets)
- Let one disciplined sans family span navigation, headlines, metadata, and long-form copy; hierarchy comes from a broad 300–800 weight range and a compact, explicitly stepped scale rather than decorative type pairing.
- Separate brand theatre from legal substance: immersive full-width storytelling leads the homepage, while article pages revert to a predictable 8/4 editorial grid with authors and contact details always adjacent.
- Build a warm neutral system around dark aubergine rather than default black/gray: `#333447`, `#b1a99f`, `#e2ddd7`, and `#f5f3f2` create sober contrast while green, teal, and blue carry interaction and sector identity.
- Use dense 13–15px utility and card typography, then reserve 30–40px display sizes for section framing; this keeps information-heavy legal content compact without flattening the homepage hierarchy.

## Avoid (1-2 bullets)
- Do not copy the 150px desktop container padding without responsive testing; it creates generous framing on wide screens but can consume too much usable width for dense legal tables, filters, or long titles.
- Do not imitate the stacked third-party Ceros bands as mere decoration: without equivalent interaction, editorial pacing, and mobile-specific aspect ratios, the negative overlap and multiple embeds would add weight and fragility without the signature effect.
