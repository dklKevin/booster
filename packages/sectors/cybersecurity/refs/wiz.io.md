# https://www.wiz.io (sector: cybersecurity, sweep: excellence, fetched 2026-08-06)
status: full-css

## Token block (~10 lines)
- Primary action/link blue: #0254EC; deep blue: #01123F; medium blue: #6195FF; light blue: #B8D3FF.
- Primary accent/interaction shadow pink: #FFC6F8; research accent pink: #FC80FF.
- Main neutrals: page #FFFFFF; primary ink #25242F; heading ink #393F49; secondary text #717783; pale blue-gray surface #EAF1FF.
- Body: DM Sans, ui-sans-serif, system-ui, sans-serif; weights present 400, 500, 700.
- Headings: Poppins, ui-sans-serif, system-ui, sans-serif; homepage hero 32px/38px mobile and 52px/66px desktop, weight 600.
- Supporting display/serif: Crimson Pro, ui-serif, Georgia, Cambria, "Times New Roman", Times, serif; extracted weights 300, 400, 500, 700.
- Core type scale: 12, 14, 16, 18, 20, 24, 30, 36, 48, 60, 128px; page-specific heading steps also include 22, 27.6, 34, 40, and 52px.
- Spacing rhythm: 4px base token; frequent gaps 4, 8, 12, 16, 20, 24, 32, 40, 48, and 64px; section padding commonly 64px at medium screens, with 80 and 96px also used.
- Layout intent: centered 68rem (1088px) core canvas with 24px mobile and 32px small-screen side margins; responsive 1-to-2/3-column grids and a repeated full-bleed grid of `1fr min(98ch, calc(100% - 4rem)) 1fr`.
- Signature element: pill CTAs in #0254EC lift 5px on hover and gain a 5px #FFC6F8 offset shadow, compressing to a 3px lift/shadow when active.

## Lessons (3-5 bullets)
- Make enterprise-security pages feel approachable without losing hierarchy: reserve #0254EC for decisive actions and links, then use #FFC6F8 as a small interaction accent rather than a large decorative field.
- Pair compact Poppins semibold headings with DM Sans body copy; the homepage’s 52px/66px desktop hero is prominent but leaves room for product UI and proof content.
- Build long pages from one 4px spacing token and a stable 1088px content canvas; vary composition with 1/2/3-column grids instead of changing the alignment system section by section.
- Give conversion controls a recognizable physical response—the repeated 5px hover lift and colored offset shadow makes CTAs distinctive while preserving simple pill geometry.
- Keep readable narrative content narrower than the main canvas: the source repeatedly uses a 98ch center track inside full-bleed sections and `max-w-prose` for centered introductions.

## Avoid (1-2 bullets)
- Do not spread the pink accent across every surface; in the fetched source it is concentrated in interaction shadows and the separate research theme, so overuse would erase the blue-led hierarchy.
- Do not copy the large type and generous 64-96px section spacing without the 1088px alignment spine; the result would become loose rather than deliberately spacious.
