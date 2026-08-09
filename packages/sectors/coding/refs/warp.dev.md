# https://www.warp.dev (sector: coding, sweep: excellence, fetched 2026-08-06)
status: full-css

## Token block (~10 lines)
- Canvas/card palette: `#ffffff`; body copy: `#292927`.
- Inverted product-surface palette: surface `#08090a`, primary text `#eef7fa`, body text `#b8bfc1`, secondary text `#9ea4a6`, border `#424647`.
- Accent/status palette: tertiary purple `#c59fff`; success `#43c251`, active blue `#238dff`, warning `#f6ba00`, error `#ee343b`.
- Display type: `theFuture, "theFuture Fallback"` / `var(--font-the-future), "The Future", system-ui, sans-serif`, weight 400, tracking `-0.035em`.
- Body type: `Matter, system-ui, sans-serif` (400/500 supplied); code/labels: `Azeret Mono, "Azeret Mono Fallback", ui-monospace, monospace` (400/500).
- Type scale from a 16px base: 12, 14, 16, 18, 20, 24, 30, 36, 48, 60, 72, 96px; line-height tokens 1, 1.1, 1.25, 1.5, 1.75, 2.
- Homepage H1: `clamp(3.5rem, 5vw, 5rem)` (56–80px), line-height `clamp(60px, 7vw, 90px)`; section H2: `clamp(1.75rem, 3.5vw, 3.5rem)` (28–56px).
- Spacing rhythm: 4px base; semantic steps 4, 8, 16, 24, 32, 48, 64px; sections use 64px, with 24px mobile / 40px desktop side gutters.
- Layout intent: centered fluid containers capped at 80rem (1280px), moving from one column to asymmetric 320px/content, two-column, or three-column grids at large breakpoints.
- Signature element: oversized terminal/agent UI simulations with source-defined row reveals, prompt/control reveals, shimmer text, typing dots, and purple scanner motion.

## Lessons (3-5 bullets)
- Make the product UI the visual proof: Warp gives terminal/agent simulations the large-media role that coding sites often reserve for generic illustration.
- Separate voices by task: a distinctive low-weight display face carries the proposition, Matter keeps explanations neutral, and uppercase Azeret Mono makes labels feel native to developer tooling.
- Keep expressive demos inside a restrained system: 4px spacing, 64px section intervals, fixed 24/40px gutters, and an 80rem cap let animated surfaces feel deliberate instead of chaotic.
- Use near-black product panels inside a white editorial canvas; the explicit `#08090a`/`#eef7fa` inversion focuses attention while preserving long-form readability elsewhere.
- Let interior pages inherit tokens but change composition: the agent page keeps the centered product-marketing system, while the blog uses a simpler responsive article-title scale.

## Avoid (1-2 bullets)
- Do not copy every bundled color as brand palette: the CSS includes framework utilities and status colors; the page-level canvas, text, inverted-surface, and tertiary tokens carry the recognizable system.
- Do not reproduce the motion density without reduced-motion handling; Warp explicitly disables reveal, shimmer, typing, scanner, and autoplay behavior under `prefers-reduced-motion`.
