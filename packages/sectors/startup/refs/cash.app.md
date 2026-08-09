# https://cash.app (sector: startup, sweep: excellence, fetched 2026-08-06)
status: full-css

## Token block (~10 lines)
- Palette / brand: `#00E013` is the homepage hero and primary accent; `#000000` is primary text, dark surface, and default button fill.
- Palette / surfaces: `#FFFFFF` is the main surface and inverse text; `#E5E5E5` is the light section background; `#1D1D1D` is the alternate dark section background.
- Palette / secondary: `#737373` is muted text; borders and quiet fills use `#D8D8D8`, `#E0E0E0`, and `#F0F0F0`.
- Type pairing: `Cash Sans Wide` for display emphasis, `Cash Sans` for interface/body copy, and `Cash Sans Mono` for monospaced details; fallback stack is `"Helvetica Neue", helvetica, sans-serif`.
- Homepage type scale: h1 `2.5em` mobile / `3.25em` tablet / `3.5em` desktop; h2 `2em` / `2em` / `2.5em`; h3 `1.75em` / `1.5em` / `1.75em`; body `1em` / `1.125em` / `1.125em`.
- Type treatment: headings use weight `400`, `-0.03em` tracking, and `0.95` (h1) or `1.1` line-height; body uses weight `400`, `-0.03em` tracking, and `1.4` line-height.
- Spacing rhythm: core card/grid gaps step from `16px` mobile to `20px` desktop; card rows use `32px`; hero copy uses `32px` blocks and `clamp(40px, 2em, 54px)` before its CTA.
- Layout grid: centered page capped at `1440px`; 5 equal columns with `5px` outer margin and `2.75vw` gaps become 8 columns at `1024px`, with `20px` margins and `0.7vw` gaps.
- Layout intent: full-viewport narrative sections (`min-height: 100vh`) place concise copy and CTA around a central product visual, then shift into responsive 2-to-4-column card grids.
- Signature element: a `#00E013` viewport hero with alpha video clipped by a rounded-phone SVG mask (`336×728`, `44px` radius), animated via independent mask scale, background opacity, and content opacity.

## Lessons (3-5 bullets)
- Make the category color structural, not decorative: Cash App turns `#00E013` into the entire hero field while keeping the operational palette almost entirely black, white, and gray.
- Pair plainspoken financial copy with restrained typography: regular-weight, tightly tracked headlines feel confident without borrowing the visual language of a traditional bank.
- Let one product-shaped motion device carry the brand: the masked phone video demonstrates the app while also functioning as the hero transition system.
- Keep complex storytelling orderly underneath: a stable 5/8-column grid, `16px`/`20px` gaps, and repeated full-height sections allow varied video and card content without losing rhythm.
- Scale display type through em-based role tokens over a fluid page font size, preserving hierarchy across breakpoints without hard-coding every component in pixels.

## Avoid (1-2 bullets)
- Do not copy the neon-green field without the sparse monochrome system and generous full-viewport composition; used as a routine accent everywhere, it would become noisy and lose its signal.
- Do not reproduce the masked-video hero without performance fallbacks: the source includes poster imagery, WebM/MP4 sources, and a no-animation state, so a video-only imitation would be fragile.
