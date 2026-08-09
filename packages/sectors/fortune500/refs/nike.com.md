# https://www.nike.com (sector: fortune500, sweep: excellence, fetched 2026-08-06)
status: full-css

## Token block (~10 lines)
- Core palette: #FFFFFF primary/modal background; #111111 primary text, inverse background, and primary button; #F5F5F5 secondary/image/loading background.
- Neutral roles: #707072 secondary text and primary border; #CACACB secondary border; #E5E5E5 tertiary border/disabled background; #9E9EA0 disabled text.
- Functional/brand accents: #FF5000 Nike orange; #1151FF link/focus; #D30005 critical; #007D48 success; #FEDF35 warning.
- Display type: "Nike Futura ND", "Helvetica Now Text Medium", Helvetica, Arial, sans-serif; uppercase, weight 400, line-height .9; responsive display sizes 24/32/40/48px at 320–959, 48/60/76/96px at 960–1919, and 60/76/96/120px at 1920+.
- Title type: "Helvetica Now Display Medium", Helvetica, Arial, sans-serif, weight 500; 20/24/32/40px through 1919 and 24/32/40/48px at 1920+, line-height 1.2.
- Body type: "Helvetica Now Text", Helvetica, Arial, sans-serif, weight 400; 10/12/14/16px with 1.5 line-height; editorial body grows from 16px to 20px at 960px.
- Optional editorial voice: "Palatino LT Pro Light", Helvetica, Arial, sans-serif, weight 300; 16–48px depending on tier and viewport, line-height 1.1–1.35.
- Spacing rhythm: 4, 8, 12, 24, 36, 60, 84, 120px; exterior grid gutter 24px small / 48px large; internal grid gutter 16px small / 12px large.
- Layout intent: 12-column fluid grid at 320/600/960/1440/1920px breakpoints, capped at 1824px for fixed-fluid content; browse/product-grid shells reach 1920px.
- Controls: pill buttons use 30px radius, 34/46/58px heights, 16/24/24px side padding; component radii also include 4/8/12/24px.
- Signature element: full-bleed image/video campaign cards with overlay copy and pill CTAs, punctuated by uppercase Nike Futura display headlines set at a compressed .9 line-height.

## Lessons (3-5 bullets)
- Let campaign storytelling and commerce use different typographic gears: a proprietary condensed face makes launches unmistakable, while a neutral text family keeps navigation, filters, prices, and product details fast to scan.
- Build dramatic scale into tokens instead of one-off hero CSS: Nike's display tiers jump from 24–48px on small screens to 60–120px on 1920px+ screens while preserving the same .9 rhythm.
- Keep the permanent UI nearly monochrome (#FFFFFF, #111111, and a short grey ladder), reserving saturated colors for semantic states and brand moments so merchandise supplies most of the page color.
- Combine a wide 1824px editorial container with explicit 24/48px exterior gutters and a 12-column system; this supports immersive media without letting utility content touch the viewport edge.
- Reuse one rounded control geometry across campaign CTAs and commerce actions; the 30px pill radius and three fixed heights create continuity as page structures change.

## Avoid (1-2 bullets)
- Do not copy the oversized uppercase treatment without the condensed face and .9 line-height; a conventional sans at 60–120px will occupy more space and lose the compact, athletic silhouette.
- Do not apply the full-bleed overlay-card pattern to dense product information; Nike's listing and product structures deliberately return to restrained text, grids, and semantic greys.
