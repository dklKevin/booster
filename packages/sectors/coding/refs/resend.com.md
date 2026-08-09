# https://resend.com (sector: coding, sweep: excellence, fetched 2026-08-06)
status: full-css

## Token block (~10 lines)
- Palette / dark ground: background `#000000`; raised neutral `#141517`; canvas overlay `#14151799`.
- Palette / dark text: primary `#f0f0f0`; secondary `#a1a4a5`; translucent secondary `#fdfeffa6`.
- Palette / dark structure and accents: subtle line `#b0c7d925`; blue `#3080ff`; cyan `#00d1c6`; amber `#e9ac48`; purple `#611c98`.
- Type pairing: Inter for body/UI; ABC Favorit for display; Domaine for editorial hero statements; Commit Mono for code.
- Font stacks: `Inter, ui-sans-serif, system-ui, sans-serif`; `Commit Mono, ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace`.
- Type scale in use: hero `64px` to `96px` at `100%` line-height; section display `48px` to `56px` at `120%`; body `16px` to `18px`; UI `14px`; micro `12px`.
- Spacing rhythm: `4px` base unit; recurring `16/32/48px` gaps, `24px` horizontal page padding, and `48px` to `96px` section padding.
- Shape: `8/12/16/24px` radii are defined and used; primary buttons use `16px` radius with `40px` or `48px` heights.
- Layout intent: centered single-column sections at `1024px`, expanding to `1280px` on medium screens, with 2/3/6-column responsive grids and dense product UI nested inside generous vertical whitespace.
- Signature element: a black cinematic hero combines a Domaine `64px`/`96px` headline filled by a `#ffffff` to `#ffffff80` diagonal gradient with `/static/landing-page/bg-hero-1.jpg` and `/static/cube.mp4` product imagery.

## Lessons (3-5 bullets)
- Separate prose, product claims, and code by voice: Domaine makes the promise feel editorial, ABC Favorit structures feature headings, Inter handles controls, and Commit Mono makes implementation detail immediately legible.
- Let a strict `4px` spacing system support both extremes: compact code/product simulations can sit inside `48px` to `96px` section intervals without making the page feel mechanically uniform.
- Treat product proof as the page's visual content: the homepage repeatedly embeds dashboard, editor, analytics, and code interfaces inside the same `1024px`/`1280px` shell instead of switching to generic illustration.
- Build hierarchy inside a nearly monochrome dark palette with alpha steps (`#b0c7d925`, `#fdfeffa6`) and text gradients; reserve saturated blue/cyan/amber/purple for status and focused moments.
- Keep the widest display typography concise: the `96px` hero is paired with a roughly `480px` body-copy measure, preserving fast scanning before the product demonstrations begin.

## Avoid (1-2 bullets)
- Do not copy the black background, translucent borders, and oversized serif headline without equally polished product imagery; the restrained palette depends on the dashboard and cube assets for depth.
- Do not apply the `48px` to `96px` display scale to long technical copy; the source confines it to short promises and uses `14px` to `18px` sans/mono text for operational detail.
