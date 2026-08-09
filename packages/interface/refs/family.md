# family (family.co, extracted 2026-08-07)
status: full-css

- Neutrals: #FFFFFF page/card ground; #FBFAF9 beige panels and hover surface; #343433 headings, #494440 body, #848281 muted/focus, #F2F0ED rules; white cards step to #FBFAF9, pale buttons #F6F4EF to #EAE6DD.
- Accents: #3784F4 marks informational feature labels; #FF5310 marks warm actions/highlights; #44C67F, #7DC4FF, and #FFCF7B are illustration-only character colors rather than UI state.
- Type: custom "Family" 400/500/600 for display, then "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, "Apple Color Emoji", Arial, sans-serif for UI/body; hero 68px/1.1 at 500, section heads 44/48, body slots 19/27, 17/26, 15/22, 14/20, 13/18, mostly 400-600; hero drops to 44/48 at 580px and heads to 32/35 at 420px.
- Space: 4px-derived spacing with frequent 8/12/16/24/32px steps; 24px page gutters, 67rem main max-width and 48.75rem article width; 6/8/10/12px component radii, 32px pills; desktop sections use roughly 74-132px vertical padding.
- Motion: controls use 100ms ease, image hover 180ms ease, nav 200ms ease, media 220ms cubic-bezier(0.19,1,0.22,1); skeleton shimmer is 1200ms linear infinite and testimonial translation 120s linear infinite.
- Structure: sticky neutral header over a centered 67rem shell; large centered intro gives way to alternating two-column demos, three-column phone panels, a 3x2 asymmetric feature grid, sticky-copy/detail pairs, then a full-width testimonial conveyor; collapses at 920/880/768/720/580/420/410/390px.
- Signature: rounded #FBFAF9 product-demo modules reproduce miniature wallet screens and phone frames, capped by a playful ten-image emoji asset strip repeated three times as a continuous horizontal band.

Avoid: Copying the beige cards and emoji band without the dense, product-specific wallet micro-UI becomes generic playful fintech. The character palette depends on a nearly colorless shell and restrained 12px geometry; spreading those colors into general chrome removes the contrast that makes it work.
