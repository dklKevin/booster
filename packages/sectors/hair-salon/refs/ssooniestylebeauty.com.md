# https://ssooniestylebeauty.com (sector: hair-salon, sweep: excellence, fetched 2026-08-15)
status: full-css

## Token block (~10 lines)
- Palette / foundation: `#ffffff` is the page and header field, `#3a3a3a` carries primary ink and solid actions, `#333232` carries supporting and footer text, and `#f6f6f6` closes the page behind the retail footer.
- Palette / identity: the announcement strip uses vivid pink `#ff73be`; `#ff90cb` is declared for linked-announcement hover, although the current announcement is plain text. White carries its message and all text over photography.
- Palette / image treatment: `#685858` veils hero and linked portrait photography at `0.4` opacity, increasing to `0.8` on hover or focus; `#f7f7f7` is the verified image-loading ground and `#ebebeb` is the quiet border token.
- Type system: rendered header, display, body, product, and action text all use `Helvetica, Arial, sans-serif`; display, product titles, and actions use weight 700 while body and navigation use 400.
- Display scale: the hero title is 35/42px desktop and 32/38.4px narrow; linked portrait captions are 26/31.2px and 20/24px, while retail section headings are 20/24px and 18/21.6px across the same layouts.
- Supporting scale: body and navigation render at 15/22.5px, the announcement is 16/24px, product titles measure 17/20.4px desktop and 14/16.8px narrow, and hero actions are 13/19.5px with `0.08em` tracking.
- Spacing and shape: standard sections use 55px vertical padding desktop and 35px narrow; content gutters switch from 55px to 22px and grid gaps from 30px to 22px. Actions use a restrained 2px radius with 10px 18px desktop padding and 8px 15px narrow padding.
- Frame and responsive behavior: retail content caps at 1200px, while the hero and portrait bar remain full bleed. Below 750px the 475px hero becomes 357px and three equal portrait columns become three stacked tiles capped at 400px and centered on white.
- Motion: the final in-salon video is an 81.9-second muted, looping, plays-inline autoplay that starts when brought into view; its cover frame measures 800px high desktop and 500px narrow. Linked portrait captions declare a `100ms` cubic-bezier transition.
- Signature element: a wide three-portrait hair collage headed only by `#ssooniestyleteam` and a booking action hands directly to three more portrait panels labeled Salon Experience, Salon work, and Salon Playlist.

## Lessons (3-5 bullets)
- Make hair results the category signal. Six face-and-hair portraits fill the opening sequence before the catalog begins, so cut, color, finish, and point of view are visible without a generic beauty promise or an interior-only hero.
- Give different kinds of social proof different doors. The three portrait panels route to Yelp experience, Instagram work, and a YouTube playlist with plain labels rather than presenting one undifferentiated social feed.
- A salon with meaningful product sales can join appointment and retail tasks without disguising either one: booking stays in the header and hero, while product collections retain prices, sold-out states, cart, search, and checkout infrastructure.
- Substantiate Korean hair specialization in the service inventory. The live booking layer exposes 35 services across seven categories, including digital and setting perm, down perm, magic straight perm, cuts for men, women, and children, and a free consultation.
- Carry operational detail into the booking handoff. The verified flow includes ten named professionals plus an any-stylist option, daily hours, address, map, phone, parking and valet instructions, starting prices, and a 24-option language menu that includes Korean, Japanese, Vietnamese, Chinese, and traditional Chinese.

## Avoid (1-2 bullets)
- Do not copy the exact pink announcement strip, Helvetica system, brown photo veil, or three-panel collage followed by three portrait tiles; transfer the principle of making recognizable hair work carry the opening identity.
- Do not copy the split ownership of essential information: the salon site quickly becomes a retail catalog and sends reviews, portfolio, and all service operations elsewhere. Keep key service, price, duration, location, and consultation facts on the owned site; the verified booking flow omits durations, warns that shown availability may be inaccurate, and the homepage's feminine portrait and heart cues underrepresent the men's and children's services in its own menu. Give the autoplay loop a reduced-motion fallback, which the fetched CSS does not provide.
