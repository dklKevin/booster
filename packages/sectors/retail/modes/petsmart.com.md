# https://www.petsmart.com (sector: retail, sweep: mode, fetched 2026-08-09)
status: full-css

## Default patterns observed (5-8 bullets)
- Hero: a rounded (`12px`) split campaign block, with a left offer panel and right lifestyle image on desktop, stacking image above copy on mobile; the fetched campaign uses `#6F7A6F`, white copy, the H1 “Save an EXTRA 20% OFF,” a coupon/deadline line, and a “Shop now” button beside a dog, cat, and guinea pig promotional photo.
- Palette: the CSS theme makes `#206EF6` the primary/link/button blue, `#131313` the main body text, `#FFFFFF` the body background, and `#F7F7F7` the neutral container/footer tone; brand tokens also include red `#FE3744`, green `#24AA2E`, and yellow `#F6E84A`. Campaign modules override this system with merchandising colors such as hero green-gray `#6F7A6F` and essentials-section beige `#D5D2C3`.
- Type: `Euclid` is the declared primary family for the Sparky UI and footer; `Proxima Nova A Black` is preloaded, but its specific homepage role is unverified. Legacy header CSS explicitly uses Arial/Helvetica, producing a mixed current/legacy typography stack.
- Layout: the page is a long merchandising sequence of six-up category/logo carousels, three-up promotional cards, a four-card services stack, horizontal product carousels, and repeated full-width campaign banners; CSS caps the main container at `78.5rem` and switches the hero from stacked to side-by-side at `60rem`.
- Imagery: source alt text verifies staged pet lifestyle photography (pets on beds/rugs, pets wearing products), isolated package/product packshots, brand-logo tiles, and illustrated event/fulfillment banners; seasonal campaign art and deal callouts are interleaved with the product imagery.
- CTAs: short transactional labels recur - “Shop now,” “Shop all,” “Activate,” “Learn more,” “Find a store,” “Enter now,” and “Download now.” The tokenized primary button is blue `#206EF6` with white text; the fetched hero instead uses a white secondary button with blue text.
- Trust and footer: reassurance is staged through “11,765,235 lives saved,” Treats Rewards points multipliers, a Price Match Promise, Autoship and fulfillment claims (“2 hours or less,” “FREE Shipping on orders $49+”), plus LegitScript Certified and .pharmacy badges. The footer is heavy: four desktop columns containing 21 navigation links, followed by social icons, two trust badges, copyright, and six legal/privacy links.

## Tells (3 one-liners)
- A coupon-and-deadline split hero immediately hands off to a six-across “shop by” carousel.
- Pet cutouts, package packshots, logo tiles, and red deal callouts repeat inside the same rounded merchandising-card system.
- A long pre-footer converts convenience promises into four illustrated fulfillment options before an equally dense four-column link footer.
