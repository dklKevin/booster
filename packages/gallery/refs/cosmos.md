# Cosmos (cosmos.so, extracted 2026-08-06)

- Canvas: warm paper #f9f7f3, text #0d0d0d; not dark-first, the imagery supplies all color. Neutral ramp near-zero-chroma but warm (#fcfbfa to #0d0d0d, off-neutral under 1.5 Lab units); secondary text #6e6a69.
- Panel backgrounds sampled from the artwork inside them (#d1543e, #eac7a0, #a4a38f), never from the neutral palette, re-tinting on content swap with a .5s ease.
- Type: one custom face; display at weight 350 (74px/1.0/-0.05em) so the largest type is also the least heavy; tracking always negative, tightening as size grows; body clamped to 330-520px.
- Spacing: 4px base; one idea per 120-300px band; content max 1300px.
- Chrome is one shape and one material: full-round glass pill (backdrop-blur over media, inset top highlight off media); the header has no edge at all, just a 168px paper-color gradient content dissolves through.
- Motion: blur-to-sharp at three scales (6px word blur, 20px canvas blur, images sliding into composition); ease cubic-bezier(.22,1,.36,1).
- Signature: radial mask punching the image field to zero exactly where the headline lands; type on untouched paper at full contrast while photography fills every edge.

Avoid: the whole landing renders via JS from opacity 0 (no-JS sees nothing); don't inherit that trade without a fallback.

Note: this site uses techniques our ban list forbids (frosted glass / blur chrome). Documented for range; learn the thinking, never the banned material.
