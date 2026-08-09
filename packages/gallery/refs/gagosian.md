# gagosian (gagosian.com, extracted 2026-08-07)
status: full-css

- Neutrals: #FFFFFF canvas and reversed text, #111111 primary text/rules/buttons, #B2B2B2 inactive navigation stepping to #111111 on hover, #CCCCCC section rules; dark sections use #222222 with #FFFFFF text.
- Accents: #FEBE29 and #70588A are not global brand accents; each is a current homepage slide's artwork-specific ground and becomes the button color on an inverse #111111 or #FFFFFF fill, swapping on hover.
- Type: GagosianHeadline/Times New Roman/serif is 50, 60, 75, then 100px at 1024px, 700 uppercase at .8 line-height; minion-pro-condensed/Times New Roman/serif is 21-35px/1, 700; minion-pro/Times New Roman/STSong/serif body is 17.5/20 to 20/24px, 400; GTAmerica/sans-serif UI is 12.5/15, 15.5/19.5, 18/22.5px, weights 400/500/700.
- Space: 4px utility base; live section variables step 18/20/32px and wide 28/32/40px; 16px page gutters, 1224px content and 1832px canvas maxima, 4-column mobile to 12-column desktop grid at 768px; content and buttons are square, with 2px radius limited to small focus targets.
- Motion: color, opacity, and max-width transitions are 300ms cubic-bezier(.4,0,.2,1); slideshow logo color is delayed 200ms then runs 200ms; route progress opacity and position run 200ms linear.
- Structure: A fixed 37px navigation rail caps stacked edge-to-edge sections; the homepage opens with a viewport-height carousel, while exhibition and article pages reuse a 4/12-column editorial grid for title, media, metadata, prose, and related modules.
- Signature: Each hero slide mechanically couples one artwork image to a full-bleed color field, switches between split 50/50 landscape and stacked portrait composition, and recolors logo, display type, and inverse-outline CTA from per-slide inline variables.

Avoid: Copying the uppercase masthead plus yellow/purple panels produces a costume; the color fields and inversions depend on the active artwork, while the compressed 50-100px headline only works with sparse copy and exhibition-scale imagery.
