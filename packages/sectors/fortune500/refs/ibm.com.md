# https://www.ibm.com (sector: fortune500, sweep: excellence, fetched 2026-08-06)
status: full-css

## Token block (~10 lines)
- Palette - canvas `#ffffff`; layer/subtle surface `#f4f4f4`; divider `#e0e0e0`; strong border `#8d8d8d`.
- Palette - primary text and dark field `#161616`; secondary text `#525252`; inverse surface `#393939`; inverse text `#ffffff`.
- Palette - brand/link/button `#0f62fe`; link/primary hover `#0043ce`/`#0050e6`; dark-theme interactive `#4589ff`.
- Palette - support roles: success `#24a148`, error `#da1e28`, warning `#f1c21b`; visited link `#8a3ffc`.
- Type - IBM Plex Sans with stack `IBM Plex Sans, system-ui, -apple-system, BlinkMacSystemFont, .SFNSText-Regular, sans-serif`; IBM Plex Mono for code and IBM Plex Serif for quotations.
- Type scale - 12px labels/captions; 14px compact/body; 16px body; headings 20, 28, 32, 42 and 54px; expressive heading 05 fluidly rises from 32px to 60px at the 99rem breakpoint.
- Type behavior - body line-heights 1.375–1.5; large headings use weight 300–400 and line-height 1.17–1.25; small headings use weight 600.
- Spacing - Carbon rhythm `0.125, 0.25, 0.5, 0.75, 1, 1.5, 2, 2.5, 3, 4, 5, 6, 10rem`; fluid spacing tokens `0, 2vw, 5vw, 10vw`.
- Layout - 4 columns mobile, 8 from 42rem, 16 from 66rem; 2rem grid gutter; 1/2/2.5rem container padding; content max-width 99rem; grid margin becomes 1rem at 42rem and 1.5rem at 99rem.
- Signature - an expanded 6/8/2-column leadspace pairs content, media and a slim aside; its current headline uses a 90deg blue-to-purple text gradient, `#0f62fe` → `#8a3ffc`.

## Lessons (3-5 bullets)
- Give complex enterprise content one rigid responsive skeleton: IBM's 4/8/16-column progression lets hero, product-card and editorial modules align without looking templated.
- Use the brand blue as an interaction color, not a blanket background; neutral `#ffffff`/`#f4f4f4` fields and `#161616` text carry most of the information density.
- Separate expressive and productive typography: light 32–60px display text creates authority while 14–16px body styles and 600-weight small headings keep dense material scannable.
- Make the hero asymmetric but mathematically disciplined: the 6/8/2 split creates room for a narrative, a strong visual and a narrow news/context rail within the same grid.
- Preserve rhythm through a named spacing ladder, then reserve viewport-relative 2vw/5vw/10vw spacing for major section transitions.

## Avoid (1-2 bullets)
- Do not copy the 16-column density without the 4- and 8-column collapses; the source explicitly changes column count at 42rem and 66rem and hides the leadspace aside below 42rem.
- Do not spread the blue-purple gradient across routine copy; in the fetched homepage it is a distinctive leadspace headline treatment, while standard text remains `#161616` or `#525252`.
