# https://www.blender.org (sector: opensource, sweep: excellence, fetched 2026-08-06)
status: full-css

## Token block (~10 lines)
- Palette — content canvas `#f2f2f3`, raised surface `#fafafa`, secondary surface `#eaebeb`, tertiary/border surface `#e2e3e4`.
- Palette — body ink `#4c4d52`, stronger ink `#424348`, secondary ink `#8d8e96`, tertiary ink `#b2b3b8`.
- Palette — interaction accent `#0099ff`; global-nav background `#1c1e22`, nav control background `#292d32`, nav text `#d2d6da`.
- Palette — homepage editorial accents include mint `#46ebc2`, blue `#0066ff`, and violet `#9300ff`.
- Type pairing — body/display: `Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Oxygen, Ubuntu, Cantarell, "Open Sans", Arial, sans-serif`; mono: `ui-monospace, Menlo, Monaco, "Cascadia Mono", "Segoe UI Mono", "Roboto Mono", "Oxygen Mono", "Ubuntu Monospace", "Source Code Pro", "Fira Mono", "Droid Sans Mono", "Courier New", monospace`.
- Type scale — mobile `10/12/14/21px` (xs/sm/base/lg), `28/24/21/18/16/14px` (h1–h6), hero `36px`; ≥900px base `16px`, h1/h2 `32/28px`, hero `55px`; ≥1220px base `18px`, hero `72px`.
- Type weights — regular `400`, bold `600`, large feature/hero title `800`; desktop base line-height `28px`.
- Spacing rhythm — `16px` base with `4, 8, 16, 24, 48, 96, 192px` steps; radii `6px` and `12px`.
- Layout intent — centered responsive containers at `820/940/1170/1320/1600px`, `16px` side padding, CSS-grid cards with `16px` column and `24px` row gaps, plus alternating two-column feature rows that stack below `900px`.
- Signature element — a full-width artwork hero, `480–640px` tall on the homepage, carrying an `800`-weight `36–72px` title over a `25deg` black-to-transparent gradient and frosted translucent CTAs.

## Lessons (3-5 bullets)
- Let project output do the persuasion: place community artwork edge-to-edge in the hero, then use a directional gradient to preserve legibility without flattening the image.
- Give one shared responsive type system to editorial headlines, release messaging, cards, and feature pages; reserve the `800` weight and hero scale for the few statements that define the project.
- Support a broad open-source ecosystem with repeatable content machinery: auto-fit card grids, fixed thumbnail ratios, and transparent cards let news, development, and studio work coexist without visual noise.
- Alternate text and imagery on deep feature pages, with generous `80px` vertical padding and subtle `1.02` image hover scaling, to turn a long capability list into a paced product tour.
- Pair a neutral light reading canvas with a persistent dark global navigation and one consistent blue interaction color, leaving brighter colors to individual stories and community work.

## Avoid (1-2 bullets)
- Do not copy the oversized art hero without art-direction controls: Blender explicitly shifts background position at `980px` and balances the text; generic center-cropping would obscure either subject or message.
- Do not apply every display treatment at once; the colored massive headings, artwork, gradients, translucent buttons, and image scaling work because ordinary content remains neutral and structurally repetitive.
