# https://www.luxcapital.com (sector: vc, sweep: excellence, fetched 2026-08-06)
status: full-css

## Token block (~10 lines)
- Palette / canvas: blue-black #16191e; deeper near-black #121418; secondary panel blue #1e2229.
- Palette / text: blue-grey neutral #d9e0e9 on dark; smoke #efeeeb for light sections; muted slate #5c6778 and grey-blue #8493ab.
- Palette / accent: Lux red #ff1c24; low-contrast rules and fills use source alpha tokens such as #efeeeb1a and #16191e1a.
- Type pairing: Brown, sans-serif for body and display (weights 300, 400, 700); Spacemono, sans-serif for uppercase labels and metadata (400, 700, plus italics).
- Type scale: 13px mono labels; 14px small; 16px base; 20px medium/body; 24px large; 32px body display; 40px heading; 48px page heading; 64px small display/interior hero; 120px primary display.
- Type behavior: display text is uppercase at 1.0 line-height; body defaults to 16px/1.5; 20px body uses 1.4; the interior hero is 64px/1.1 with a 24ch maximum.
- Spacing rhythm: an 8px base is visible in .5rem, 1rem, 1.5rem, 2rem, 2.5rem, 3rem, 4rem, 5rem and 7.5rem increments; major sections commonly use 5rem or 7.5rem vertical padding.
- Layout intent: full-width dark editorial canvas inside a 100rem max-width container, with 5rem desktop gutters collapsing to 1rem at <=991px; grids and horizontal scrollers carry dense portfolio/media content.
- Responsive scale: the 120px primary display drops to 64px at <=991px and 40px at <=479px; the 64px interior hero drops to 40px at <=767px.
- Signature element: a two-row, offset uppercase “WE TURN / SCI-FI / INTO / SCI-FACT” hero interleaves four autoplaying looped video tiles over a repeating plus-gap SVG at 5% opacity.

## Lessons (3-5 bullets)
- Make the investment thesis the composition itself: Lux splices moving frontier-technology footage directly into its four-part “sci-fi” to “sci-fact” claim instead of placing a generic reel behind a headline.
- Separate expressive and operational typography: Brown carries large thesis statements and readable prose, while 13px uppercase Space Mono makes filters, categories and metadata feel technical without forcing the whole site into a code aesthetic.
- Let portfolio proof become an immersive chapter: the homepage showcase uses a 300vh section with a sticky panel, large company names and restrained metadata, while the companies page switches to a practical grid and filters.
- Preserve hierarchy across page types: the homepage earns a 120px display treatment, but interior pages use a balanced 64px, 24ch title and then return to 16–24px content scales.
- Use a narrow token set with alpha variants: #16191e, #d9e0e9, #efeeeb and #ff1c24 recur across backgrounds, copy, borders and actions, creating range without introducing unrelated colors.

## Avoid (1-2 bullets)
- Copying the four autoplay loops and 300vh sticky showcase without aggressive media optimization and motion/accessibility handling would make the experience heavy and tiring rather than cinematic.
- Reusing 120px uppercase Brown display type on routine portfolio or news pages would flatten the hierarchy; Lux reserves it for the thesis-led homepage and scales interior titles down to 64px.
