# https://www.novonordisk.com (sector: pharma, sweep: excellence, fetched 2026-08-06)
status: full-css

## Token block (~10 lines)
- Primary palette: Novo navy `#001965` for text, rules, icons, and solid backgrounds; white `#fff` for reversed text and surfaces.
- Interactive palette: bright blue `#005ad2` for action surfaces, controls, and selected/filter elements.
- Neutral palette: granite gray `#939aa7`, granite-gray-40 `#d4d7dc`, and light gray `#e4e6e9`; the footer watermark uses `#939aa7` at `0.08` opacity.
- Feedback palette: error red `#ba4242`; subdued copy/input gray `#595959`.
- Type family: one sans system, `"Google Sans Flex", "Noto Sans", "Noto Sans JP", "Noto Sans KR", "Noto Sans SC", "Noto Sans TC", "Noto Sans HK", "noto-sans-hebrew", "noto-sans-arabic", "noto-sans", "Arial", sans-serif`; Adobe CSS supplies `noto-sans` weights 100–900.
- Desktop type scale (`max-width: 2000px` rules): large display `148px/156px`, small display `96px/102px`, H2 `32px/38px`, lead `24px/42px`, large/body copy `20px/36px`, small copy `16px/26px`, tagline `14px/18px`, info `13px/21px`.
- Mobile type scale (`max-width: 525px`): large display `64px/68px`, small display `48px/52px`, H2 `22px/26px`, lead `21px/32px`, rich copy `17px/28px`, small copy `15px/24px`, info `13px/20px`.
- Spacing rhythm: named desktop steps `12, 20, 28, 52, 80, 100, 120px`, with standard component padding `60px` top/bottom; mobile compresses upper steps to `40, 52, 60px` while retaining `12, 20, 28px`.
- Layout intent: full-viewport, no extracted global max-width cap; a 24-column grid uses desktop tracks `calc((100vw - 330px) / 24)` inside asymmetric `150px` left/`180px` right gutters, then `calc(100vw / 24)` at `1280px` and below. Extracted component maxima include `1020px`, `400px`, and `344px`.
- Responsive structure: primary CSS breakpoints are `2000px`, `1280px`, `768px`, and `525px`; content grids use 6-track three-up and 9-track two-up widths, then wrap to `100%` below `525px`.
- Signature element: an oversized footer word, literally “change,” sits centered behind the content from `left: -3%`, `bottom: -40px`, and `width: 106%`, rendered granite gray `#939aa7` at `0.08` opacity; the homepage also opens with `100vh` image slides and directional black gradients.

## Lessons (3-5 bullets)
- Build scientific and corporate content on one explicit 24-column grammar: the same track math supports a full-bleed hero, editorial pages, card grids, and the dense R&D pipeline without changing the underlying system.
- Let brand color carry hierarchy more than decoration: `#001965` consistently unifies copy, dividers, icons, and backgrounds, while `#005ad2` is reserved for interactive emphasis.
- Use a deliberately wide display-to-body ratio—`148px/156px` display against `20px/36px` copy—then preserve the hierarchy with explicit mobile tokens rather than simple proportional scaling.
- Keep long-form healthcare material readable with generous line-height and section cadence: `20px/36px` body copy, `60px` component padding, and the `12–120px` spacing ladder recur across editorial and data-heavy interiors.
- Place the expressive brand moment at the edge of the experience: the faint “change” footer watermark adds distinctiveness without competing with regulated or evidence-heavy page content.

## Avoid (1-2 bullets)
- Do not copy the asymmetric `150px`/`180px` desktop gutters without the matching 24-column calculations; isolated use would produce arbitrary alignment and poor behavior around the `1280px` transition.
- Do not reuse the `148px` display scale or the `100vh` hero by default on information-dense pages; the fetched interiors instead use plain editorial or full-width headers and smaller content-specific title classes.
