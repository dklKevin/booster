# https://www.virginatlantic.com (sector: aviation, sweep: excellence, fetched 2026-08-06)
status: full-css

## Token block (~10 lines)
- Core palette: brand red `#f92b47`; inverse brand red `#da0530`; Flying Club/economy red `#f32844`.
- Neutral palette: primary dark `#030c16`, secondary dark `#111921`, primary white `#ffffff`, secondary light `#f5f5f6`.
- Supporting brand/status palette: purple `#c256d7`, Upper Class purple `#4f145b`, gold `#bda05d`, silver `#99a4af`, info `#43acf0`, success `#10a871`, warning `#f7803e`, error `#f25878`.
- Type family: `Gotham, Helvetica, Arial, sans-serif`; shipped Gotham weights are 300 (light), 325 (book), and 350 (medium).
- Display scale: 40/48px mobile to 48/60px tablet to 64/76px desktop; next levels are 32/40px to 48/60px and 28/36px to 40/48px.
- Body scale: 20/32px, 16/24px, 14/22px, and 12/16px; captions are 12/12px.
- Spacing rhythm: recurring 8, 12, 16, 24, 32, and 48px gaps/padding; section padding steps from 48px to 64px to 96px.
- Responsive gutters: 16px below 640px, 24px from 640px, and 40px from 768px; key breakpoints are 640, 768, and 992px.
- Layout intent: 12-column grid, 16px mobile/24px wider row gaps, 1200px bounded content, and 1280px outer stages for image-led modules.
- Signature element: a full-width destination image with a `#030c16` content panel pulled upward over its lower edge; the panel is 24px padded on mobile and up to 608px wide with 48px side padding on desktop.

## Lessons (3-5 bullets)
- Separate the bounded information grid (1200px) from the wider visual stage (1280px), so booking and editorial content feel related without making imagery timid.
- Use a light-weight, generously led display scale (up to 64/76px) while keeping operational copy at 16/24px; this preserves an aspirational tone without weakening scanability.
- Make responsive spacing systematic: increase gutters 16→24→40px and section padding 48→64→96px at explicit breakpoints instead of scaling every component independently.
- Carry one recognizable hero construction across sales and destination pages—the overlapping dark copy panel turns varied campaign photography into a consistent branded frame.
- Reserve vivid reds and cabin/status colors for meaning and interaction, letting near-black and white backgrounds do most of the compositional work.

## Avoid (1-2 bullets)
- Do not copy the large palette as decoration; the extracted CSS assigns distinct reds, purples, metallics, and semantic colors to specific brand, cabin, loyalty, and status roles.
- Do not reuse the overlapping hero panel without equivalent image height and breathing room; its 24–48px internal padding and 1200/1280px surrounding layout prevent it from crowding the photography.
