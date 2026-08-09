# https://gleam.run (sector: opensource, sweep: excellence, fetched 2026-08-06)
status: full-css

## Token block (~10 lines)
- Core canvas: underwater blue `#292d3e`; main text `#f0eeff`; subtle text `#c9cfea`; bright text/link white `#fefefc`.
- Light surfaces: aged-plastic yellow `#fffbe8` for the page header; near-white `#fefefc` for footer and gradient endpoints; black text `#151515`.
- Brand/action accents: pink `#ffaff3` for mascot, underlines, sponsor band, and hover states; aubergine `#584355` for pill CTAs.
- Supporting surfaces: card charcoal `#313546`, border charcoal `#616682`, code background `#1e1e1e`, deepest shadow `#151515`.
- Syntax palette: blue `#9ce7ff`, green `#c8ffa7`, yellow `#fdffab`, pink `#ffaff3`, red `#ff6262`, orange `#ffd596`, light pink `#ffddfa`, grey `#d4d4d4`.
- Type pairing: body `"Outfit", sans-serif`; headings, navigation, logo, and hero `"Lexend", sans-serif` at weights 400/700; `"Cascadia Mono"` is loaded, but its CSS variable assignment is commented out.
- Type scale: 12px small, 16px code, 18px body/nav, 22px news titles, 24px hero CTA/subtitle, 28px logo, 36px hero/feature titles, and 48px friendly/sponsor display titles.
- Spacing rhythm: a 10px base with `20/30/40/50/60px` multiples; content padding 20px, feature-section vertical padding 40px, and primary CTA padding 10px 40px.
- Layout intent: center a 960px max-width content rail; alternate wrapping 50/50 text-and-code rows with 40px gaps, then collapse naturally below 960px; long-form pages keep the same single rail.
- Signature element: Lucy, a pink `#ffaff3` smiling star mascot, swaps to a happy SVG and rotates 23° on hover; 100px-high, 1200px-wide soft waves carry the yellow/pink header into the dark canvas.

## Lessons (3-5 bullets)
- Make the open-source project feel approachable without weakening technical credibility: warm mascot and rounded 100px CTAs sit beside real, color-coded code samples in every feature row.
- Reuse one narrow 960px rail across marketing, documentation, and news; structural consistency lets content type - not a new shell - signal the page mode.
- Turn the brand palette into navigation: pale yellow identifies the global header, dark blue holds technical content, pink marks community/sponsorship moments, and near-white closes the page.
- Use alternating text/code pairs to translate each product claim directly into evidence, with both columns sharing the rail equally and wrapping from a 250px minimum.
- Keep delight small and repeatable: the mascot’s 200ms hover swap/rotation and the shared wave divider add personality without interrupting reading.

## Avoid (1-2 bullets)
- Do not copy the pink/yellow/dark palette without similarly strict role assignment; using `#ffaff3` everywhere would erase its current value as an interaction and community cue.
- Do not preserve the desktop navigation unchanged on narrow screens: this implementation hides the large hero mascot and stacks the navbar below 960px.
