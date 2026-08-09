# walkerart (walkerart.org, extracted 2026-08-07)
status: full-css

- Neutrals: #FFFFFF ground with #000000 text and rules; homepage ticker overrides to #ffffff/#020202, while Walker Reader alone shifts the page and fixed header to pale pink #fff0ff.
- Accents: #0000FF marks functional/accessibility controls (skip link and carousel pause); #FFCC00 is reserved for high-intent conversion pills such as “Plan a Visit” and “Join Today,” always with #000000 text.
- Type: custom “ABC Walker”, “ABC Walker Fallback”, sans-serif; regular/italic 400 and medium 500. Base is 16px/24px; body content scales 18→20px at 1.5; masthead titles scale 32→72px, reaching 72px/1.0 at ≥1200px; weight stays mostly 400.
- Space: 6px root rhythm expressed as 6/12/24/48/96px; section spacing is 24px, 30px at 48em, 36px at 64em. Wrappers max at 1400px (contained blocks 1352px); large grids use 48px gutters. Images/panels stay square-cornered; action pills use 50px radii.
- Motion: links transition all 250ms ease-in-out; buttons 150ms ease-in-out; the fixed header/menu uses .4s cubic-bezier(0.16, 1, 0.3, 1). The full-width ticker translates linearly and pauses on hover; its duration is runtime-calculated, not fixed in CSS.
- Structure: A fixed 70/80/100px header tops a max-1400px flex-grid system; the home page alternates a contained 19:10 image masthead, half-width editorial pairs, full-width tickertape, and horizontal carousels, while detail pages center a large title over full-width media before narrower content.
- Signature: a three-column masthead locks the oversized WALKER wordmark dead center between navigation banks; immediately below, a square-cornered 19:10 artwork slide carries a centered white 72px title with date and discipline pinned to opposite bottom corners.

Avoid: Copying the black/white shell without the custom face, strict ruled grid, and strong commissioned imagery becomes generic. The over-image white titling and artwork-led color depend on photography with enough clean contrast; do not add blanket scrims or treat the WordPress preset palette as applied branding.
