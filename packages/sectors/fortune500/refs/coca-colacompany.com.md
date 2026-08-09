# https://www.coca-colacompany.com (sector: fortune500, sweep: excellence, fetched 2026-08-06)
status: full-css

## Token block (~10 lines)
- Palette / canvas: `#f2f2f2` page background; `#fff` regular surface and inverse text.
- Palette / ink: `#000` primary text, icons, actions, and footer surface; `#6c6c6c` subtle text and dark hover; `#d5d5d5` subtle stroke.
- Palette / selective accents: `#f5010a` red article/stat accent; `#ff570f` orange gradient edge; `#6acf7f` green and `#f79a01` orange labels.
- Type family: `TCCCUnity-head-regular, TCCC-UnityText, sans-serif` for the page; headings/components also use `TCCCUnity-head-medium` and `TCCCUnity-head-bold`, each falling back to `sans-serif`.
- Core type scale, mobile → desktop: body `16/24px` → `16/24px`; h4–h6 `20/28px` → `24/32px`; h3 `24/32px` → `28/36px`.
- Upper type scale, mobile → desktop: h2 `28/36px` → `32/40px`; h1 `32/40px` → `38/48px`; display token `48/56px` → `96/112px`; heading tracking `-1.5px`.
- Spacing primitives: `2, 4, 8, 12, 16, 20, 24, 32, 40, 64, 80, 120px`; card padding is `24px` mobile and `32px`/`64px` desktop.
- Vertical rhythm, mobile → desktop: text→text `8px`; module→text `32px`; hero→module `40px` → `56px`; module→module `56px` → `120px`.
- Layout: 4-column mobile with `24px` margins and `16px` gutters; 12-column desktop with `24px` gutters, `1120px` content max, and `1280px` expanded max.
- Shape: cards/images use `16px` radii; buttons use a pill radius (`8000px`); the homepage feature wrapper uses `clamp(16px, 1.67vw, 24px)`.
- Signature element: a responsive square hero pairs an animated headline with a 50%-width rounded media carousel; slides enter over `.8s` and use circular image bullets with SVG progress rings.

## Lessons (3-5 bullets)
- Let a restrained corporate shell carry a varied brand portfolio: the shared canvas stays `#f2f2f2`/black/white while product tiles and a few editorial modules introduce controlled accent color.
- Encode editorial pacing as tokens: the jump from `56px` mobile to `120px` desktop between modules creates deliberate breathing room without bespoke section margins.
- Make the lead story a recognizable interaction, not just a large photograph: the 50/50 square composition, animated copy, media slides, and thumbnail progress controls form one repeatable story system.
- Keep interior templates structurally distinct but token-consistent: the fetched About page uses narrative/content-card and draggable-card sections, while Brands uses a full-width hero and inline brand cards under the same type, spacing, and grid rules.

## Avoid (1-2 bullets)
- Do not flood a corporate imitation with Coca-Cola red: the extracted default brand surface and action tokens are black/white, with `#f5010a` reserved for specific article/stat treatments.
- Do not copy the hero motion without reduced-motion and content-density checks; blurred headline entry, slide translation, autoplay progress rings, and media in one viewport can become distracting or expensive.
