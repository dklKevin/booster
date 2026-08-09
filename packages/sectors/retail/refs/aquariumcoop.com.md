# https://www.aquariumcoop.com (sector: retail, sweep: excellence, fetched 2026-08-09)
status: full-css

## Token block (~10 lines)
- Palette - primary ground #FFFCF0; body ink rgba(0,0,0,.81); heading ink #000000; link/action green #10891A.
- Palette - masthead field #036626 with #FFFFFF foreground; the header is the strongest brand-color block.
- Palette - footer/secondary ground #F2EDE9; optional pale-blue surface #E1EDF5; dark surface #333333.
- Palette - input fill #FFFFFF, input ink #333333, input border #DFDFDF; stock states #3ED660 / #EE9441 / #C8C8C8.
- Type - all body, heading, subheading, and accent roles use `"system_ui", -apple-system, "Segoe UI", Roboto, "Helvetica Neue", "Noto Sans", "Liberation Sans", Arial, sans-serif`; weights are 400, with h5 overridden to 600.
- Type scale - paragraph 1rem; h6 .75rem; h5 1rem; h4 1.25rem; h3 1.875rem; h2 2.25rem; h1 2.5rem; auxiliary ladder .625/.75/.8125/.875/1/1.125/1.25/1.5/2/2.5/3/3.5rem.
- Leading - body 1.4; h1-h4 1.1; h5-h6 1.2; available body presets 1.2/1.4/1.6 and heading presets 1.15/1.25/1.35.
- Spacing - reusable margin/padding/gap tokens cluster at .125, .25-.3, .5, .7-.9, 1, 1.25, 1.5, 1.75, 2, 3, and 4-5rem; section padding commonly uses `max(20px, scale * value)`.
- Layout - 16px page margins below 750px and 40px above; active homepage cap 90rem, with 120rem and 150rem normal/wide tokens; product grid is 6 columns desktop and 2 mobile, while articles become a 4fr/1fr content-sidebar grid.
- Signature element - a randomized two-slide image banner (5s autoplay; 17.5rem mobile and 26.25rem desktop minimum height) hands directly into a zero-gap, square-image 6-column product mosaic.

## Lessons (3-5 bullets)
- Let branded chrome do the identity work, then keep the selling surface warm and quiet: the #036626 header clearly frames a predominantly #FFFCF0 catalog without tinting every card.
- A broad assortment can read as one confident visual wall when square product photography supplies the rhythm: the homepage uses no row or column gap and changes from six columns to two instead of introducing extra card decoration.
- Treat education as retail infrastructure: the article template pairs long-form content with a 4:1 sidebar containing search, subscription, recent posts, and featured products, so advice and discovery stay connected.
- Give product pages room to teach after the buy decision: the source uses a half-width media/details grid followed by dosing, growth, guarantee, safety, recommendations, reviews, and FAQ sections.

## Avoid (1-2 bullets)
- A zero-gutter six-column grid will turn chaotic if image ratios, crops, or backgrounds are inconsistent; this implementation depends on 1:1 product media and hairline card borders.
- Copying the green masthead plus warm cream ground wholesale would reproduce the brand more than the principle; transfer the strong-chrome/quiet-catalog contrast, not these exact colors.
