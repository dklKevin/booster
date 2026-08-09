# https://www.kleinerperkins.com (sector: vc, sweep: mode, fetched 2026-08-06)
status: full-css

## Default patterns observed (5-8 bullets)
- Hero pattern: a horizontally sliding portfolio showcase opens with a 12-column field of company names around the typed tagline “Make History,” followed by 29 company slides; each slide is a rounded, object-cover image (16:9 from 670px up, 9:16 below) with a black-to-transparent gradient, company name, one-line claim, and “Read More” pill.
- Palette: the CSS theme is essentially monochrome - `#000` black and `#fff` white as light/dark surfaces and text, `#fff9` for 60%-white secondary copy, `#d9d9d9` for light buttons, and `#272727` for hover/dark buttons; borders use translucent black/white and image slides supply the color.
- Type: the default sans is `Söhne` at weight 400 (upright and italic files); `Montserrat-ExtraLight` (200) and `Montserrat-Light` (400) are also loaded, but their homepage role is unverified. Homepage headings and navigation largely use restrained 12–20px utility sizes rather than a giant display headline.
- Layout: a centered max-width system (`margin-inline: max(22px, 50% - 634px)`) and responsive 6/12-column grid underpin the page; the dominant structure is one oversized carousel followed by “History in the Making …,” a horizontal perspectives carousel showing one, two, or three 16:9 cards by breakpoint.
- Imagery: company-specific brand/editorial assets, not one consistent stock-photo set - verified samples include a dark close-up of a Google mobile UI, a pastel-gradient Engram logo card, and a smoky dark Saronic logo card. Hero sources provide separate desktop and portrait-mobile crops, all rendered `object-cover`.
- Trust signals: credibility is staged as portfolio recognition rather than badges or accreditations - the opening name field includes Google, Amazon, Spotify, Stripe, Anthropic, Figma, Waymo, and others, while company slides open detailed case-study modals and related perspective cards. Homepage badges/accreditations are unverified.
- CTA/footer pattern: interaction stays low-pressure and editorial - repeated translucent glass “Read More” pills (`#d9d9d90d`, 4px blur), a plain “View All” perspectives link, carousel arrows, and no verified homepage contact/fundraising CTA. The footer is a compact 12-column directory with About, Company, Connect, and Login groups, an LP Login, theme toggle, and copyright; mobile converts the groups to accordions.

## Tells (3 one-liners)
- A wall of famous portfolio-company names with a terse “Make History” line standing in for a conventional value-proposition hero.
- Full-bleed 16:9 portfolio case-study slides with bottom-left white copy, dark gradient, and glass “Read More” pills.
- Monochrome Söhne typography and large whitespace, with borrowed color arriving almost entirely through founder/company brand assets.
