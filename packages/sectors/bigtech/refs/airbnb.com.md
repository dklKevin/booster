# https://www.airbnb.com (sector: bigtech, sweep: excellence, fetched 2026-08-06)
status: full-css

## Token block (~10 lines)
- Palette / foundation: page background `#FFFFFF`; primary surface `#FFFFFF`; secondary surface `#F7F7F7`; tertiary surface `#EBEBEB`.
- Palette / text: primary `#222222`; secondary `#6C6C6C`; inverse `#FFFFFF`; disabled `#DDDDDD`.
- Palette / structure: primary border `#222222`; secondary border `#8C8C8C`; tertiary border `#DDDDDD`; subtle divider `#EBEBEB`.
- Palette / brand and action: Airbnb red `#FF385C`; active action red `#DA1249`; action gradient `#E61E4D 1.83%` → `#E31C5F 50.07%` → `#D70466 96.34%`.
- Type family: `'Airbnb Cereal VF', 'Circular', -apple-system, 'BlinkMacSystemFont', 'Roboto', 'Helvetica Neue', sans-serif`; one variable family supplies the hierarchy rather than a separate display face.
- Body/type scale: `12/16`, `14/18`, `14/20`, `16/20`, `16/22`, `16/24`, `18/24`, `18/28` px; title weights `500–600`.
- Title/display scale: `22/26`, `26/30`, `32/36`, `40/44`, `48/54`, `60/68`, `72/74` px; display weight `600`.
- Spacing rhythm: recurring `4, 8, 12, 16, 24, 32, 40, 48, 80px`; responsive content gutters extracted at `16, 24, 32, 40, 48, 80px`.
- Layout intent: centered, fluid page shell capped at `1920px`, with responsive repeat grids (including 4- and 5-column states), generous adaptive gutters, and horizontal content scrollers below the breakpoint where a grid would become cramped.
- Signature element: the segmented search pill is max `850px` wide and `66px` high with `32px` outer radius; its grid gives location `2fr`, three following fields `1fr` each, separated by `1px` tracks, ending in a `48px` circular `#DA1249` search action.

## Lessons (3-5 bullets)
- Reserve the saturated brand color for the final action and selection state; the extracted shell remains almost entirely `#FFFFFF`, `#222222`, and quiet grays, so `#FF385C`/`#DA1249` carries immediate meaning.
- Use one variable sans family with line-height-specific tokens instead of accumulating near-duplicate text styles; Airbnb explicitly defines compact UI text separately from more breathable paragraph text at the same nominal size.
- Let gutters and column count change independently: the source steps padding through `16–80px` while moving among repeat-grid states, preserving both card usability and page-level calm.
- Make the primary discovery control express task structure: the search pill gives the open-ended location field twice the width of the bounded date/guest fields, then visually terminates the sequence with a fixed-size action.

## Avoid (1-2 bullets)
- Do not copy the pill radius onto every component; the source also uses `8`, `12`, `16`, and `24px` radii, and making everything fully rounded would erase the search control’s signature role.
- Do not treat `1920px` as a target content width without the responsive gutters and changing grid count; on ordinary displays that would produce overlong text and undersized cards.
