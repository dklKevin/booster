# https://www.gnu.org (sector: opensource, sweep: mode, fetched 2026-08-06)
status: full-css

## Default patterns observed (5-8 bullets)
- Hero pattern: there is no visible H1 or slogan-led hero; the main column opens with a centered 512×288 HTML video (`Escape to Freedom`) at `width: 32em; max-width: 100%`, then the “What is GNU?” H2, explanatory copy, and a bordered “Try GNU/Linux” CTA.
- Palette: white content sits on a `#e4e4e4` page field with `#bbb` border/shadow and `#222` body text; the GNU brand/nav uses `#a32d2a` with a `#800300` hover state, normal links are `#049` and visited links `#503`, and CTA links use `#55b` on white with `#ebebff` hover fill.
- Type: the base body and headings have no explicit family in the fetched CSS (browser default, therefore the rendered family is unverified); ordinary links explicitly use `sans-serif`, utility/header/button text uses `"Noto Sans Display", "Noto Sans", "Liberation Sans", sans-serif`, and navigation uses `"Dosis"` followed by the same fallbacks. H2 is bold at `2em`.
- Layout: a centered body is capped at `74.92em`; homepage content is two stacked `46em`-maximum columns until `60em`, then becomes a `65%` article column plus a `30%` complementary sidebar. The article proceeds as long explanatory sections, freedom lists, GNU/Linux screenshot thumbnails, and text links rather than a card grid or carousel.
- Navigation/CTA pattern: a full-width maroon bar contains 16 bold, uppercase inline destinations; calls to action are mostly text links, with the primary GNU/Linux choices rendered as white, `#55b` bordered, `.3em`-radius buttons and FSF actions repeated as JOIN, DONATE, and SHOP outlined buttons.
- Imagery style: verified assets are project-owned functional media - a small GNU-head logo, search/language icons, an FSF video poster, six 128×72 desktop-distribution screenshots, an RSS icon, a Tor Snowflake graphic, and package logos; no stock-photo hero or abstract product render is present in the fetched homepage.
- Trust signals: authority is staged through the “Supported by the Free Software Foundation” label, an FSF nonprofit mission statement and logo, the stated 1983 project origin, named sister organizations, current release/community feeds, maintainer requests, copyright/license text, and a page-updated timestamp; badges, customer counts, and third-party accreditations are unverified.
- Footer weight: a distinct white FSF mission band with a `3px solid #999` top rule and three support CTAs precedes a `#f4f4f4` footer (`.875em`, `1.5em 3%`, another `3px solid #999` rule) carrying contact, translation, copyright, Creative Commons license, infringement, and update details.

## Tells (3 one-liners)
- A small GNU-head wordmark immediately above a maroon, all-caps navigation strip packed with 16 destinations.
- A headline-free opening that leads with an embedded advocacy video and then drops directly into “What is GNU?” documentation copy.
- Alternating pale lavender (`#eef` to white) and cyan (`#dff` to white) sidebar boxes filled with feeds, action items, and maintainer requests.
