# https://mghairartistic.com (sector: hair-salon, sweep: excellence, fetched 2026-08-15)
status: full-css

## Token block (~10 lines)
- Palette / core: `#111111` is the page and fixed-header ground, `#1d1d1d` carries content panels, metric blocks, location content, and review cards, and `#ffffff` is the primary reversed ink.
- Palette / supporting: long supporting copy renders at `rgba(255,255,255,.8)`; the live stylesheet also declares `#4a4a4a`, `#737373`, and `#999999`, but their stable semantic roles were not verified.
- Type pairing: `Archivo Black` at weight 400 carries display headings and uppercase action labels; `Archivo` at weight 300 carries descriptions and supporting copy.
- Display scale: the primary H1 preset is 56/48/42px and the large H2 preset is 66/32/28px across desktop/tablet/mobile; both use 1.0-1.1 line-height and negative tracking.
- Supporting scale: H3 is 26/24/22px in Archivo Black, H5 is 20/18/16px in Archivo, and one centered H6 preset changes sharply from 26px desktop to 15px tablet and 13px mobile.
- Spacing: 8, 10, 16, 20, 24, and 40px recur inside components; major sections use 80 and 100px vertical padding.
- Shape and action: content panels use 32px radii, review cards 20px, hero frames 24px, and outlined CTAs 8px; the hero CTA uses 14px 16px padding with a 1px white outline drawn by its pseudo-element.
- Frame: layout variants switch below 1200px and 810px; at 1440px the hero uses a 20px inner frame and 16px gaps, while the fixed header is 100px high.
- Motion: the nine-image Instagram strip repeats 180px tiles at 10px gaps in a linear infinite marquee, measured at 37.8s on a 1440px viewport and 18.9s on the 500px mobile variant.
- Signature element: a viewport-wide, grayscale triptych hero leaves two narrow photographic panels beside one expanded 24px-radius panel; below 810px it becomes one tall image panel followed by two 80px teaser bands.

## Lessons (3-5 bullets)
- Build a salon identity from image treatment, crop, and type rather than the category's beige-luxury shorthand: grayscale close-up photography, a nearly black canvas, and blunt Archivo Black make the salon legible without blush or gold.
- Give a multi-location operator one clear decision point. The homepage chooser exposes six named locations and addresses, then routes each visitor to a branch page instead of forcing one generic booking destination.
- Put branch facts on the branch page. The verified Flushing route includes opening hours, street address, phone, email, WeChat, an embedded map, a price-list asset, named stylists with levels, and a direct phone booking action.
- Treat social work as one layer of proof, not the whole site: the moving nine-image Instagram portfolio sits alongside location routes, reviews, service categories, and branch operations.
- Language and contact choices can acknowledge an Asian audience without vague identity claims: English and Chinese are explicit navigation options, while the Flushing page keeps both conventional contact details and WeChat visible.

## Avoid (1-2 bullets)
- Do not copy the exact `#111111` plus Archivo Black system or the grayscale three-panel hero; transfer the principle of one controlled image treatment carrying the identity.
- Do not copy the operational gaps: the general service page gives category names but no prices, durations, consultation rules, or preparation detail, and the Flushing price list is an image rather than structured text. Keep those details searchable and accessible, and give any continuous portfolio motion a reduced-motion fallback.
