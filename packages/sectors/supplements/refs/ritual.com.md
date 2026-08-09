# https://ritual.com (sector: supplements, sweep: excellence, fetched 2026-08-06)
status: full-css

## Token block (~10 lines)
- Core palette: indigo `#142B6F` for foreground, links, primary buttons, and dark section backgrounds; white `#FFFFFF` for the base surface and inverse text.
- Signature accent: yellow `#FFD600` for brand emphasis, hover fills, rules, stars, and full-bleed accent sections; supporting tints are `#FFE666`, `#FFEF99`, and `#FFF7CC`.
- Supporting surfaces: warm cream `#FCF8EE`, pale cream `#FEF6EB`, and cool gray `#F5F7F8`; secondary text is `#717171`, borders/disabled controls `#B3B2B1`.
- Secondary accents/status: rust `#AB4824`; danger `#C83D1E`, warning `#DB7F16`, success `#4C840D`, and focus `#4B3DC4`.
- Type pairing: `CircularXX` is the primary family for headings and body; `Dutch801 Rm BT`, serif is the secondary family used for blockquotes/editorial contrast.
- Display scale: h1 `clamp(40px, 4.58333vw, 66px)`/1.1 with `-0.02em`; h2 `clamp(40px, 3.33333vw, 48px)`/1.2; h3 `clamp(32px, 2.77778vw, 40px)`/1.25; all use CircularXX weight 450.
- Supporting scale: h4 `24–32px`/1.25, h5 `20–24px`/1.5, h6 `12–16px`/1.5 uppercase with `0.08em`; body `16–18px`/1.5; caption `12px`/1.5.
- Spacing rhythm: a 4px base token plus fluid named steps—xs `8–16px`, sm `16–24px`, md `24–32px`, lg `32–48px`, xl `48–64px`—reused for gaps, margins, and padding.
- Layout intent: centered responsive containers at `640/768/1024/1280/1536px`, `15–20px` inline gutters, and 12-column grids at tablet/desktop breakpoints support alternating editorial, commerce, and proof modules.
- Controls: primary buttons are 45px high with `12px 24px` padding and a 25px radius; the default indigo fill flips to yellow on hover.
- Signature element: electric-yellow highlighter language—animated underline bars, yellow hover fills, and emphasized review text with `0 0 14px 3px #FFE666E6` glow—threads the same accent through navigation, proof, and commerce.

## Lessons (3-5 bullets)
- Assign one high-energy accent to both storytelling and interaction: Ritual's `#FFD600` marks claims and reviews, but also makes button and navigation states feel native to the brand.
- Build trust content into the same modular grid as products: the homepage, product page, and standards page reuse containers, cards, accordions, and 12-column compositions instead of making traceability feel like a detached report.
- Use warm and cool near-white section surfaces (`#FCF8EE`, `#FEF6EB`, `#F5F7F8`) to create long-page pacing while keeping indigo text and yellow interaction cues consistent.
- Keep the commerce typography direct and highly legible in CircularXX, then reserve Dutch801 for quotations and editorial moments; the contrast adds humanity without weakening product clarity.
- Let spacing scale fluidly within bounded steps rather than jumping only at breakpoints; the extracted xs–xl ladder keeps dense product controls and expansive evidence sections visually related.

## Avoid (1-2 bullets)
- Do not spread saturated yellow across every surface: Ritual balances `#FFD600` with large white, cream, and cool-gray fields; copying only the accent would flatten hierarchy and exhaust attention.
- Do not copy the serif as a general body face: in the fetched CSS, CircularXX carries body and heading legibility while Dutch801 is constrained to editorial contrast.
