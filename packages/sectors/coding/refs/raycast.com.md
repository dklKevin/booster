# https://www.raycast.com (sector: coding, sweep: excellence, fetched 2026-08-06)
status: full-css

## Token block (~10 lines)
- Canvas and text: #07080a page background; #ffffff primary text.
- Surface ladder: #111214 raised card, #0c0d0f recessed card, #1b1c1e control/secondary surface, #2f3031 stronger control surface.
- Muted text ladder: #9c9c9d default muted, #6a6b6c quieter copy, #434345 faint/inactive.
- Accents: #ff6363 red, #56c2ff blue; the Teams interior page adds #ff9217 orange.
- Primary type: Inter, Inter Fallback, sans-serif; body enables liga, calt, kern, and ss03.
- Monospace pairing: JetBrains Mono, JetBrains Mono Fallback, Menlo, Monaco, Courier, monospace; GeistMono is also loaded for code/utility UI.
- Homepage type scale: 14px nav/button, 14→18px hero copy, 36→48→64px hero h1 at 420px/720px breakpoints; section title pairs use 18→20px, with large h2 at 20→32px.
- Spacing rhythm: 4, 8, 12, 16, 20, 24, 32, 40, 48, 56, 64, 80, 96, 112, 168, 224px; grid gap is 24px below 720px and 32px above.
- Geometry: radii 4, 6, 8, 12, 16, 20, 24px; standard buttons are 36px minimum height with 8px × 12px padding.
- Layout intent: centered 746/1064/1204/1280px container tiers, 1204px primary content width, responsive one-to-two-column grids, and deliberately deep hero spacing (260→370px top padding on home).
- Signature element: product-accurate Raycast command windows (750×475px) nested inside translucent, blurred dark frames with hairline white borders, inset highlights, and soft radial glows.

## Lessons (3-5 bullets)
- Let the product UI carry the visual identity: Raycast reuses its command window, list rows, action bar, hotkeys, and search interactions as the main storytelling medium instead of surrounding screenshots with unrelated decoration.
- Build depth from a very narrow neutral ramp (#07080a, #0c0d0f, #111214, #1b1c1e), then separate layers with blur, 6%-white borders, and inset highlights rather than large color shifts.
- Keep dense interface chrome compact (12–16px) while giving the marketing promise a sharp scale jump to 64px; this preserves a technical feel without weakening hierarchy.
- Use a fixed spacing vocabulary even for cinematic compositions: the same 4/8px-derived tokens drive controls, cards, reels, navigation, and large 96–224px section intervals.
- Preserve a shared container system while letting interior pages change their hero expression: Store uses an 80px title and search-led entry, while Teams uses a 72px gradient title and orbital icon field.

## Avoid (1-2 bullets)
- Copying the glass-and-glow treatment without the tight neutral palette and hairline borders would turn the restrained depth system into generic “glassmorphism.”
- Reusing the 168–224px gaps and 260–370px hero padding on content-heavy pages would bury information; these values work here because the product demonstrations are the content.
