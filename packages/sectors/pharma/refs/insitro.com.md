# https://www.insitro.com (sector: pharma, sweep: excellence, fetched 2026-08-06)
status: full-css

## Token block (~10 lines)
- Palette / foundation: #232e4f body and navigation background; #ffffff default body text.
- Palette / depth: #010b1c for dark overlays and translucent panels; #191e46 for glass-panel gradients and dark text states.
- Palette / action: #ffef00 primary pill-button fill and key rules; #00d9ea links, active borders, arrows, and hexagons; #1d78da blue panels and gradient endpoint.
- Type pairing: Tiempos Headline Regular/Medium for h1-h6; TT Commons Regular/Medium/Semibold for body, controls, and eyebrows; each self-hosted as WOFF2 with sans-serif fallback.
- Desktop display scale: h1 80px/1.1, h2 64px/1.1, h3 46px/1.1, h4 34px/1.1, h5 30px/1.1, h6 22px/1.1.
- Responsive display scale: at <=1024px, 60/50/40/28/26/18px; at <=767px, 40/40/30/24/22/16px.
- Body/control scale: body 18px/1.2; larger copy 22px; scroll cue 16px; buttons 18px with .04em tracking; uppercase eyebrow uses 1.8px tracking.
- Spacing rhythm: modules 85px vertical desktop, 60px at <=1024px, 40px at <=767px; recurring content gaps are 20, 25, 30, and 40px.
- Layout intent: centered 95%-wide, 1130px base container; 1320px large container; x-large is 90%/1700px, becoming 95%/1320px below 1440px.
- Signature element: staggered, overlapping hexagonal image/text clusters using polygon(50% 0,100% 25%,100% 75%,50% 100%,0 75%,0 25%), cyan/yellow/blue gradients, and offset rows with negative margins.

## Lessons (3-5 bullets)
- Make scientific complexity feel ownable by repeating one geometry across culture imagery, value tiles, page callouts, and interactive explainers; here the hexagon becomes a system rather than a one-off decoration.
- Pair a restrained midnight field (#232e4f) with narrowly assigned high-energy signals: yellow for primary action, cyan for links/active states, and blue for content panels.
- Preserve editorial authority with Tiempos display faces while keeping dense scientific copy and controls in TT Commons; the explicit 80-to-22px heading ladder makes the pairing systematic.
- Use a stable centered content rail (1130px) and selectively widen visual/data modules to 1280-1320px, so immersive science graphics do not loosen ordinary reading measure.
- Scale section breathing room deliberately from 85px to 60px to 40px, while retaining smaller 20-40px internal gaps, instead of compressing every spacing value equally on mobile.

## Avoid (1-2 bullets)
- Do not copy the hexagon clipping and staggered negative margins without the site's responsive width/padding overrides; the desktop clusters switch to column layouts and substantially larger percentage widths below 1023px.
- Do not spread #ffef00 and #00d9ea across every surface: the source reserves them for actions, active states, rules, arrows, and signature geometry against the dark foundation.
