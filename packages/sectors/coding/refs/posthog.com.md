# https://posthog.com (sector: coding, sweep: excellence, fetched 2026-08-06)
status: full-css

## Token block (~10 lines)
- Palette / primary surface: #FDFDF8 background, #111111 primary text, #65675E secondary text, #9EA096 muted text.
- Palette / structure: #E5E7E0 accent surface and #BFC1B7 border on the primary light scheme.
- Palette / nested surfaces: #EEEFE9 secondary background, #D2D3CC secondary accent, #B6B7AF secondary border.
- Palette / emphasis: #2F80FA blue (the homepage hero highlight), plus #F54E00 red, #EB9D2A orange, #6AA84F green, #F7A501 yellow, and #A621C8 fuchsia.
- Type pairing: RoundHog, sans-serif for the site body/UI; Source Code Pro, Menlo, Consolas, monaco, monospace for code; IBM Plex Sans Variable is also bundled for product UI.
- Type scale: 12/16, 14/20, 16/24, 18/28, 20/28, 24/32, 30/36, 36/40, 48/48, 60/60, 72/72px; the homepage hero is 30/36px and becomes 36/40px at its `@xl` container breakpoint.
- Body copy: the homepage intro uses 17px text; the global body uses RoundHog and #151515, while the semantic primary scheme resolves text to #111111.
- Spacing rhythm: a 4px base expressed as 4, 8, 12, 16, 20, 24, 32, 40, 48, 64, 80, and 96px utilities; homepage reader padding steps from 16px through 24, 32, 48, 64, and 80px by container width.
- Layout intent: responsive container queries drive a single-column-to-two-column reader; core homepage content uses a 64rem (`max-w-5xl`) centered measure, with 32px two-column gaps and 64px section-grid gaps.
- Signature element: the page is framed as a web desktop/application, with `app-reader`, `app-scroll-area`, `window-expand-control`, window-slide animation, and embedded product UI rather than conventional flat marketing screenshots.

## Lessons (3-5 bullets)
- Let the product metaphor organize the whole site: PostHog carries app-reader, scroll-area, window-control, and product-interface patterns from the homepage into structurally different docs and pricing pages.
- Use a quiet semantic surface ladder (#FDFDF8 → #EEEFE9 → #E5E7E0) so dense product UI can create hierarchy without relying on many saturated fills.
- Reserve saturated color for meaning and small emphasis: the hero puts #2F80FA at 10% behind one phrase, while most layout and copy stay on neutral semantic tokens.
- Scale layouts from their own available width with named container contexts (`app-reader`, `reader-content`, and `reader-content-container`), not only from the viewport.
- Pair a characterful proprietary face (RoundHog) with a practical code face (Source Code Pro) to keep an engineering site personable without weakening technical credibility.

## Avoid (1-2 bullets)
- Do not copy the desktop/window treatment as decoration alone; without real product UI and consistent behavior across interior pages, it becomes a cumbersome visual costume.
- Do not reproduce every bundled accent color at equal prominence; the observed homepage hierarchy depends on neutral surfaces and sparse, semantic color emphasis.
