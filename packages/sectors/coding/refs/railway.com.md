# https://railway.com (sector: coding, sweep: excellence, fetched 2026-08-06)
status: full-css

## Token block (~10 lines)
- Light canvas/surfaces: #F1F0EF page canvas, #FAFAFA surface, #FFFFFF raised surface, #E0DFDD footer.
- Light text/borders: #1C1A28 primary text, #868593 secondary text, #545260 tertiary text, #DCDCE0 border.
- Dark canvas/surfaces: #0D0C14 page canvas, #13111C surface/hero/footer, #181622 raised surface, #33323E border.
- Dark text: #F7F7F8 primary, #868593 secondary, #535260 tertiary.
- Accents: #59497A light purple accent, #553F83 dark purple accent, #A667E4 dark strong accent, #F2E9FB light accent wash; success #367859 light / #42946E dark; info #5B8DEF.
- Display face: IBM Plex Serif, Georgia, Cambria, "Times New Roman", serif; used for hero and section headlines at 36/48px, 40px/1.12, 48px, 54px, and up to 56px/1.25 on pricing.
- UI/body face: Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen-Sans, Ubuntu, Cantarell, "Helvetica Neue", sans-serif; recurring sizes 14/20px, 16/24px, 18px/1.5-1.6, and 20px/1.5.
- Condensed emphasis face: Inter Tight falling back to Inter; mono stack is ui-monospace, SFMono-Regular, "SF Mono", Consolas, "Liberation Mono", Menlo, monospace.
- Spacing rhythm: 4px base utilities with frequent 8, 12, 16, 24, 32, 48, 64, 96, and 128px steps; section grids use 24px gutters, rising to 32px at md.
- Layout intent: centered 1160px content container and 12-column grids sit inside rounded, overflow-clipped feature canvases up to 1696px; prose is capped at 65ch and hero copy at 740px.
- Signature element: a long, scroll-driven illustrated train/boarding sequence (including explicit train body, door, stripe, track, and scroll-distance tokens) turns deployment progress into Railway's literal visual metaphor.

## Lessons (3-5 bullets)
- Pair restrained infrastructure UI colors with one editorial serif: IBM Plex Serif makes the promise feel calm and human while Inter keeps navigation, controls, and technical detail precise.
- Separate reading width from spectacle width: 65ch/740px copy caps and a 1160px working grid preserve legibility while 1696px canvases give product narratives cinematic scale.
- Give each technical capability a distinct but muted environmental color: the source assigns dedicated build (#254B69), scale (#E1DDD5), monitor (#2A6A71), and trust (#55394F) panel backgrounds without abandoning the shared neutral system.
- Make the brand metaphor operational, not ornamental: the train motif is supported by responsive scroll-distance variables from 76px to 640px and is tied to the closing “now boarding” message.
- Reuse a consistent 12-column shell while changing composition by section; the homepage alternates centered, split, and three-up arrangements, while pricing returns to simpler two-column and five-column grids.

## Avoid (1-2 bullets)
- Do not copy the 1696px canvases or the homepage's 1700px minimum-height hero without equally disciplined 1160px/740px inner constraints; the result would become sparse and hard to scan.
- Do not imitate the train as a generic animated mascot: its many bespoke colors, parts, and responsive motion values work because they reinforce the Railway name and deployment story.
