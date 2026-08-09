# https://www.chewy.com (sector: retail, sweep: mode, fetched 2026-08-09)
status: full-css

## Default patterns observed (5-8 bullets)
- The opening is a personalized account-and-offer module rather than a single editorial hero: “Welcome to Chewy” and “Hey, friend! Sign in” lead into two offer/CTA pairs - “Save 50% on first Pharmacy order / Set up a prescription Autoship” and “Save 35% on first order / Set up an Autoship.”
- Palette roles verified in fetched CSS are Chewy/CTA blue `#1c49c4` (an alternate bundle also falls back to `#1c49c2`), transaction orange `#f06c00`, dark display navy `#002857`, body text `#121212`, pale divider/surface gray `#ededed`, and white `#ffffff`.
- Typography tokens set Gordita as the display and text face, followed by Verdana, Lucida Sans, Helvetica Neue, Arial, Roboto, and sans-serif fallbacks; the linked font CSS also defines Work Sans, Poppins, Roboto, and multiple Gordita faces. Homepage component CSS repeatedly applies Gordita to headings, paragraph, product, and utility styles at weights 400, 500, and 700.
- The page is a stacked retail feed: “Who are you shopping for today?” pet tiles, “Explore popular categories” tiles, promotional image banners, the seasonal “Keep the summer fun going!” SKU carousel, and a four-item “Pet parenting made easy” service grid. Source recipes explicitly identify `layoutType:"grid"`, `standard-nonsku-collection`, `hero-carousel`, tile carousels, and product carousels.
- Imagery is commerce-first: square 920×920 JPEG category tiles, campaign banners whose alt text carries offer copy, brand-logo rows (Purina Pro Plan, Hill’s, Blue Buffalo, Royal Canin, Bark), and product thumbnails paired with full product names and “Add to Cart.” The fetched source does not verify a single dominant photography treatment beyond those formats.
- Trust and retention are staged as savings plus service access: 35% first-order Autoship, 50% first Pharmacy Autoship (with exclusions and a $50 maximum in banner copy), Chewy+ “Free shipping plus 5% rewards,” “Award-winning 24/7 customer care,” free chat with a licensed vet team, prescription delivery, and pet insurance.
- CTA language is short and transactional - “Shop now,” “Shop toys & more,” “Start free trial,” “Set up an Autoship,” and repeated “Add to Cart.” CSS separates general primary CTA blue `#1c49c4` from purchase-action orange `#f06c00`.
- Footer weight is unverified: fetched HTML exposes a separately mounted `chewy-footer`/header-footer SPA hook, but not enough rendered footer content to confirm its columns, density, or visual depth.

## Tells (3 one-liners)
- A personalized welcome immediately split into percentage-off Autoship and Pharmacy offers.
- Pet-type tiles followed by category tiles, promotional banners, and a horizontally repeated “Add to Cart” product carousel.
- Blue general CTAs plus a distinct orange purchase action, reinforced by free-shipping, rewards, 24/7 care, vet, pharmacy, and insurance messaging.
