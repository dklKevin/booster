# https://amie.so (sector: startup, sweep: excellence, fetched 2026-08-06)
status: full-css

## Token block (~10 lines)
- Canvas: #FAFAFA (`--color-background` / gray-50); raised product cards and secondary buttons: #FFFFFF.
- Text: primary #171717, secondary #5C5C5C, tertiary #A0A0A0; separators use #000000 at 4% opacity.
- Action palette: blue #11A8FF with hover #218FCD; white #FFFFFF button text.
- Accent palette: system accent red #FD2B38; homepage recording badge coral #FF6154; Amie pink token #F6A6A6.
- Primary type: Inter, Inter Fallback; CSS fallback stack continues ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, Noto Sans, sans-serif.
- Display/accent face available: Averia Serif Libre, Averia Serif Libre Fallback, weight 400; its visible homepage usage is unverified.
- Extracted scale: 12/1.32, 14/20, 16/25.6, 18/28, 20/28, 24/32, 30.8/36, 40/54, and 56/64px; the homepage hero progresses 28/36 → 30.8/36 → 40/54 → 56/64 across breakpoints.
- Tracking: large display styles use -0.0125em; compact headings use -0.025em; weights concentrate at 500, 600, and 700.
- Spacing rhythm: 4px base with frequent 8, 12, 16, 20, 24, and 32px gaps; 24px page gutters; major section separation reaches 64, 96, 128, and 192px.
- Layout intent: centered `max-w-5xl` (1024px) content rail with 24px gutters, narrower 672px copy, and responsive 2/3/4-column grids; showcased UI frames also use 900px and 972px caps.
- Signature element: animated, product-real interface tableaux inside white 12px-radius cards, using fine 4%-black dividers and layered “natural” shadows; source includes horizontal logo scrolling plus slide-up/slide-down UI states.

## Lessons (3-5 bullets)
- Let the product interface carry the visual argument: place detailed, near-real UI demonstrations in a quiet neutral rail instead of surrounding them with unrelated illustration.
- Use one vivid operational color (#11A8FF) for actions and reserve warm accents (#FF6154/#FD2B38) for recording or status cues, so color also explains product state.
- Keep marketing typography on the same compact scale as the product: 14–20px does most of the work, while only the hero and section statements expand to 40–56px.
- Make polish cumulative and low-contrast: 4%-black rules, 12px card radii, and multi-stop shadows create depth without breaking the desktop-app character.
- Hold navigation, hero, feature sequences, FAQ, and footer to the same 1024px rail, then narrow prose independently; this makes structurally different pages such as pricing and blog still feel related.

## Avoid (1-2 bullets)
- Do not copy the many animated product panels without comparable real UI detail; generic mockups would turn the strongest proof device into decoration and create unnecessary motion cost.
- Do not promote every extracted palette token to a marketing color: most are product-system utilities, while the homepage visibly depends on a much smaller neutral/blue/coral set.
