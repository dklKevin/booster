# https://vite.dev (sector: opensource, sweep: excellence, fetched 2026-08-06)
status: full-css

## Token block (~10 lines)
- Light palette: white/background `#fff`, primary text `#16171d`, beige alternate/soft surface `#f4f3ec`, grey secondary text `#867e8e`, stroke/divider `#e5e4e7`.
- Dark palette: primary background `#16171d`, midnight alternate `#0c0912`, slate soft/code surface `#14121a`, nickel borders `#3b3440`, white text `#fff`.
- Accent palette: electric `#6c3bff`, Vite lavender `#b39aff`, wine `#140033`, space `#103`, zest `#22ff73`, aqua `#32f3e9`; the brand variable resolves to electric or Vite by variant.
- Type pairing: `"APK Protocol", sans-serif` headings (500/700), `Inter, sans-serif` body (100–900 roman/italic), and `"KH Teka Mono", monospace` code/labels (400/500).
- Marketing type scale: 12, 14, 16, 18, 20, 24, 30, 36, 48, 60px; h1 is 36px mobile, 48px at 40rem, and 60px/67.2px line-height at 48rem.
- Documentation type: h1 32/40px, h2 24/32px, h3 20/28px, h4 18/24px, body 16/28px, inline code `.875em`.
- Spacing rhythm: `--spacing: .25rem` (4px); composed utilities repeatedly use 8, 12, 16, 20, 24, 32, 40, 48, 64, 80, 112, and 120px.
- Layout intent: marketing sections sit in a centered ruled wrapper, `calc(100vw - 2rem)` from 48rem and capped at `90rem`/1440px, with responsive two-column grids; the global layout cap is 1440px.
- Interior-page layout: documentation uses a 1104px container around a 688px reading column, with 32px horizontal content padding and 48px top/128px bottom padding at the extracted desktop rule.
- Signature element: the split dark hero pairs package-manager install tabs with a 641×629 canvas driven by Rive/WebGL, inside the bordered/ticked 1440px frame.

## Lessons (3-5 bullets)
- Put the first successful developer action in the hero: Vite exposes copyable npm/Yarn/pnpm/Bun/Deno commands beside the proposition instead of making setup a later documentation step.
- Separate expressive marketing typography from utilitarian reading typography: APK Protocol gives the homepage identity, while Inter and a narrow 688px documentation measure protect long-form legibility.
- Reuse the same 1px ruled wrapper and 4px-derived spacing system across hero, proof logos, feature grids, community metrics, sponsors, and footer so varied content still reads as one system.
- Treat dark and light modes as role remaps, not inversions: dark mode deliberately moves backgrounds through `#16171d`, `#0c0912`, and `#14121a` while retaining `#867e8e` secondary text and switching dividers to `#3b3440`.
- Make technical capability tangible with one interactive artifact - the canvas animation - then keep supporting illustrations, terminals, and framework logos inside restrained grid cells.

## Avoid (1-2 bullets)
- Do not copy the 60px display face or 641×629 canvas without the extracted 48rem breakpoints; the source drops h1 to 36px and collapses the grid for smaller screens.
- Do not apply the dense bordered marketing grid to documentation prose; the source switches to a 688px reading column and a quieter 16px/28px body rhythm.
