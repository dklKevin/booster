# https://www.ginkgo.bio (sector: biosecurity, sweep: excellence, fetched 2026-08-06)
status: full-css

## Token block (~10 lines)
- Palette - Ginkgo navy `#0b1f30`: default text and secondary-button background.
- Palette - soft white `#fcfcfc`: page/section background and dark-mode text.
- Palette - soft black `#141414`: dark sections; translucent rules use `#14141426` and `#1414144d`.
- Palette - Ginkgo green `#056b39`: named brand token; amber `#ffedde`: warm gradient-section ground fading to `#ffedde66`.
- Type pairing - display: Recoleta 400/500 with `Palatino Linotype, sans-serif`; interface/body: Ag 400/500/600 with `Arial, sans-serif`; Calluna/Georgia and IBM Plex Mono are supporting editorial/data faces.
- Type scale - 1rem body; H4 `1.25em`, H3 `1.56em`, H2 `2em`, `.h2-size` `3.25em`, H1 `4.5em` (computed 72px at the inspected desktop viewport), jumbo `5.25em`; H1 line-height `.95` and tracking `-.015em`.
- Reading measure - H1 max `20ch`; large copy `1.25em/1.52` capped at `64ch`; standard content cells cap at `40em`, hero copy at `48em`.
- Spacing rhythm - em-based: recurring gaps `1.25em`, `2.5em`, and `4em`; standard sections `7.5em` vertical, medium sections `4em`; desktop section divider margins `2em 0 2.25em`.
- Layout intent - centered `88%` container, with content capped locally (`70em` bordered inner frame); primary compositions use two-column flex/grid, 1px translucent rules, and full-bleed or circular-cropped lab photography.
- Responsive system - at ≤767px the container becomes full width with `1.5em` side padding and sections reduce to `3.75em`; at ≤479px side padding is `1.25em` and `.h1-size` is `2.4em`.
- Signature element - a hand-drawn repeating squiggle SVG (`124px × 10px` tile in a `21px`-high strip) animates open on CTAs and reappears as a divider, adding organic motion to the rigorous grid.

## Lessons (3-5 bullets)
- Pair an expressive biological-feeling serif with a restrained sans interface: Recoleta supplies ambition while Ag keeps technical explanations and navigation credible.
- Let evidence-heavy pages inherit one stable frame - 88% container, 7.5em section cadence, fine rules - then vary only the hero from immersive photography to compact content grids.
- Keep scientific copy readable by enforcing character measures (`20ch` headlines, `64ch` large copy) instead of merely shrinking type inside wide layouts.
- Use a single organic micro-motif - the animated squiggle - across links and dividers; repetition creates identity without turning every biotech element into literal cells or DNA.
- Reserve the near-black section and high-contrast full-bleed imagery for major narrative turns, while most information sits on `#fcfcfc` for clarity.

## Avoid (1-2 bullets)
- Do not copy the `4.5em`/`.95` display treatment without the `20ch` cap and responsive reductions; long scientific titles will collide or become tiring.
- Do not layer the translucent borders, blurred cards, dark photo overlays, and squiggles everywhere; their hierarchy depends on a mostly quiet soft-white field.
