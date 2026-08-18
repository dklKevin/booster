# https://atelierbytiffany.com (sector: hair-salon, sweep: excellence, fetched 2026-08-15)
status: full-css

## Token block (~10 lines)
- Palette / ground and ink: `#ffffff` is the primary page field and photographic mat; major display type uses `#333333`, body copy and solid actions use `#000000`, and service-card titles use `#383838`.
- Palette / accents: deep green `#154034` carries section labels and text actions, while `#919191` carries quiet uppercase eyebrows; the product feature uses `#f0d991` for its eyebrow and white type over a photographic field with a black `0.3`-to-`0.85` vertical overlay.
- Type system: rendered content uses `Zen Old Mincho` with Georgia and Times fallbacks for display, body, and controls; `Montserrat` at weight 800 is reserved for the compact utility label over the opening portrait.
- Display scale: desktop intro headings are 70px/60px at weight 300; later uppercase chapter headings are 70px/80px, and the photographic product statement is 50px/65px. At the verified phone breakpoint these become 40px/50px and 24px/32px respectively.
- Supporting scale: opening copy is 18px/26.6px at the verified desktop width; service titles are 20px/36px at weight 700 with 4px tracking, while section eyebrows are commonly 16px/32px with 3px tracking.
- Spacing: standard rows occupy 80% of the viewport and cap at 1600px; standard sections use 4vw vertical padding, measured at 57.6px on a 1440px viewport, while the product feature uses 7vw and the verified narrow layout resolves standard section padding to 50px.
- Shape and action: service images sit in square white mats with a 20px border and a 1px outer rule; black rectangular CTAs use 14px 48px padding with no radius.
- Frame and responsive behavior: above 980px, the opening chapter measured 1,975px tall at the verified 1440x1000 viewport and uses a `background-attachment: fixed` composition sized to 100% width, holding a grayscale portrait on the left while two content sequences move through the right half. At 980px and below, that chapter is replaced by a 100vh cover portrait followed by normal-flow content.
- Motion: service mats increase from a 20px to 30px white border and strengthen their outer rule on hover; border, shadow, and button changes use `300ms` transitions.
- Signature element: one wind-swept grayscale hair portrait remains visually fixed through the two-part desktop introduction, opposed by salon-tool silhouettes, tilted instant-photo interior crops, and restrained green labels on white.

## Lessons (3-5 bullets)
- Let one art-directed hair image establish the identity, then sustain it across more than a hero moment. Separating that fixed image from the moving introduction creates editorial tension, while the mobile replacement cleanly sequences image before content.
- Prove Korean and cross-Asian hair knowledge through service vocabulary rather than a broad technique claim. The live booking menu names digital/setting perm, volume magic, down perm, magic straightening, Mucota magic, acid perm, Japanese straightening, and head spa alongside cut, color, and treatment.
- Connect stylist proof directly to service choice. The team route exposes 21 named profiles with role and specialties; the verified JungMin page adds experience and a personal Instagram route, grounding Korean experience in specific entertainment and production work rather than leaving it as an unsupported label.
- Keep complex salon operations inside a legible booking sequence. The embedded Boulevard flow separates individual appointments, group appointments, and gift cards, then moves from 13 service categories to a specific treatment, professional, and starting price.
- Support varied clients without turning the salon into either a barber site or a narrowly feminine template. The service inventory explicitly includes women, men, and children, while the site exposes address, daily hours, phone, map, call and text details, and WeChat in its rendered Instagram profile.

## Avoid (1-2 bullets)
- Do not copy the exact grayscale portrait, fixed split composition, white instant-photo mats, or Zen Old Mincho system; transfer the principle of making one salon-specific photographic treatment carry the identity across viewport changes.
- Do not copy the operational gaps: homepage service cards omit price, duration, and consultation detail; the verified digital/setting-perm path reveals its starting price only after professional selection and gives no duration or treatment explanation. The rendered homepage also returned HTTP 404 despite displaying content, and the team card for Eric routed to Winter.
