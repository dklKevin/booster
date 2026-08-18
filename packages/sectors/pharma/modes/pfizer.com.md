# https://www.pfizer.com (sector: pharma, sweep: mode, fetched 2026-08-06)
status: full-css

## Default patterns observed (5-8 bullets)
- Hero: full-width 1921x711 molecular/cell render with a deliberately dark left field behind a white H1, explanatory paragraph, and one solid primary CTA; the source supplies separate desktop, tablet, and portrait-mobile crops, while CSS uses `object-fit: cover` and a 600px landing-hero minimum height at large sizes.
- Palette: white base `#ffffff` and near-black text `#0a0a0a`; primary CTA/brand field `#2e29ff` (`--pfizer-blue-60`), link blue `#0000c9` (`--pfizer-blue-70`), bright cyan `#0095ff`, pale cyan `#e0f5ff`, pale blue `#e8f2ff`, and muted eyebrow gray `#666666`. Homepage sections explicitly alternate `#F2F9FC`, `#0095ff`, `#2e29ff`, and `#E0F5FF` fields.
- Type: custom `PfizerDiatype` family (Regular for body, Medium for eyebrow labels, plus Bold/Black/Heavy/Light/Thin/Ultra files) with Arial fallback; `PfizerTomorrow` and `PfizerDiatypeMono` files are also bundled. Typography is a clean corporate sans hierarchy with large H1/H4 statements, small muted eyebrow labels, and heavier CTA/link weights.
- Layout: long modular scroll built from responsive two-column splits, an Impact Report image/text promo beside stacked Articles and Press Releases lists, a product-search/RxPathways split, a large pipeline infographic, an Areas of Focus Swiper carousel, full-width text statements, a colored image/text Accord band, and a newsletter signup band.
- Imagery: science visualization leads - soft-focus floating cells in the hero, blue/white molecular-ribbon renders in focus-area cards, and an animated 3D pipeline graphic - mixed with polished human-impact photography (a smiling woman and child) and a branded globe illustration; responsive `<picture>` sources and rounded-image utility classes are present.
- Trust signals: credibility is staged as quantified process and pipeline evidence rather than badges: “1,500 scientists,” “500,000 lab tests,” “over 36 clinical trials,” and an August 4, 2026 pipeline snapshot of 37 Phase 1, 25 Phase 2, 31 Phase 3, 2 registration, 95 total; this is reinforced by the 2025 Impact Report, dated press releases, 1849 origin story, and a downloadable pipeline PDF. Accreditations are unverified.
- CTA/footer pattern: repeated solid-blue primary buttons (`#2e29ff` with white text), secondary outlined controls, inline “More … >” links, search/arrow buttons, and stacked “Learn/Explore/Read/Sign up” actions. The footer is heavy and institutional: logo plus three link columns, country picker, copyright, US-only/product-labeling disclaimers, and five social channels.

## Tells (3 one-liners)
- A white mission headline laid over a darkened microscopic-cell hero, followed immediately by a “Learn more” button.
- Oversized clinical-pipeline phase counts paired with an animated molecular/3D science graphic and PDF download.
- Alternating white, pale-cyan, electric-blue, and violet-blue corporate modules that cycle through products, patient help, focus areas, impact, and newsletter signup.
