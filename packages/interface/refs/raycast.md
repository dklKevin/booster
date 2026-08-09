# raycast (raycast.com, extracted 2026-08-07)
status: full-css

- Neutrals: dark-only ground #07080a; raised steps #0c0d0f and #111214; primary text #fff, secondary #9c9c9d, quiet #6a6b6c; muted nav text rises #9c9c9d -> #fff, while light buttons rise #e6e6e6 -> #fff.
- Accents: #FF6363 is the Raycast brand mark; #56c2ff is informational/selection color and #59D499 is success color inside the product demonstrations, not general page decoration.
- Type: Inter, "Inter Fallback", sans-serif; code/shortcut UI uses "JetBrains Mono", "JetBrains Mono Fallback", Menlo, Monaco, Courier, monospace. Hero scales 36/39.6 -> 48/52.8 at 420px -> 64/70.4 at 720px; article body is 16/25.6; weights stay 400/500/600.
- Space: 8px base with 4/8/12/16/20/24/32/40/48/56/64/80/96/112/168/224 tokens; radii 4/6/8/12/16/20/24px; grid gap 32px (24px at <=720px); containers 746/1064/1204/1280px.
- Motion: hero enters from translateY(20px) over 1s ease; nav is .2s ease-in-out, button color/shadow .2s with .1s press; extension cards enter .7s cubic-bezier(.215,.61,.355,1). Custom --spring-1 linear() peaks at 1.042827 at 40% and settles to .99965 at 100%; marquees pause under prefers-reduced-motion.
- Structure: centered max-width containers sit on a full dark canvas; 720px is the main reflow gate, with a deep hero, alternating product-demo bands, extension reels, and a 746px reading column for articles versus a 1204px store grid.
- Signature: a 1200px max-width WebGL canvas is absolutely inset behind the hero and edge-faded into #07080a, while later sections reproduce the Raycast launcher itself - search rows, command lists, live state, and keyboard-action footers - as the page's visual language.

Avoid: Copying only the black ground, soft gradients, and rounded cards becomes generic; the effect depends on proprietary canvas motion and unusually faithful product-UI choreography. The long hero spacing and low-contrast quiet text also need content density and contrast checks before reuse.
