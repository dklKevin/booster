# Pagani (pagani.com, extracted 2026-08-06, deep pass)

- Purely achromatic: black ground, white ink at 100%/50%, #cdcdcd pull quotes, near-black hairlines (#191919/#151515); no gold, no serif. One family: Istok Web sans.
- The maximalism is temporal, not visual: 1.5s panel transitions, 2s veil fades (each panel resolves out of its own ground color), backgrounds perpetually scaling 1 to 1.1. Nothing ever cuts; no image is ever motionless.
- Tracking carries the identity a display face normally would: .2em section headings, .1em h1, 1.3px justified 13px body. Survives any fallback.
- The type scale has a hole: intimate 10-36px or monumental ~24vw at line-height .8; nothing between, so big moments land as events.
- Ornament rule: large or opaque, never both (149px quote marks at opacity .15); everything else is 1px hairlines. The founder's handwritten signature appears once per page: scarcity makes it authorship, not branding.
- Two grounds encode content modes: black = cinematic spectacle (full-viewport, centered), white = documentary craft (two justified 13px columns, 1px rules).
- Signature: left-edge chapter rail; fixed 1px vertical rule, zero-padded numerals, labels revealed as items expand 55px to 180px on hover.
- When content is all photography, move the craft into navigation chrome: counters, arrow sprites, rail detailing.

Avoid: their font-weight:100 is a lie (thin face never loads; airiness is tracking + size, not weight). prefers-reduced-motion appears zero times and focus styling is stripped: our floors override. The slow one-panel pacing only works when there is nothing to browse.
