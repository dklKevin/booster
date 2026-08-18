# https://www.anduril.com (sector: defense, sweep: excellence, fetched 2026-08-06)
status: full-css

## Token block (~10 lines)
- Core palette: near-black `#010101` is the default dark background/ink; `#fff` is the inverse text/light background; warm off-white `#f1f0ea` is used for panels, cards, and list surfaces.
- Accent palette: electric chartreuse `#dff140` is used for selection, hover, active text, controls, and expanding accordion backgrounds; pale chartreuse `#eff8a0` is its hover variant.
- Support/status palette: `#b0b0a9` for muted text, rules, and secondary surfaces; `#565654` for darker rules/details; `#8e9291` for product-grid borders; error red `#ff3535`.
- Type pairing: `HelveticaNowDisplay, Helvetica, Arial, sans-serif` carries display and body copy (weights 50-950 are loaded); `Elios, sans-serif` is a sparingly used technical label face, typically uppercase at `.75rem` with `.03rem` tracking.
- Base desktop type scale: h1 `5rem/105%` 700, h2 `4rem/105%`, h3 `3.5rem/110%`, h4 `2.5rem/115%`, h5 `2rem/115%`, h6 `1.5rem/115%`, h7 `1.25rem/115%`, paragraph `1.05rem/120%`; headings use negative tracking.
- Mobile type scale at `max-width: 768px`: h1 `2.714rem/100%`, h2 `2.571rem/100%`, h3 `2.429rem/115%`, h4 `2.286rem/105%`, h5 `1.929rem`, h6 `1.714rem`, h7 `1.429rem`, paragraph `1.286rem`.
- Responsive root: `14px` below 1280; `calc(1.25vw - 2px)` from 1280, `calc(.416667vw + 10px)` from 1440, `calc(1.25vw - 6px)` from 1920, capped at `24px` from 2400.
- Spacing rhythm: named row gaps `0`, `.5rem`, `1rem`, `2rem`, `3rem`, `4rem`, `7rem`; recurring section inset is `2rem` desktop and `1.428rem` mobile, with standard section margin `2rem auto`.
- Layout intent: fluid 12-column grid with `1.125rem` column and `1.25rem` row gaps (`.357rem` mobile); ordinary sections are `calc(100% - 4rem)`, capped at `calc(1440px - 4rem)` on viewports at least 1920px, while cinematic/header slices opt into full width.
- Signature element: the `#dff140` reveal layer - used as bright text/overlay and as a bottom-origin accordion background that scales from `scaleY(0)` - punctuates near-black, full-bleed video/product imagery.

## Lessons (3-5 bullets)
- Build authority through controlled contrast: reserve one high-energy accent (`#dff140`) for state changes and reveals, while the majority of the interface stays near-black, white, or warm gray.
- Keep dense technical content legible with one shared 12-column system: the Thunder product page places metadata in columns 1-2, narrative in 3-7, and CTA/media in 8-13 instead of inventing a new layout per content type.
- Make product storytelling editorial before it becomes tabular: Thunder opens with a `calc(var(--fontSizeMultiplier) * 12.5rem)` title and 16:9 media, then moves into bordered application blocks, qualities, and three four-column variation cards.
- Use typography to distinguish voice from telemetry: Helvetica Now Display handles expressive headlines and readable copy; Elios is confined to small uppercase labels, counters, and control text.
- Let section types control density: full-width cinematic slices sit beside inset content modules, while the consistent `2rem` inset and `.5/1/2/3/4/7rem` rhythm keep the transition coherent.

## Avoid (1-2 bullets)
- Do not spread chartreuse across large static surfaces: the extracted CSS uses it chiefly for selected, hover, highlighted, and expanding states, so constant use would erase its signaling value.
- Do not copy the oversized product type without the responsive multipliers and clipping rules; the desktop product title reaches `12.5rem` before its multiplier, while mobile drops to a `4rem` basis and changes media to an 8:10 aspect ratio.
