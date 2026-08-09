# https://latch.bio (sector: biosecurity, sweep: excellence, fetched 2026-08-06)
status: full-css

## Token block (~10 lines)
- Palette / light surfaces: `#fff` background, `#fafbfc` secondary background, `#f0f1f5` pale neutral, and `#dfe1e6` light border neutral.
- Palette / ink: `#101426` primary dark surface/foreground, `#151a30` secondary dark surface, `#091e42` deep navy, and `#42526e` muted slate.
- Palette / brand: Yves blue `#001aae` is the main accent; `#1d60fa` is the brighter primary blue; `#1ce9d0` is the dark-mode accent green; the light brand gradient runs `#001aae` to `#3b58ff`.
- Type pairing: `"InterVariable", "Inter", sans-serif` for interface and body; `"Instrument Serif", serif` for `.serif` display accents; `ui-monospace, Menlo, Monaco, "Cascadia Mono", "Segoe UI Mono", "Roboto Mono", "Oxygen Mono", "Ubuntu Monospace", "Source Code Pro", "Fira Mono", "Droid Sans Mono", "Courier New", monospace` for code.
- Heading scale: 40/32/28/24/20/16px for h1-h6; h1-h2 use 1.25 line-height and -0.04em tracking, while h3-h4 use 1.45 line-height.
- Body/display scale: 40, 32, 24, 18, 16, 14, and 12px (`p-xxl` through `p-xs`), generally at 145-165% line-height; the homepage hero uses `clamp(36px, 6.5vw, 72px)` at 1.1 line-height.
- Spacing rhythm: recurring extracted increments are 8, 12, 16, 24, 32, 40, 48, 64, 80, 120, and 160px; tight component gaps are 8-16px, while section separation commonly reaches 64-160px.
- Layout system: centered 12-column percentage logic; the main container is 10/12 (83.333333%) wide, 11/12 below 576px, capped at 1280px and then 1464px on viewports at least 1536px wide.
- Layout intent: generous single-column narrative headers lead into bordered two-column evidence/product modules; benchmark browsers use `minmax(280px, .8fr) 1.2fr` and collapse to one column below 1024px.
- Signature element: an interactive benchmark-paper browser—scrolling list at left, abstract/detail pane at right—with 0.5px borders, 8px radius, Yves-blue active rails, and a paired AI-agent prompt field above it.

## Lessons (3-5 bullets)
- Make scientific evidence part of the primary interface: the paper browser exposes year, benchmark name, authors, venue, abstract, and paper link in a scan/detail pattern instead of hiding credibility in a generic resources page.
- Use one restrained technical accent consistently: `#001aae` carries headlines, selected states, links, thin borders, and gradients while white and navy surfaces preserve clinical clarity.
- Let dense scientific content breathe through hierarchy rather than decoration: 12px uppercase eyebrows, 30-64px titles, 14-18px explanatory copy, and 64-160px section spacing separate claim, evidence, and action.
- Reuse the same responsive content frame across marketing and technical pages: 83.333333% width with 1280/1464px caps supports both prose-led `/product` sections and denser two-column `/security` modules.
- Translate platform complexity into bounded interface-like artifacts—paper browsers, prompt inputs, diagrams, and product wells—so capabilities feel operable and verifiable rather than merely asserted.

## Avoid (1-2 bullets)
- Do not copy the many large gaps mechanically: 120-200px section padding and a 100vh hero can make a thinner content set feel sparse or slow.
- Do not reproduce every module accent gradient at once; the source defines separate yellow, blue, pink, green, and purple product gradients, which would weaken the disciplined Yves-blue evidence aesthetic if used without the same module taxonomy.
