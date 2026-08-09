# https://www.vrtx.com (sector: pharma, sweep: excellence, fetched 2026-08-06)
status: wayback

## Token block (~10 lines)
- Palette — primary purple #42247F: hero background, headings, links, buttons and carousel panels.
- Palette — ink #1F0E30: body copy and dark UI text; deep-purple hover #381F60.
- Palette — light lavender #E2DAF2: pale section field, hero supporting copy and button-hover fill; white #FFFFFF: cards, hero text and inverse controls.
- Palette — soft purple #C09BCC: card borders and the 11px news-carousel top band; olive #AFB588 and orange #FABC95 appear as hero-title highlight accents.
- Type family — Cabin variable, loaded from Cabin-VariableFont_wdthwght.ttf; body stack is 'Cabin', sans-serif.
- Type scale — h1 64/72, h2 48/56, h3 40/48, h4 32/40, h5 24/32, h6 18/24px; headings use weight 600.
- Responsive type — hero h1 becomes 40/48px below 1024px; news display copy shifts 32/40 to 24/32px; body is 18/24px, with 16/20px used for compact copy and controls.
- Spacing rhythm — 10px micro-gaps; 20px component gaps/padding; 30px column gaps; 40px card/panel padding; 60px section spacing; the overlapping card band uses 120px.
- Layout — full-bleed fields cap at 1920px; primary content/carousels cap at 1110px; hero inner row caps at 1519px with a 445px copy column and media up to 806×601px; cards are three flex items up to 350px with 30px gaps.
- Signature element — large photographic/video media is clipped by big-bg-mask.svg at a fixed 806:601 aspect ratio, paired with a short 80×6px clipped highlight bar and echoed by the 11px accent band on the news carousel.

## Lessons (3-5 bullets)
- Use one saturated institutional color (#42247F) across hero, headings, CTAs and editorial panels, then preserve readability with #FFFFFF and #E2DAF2 instead of introducing many competing brand colors.
- Build the hierarchy from a compact, explicit Cabin scale: 64/72px for the promise, 24/32px for supporting claims, and 18/24px for reading copy; reduce the hero to 40/48px below 1024px.
- Alternate the 1920px color field with a disciplined 1110px content measure; the homepage lets the masked hero media extend to 806px while keeping the copy column to 445px.
- Make visual distinctiveness structural: reuse clipped masks, shallow trapezoid-like accent bands and rounded 100px CTAs, while keeping cards conventional and scannable.
- Let cards overlap the hero field by exactly 120px to connect the opening brand statement to three concrete pathways without breaking the 1110px grid.

## Avoid (1-2 bullets)
- Do not copy the 64px hero, 120px overlap or three 350px cards without the extracted breakpoints; the source changes the hero to 40px, reverses its columns and wraps cards below 1024/768px.
- Do not treat every accent as interchangeable: #C09BCC is used for boundaries/bands, while #AFB588 and #FABC95 are sparse highlight colors; broad use would weaken the purple-led hierarchy.
