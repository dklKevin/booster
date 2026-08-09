# https://www.cooley.com (sector: law, sweep: excellence, fetched 2026-08-06)
status: full-css

## Token block (~10 lines)
- Palette, primary red theme: maroon #33040e (dark ground/text), red #fd1434 (brand accent), accessible red #de0220 (small-text/link accent), rose #fff2f4 (light ground), white #fff (solid ground).
- Palette, alternate blue theme: navy #05046e (dark ground), royal #5a46ff (mid/accent and solid-page link/button fill), sky #e6eaff (light ground/button text).
- Display type: "GT-Sectra-Book", Garamond, "Times New Roman", serif for H1-H4; "GT-Sectra-Regular" with the same fallback for H5-H6; ss01 enabled.
- Body type: "ArialNova", Arial, Helvetica, sans-serif; supplied at weights 300, 400, and 700, with italic files.
- Heading scale: H1 clamp(4.25rem, 8.5vw, 8.75rem)/.9; H2 clamp(2.75rem, 5.5vw, 5.75rem)/1; H3 clamp(2.625rem, 5.25vw, 3.75rem)/1; H4 clamp(2rem, 4vw, 3rem)/1; H5 clamp(1.5rem, 3vw, 2.25rem)/1.1; H6 clamp(1.25rem, 2.5vw, 1.5rem)/1.1.
- Body scale: clamp(1.5rem, 3vw, 1.75rem), clamp(1.25rem, 2.5vw, 1.5rem), clamp(1rem, 2vw, 1.25rem), clamp(.875rem, 1.75vw, 1rem), clamp(.75rem, 1.5vw, .875rem); line heights 1.2-1.4.
- Spacing rhythm: .125, .25, .5, .75, 1, 1.5, 2, 3, 4, 6, 8, 16rem; responsive component padding clamp(4rem, 10vw, 8rem) and hero padding clamp(2rem, 10vw, 4rem).
- Layout intent: 4 columns with 1rem gutters below 800px, 12 columns with 2rem gutters from 800px; full-bleed sections wrap a named main grid and cap the live area at 1920px.
- Widths: homepage hero copy max-width min(1200px, 100%); secondary-hero copy max-width 100ch; editorial titles max-width clamp(600px, 100%, eight grid columns).
- Signature element: the full-viewport centered serif statement is surrounded by five independently positioned photo/video slots and an animated 100-180px “formations” mark cycling among branching, divide, network, ripple, and web motion sources.

## Lessons (3-5 bullets)
- Treat institutional authority as editorial scale rather than visual conservatism: the 4.25-8.75rem serif headline carries the page while Arial Nova keeps navigation, metadata, and long reading practical.
- Encode brand color as role-based theme tones; the same dark/mid/light/solid component logic swaps coherently between maroon/red/rose and navy/royal/sky families.
- Let a strict 12-column system support expressive composition: centered legal-service heroes, eight-column article titles, and asymmetric homepage media all resolve to the same gutters and 1920px ceiling.
- Use a single motion vocabulary repeatedly: the named “formations” asset appears in home, secondary, and article heroes, while page-specific imagery and copy change around it.
- Preserve generous pacing with clamp-based 4-8rem component spacing instead of accumulating one-off section margins.

## Avoid (1-2 bullets)
- Do not copy the 8.75rem headlines without the supplied .9-1 line heights, balanced wrapping, and responsive clamp minima; otherwise long legal titles will dominate or break layouts.
- Do not reproduce the floating media collage as decoration alone: without the centered headline, fixed slot rules, overflow clipping, and motion controls, it will compete with navigation and obscure content.
