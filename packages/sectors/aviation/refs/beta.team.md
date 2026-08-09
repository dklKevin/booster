# https://www.beta.team (sector: aviation, sweep: excellence, fetched 2026-08-06)
status: full-css

## Token block (~10 lines)
- Palette / primary surfaces: #FFFFFF page, card, nav, and light-button background; #27272A primary text, dark buttons, menus, and icons; #09090B high-contrast button text.
- Palette / secondary neutrals: #52525C secondary text and button hover; #9F9FA9 tertiary labels; #E4E4E7 dividers and borders; #D4D4D8 inactive indicators; #FAFAFA and #F4F4F5 soft panels.
- Palette / telemetry states: #22C55E in-flight status dot, #00A6A0 focus outline; errors and popup close use #E01F3A.
- Type pairing: Titillium Web, "sans-serif" for body, headings, navigation, and controls; JetBrains Mono, monospace for the flight-mile telemetry panel.
- Core scale: body 16px/24px (14px on <=767px); h1 and h2 40px at 1.2 line-height (32px on <=767px); full-bleed/hero copy 18px/28px (16px mobile).
- Display and UI scale: comparison heading 70px desktop, 50px at <=1360px, 40px mobile; nav/buttons 14px with 1px tracking; telemetry 10-12px.
- Controls: uppercase 14px CTAs, 15px 20px padding, 4px radius, 150-180px minimum width; light hero CTAs scale to 1.1 on hover.
- Spacing rhythm: 20px mobile/component gutter, 80px desktop full-bleed gutter; recurring 20/40/50/80/100/120px steps, including 100px section padding and hero copy anchored 120px from bottom (40px mobile).
- Width system: 700px text measure, 1200px primary content container, 1600px wide container, 1920px component ceiling.
- Layout intent: alternate 80-100vh image/film fields with restrained 1200px content modules; place short white copy low-left over a 45deg black-to-transparent gradient.
- Signature element: fixed bottom-right 220px “NM Flown” telemetry capsule, rounded 120px 0 0 0, expandable into live JetBrains Mono flight equivalents and airport/route/country statistics.

## Lessons (3-5 bullets)
- Make operating evidence persistent: the expandable mileage instrument turns fleet activity into a compact proof point without interrupting the primary story.
- Let aviation imagery carry scale, then protect legibility with a directional gradient and a strict 600px copy limit rather than covering the scene with a large opaque panel.
- Separate cinematic storytelling from technical comparison: full-viewport mission scenes lead into a 1200px configuration matrix with aligned 100px gaps and fine #E4E4E7 rules.
- Use the same spatial anchors across formats: 80px desktop/20px mobile gutters and 120px/40px bottom offsets keep full-screen heroes, full-bleed modules, and interior aircraft pages visually related.
- Shift editorial stories to a contained-image hero plus narrow rich-text flow while retaining the same type and neutral palette; the source uses a different blog-post structure rather than forcing the marketing-page template.

## Avoid (1-2 bullets)
- Do not copy only the full-screen aircraft photography; without the live telemetry device and configuration data, the result loses the site's distinctive evidence-led character.
- Do not preserve 80-100vh imagery and 70px display type unchanged on small screens; the source explicitly reduces heroes to 70vh in one variant, gutters to 20px, copy width to 300px, and headings to 32-40px.
