# https://zed.dev (sector: coding, sweep: excellence, fetched 2026-08-06)
status: full-css

## Token block (~10 lines)
- Surfaces: light body tint `#d1cfc8` at 20%, light nav `#f5f4f3`; dark body `#111216`, dark nav `#121316`.
- Text: light body `#727a89`, high contrast `#000000`; dark body `#aaa599`, high contrast `#ffffff`.
- Accent and rules: light accent/title `#1348dc`, dark accent/title `#90c5ff`; light default rule `#dadde2`.
- Type pairing: iA Writer Quattro S for body (`"iA Writer Quattro S", sans-serif` in docs; loaded as `writer` with Arial fallback on the homepage) and IBM Plex Serif for display (`"IBM Plex Serif", "Helvetica Neue", Helvetica, Arial, sans-serif` in docs; variable 300–700 on the homepage).
- Code/UI type: Lilex (`"Lilex", ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, Courier New, monospace`), loaded as `zedMono`; uppercase subheaders are 11px with 0.05em tracking.
- Display scale: h0 `clamp(41.6px, 32px + 2.5vw, 48px)`, h1 `clamp(27.2px, 24px + 1.85vw, 32px)`, h2 `clamp(22.4px, 24px + 1.55vw, 25.6px)`; body scale 12/14/16/18/20/24/30/48/60px.
- Spacing rhythm: 4px base token; repeated gaps and padding resolve especially to 16, 24, 32, and 48px.
- Widths: homepage `.container-max-w` is 1080px, with responsive minimums 680px at 768, 920px at 1024, and 1120px at 1280; docs use a 690px reading column, 280px sidebar, and 15px page padding.
- Layout intent: full-width stacked sections hold a centered content rail, then switch feature content among 1-, 3-, 4-, 6-, and 12-column grids while persistent borders align sections into one page-wide scaffold.
- Signature element: a working-editor/terminal-style hero framed by fine ruled rails and 6px rotated-square node markers at section intersections, making the marketing page feel like a precise developer tool canvas.

## Lessons (3-5 bullets)
- Pair an editorial serif headline with a practical writing face and a real coding mono; the three roles make product narrative, interface copy, and code immediately distinguishable.
- Carry the editor metaphor into structure, not decoration alone: aligned rules, intersection nodes, monospace labels, and the hero UI all speak the same product language.
- Keep the palette quiet enough for dense interface demonstrations: warm near-neutral surfaces and gray copy leave the single blue accent to organize titles, links, and actions.
- Let marketing and documentation diverge where their jobs differ: the homepage uses broad modular grids, while docs constrain prose to 690px beside a fixed 280px navigation rail.

## Avoid (1-2 bullets)
- Do not copy the many fine rules and tiny 11px labels without the same strict alignment and contrast handling; small drift would turn the deliberate tool-like scaffold into visual noise.
- Do not treat the embedded editor UI as generic ornament: without accurate code typography, states, and responsive clipping, the most product-specific element would read as a fake dashboard.
