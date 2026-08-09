# https://jobs.netflix.com (sector: bigtech, sweep: excellence, fetched 2026-08-06)
status: full-css

## Token block (~10 lines)
- Palette, base: black `#000000` canvas, white `#ffffff`, and softened neutral white `#f7f5f5` for body text.
- Palette, brand/action: Netflix red `#e50914`; the source also defines dark red `#080202` and bright red `#fceeee` for tonal states.
- Palette, section accents: orange `#d23c01`, yellow `#e68e01`, green `#00ccab`, blue `#012be6`, purple `#7e01d2`, and pink `#d201b6`, each paired with near-black and near-white variants.
- Type pairing: `Netflix Sans, sans-serif` for the body and display copy; `Netflix Sans Condensed, sans-serif` for captions, labels, and buttons. Loaded weights are 400, 500, 700, 900 (Condensed: 500, 700).
- Type scale: 10px utility labels; 12-18px supporting/body text; fluid section headings `clamp(0px, 8.53333vw, 96px)` mobile and `clamp(0px, 2.08333vw, 60px)` desktop.
- Display scale: uppercase 900-weight heroes use `clamp(0px, 21.3333vw, 240px)`, `clamp(0px, 20.8333vw, 320px)` tablet, and `clamp(0px, 12.5vw, 360px)` desktop, with `-0.02em` tracking and 0.8 line-height.
- Spacing rhythm: 0.5rem/1rem grid gaps; 1rem, 1.25rem, 1.5rem, 2rem, 3rem, 4rem increments; full sections commonly step to 7.5rem mobile and 10rem desktop.
- Responsive gutters: 1.25rem default, 1.5rem from 769px, and 2rem from 1025px; breakpoints prominently include 653/654px, 768/769px, 1024/1025px, and 1160/1161px.
- Layout intent: a full-width `100vw` canvas with flex-based percentage columns (for example 34.375%, 37.5%, 40.625%) instead of a fixed centered max-width; narrower copy is capped by widths such as 34rem.
- Signature element: a 500vh scroll chapter holding a 100vh sticky, overflow-hidden mosaic stage with 200px perspective, giant 12.5vw/360px type, image squares, and top/bottom mosaic overlays.

## Lessons (3-5 bullets)
- Treat the careers narrative like entertainment: couple very large, compressed headlines with image-led, full-viewport chapters, then reserve ordinary UI scale for search and navigation.
- Build responsiveness into type and column proportions, not just breakpoints: fluid `clamp()` headlines and percentage spans keep the composition cinematic from phone to wide desktop.
- Use one stable black/soft-white/red identity while rotating a controlled family of section accent colors; this creates variety without weakening brand recognition.
- Let generous 7.5-10rem section spacing and narrow 34rem reading measures separate immersive moments from explanatory copy.
- Keep the job-finding action concrete inside the spectacle: red, uppercase Condensed buttons remain visually consistent across content chapters.

## Avoid (1-2 bullets)
- Do not copy the 500vh sticky/perspective treatment throughout a site; repeated scroll capture would turn the signature moment into friction and raise motion/performance costs.
- Do not reuse the extreme 0.8-line-height, 900-weight uppercase display treatment for long or localized copy; the source includes language-specific line-height overrides, showing that the composition needs adaptation.
