# grandseiko (grand-seiko.com, extracted 2026-08-07)
status: full-css

- Neutrals: #fff page/media text, #000 body and hero ground, #f6f6f6 alternate/spec ground, #212121 collection-card fallback, #dbdbdb 1px dividers; neutral hovers mostly keep color and fade/zoom imagery, while black/white outline buttons invert.
- Accents: #000040 is the single brand navy for headings, rules, controls, buttons, and dark sections; #000027 only edges filled navy buttons, while #00003d is confined to circular chapter navigation.
- Type: adobe-text-pro, "Times New Roman", Georgia, "Hiragino Mincho ProN", "Yu Mincho", serif; body 14px/1.85 at 400 with .05em tracking, hero title 20px -> 40px/1.5, section title 24px/1.5, product title 32px/1.5, story hero 48px/1.2 at 500.
- Space: 8px utility step; 16px mobile and 32px desktop gutters, 1164px main / 844px narrow columns, sections commonly 32-64px vertical; square corners except 50% carousel/chapter controls; core breakpoints 576/768/992/1200px, story adds 640/900/1024px.
- Motion: links/buttons 0.2s, collection-image scale(1.05) 0.4s, mobile collection fade-up 2s from translateY(100px), hero slides dwell 5000ms with wrapper easing cubic-bezier(0.1, 0.5, 0.2, 1); only nav-link transitions are explicitly removed under reduced motion.
- Structure: a 100vh product-image carousel gives way to stacked collection photo slabs, product/news carousels, and editorial bands; product pages use a 30/40/30 data-object-actions triptych, while stories alternate narrow prose, full-bleed images, and 50/50 image-text splits.
- Signature: the homepage behaves as a changing watch vitrine: many fixed/random full-viewport product portraits, each bottom-labeled in small-to-40px serif type and timed by a 1px horizontal progress rail plus a 20px circular pause control.

Avoid: The near-empty navy/white system and five-second vitrine depend on exceptional, consistently art-directed watch photography and a deep product reservoir; with ordinary assets it becomes a slow generic carousel. Do not promote shipped Bootstrap palette tokens or the story-only chapter colors into brand accents.
