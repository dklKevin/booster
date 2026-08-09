# https://www.isomorphiclabs.com (sector: pharma, sweep: excellence, fetched 2026-08-06)
status: full-css

## Token block (~10 lines)
- Core palette: page #FFFFFF; primary text #000000; carbon black #1E1E1E for key borders/dark surfaces; secondary carbon #3A3A3A for the footer.
- Scientific neutrals: calcium white #D8D8D8 for fine rules/grid lines; hydro blue #F5F8F9 for cool pale surfaces; hydro blue dark #304A57.
- Primary ambient pair: amino azure #E6F7FF to acid green #E9FFE9 in a 0deg linear gradient used behind the home hero and interactive model.
- Secondary ambient accents: genesis orange #FFE4CC, evo pink #FFECFC, and alpha chartreuse #E8FAC3; the work hero uses an orange-to-pink 180deg gradient.
- Display pairing: "Soehne Extraleicht", Arial, sans-serif at weight 200; desktop display scale 70/77, 56/61.6, 48/57.6px with -2, -1.7, and -1px tracking.
- Supporting type: "Soehne Leicht", Arial, sans-serif at weight 300 for headlines/body; "Soehne Buch", Arial, sans-serif at 400 for microcopy; "Sohne Mono", Arial, sans-serif at 400 for tags.
- Desktop content scale: headlines 36/43.2, 28/36.4, 24/31.2px; paragraphs 24/32.4, 20/28, 16/22.4, 14/19.6, 12/16.8px; mono tags 14/19.6 and 12/16.8px.
- Spacing rhythm: 4, 8, 12, 16, 20, 30, 40, 60, 80, 120, 200px on desktop; sections use 120px bottom spacing and 200px extra top spacing; cards use 20-80px padding by context.
- Layout intent: a 1240px max-width container with 8vw desktop side margins, 16px grid gaps, frequent 1:1 and 2:3 splits, a 72px navigation height, 660px hero height, and 20px container radius.
- Signature element: transparent scientific motion media floats across a fine, black-outlined 2x2 hero grid over the #E6F7FF-to-#E9FFE9 ambient gradient, echoed by an auto-rotating DNA 3D model inside a rounded, #1E1E1E-bordered square with #D8D8D8 dashed grid lines.

## Lessons (3-5 bullets)
- Give scientific imagery a functional interface frame: the bordered grid, square model viewport, dashed measurement-like lines, and mono labels make molecular media feel investigational rather than decorative.
- Make optimism precise through near-white scientific color families: the pale azure/green and orange/pink gradients add warmth while black typography and one-pixel borders preserve clinical clarity.
- Separate voice by type role: weight-200 displays carry the ambitious mission, weight-300 text explains it, and compact tracked mono tags supply taxonomy and wayfinding.
- Use a small set of repeatable proportions across very different content: 1:1 grids for heroes/cards, 2:3 for explanatory text plus interactive media, and 400/600/1000px reading caps inside the 1240px shell.
- Scale tokens at the breakpoint rather than merely shrinking components: the fetched CSS changes display type from 70px desktop to 28px mobile, side padding from 8vw to 24px, section spacing from 120px to 80px, and container radius from 20px to 12px.

## Avoid (1-2 bullets)
- Do not copy the pale gradients without the dark one-pixel structure and restrained type weights; the extracted composition relies on that contrast to avoid looking like generic wellness branding.
- Do not reproduce the transparent hero video and interactive 3D model without fallbacks and performance controls; both are structurally prominent media layers, not optional embellishments.
