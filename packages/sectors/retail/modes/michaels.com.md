# https://www.michaels.com (sector: retail, sweep: mode, fetched 2026-08-09)
status: full-css

## Default patterns observed (5-8 bullets)
- Hero: a Slick carousel of promotion slides, with cloned slides and dot navigation. Each slide is a 50/50 text-and-image split from 640px upward and a stacked layout below that breakpoint; the image panel is 250px tall on small screens. The first verified slide leads with “70% off All Custom Frames. Online Only.”, supporting copy, and “Shop Now”; its text half uses `#86858A`, while the lazy hero image URL is unverified in the returned slide markup.
- Palette: Michaels primary/action red is `#CF1F2E` with `#B8002E` hover; primary ink is `#1C1C1C`/`#1B1B1B`, white is `#FFFFFF`, light surface/disabled fill is `#F8F8F8`, semantic link blue is `#0475BC`, and focus blue is `#006BA6`. Seasonal modules also introduce values such as orange `#FF9B2E`; MakerPlace uses `#517A9A` with `#3F6079` hover.
- Type: CircularStd is the Michaels display face (verified hero Display2: 32px, weight 900); Inter handles headings, body, controls, and buttons (verified body: 16px/150%, weight 400; buttons: 16px/24px, weight 700). MakerPlace display text switches to Gelica-Light (verified Display2: 24px/120%, weight 400).
- Layout: after the promotional carousel, the source exposes stacked merchandising bands titled “Trending at Michaels,” “Shop by category,” “More at Michaels,” and “Learn with Michaels,” using responsive grids that range from 2 to 6 columns, plus campaign panels such as “The Knit & Sew Shop” and “New party theme must-haves.”
- Imagery: verified alt text shows product-first craft imagery - isolated or tightly cropped yarn, fabric, frames, balloons, beads, paint, tools, and supplies - mixed with hands-on project photography such as hands adding flowers to a wreath, handmade squishy balloons, and diamond-art bookmarks. The exact first hero image is unverified.
- CTAs: repeated imperative commerce labels (“Shop Now,” “Shop All Halloween,” “Shop Lemax®,” “Shop New Arrivals”) appear as rounded pills. Verified primary buttons use `#CF1F2E` with white text, 12px 20px padding, and a 100px radius; secondary buttons use white, a 2px `#1C1C1C` outline, and a 28px radius.
- Trust/service staging: confidence is built through quantified assortment and convenience copy - “1,000s of items,” “700+ styles,” “4,500 party supplies,” “60+ trending party themes,” “easy pickup and delivery” - and through “More at Michaels” service content including Michaels Rewards, pickup/same-day delivery, and MichaelsPro Education. Accreditation or third-party trust badges are unverified.
- Footer: the fetched footer is relatively light rather than a dense retail directory: a centered email capture with marketing-consent copy, a black `#1B1B1B` pill “Sign up” button, social links (Facebook, Instagram, Pinterest, Twitter, YouTube), copyright, and an Accessibility Statement; a multi-column footer link index is unverified.

## Tells (3 one-liners)
- A rotating, percentage-off hero that pairs urgency copy with a rounded “Shop Now” button.
- A long stack of named merchandising grids - trending, categories, services, and learning - each driven by product or project thumbnails.
- Assortment counts, pickup/delivery reassurance, rewards/service cards, and an email-offer signup used as the confidence layer.
