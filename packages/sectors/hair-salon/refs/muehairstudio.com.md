# https://muehairstudio.com (sector: hair-salon, sweep: excellence, fetched 2026-08-15)
status: full-css

## Token block (~10 lines)
- Palette / foundation: `#ffffff` carries the page and price schedules, `#171717` carries the fixed desktop header, `#555555` is the shared body ink, and near-black `#0e121d` carries major section headings.
- Palette / utility: warm tan `#cca27a` marks interior-page banners, the mobile menu bar, active FAQ questions, and price values; pale greige `#f2efea` holds closed FAQ rows, while blush-gray `#f5f1f2` separates the homepage service chapter.
- Type system: Jost carries the shared shell, body, headings, actions, and pricing; Playfair Display at italic 600 marks 21/35px homepage eyebrows, while Yantramanav at 500 carries the 22/28px FAQ questions.
- Display and text scale: shared body copy is 15/28px at weight 300; desktop page titles are 45/45px at weight 500, pricing chapters are 45/50px at 600, price rows are 18/30px, and values are 24/30px at 600.
- Utility scale: the owned pricing route presents 50 rows in seven chapters as exact, starting, or consultation prices; each row is 52px high in an 808px list, with dotted leaders connecting service and tan value.
- Spacing: major desktop sections commonly use 60-120px vertical padding; the 1440px verification viewport resolves a 1320px header frame, 1120px standard content frame, and 808px price-list measure.
- Shape and action: primary actions, price fields, gallery tiles, and FAQ rows use `0px` radii; the header booking action is 175x62px, the desktop hero action is 227x60px, and the verified narrow hero action is 177x48px.
- Frame and responsive behavior: the fixed 98px desktop header becomes a 143px centered-logo block plus a 61px tan menu bar at the verified 500px viewport; the interior-photo hero contracts from 890px to 400px, while pricing headings step from 45px to 20px and rows from 18/24px to 15px.
- Motion: homepage columns enter with 0.8-1s directional fades and the hero uses a one-slide Slick instance configured to autoplay every 7s; Elementor's reduced-motion rule disables `.animated` effects, but the hero action retains a directly declared 1s fade, so reduction is incomplete.
- Signature element: a restrained black, tan, and white shell opens on a real salon interior, then turns utility into the identity through long price registers, seven FAQ rows, deep service routes, and dense owned result galleries.

## Lessons (3-5 bullets)
- Build one connected decision path instead of a brochure page. Mue links a service overview to focused haircut, color, perm, treatment, and wedding routes, then keeps pricing, FAQ, stylist choice, contact, and booking in the owned navigation.
- Make price status explicit and scannable. Fifty rows distinguish fixed prices, starting prices, and consultation-only color correction across cutting, color, men's and women's perms, treatment, wedding, and styling.
- Carry the nuance into the booking card. The embedded catalog exposes 49 bookable entries in seven categories and specifies details such as haircut inclusion, 2-3 inches of retouch growth, short/medium/long treatment tiers, extra-bleach charges, and services that require contact first.
- Organize proof by the same vocabulary clients use to shop. Eleven menu-linked gallery routes separate men's and women's cuts and perms, children's work, color techniques, treatment, and event styling; the men's-perm route alone exposes 74 linked result images rather than outsourcing all proof to social media.
- Let people choose through relevant expertise and communication, not demographic assumptions. Seven named profiles provide roles, experience, and specialties; Anna explicitly offers Korean and English, Leo offers Mandarin, and the service and proof surfaces include women, men, and children without presenting one client type as universal.

## Avoid (1-2 bullets)
- Do not copy the Hairling/Elementor template, exact black-tan palette, interior hero, dotted price table, or SEO superlatives; transfer the unusually complete service-to-proof-to-price-to-booking path, and substantiate celebrity history, experience, treatment efficacy, and duration claims before publishing them.
- Do not copy its source-of-truth and interaction gaps: the 50-row owned price list and 49-item booking catalog are not identical, the verified Vagaro load raised three API-error dialogs and exposed no service durations, stale On Hair naming remains in review and asset content, and the FAQ links lack expanded-state semantics while the hero fade is not fully reduced.
