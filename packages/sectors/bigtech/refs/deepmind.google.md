# https://deepmind.google (sector: bigtech, sweep: excellence, fetched 2026-08-06)
status: full-css

## Token block (~10 lines)
- Core light palette: surface #ffffff; ink/on-surface #121317; secondary text #45474d; container #f8f9fc; raised containers #eff2f7, #e6eaf0, #e1e6ec; outline rgba(33, 34, 38, 0.12).
- Dark palette: surface #121317; ink #f8f9fc; secondary text #b2bbc5; containers #18191d, #212226, #2f3034, #45474d; outline rgba(230, 234, 240, 0.12).
- Accent/data palette: blue #3186ff / pale #dcf1ff; green #00af57 / pale #daf9d4; red #fc413d / pale #ffeef7; yellow #fec700 / pale #fcffad; Gemini gradient #3b6bff 0%, #2e96ff 65%, #acb7ff 100%.
- Type pairing: Google Sans Flex, Arial, Helvetica, sans-serif for display and body; Google Sans Code, monospace for code; Google Symbols for icons.
- Body type: 17.5px/1.45, weight 400, letter-spacing 0.01188em; display headings use weights 400-500 and line-height 1.06-1.14 with slight negative tracking.
- Responsive type scale: through 1023px, 10, 14.5, 17.5, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38px; at 1280px+, display steps expand to 20, 22, 24, 28, 32, 42, 54, 72, 98, 124, 148px.
- Base spacing rhythm: 4, 8, 16, 24, 28, 36, 40, 48, 60, 64, 72, 80, 88, 120, 180px; semantic spacers are 4, 8, 16, 24, 36, 48, 60, 80, 88, 120px.
- Responsive page geometry: margins/gutters are 28/28px below 1024px, 40/40px at 1024px, 72/48px at 1280px, and 72/64px at 1728px.
- Layout intent: centered max-width 1440px; 4 columns below 768px, 8 columns from 768px, and 12 columns from 1024px, with full-bleed media nested inside disciplined grid-aligned text.
- Signature element: a leading carousel of autoplaying, muted 2:3 motion promo cards with media scrims, overlaid text, and 24px rounded clipping (the source also supplies light/dark alternate media).

## Lessons (3-5 bullets)
- Let one responsive grid serve both spectacle and scholarship: the same 4/8/12-column system supports motion-heavy landing pages, peak covers, card carousels, and restrained long-form articles.
- Keep the default UI nearly monochrome (#ffffff, #121317, #45474d), then reserve saturated blue/green/red/yellow ramps and gradients for scientific data, model identity, and moments of emphasis.
- Use a variable optical-size family across body and display, but create hierarchy through a sharp breakpoint jump: the largest token moves from 38px to 148px at 1280px while body copy stays 17.5px.
- Make media modular and theme-aware: promo cards combine fixed aspect-ratio wrappers, scrims, lazy autoplay video, responsive posters, and separate light/dark assets without changing the content component.
- Scale whitespace with the viewport as deliberately as typography: the page margin grows from 28px to 72px and the major block spacer reaches 120px, while the content cap stays 1440px.

## Avoid (1-2 bullets)
- Do not copy the 148px display scale or 120-180px spacing without the 1280px breakpoint and 1440px cap; on narrower layouts the source deliberately holds headings to 38px and margins to 28-40px.
- Do not imitate the motion-card carousel with autoplay alone; its legibility depends on scrims, poster fallbacks, lazy loading, muted/playsinline behavior, and theme-specific alternate media.
