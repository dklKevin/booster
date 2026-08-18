# https://www.modernatx.com (sector: pharma, sweep: excellence, fetched 2026-08-06)
status: full-css

## Token block (~10 lines)
- Palette / canvas: #F8FDFF; surfaces: #FFFFFF; primary text: #053F68; secondary text: #376586; tertiary text: #507995.
- Palette / brand and interaction: CTA red #D1343E, hover #D5464F, active #BF3440; focus blue #079AE0 (also #079AE050 translucent focus fill).
- Palette / structure: dark footer/nav #083952; pale controls #E7F3F8; rules #CDD9E1; muted footer text #CED7DC.
- Type pairing: Aeonik, Arial, sans-serif is the site-wide family (weights 300/400/500/700); Roboto Mono is loaded in weights 300/400/500/700 as the companion face.
- Type scale: 14/20, 16/28, 18/32, 20/36, 24/36, 32/40, 40/48, 48/54, 64/72, and 80/88px (size/line-height); bold headings use weight 700.
- Spacing rhythm: a 4px-rooted sequence appears repeatedly - 8, 12, 16, 20, 24, 32, 40, 48, and 64px; section margins commonly step from 40px to 64px at desktop.
- Layout grid: wrapped flex rows use negative 8/12/16px margins and matching column padding at mobile/tablet/desktop, with 25%, 33.333%, 50%, and 75% column spans.
- Container: 16px mobile inset, 3.9vw at >=768px, 4.16vw at >=1024px; capped at calc(1600px + 4.16vw + 4.16vw) from 1440px.
- Breakpoints: 768px and 1024px drive the principal layout changes; 1440px raises display type and applies the wide-container cap.
- Shape/motion: cards and media use 12–16px radii, soft two-layer shadows, 0.2–0.3s interaction transitions, and 0.6s entrance fades with 10/20/40px vertical offsets.
- Signature element: staggered, overlapping rounded-image hero collages - three images on the homepage (70%, 125%, 125% aspect treatments) and two on subpages - fade upward in sequence at 0.2s, 0.3s, and 0.4s delays.

## Lessons (3-5 bullets)
- Build clinical credibility with a cool near-white canvas and deep navy typography, then reserve red for calls to action and active states; the extracted system avoids flooding scientific content with brand color.
- Pair a broad 1600px content ceiling with fluid 3.9–4.16vw side insets, so editorial modules feel spacious on large screens without losing alignment across breakpoints.
- Make dense pharma narratives scannable through a strict hierarchy: 18/32px body copy, 40–48px section titles, and 64/72px subpage heroes, all within one geometric sans family.
- Use the staggered image collage as a repeatable storytelling frame: different image scales and delayed vertical fades add human energy while preserving rounded, orderly containment.
- Carry the same interaction grammar across cards, navigation, and carousels: pale-blue controls, red active markers, blue focus outlines, and subtle shadow/scale changes.

## Avoid (1-2 bullets)
- Do not copy the three-image overlap without reserving its absolute-positioning space; the homepage implementation needs a 120px mobile top margin and lets the smallest image extend 55px below the main image.
- Do not treat every loaded font as body copy: Aeonik is explicitly assigned site-wide, while Roboto Mono is loaded but its visible role in the fetched page selectors is unverified.
