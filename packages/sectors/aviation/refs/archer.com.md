# https://archer.com (sector: aviation, sweep: excellence, fetched 2026-08-06)
status: full-css

## Token block (~10 lines)
- Core palette: #000000 page/media ground; #FFFFFF primary text, rules, and inverse controls.
- Supporting palette: #1A1B21 “Archer ink” surfaces; #A9A9A980 muted text/rules (50% alpha).
- Display face: "MBF Ligione Expanded", sans-serif; weights 200/400/700/900; uppercase with 1-5.6px tracking and `'salt'` alternates.
- Body face: "Archivo Narrow", sans-serif; weights 400/500/600/700; body token clamp(14px, 1.19vw, 20px), with product-page copy at 18px/1.5.
- Utility face: "Chakra Petch", sans-serif; weights 400/700; uppercase technical labels at 9-14px with 0.8-2px tracking.
- Display scale: hero clamp(15px, 5vw, 37px); section headings clamp(24px, 5vw, 44px); News H1 31px mobile / 62px desktop, line-height 1.
- Spacing rhythm: 4px base (`--spacing: .25rem`); repeated 16/24/32px gaps and 96px mobile / 128px desktop section padding.
- Content geometry: interior gutters 10% mobile / 64px desktop; heading measure 700px and copy measure 460px; wide footer shell max-width 1682px.
- Layout intent: full-bleed media alternates with asymmetric two-column heading/copy bands and responsive one-to-two-column grids.
- Hero frame: 960:1920 mobile and 1280:878 desktop, capped at 100svh; imagery/video stays edge-to-edge with object-fit: cover.
- Signature element: autoplay aircraft video under expanded all-caps type, completed by a 28-tick animated instrument-like divider and blur-to-sharp letter reveal.

## Lessons (3-5 bullets)
- Treat the aircraft as the primary interface: reserve the full viewport for motion, then keep the message to one compact, highly tracked display lockup.
- Separate brand voice by function: expanded Ligione for aspiration, narrow Archivo for readable explanation, and Chakra Petch for cockpit-like labels and data.
- Make technical precision a repeatable motif through fine rules, dense tick marks, tabular numerals, restrained uppercase labels, and measured tracking - not decorative “futurism.”
- Keep long product narratives legible by pairing a 700px heading column with a 460px copy column, then returning to full-bleed demonstrations and scrub/route interactions.
- Use a strict monochrome foundation so route-specific photography, video, maps, and restrained steel/sky accents carry the product story without fragmenting the system.

## Avoid (1-2 bullets)
- Do not copy the very wide uppercase face for paragraphs or dense UI; the source confines it to short display lines and uses Archivo Narrow for sustained reading.
- Do not reproduce the cinematic treatment without optimized mobile/desktop video variants and constrained hero aspect ratios; otherwise the signature becomes slow, cropped, and content-poor.
