# https://www.saronic.com (sector: defense, sweep: excellence, fetched 2026-08-06)
status: full-css

## Token block (~10 lines)
- Core darks: Midnight 300 `#162029` (primary text/dark panels), Midnight 400 `#0f161c` (deep panel), Midnight 200 `#44505c` (secondary panel/border).
- Core lights: Sunlight 100 `#f2f6fa` (light surface/light text), Sunlight 200 `#d8e4eb` and Sunlight 300 `#afc2cc` (cool secondary tones), white `#fff` (body background).
- Signals: Sonar `#acff24` (status/accent dots), Beacon `#fb6b3c` (alternate label/accent); Twilight 100 `#89a2b0` and Twilight 300 `#1d4d68` bridge the cool palette.
- Type pairing: Suisse (`__Suisse_ddcbba`, Arial fallback) for display/body at weights 400/450/500; Suisse Mono (`__SuisseMono_68313c`, Arial fallback) for uppercase captions.
- Display scale: 64–300px/1 (`-0.04em`), 40–96px/1.1 (`-0.04em`), 32–64px/1.12 (`-0.02em`), 24–40px/1.2 (`-0.02em`).
- Text scale: 20–32px/1.25, 18–24px/1.33, 14–20px/1.4, 14–16px/1.5, and 12px/1.5 mono caption.
- Spacing rhythm: `2, 4, 8, 16, 24, 32, 40, 64, 80, 120, 160, 200px`; section spacing is 80/120/160px by breakpoint.
- Responsive page margin: 16px under 640px, 24px at 640–959px, 32px at 960–1279px, and 40px at 1280px+; header height is 64px.
- Layout intent: fluid full-bleed media alternates with centered content capped at 1280px; split sections become equal 1fr/1fr columns at 960px, while data panels use 1px grid gaps.
- Signature element: a faint square tactical grid drawn as an inline SVG over dark surfaces, scaling from 24px to 32px to 40px cells across breakpoints.

## Lessons (3-5 bullets)
- Treat operational green as telemetry, not decoration: `#acff24` appears in small status markers while most surfaces stay within the restrained midnight/sunlight system.
- Pair cinematic, full-bleed mission imagery with rigid 1px data grids and mono uppercase labels; the emotional and technical modes reinforce one another.
- Let type scale carry the drama: oversized 64–300px page titles coexist with compact 12px mono controls, avoiding extra ornamental UI.
- Make responsive spacing systematic: the page margin and section interval each step up at the same 640/960/1280px breakpoints, keeping dense modules and open storytelling sections aligned.
- Use a fixed 1280px content ceiling but deliberately let selected split-media modules bleed edge to edge; this creates cadence without abandoning the grid.

## Avoid (1-2 bullets)
- Do not spread the sonar green across large surfaces or routine body copy; that would erase its source role as a scarce status signal.
- Do not copy the huge 300px display ceiling without the site's fluid clamp and tight line-height; static oversized headings would overflow smaller viewports.
