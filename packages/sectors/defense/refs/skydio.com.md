# https://www.skydio.com (sector: defense, sweep: excellence, fetched 2026-08-06)
status: full-css

## Token block (~10 lines)
- Palette / primary text: Skydio Black `#22211f` (`--gray-850`); true black `#000` (`--gray-1000`) is used for dark media sections.
- Palette / surfaces: white `#fff`, quiet gray `#f7f7f7`, panel gray `#f0f0f0`, and rule/muted gray `#c6c5c2`.
- Palette / secondary text: `#4a4947` and `#6d6c69`; brand/action blue is `#027bc6` with hover using the same token.
- Type family: `"Case", sans-serif`; variable source `CaseVAR.woff2` at weights 400–500, with separate Case Regular and Medium files.
- Display scale: H1 XXL `clamp(3.5rem, -0.7955rem + 11.9318vw, 8.75rem)`; H1 XL `3–6rem`; H1 `2.375–3.75rem`; H2 `1.75–3rem`.
- Supporting scale: H3 `1.375–2rem`; H4 `1.125–1.75rem`; body 1 `1.125–1.5rem`; body 2 `1–1.125rem`; body 3 `0.875–1rem`; note `0.75–0.875rem`.
- Type treatment: display weights are 400/500, H1 letter-spacing is `-1px` (`-2px` on H1 XL), and display line-height ranges from 100% to 120%; body 1 uses 140%/150%.
- Spacing rhythm: fixed core steps `0.5, 1, 1.5, 2, 2.5, 3, 4, 4.5, 6, 7.5, 10, 11.25, 14.25rem`, plus fluid paired steps such as `1–1.5rem`, `2–4rem`, and `4–6rem`.
- Layout intent: nested full/content/medium/small CSS-grid tracks cap at `1920px` / `1464px` / `1280px`; default inline padding is fluid from `1.125rem` to `4.75rem`, with common copy caps of `60ch` and hero content at `60rem`.
- Signature element: a live “Customer flights and counting” counter set in H1 XXL (`3.5–8.75rem`), immediately turning operational scale into the page’s dominant proof point.

## Lessons (3-5 bullets)
- Treat evidence as display content: the live flight count gets the largest type token instead of being buried in a conventional statistics card.
- Keep a restrained near-black/white/gray foundation and reserve `#027bc6` for action; this lets field imagery and product footage carry the emotional color.
- Use a single fluid type and spacing system across cinematic homepage modules, a national-security landing page, and a denser three-column resources grid.
- Organize broad capabilities as short, numbered/captioned image columns; the source pairs these with 3:2 desktop imagery, 21:9 mobile imagery, and a restrained 1.04 hover scale.
- Combine very wide shells with tight reading measures: the system permits 1920px media while limiting supporting copy to 50–60ch and hero text to 60rem.

## Avoid (1-2 bullets)
- Do not copy the oversized counters and 8.75rem display type without equally concrete operational evidence; otherwise the scale reads as spectacle rather than proof.
- Do not apply the full-bleed autoplay-video treatment to every section; the source alternates dark cinematic modules with quiet white/gray evidence and product sections.
