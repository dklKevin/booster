# https://www.figma.com (sector: startup, sweep: excellence, fetched 2026-08-06)
status: full-css

## Token block (~10 lines)
- Core light palette: background #FFFFFF, foreground #000000; primary button #000000 with #FFFFFF text.
- Core dark palette: background #000000, foreground #FFFFFF; primary button #FFFFFF with #000000 text.
- Brand/logo accents: blue #00B6FF, green #24CB71, orange #FF7237, red #FF3737, violet #874FFF.
- Supporting UI accents: action blue #0D99FF on pale blue #E5F4FF; focus treatment #E4FF97 with #000000.
- Type pairing: sans "figmaSans", "figmaSans Fallback", SF Pro Display, system-ui, helvetica, sans-serif at custom-face weight 320; mono "figmaMono", "figmaMono Fallback", SF Mono, menlo, monospace at 400.
- Responsive type scale: display 1 4.5/5.5/6.5rem; display 2 2.75/4/4.5rem; title 1 2.25/3.5/4rem at base/1024px/1600px.
- Supporting type: title 2 2/2.75/3rem, title 3 1.5/1.875/2rem, body 0.875/1rem; line-height tokens 1, 1.1, 1.2, 1.3, 1.4, 1.45.
- Spacing rhythm: 0.25, 0.375, 0.5, 0.75, 1, 1.5, 2, 2.5, 3.5, 4, 5, 7.5rem; section block padding 2.5/4/5rem at base/480px/1024px.
- Layout intent: 4-column mobile grid becomes 12 columns at 480px, with 1rem gutters, 1/1.5/2.5rem outer margins, and a 95rem maximum content width.
- Signature element: a condensed, tight-tracked headline paired with a large embedded product-demo media stage and explicit play control, repeated as canvas-like story sections.

## Lessons (3-5 bullets)
- Let the product demonstration carry the hero: the homepage places the headline directly beside a playable media stage instead of explaining the product through dense copy.
- Keep a stable 12-column desktop grid while changing outer margins and type at explicit breakpoints; this preserves alignment as the page becomes more editorial at larger sizes.
- Use a broad but discrete spacing ladder, then expose section padding as one responsive token so long startup pages maintain a consistent vertical cadence.
- Reserve saturated brand colors for the logo and small icon systems while the main interface remains predominantly #FFFFFF/#000000; the product imagery supplies most of the visual variety.
- Reuse the same structural rhythm across product pages—short headline and support copy followed by demonstrative media—while changing the content rather than inventing a new page system.

## Avoid (1-2 bullets)
- Do not copy the 4.5-6.5rem display scale without the extracted condensed width setting and tight letter-spacing; the same sizes in a wider font will wrap much earlier.
- Do not reproduce the many bright logo colors as equal-area section backgrounds; the fetched source uses them chiefly as compact brand and icon accents against a black-and-white theme.
