# https://www.adafruit.com (sector: retail, sweep: excellence, fetched 2026-08-09)
status: full-css

## Token block (~10 lines)
- Palette / ground and ink: #FFFFFF page ground, #000000 primary text and shop header/footer, #333333 product-card text.
- Palette / commerce action: #0062C7 links, cart, buttons, and rules; #003C7B link/button hover; #FFFFFF action text.
- Palette / support: #F0F0F0 news-ticker ground, #767676 ticker label, #DDDDDD card borders, #999999 dividers, #666666 metadata.
- Palette / states: #158930 green action, #0C4A1B green hover, #E90000 sale/error, #DD007A search focus ring.
- Type family: "Proxima Nova", "Lucida Grande", "Lucida Sans Unicode", "Lucida Sans", Geneva, Verdana, sans-serif; self-hosted Proxima Nova at 300, 400, and 500.
- Type scale: desktop body 14px/1.4286; mobile body 16px; H1 30px/30px at 400; H2 18px/18px bold; homepage section H2 30px/1 at 400; product copy 15px; price 30px at 700.
- Controls: 14px labels in 30px-high buttons; prominent buttons are 18px in 40px, while mobile purchase controls rise to 50px.
- Spacing rhythm: 10px grid gutters and common increments of 10/20/40px; main content has 20px vertical padding, homepage sections 40px vertical margins, product cards 20px internal padding/gaps.
- Layout: centered responsive containers cap at 460/728/980/1300px, with 10px side padding and a 12-column Bootstrap grid; the header independently uses a 1300px CSS-grid track.
- Layout intent: dense, operational retail chrome frames generous product imagery; homepage cards run four-up at 310px, category previews expand 2/3/4/6 columns, and desktop product pages reserve 9/12 columns for a 970px-capable gallery and 3/12 for a sticky 310px buying rail.
- Signature element: a whimsical, campaign-specific AdaBot illustration occupies a 1300x436 hero inside a 14px rounded frame, placing maker culture ahead of the catalog grid.

## Lessons (3-5 bullets)
- Let search, category access, account state, and cart remain continuously legible in a compact two-tier header; the brand color is concentrated on links, the cart, and the 5px rule beneath the black shop bar.
- Treat technical product photography as the main merchandising surface: keep a consistent 4:3 ratio, supply large 970px imagery plus thumbnails/video, and give the gallery three quarters of the desktop product layout.
- Pair editorial discovery with direct commerce: the homepage alternates campaign art, a live news strip, shoppable new/featured cards, shopping guides, and a learning-guide feature without hiding prices or add-to-cart actions.
- Scale assortment by changing visible column count rather than shrinking cards indefinitely: category previews move from 2 to 3 to 4 to 6 columns at the 768/1024/1366px breakpoints.
- Use compact 10/20px mechanics for dense catalog UI, then create hierarchy with 40px section intervals and 30px headings/prices instead of excessive decoration.

## Avoid (1-2 bullets)
- Copying the 14px desktop body size without the site's strong contrast, short labels, and enlarged 15-18px product/navigation contexts would make a catalog feel cramped.
- Repeating the 14px rounding on generic cards would miss the point: Adafruit earns it through distinctive maker artwork, real product media, dense technical detail, and blunt commerce controls.
