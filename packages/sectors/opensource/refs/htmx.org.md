# https://htmx.org (sector: opensource, sweep: excellence, fetched 2026-08-06)
status: full-css

## Token block (~10 lines)
- Light palette: page `#fff`/`white`, text `#111`, links and primary actions `#3366cc`, secondary blue `#3d72d7`, footer `#f6f6f6`.
- Light chrome: nav gradient `#fff` to `#f4f5f5`, border `#d0d0d0`, shadow `#efefef`; general hairlines/search border `#eee`.
- Dark palette: page `#1f1f1f`, text `#c7c4c1`, links `#5b96d5`, footer `#1a1d1e`; nav gradient `#161718` to `#1b1d1f`.
- Supporting colors: code block `#272822`, danger `#d9534f`, inline-code wash `#3465a41f`, dark borders `#41464b`, dark search border `#495057`.
- Type family: system sans stack `-apple-system, BlinkMacSystemFont, "Segoe UI", "Roboto", "Oxygen", "Ubuntu", "Cantarell", "Fira Sans", "Droid Sans", "Helvetica Neue", sans-serif`.
- Type scale: body/table `16px`; inline and block code `0.9em` (14.4px from body); nav logo `28px`; dark-hero logo `100px`; generic `.hero` `5em` (80px from body), reduced to `2.5em` (40px) below `45rem`; mobile nav `22px`.
- Type treatment: body line-height `1.5em`; headings weight `600`, line-height `1em`, bottom margin `.65em`; code-block line-height `1.3`; buttons use `.1em` tracking and uppercase.
- Spacing rhythm: compact content uses `4px` list-item padding, `8px` alert side margins, `12px` list indents/alert padding/figure margin, `16px` (`1em`) content and card padding, `24px` alert vertical margins; section-heading offsets are `16px`, `32px`, and `42px`.
- Layout intent: centered `.c` reading shell at `max-width: 40em` with `.7em` side padding; docs opt into `wide-content` breakpoints of `640/768/1024/1280/1536px`, a table-cell row system, a `12rem` left rail, and sticky contents above `45em`.
- Signature element: a full-viewport-width, `240px` dark hero using `/img/topo.svg` over a `#1f1f1f` to `#2d2d2d` gradient, centered oversized `</> htmx` wordmark, blue slash/x accents, inset shadows, and a `500ms` fade/vertical reveal.

## Lessons (3-5 bullets)
- Give an open-source project one unmistakable brand moment - the topographic dark hero and code-shaped wordmark - while keeping the documentation surface quiet and utilitarian.
- Use the same centered shell for marketing, essays, and reference content, then let documentation alone opt into a wider breakpoint ladder and sticky `12rem` contents rail.
- Make dark mode a token substitution through `prefers-color-scheme`, including navigation, borders, footer, search, alerts, and alternate/inverted sponsor artwork rather than only swapping page colors.
- Keep developer content dense but legible: `16px/1.5em` prose, restrained `40em` measure, small regular spacing increments, and differentiated inline versus block code surfaces.
- Let navigation search stay visually minor at `2.5rem` and expand to `10rem` only on hover, focus, or entered text, preserving room for project links and GitHub activity.

## Avoid (1-2 bullets)
- Do not copy the many inline one-off sponsor grids and pixel values as a general component strategy; they work as page exceptions but would fragment a larger design system.
- Do not reuse the `display: table/table-cell` column system blindly; modern grid or flex layouts can preserve the measured reading column and sticky rail with clearer responsive behavior.
