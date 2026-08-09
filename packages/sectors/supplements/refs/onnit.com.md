# https://www.onnit.com (sector: supplements, sweep: excellence, fetched 2026-08-06)
status: full-css

## Token block (~10 lines)
- Palette / base surfaces: black `#000000` text and dark background; white `#ffffff` light surface and inverse text; grey `#ececec` page/base background.
- Palette / supporting neutrals: `#303434` accent text, `#aaaaaa` light/disabled text, `#d5dede` accent surface and button hover.
- Palette / brand and commerce accents: orange `#ff6a1f` primary, blue `#1A4CCB` secondary/focus, red `#A12E21` tertiary/sale/error, yellow `#ffb200` tags/warnings.
- Type pairing: headings use `"Founders Grotesk Cond SmBd", Helvetica, Arial, serif`; body uses `"Sohne", Helvetica, Arial, sans-serif`; regular headings can use `"Founders Grotesk", Helvetica, Arial, serif`.
- Display scale: H1 `64–72px`, then `144–176px` from 1080px; H2 `43–53px`, then `64–79px`; H3 `28–35px`, then `43–53px`; all at `80%` line-height and uppercase.
- Supporting scale: H4 `19–22px`, H5 `16px`, H6 `14px`; body `17px` at `1.625` line-height; hero display `38–48px`, then `60–160px` from 1080px.
- Spacing rhythm: `2, 4, 8, 12, 16, 24, 32, 40, 48, 56, 64, 72, 80px`; default section spacing `24px`, desktop `48px`.
- Insets and gaps: container padding `15px` / desktop `30px`; grid gap `8px` mobile and `16px` desktop; pill buttons use `15px 60px` padding and `40px` radius.
- Layout intent: full-bleed media and content share an 8-column mobile / 24-column tablet-desktop grid, capped by `--max-width: 1920px`; hero aspect ratios are `2 / 3` mobile and `3 / 1` desktop.
- Signature element: oversized condensed uppercase hero copy (`60–160px` desktop, `80%` line-height) reveals upward from an overflow-hidden wrapper over full-bleed cover media.

## Lessons (3-5 bullets)
- Treat supplement commerce like an editorial campaign: reserve the condensed face and extreme scale for claims and section ideas, while keeping evidence, descriptions, and controls in the calmer 17px Sohne body face.
- Use one responsive grid for both full-bleed storytelling and dense shopping UI; named full/main grid lines let media reach the viewport while copy and controls retain consistent alignment.
- Build product-family variety from a stable neutral base, then assign saturated orange, blue, red, or yellow to explicit roles such as primary, focus, sale, and tags rather than decorating every surface.
- Keep the mobile narrative portrait (`2 / 3`) and the desktop narrative cinematic (`3 / 1`), with independently placed content on the same underlying grid.
- Pair dramatic typography with restrained interaction tokens: a `.2s ease` default transition, simple 1px borders, and pill-shaped calls to action keep the system legible and commercially direct.

## Avoid (1-2 bullets)
- Do not copy the `144–176px` H1 tier without the condensed font, `80%` line-height, wide canvas, and short uppercase phrases; longer claims will overwhelm the layout.
- Do not treat all saturated colors as interchangeable brand accents; the source assigns them distinct semantic roles, and flattening those roles would weaken product-state and feedback clarity.
