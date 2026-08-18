# https://boomsupersonic.com (sector: aviation, sweep: excellence, fetched 2026-08-06)
status: full-css

## Token block (~10 lines)
- Core palette: page background #000000; foreground #FFFFFF.
- Brand/accent palette: Boom yellow #FFF555 for labels, links, focus rings, badges, and selected controls; yellow hover #FFE02A.
- Supporting palette: mid-gray #88898A for secondary/footer text; border #212427; dark-gray surface #1A1A1A.
- Type family: "Styrene A", "Inter", system-ui, -apple-system, sans-serif; supplied Styrene A weights 400, 500, 700.
- Desktop type scale: h1 72px/1.25/700; h2 48px/1.15/700; h3 48px/1.15/500; h4 32px/1.2/500; h5 24px/1.3/500; body 20px/1.5.
- Responsive type: below 1440px h1 48px and h2/h3 30px; below 768px h1 30px, h2/h3/h4 24px, h5 20px, body 16px.
- Utility scale: 12, 14, 16, 18, 20, 24, 30, 36, 48px; uppercase eyebrow labels are 13px with 0.12em tracking; buttons are 15px.
- Spacing rhythm: 4px base unit; common gaps/padding use 8, 12, 16, 24, 32, 48, and 64px; content-section vertical padding is clamp(80px, 10vw, 140px).
- Layout intent: edge-to-edge black canvas and full-viewport media panels (100dvh, minimum 600px; 500px mobile) inside responsive horizontal gutters of 96px desktop, 48px below 1440px, and 24px below 768px; containers cap at 1536px.
- Signature element: a cinematic sequence of screen-height aircraft/engine image or video panels, dark gradient-overlaid and paired with a yellow technical eyebrow, large white title, restrained copy, and one compact CTA.

## Lessons (3-5 bullets)
- Let high-quality aviation imagery carry the hierarchy: keep each major program to one viewport, one technical category label, one headline, and one action instead of layering on dashboard-like chrome.
- Pair cinematic storytelling with engineering precision: 13px uppercase yellow labels and explicit program categories make dramatic imagery feel factual and navigable.
- Scale gutters as decisively as headlines - 96/48/24px preserves strong edge alignment without crowding either wide displays or phones.
- Use a narrowly controlled monochrome system, then reserve one high-visibility accent (#FFF555) for taxonomy, interaction, and focus states so the visual language stays coherent.
- Keep detail and editorial pages on the same tokens and clamp(80px, 10vw, 140px) section cadence; structural variety does not require a second visual system.

## Avoid (1-2 bullets)
- Do not copy the repeated 100dvh panel pattern without equally strong, consistently art-directed media; weak imagery would turn the homepage into a slow, oversized carousel.
- Do not use #FFF555 broadly as decoration: its impact here depends on a predominantly #000000/#FFFFFF field and tightly limited roles.
