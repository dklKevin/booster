# flighty (flighty.com, extracted 2026-08-07)
status: full-css

- Neutrals: #FFF page/card ground, #000 primary ink, #FAFAFA soft feature cards, and #05010D dark product field; dark-section fades step from #05010D00 to #05010D.
- Accents: #0085FF marks app toggles/active controls; #6100FF emphasizes Passport statistics; #08A85B marks friends/social benefits; #F7BE00 is the active Preflight stage.
- Type: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, "Fira Sans", "Droid Sans", "Helvetica Neue", sans-serif, "System Default", sans-serif; 65px/1.1 H1, 56px/56px H2 collapsing to 32px/1.3, 22px/1.5 lead, 15px/1.5 body, 13px semibold labels; weights 500/600/700.
- Space: 24px outer gutter around a 1000px shell, 680px reading measure; recurring 10/16/20/24/32/48px gaps, 120px 24px 80px feature-section padding, and 12/16/20px card radii with 999px pills; breakpoints at 790px and 1200px.
- Motion: none found in CSS; Framer runtime motion is present, but durations/easings are unverified.
- Structure: white and #05010D full-width story bands wrap a 1000px product shell; the homepage centers an 80vh sticky phone at top:20vh, while About narrows to a 638px manifesto and Pricing expands to an 800px feature table.
- Signature: a sticky phone mockup is wired to 1px scroll triggers and a black pill-shaped stage rail, swapping the app state mechanically through “Preflight,” “At the airport,” and “After landing” while notification cards orbit the device.

Avoid: Copying only the rounded screenshots and Apple-like system type yields generic app marketing; the character depends on synchronized trip-stage storytelling and credible flight telemetry. Do not invent motion timing from Framer defaults.
