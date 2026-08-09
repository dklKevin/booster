# https://astro.build (sector: opensource, sweep: excellence, fetched 2026-08-06)
status: full-css

## Token block (~10 lines)
- Canvas/surfaces: `#060913` page background; `#0c0f19` raised dark; `#17191e` and `#23262d` cards/code; `#343841` stronger surface.
- Text: `#f2f6fa` primary, `#bfc1c9` secondary, `#858b98` muted; white `#ffffff` for highest emphasis.
- Borders/focus: `#858b9833` subtle 20% gray border, `#545864` stronger border, `#e8c4f9` focus outline.
- Brand accents: blue `#3245ff` to purple `#b845ed` at 83.21deg; supporting green `#4af2c8`, red `#d83333`, pink `#f041ff`, yellow `#f8e42e`, orange `#ff7d54`.
- Heading family: `Obviously, obviously-fallback, system-ui, sans-serif`; variable weights 290/380/475 and display scale 24/36/48px at 1.25 line-height.
- Body family: `Inter, inter-fallback, system-ui, sans-serif`; 16px/24px body and 18px/1.5 large body, with 300 and 200 weights.
- Mono family: `MDIO, md-io-fallback, monospace`; homepage command text is 14px/20px; code-frame default is 13.6px at 1.65.
- Utility type scale: 12/14/16/18/20/24/30/36/48px; homepage hero steps 30px → 36px at 768px → 48px at 1280px, line-height 1.1.
- Spacing rhythm: 4px-derived utilities, commonly 8/16/24/32/40/48px; section rows expand 96px → 128px → 160px at 768/1024px.
- Layout intent: centered 1280px container with 16px gutters (32px from 768px), plus a three-column bleed grid using 24px gutters and full/start/end escape routes.
- Signature element: deep-space surfaces lit by oversized blurred hero art and masked “stardust”/dot-grid glows, consistently anchored by the `#3245ff` → `#b845ed` gradient.

## Lessons (3-5 bullets)
- Pair an expressive variable display face with a quiet UI sans and a purpose-built mono; the three roles make marketing, navigation, and code samples distinct without changing the overall voice.
- Let one central content rail support explicit full-, start-, and end-bleed variants; this keeps dense documentation-like sections aligned while allowing launch moments to feel expansive.
- Use the brand gradient as a controlled illumination system—CTA fill, clipped text, radial glow, and hover energy—against near-black neutral surfaces instead of coloring every component.
- Make code executable-looking at the top of the funnel: the hero places a copyable `npm create astro@latest` command directly under the primary CTA.
- Scale macro spacing more aggressively than card spacing: 96/128/160px section rhythm creates narrative chapters while components stay on compact 8–48px intervals.

## Avoid (1-2 bullets)
- Copying the many glows, blur layers, masks, and animated hover states without the restrained dark palette would turn depth cues into visual noise and reduce text contrast.
- Do not reuse the unusually light body weights (200–300) without the supplied Inter variable font and high-contrast background; fallback rendering may become too fragile.
