# https://www.stjude.org (sector: hospital, sweep: excellence, fetched 2026-08-06)
status: wayback

## Token block (~10 lines)
- Core palette: St. Jude red #d11947 (global red/link hover), deep red #8d0034, blue #135cb0 (global links), dark blue #00437b, teal #17818f.
- Neutral palette: text #1a1a1a, dark gray #474c55, utility gray #63666b, borders #e6e6e6, pale surfaces #f5f5f5/#f5f6f5, white #fff.
- Supporting accents: yellow #ffc32c (yellow-link hover/CCAM), green #c4d82e, violet #712d91, light blue #7ad0e4; focus #569ced99.
- Type family: "SJ Sans", "Open Sans", "Helvetica Neue", "Helvetica", "Arial", "sans-serif"; archived interior bundles include SJ Sans files at weights 300, 400, 600, 700, and 800.
- Display scale: 4.21875rem/4.5rem, 3.375rem/3.9375rem, 2.25rem/3.375rem, 1.875rem/2.8125rem, 1.5rem/2.25rem (font-size/line-height).
- Reading/UI scale: 1.25rem/2rem, 1rem/1.6875rem, .83333rem/1.40625rem, .66667rem/1.125rem, .44444rem/.6875rem; base is 16px/1.5.
- Spacing tokens: 2, 4, 8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112px; homepage critical CSS also repeats .5625rem, 1.125rem, and 2.25rem.
- Shape and motion: 8px global radius, .25s global transition; cards use a three-layer 0 2px/1px/3px shadow and lift to a 0 4px/1px/2px shadow on hover.
- Layout intent: 12-column AEM grids; at 1180px+, primary content is capped at 60%, broad page rows are 90% wide up to 90rem, and at 2000px+ prose caps at 61rem while images can reach 105rem.
- Signature element: a 16:7 photographic homepage hero with the two-part “Finding cures. Saving children.” tagline in a translucent white panel, followed by a full-width four-column gray action rail for referral, research, donation, and related links.

## Lessons (3-5 bullets)
- Put the hospital’s three highest-intent routes directly beneath the emotional hero: the source pairs “Refer a Patient,” “Explore Our Research,” and “Donate Now” in one action rail instead of forcing each audience back through navigation.
- Separate expressive and reading widths: full-bleed/105rem imagery carries human impact, while the 60%/61rem text measure keeps clinical and research content scannable.
- Use one institutional type family across patient-care and research subsites, then create hierarchy through a wide, explicit size/weight scale rather than introducing unrelated display faces.
- Preserve a small semantic core—red for brand/action, blue for links, near-black for text—while reserving the larger accent palette for tagged campaigns and differentiated content modules.
- Let section templates vary by audience while retaining tokens: the fetched research page uses an animated hero carousel and 12-column grid, while treatment uses an overlaid hero and responsive Bootstrap-style columns.

## Avoid (1-2 bullets)
- Do not treat all 15 extracted swatches as equal brand colors; copying the whole accent set without the source’s role constraints would weaken the red/blue hierarchy.
- Do not copy the desktop hero’s absolute positioning and negative overlap without its mobile rules; below 900px the source deliberately returns the caption to normal flow and stacks the hero actions.
