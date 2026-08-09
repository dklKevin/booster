# https://corporate.walmart.com (sector: fortune500, sweep: mode, fetched 2026-08-06)
status: full-css

## Default patterns observed (5-8 bullets)
- Full-bleed campaign hero: separate desktop/mobile back-to-school photographs, a 21:9 desktop and 4:5 mobile aspect ratio, `object-fit: cover`, a 15% black overlay, centered white headline/subheadline over the image, and a single white pill CTA; the headline is 72px desktop and 36px mobile.
- Palette is a corporate blue system on white: primary/accent blue `#0053E2`, pressed/deep blue `#001E60`, Spark yellow `#FFC220`, pale sky blue `#E9F1FE`, dark text/active fill `#2E2F32`, gray text `#74767C`, separators `#E3E4E5`, and white `#FFF`; the rendered footer explicitly uses `#F2F2F2` with `#333` text.
- Type is proprietary sans throughout: “Everyday Sans Headline Web” for headings (local WOFF/WOFF2 files, weights 300–900) and “EverydaySans” for body/UI, with Arial/Helvetica/sans-serif fallbacks; headings are set bold and the hero uses a 900-weight headline.
- The page stacks familiar modules: full-width hero, centered nine-card newsroom grid with one featured card, “View newsroom” CTA, five-item “Editor’s Picks” carousel with pagination and oval previous/next controls, a reversed 50/50 copy-and-photo block, then a blue Walmart+ promotional split.
- Imagery is editorial corporate/retail photography rather than illustration: back-to-school campaign imagery, associates and community portraits, products/brands, a small-business “golden ticket” winner, and a staged Walmart+ grocery bag on a modern kitchen counter are all named or described in source image paths/alts.
- Trust is staged as disclosure and proof content: the lead news grid includes an FY2026 ESG Report, a 2026 Jobs Spotlight Report, and a quantified `$500,000` flood-relief commitment; navigation exposes Investors and Purpose, while the footer adds WMT stock data with a 20-minute-delay disclaimer, policies, recalls, privacy controls, and legal notices. No accreditation badges were verified.
- CTAs are short action labels in rounded pills (`border-radius: 50px`): the hero uses “See all the ways to be prepared,” the grid uses “View newsroom,” the supplier block repeats “Apply Today,” and the membership promo uses “Start your Walmart+ free 30-day trial →”; CSS defines blue `#0053E2`, white outlined, and yellow `#FFC220` variants.
- The footer is a high-information corporate utility layer: centered black wordmark on `#F2F2F2`, primary and legal link rows, Walmart U.S./Sam’s Club/Walmart International brand marks, retail/location links, six social channels, a WMT ticker, privacy-choice and opt-out controls, pricing disclaimer, and copyright.

## Tells (3 one-liners)
- A seasonal photo hero with oversized white copy, dark image wash, and one pill-shaped “learn more” action immediately yields to a corporate newsroom grid.
- ESG, jobs, philanthropy, investor access, and a delayed stock ticker are arranged as parallel proof points rather than one narrative.
- The footer becomes a compact governance directory: brand family, policies, recalls, privacy controls, social accounts, ticker disclaimer, and copyright in one pale-gray band.
