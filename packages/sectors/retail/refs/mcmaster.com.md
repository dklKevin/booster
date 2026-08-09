# https://www.mcmaster.com (sector: retail, sweep: excellence, fetched 2026-08-09)
status: full-css

## Token block (~10 lines)
- Palette, foundation: #FFF canvas and panel ground; #333 body text; #000 high-emphasis text; #CCC and #999 borders, rules, and scrollbars.
- Palette, brand/action: #363 dark green headings, rules, nav, and primary buttons; #FED700 yellow masthead rule and secondary buttons; #069 text links.
- Palette, interaction: #FFFFB5 hover highlight; #EDF2ED category-tile hover; #EEE spec/search panels; #49D focus outlines.
- Type pairing: FuturaLTPro-BoldCond, arial, sans-serif for masthead navigation; HelveticaNeueeTextPro-Roman / HelveticaNeueeTextPro-Md, arial, sans-serif for catalog UI; DINNextLTPro-Medium, arial, sans-serif for buttons.
- Type scale: 10.5px tile and category links, 11px secondary links, 12px body and controls, 13px search and category-tile labels, 14px subcategory/presentation labels, 16px masthead links, 19px category and presentation headings.
- Line-height: 12px body uses 1.3; catalog and table content uses 14px; 14px abbreviated presentation names use 16px; 19px presentation names use 21px.
- Spacing rhythm: named gutters are 5px small, 10px default, 20px large, 50px extra-large, and 60px huge; dense local padding commonly uses 2-5px.
- Layout intent: a full-width application shell with a 73px masthead above 768px and 97px at 768px or below; content begins at 85px or 109px respectively, with no global content max-width in the extracted shell rules.
- Layout system: sticky 195px homepage navigation plus flexible category content; product filtering uses a 199px scrolling pane plus flexible content; the masthead search is fluid but capped at 700px.
- Signature element: an illustrated parts index built from 72px by 114px tiles, each holding a 60px by 60px product image and a centered 10.5px label, grouped under 19px dark-green headings and 1px green rules.

## Lessons (3-5 bullets)
- Make retrieval the dominant retail action: the search field occupies the masthead's flexible center, reaches up to 700px, and remains present while catalog and order links stay peripheral.
- Let product imagery function as taxonomy rather than decoration: uniform 60px part illustrations turn a very large industrial assortment into a compact, visually scannable index.
- Match density to repeat purchasing: a 195-199px navigation/filter rail, 12px/14px table typography, and 5/10/20px gutters keep specifications and ordering controls visible together.
- Reserve color for operational meaning: dark green anchors hierarchy and primary actions, yellow marks the shell and secondary action, and pale yellow consistently signals hover selection.

## Avoid (1-2 bullets)
- Do not transplant the 10.5-12px type and 72px-wide tiles into a low-frequency or touch-first store without adaptation; this density is tied to expert catalog scanning.
- Do not expand the yellow into large decorative fields; the extracted CSS uses it narrowly for the 2px masthead rule, secondary buttons, selection, and hover feedback.
