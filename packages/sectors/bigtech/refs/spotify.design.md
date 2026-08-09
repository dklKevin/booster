# https://spotify.design (sector: bigtech, sweep: excellence, fetched 2026-08-06)
status: wayback

## Token block (~10 lines)
- Core palette: black `#171313` for typography / dark theme backgrounds; white `#fff` for content backgrounds and dark-theme typography; muted black `#837e7e`.
- Accent palette: azure `#3e8ef1`, storm `#a4c9d8`, tangerine `#ff4935`, citric `#cdf567`, sunflower `#ffbc4b`, pink `#ffd0d5`, salmon `#fb7ea8`, factory yellow `#ffe818`.
- Theme roles swap those tokens by story category: Design = sunflower background / salmon + citric accents; Inspiration = azure / storm + citric; Noted = pink / salmon + storm; Process = storm / factory yellow + tangerine; Tools = factory yellow / azure + salmon; Listen = black / citric.
- Type pairing: headings use `SpotifyMixUITitle, -apple-system, BlinkMacSystemFont, sans-serif`; body uses `SpotifyMixUI, -apple-system, BlinkMacSystemFont, sans-serif`.
- Mobile display scale: `64, 55, 48, 42, 32px`; headings `24, 18, 14px`; body `24, 18, 16, 14px`; UI `32, 16, 16, 14px`.
- At `600px`, display becomes `90, 80, 64, 55, 42px`; at `1024px`, `152, 90, 80, 64, 55px`; desktop headings are `32, 24, 14px` and body `32, 24, 20, 14px`.
- Weights are `300/400/500/700/900`; display, heading 1–2, body 1–2, and key UI styles use `700`, while 14px UI labels are uppercase.
- Spacing rhythm is rem-based and strongly repeats `8, 12, 16, 24, 32, 60, 80, 100px`; homepage section padding steps from `32px` to `48px` to `60px`, and article vertical gaps step `60/80/100px`.
- Layout: page gutters are `16/24/60px` at base/600/1024; the centered container max is `112.5rem` (`1800px`); grids switch to 4 columns with `16px` gaps at 600 and 12 columns with `24px` gaps at 1024.
- Signature element: a full-viewport “Heavy Rotation” featured-story carousel sits over a category-colored, oversized SVG burst; the source also exposes Previous Story and Shuffle Stories controls and a `120vmin` burst behind spotlight cards.

## Lessons (3-5 bullets)
- Make editorial taxonomy visual: a small set of named category themes can recolor background, primary accent, secondary accent, and focus state while preserving one shared component system.
- Let the opening interaction carry brand energy, then return long-form and utility sections to white/black; the homepage explicitly isolates its full-height carousel from conventional card grids below.
- Scale both typography and layout at the same two breakpoints: the source coordinates the 600/1024px type jumps with 4/12-column grids and wider gutters, keeping hierarchy proportional to available space.
- Give articles a narrower reading lane inside the wide grid: desktop rich text occupies 5 of 12 columns while galleries and media occupy 6, retaining generous surrounding space without abandoning the site-wide grid.
- Use motion as system behavior, not decoration: shared `150/350/650ms` speeds govern navigation, hover reveals, carousel UI, and burst transitions, with a reduced-motion override to `1ms`.

## Avoid (1-2 bullets)
- Do not apply every saturated token at once; the source uses tightly defined category combinations and repeatedly returns content sections to white/black.
- Do not copy the `152px` desktop display size or full-viewport carousel without the responsive reductions and visually hidden semantic headings present in the source.
