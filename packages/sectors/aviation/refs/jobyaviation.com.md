# https://www.jobyaviation.com (sector: aviation, sweep: excellence, fetched 2026-08-06)
status: full-css

## Token block (~10 lines)
- Palette / canvas: warm white `#f5f4df` (`--color-white`) on deep navy `#0e1620` (`--color-black`); these are the default body background and text colors.
- Palette / primary brand field: electric blue `#007ae5`; dark blue `#1c3f99` and UI dark blue `#083e6f` support darker surfaces and controls.
- Palette / accents: orange `#eb6110`, grey `#c7c6b6`, pink `#ffd9c9`, light red `#fb9da6`, and light blue `#7cc3ff`.
- Type pairing: `jobyDisplay, "jobyDisplay Fallback"` for headings and display copy; `jobyText, "jobyText Fallback"` for body, captions, links, and controls; both are local variable fonts with `100 900` weight ranges and Arial-derived fallbacks.
- Display scale (desktop): page title `8rem/100%`, H1/H2 `6.4rem/100%`, H3/H4 `4.8rem/100–105%`, subheads `4rem`, `3.2rem`, `2.4rem`, and `1.8rem`; display weights concentrate at 500–550 with negative tracking.
- Text scale (desktop): body `1.4–1.8rem/130–140%`, captions `1–1.4rem/120–130%`, controls `1.4–1.6rem`; mobile titles step down to `3.2–4.8rem` and body commonly to `1.2–1.4rem`.
- Spacing rhythm: `0.8rem` mobile gutter, `1.6rem` desktop gutter and recurring base increment; common component gaps are `2.4rem`, `3.2rem`, `4rem`, and `8rem`, while section spacing expands to `12rem`, `14.4rem`, and `18.4rem`.
- Layout: fluid 16-column desktop grid with `4rem` side padding, switching at `768px` to 6 columns with `1.6rem` padding; root design widths are `1600`, `1024`, `375`, and `2056`, with the root `10px` scale made viewport-relative outside the main desktop range.
- Measure: no universal capped content container is declared; modules span the fluid grid, while editorial article content occupies columns 5–12 and caps at `76rem`; short supporting copy is commonly capped at `23rem`, `32rem`, or `40rem`.
- Signature element: scroll-progress-driven, full-viewport aircraft storytelling - sticky/fixed media, oversized fitted display text, and images that translate and scale between grid positions; the homepage pairs this with the fitted line “Nowhere to go but Up.”

## Lessons (3-5 bullets)
- Give advanced aviation a calm editorial frame: the warm-white/navy base keeps dense technical content credible, while `#007ae5` is reserved for immersive brand sections instead of becoming constant chrome.
- Build storytelling and utility on the same explicit grid: cinematic media can span all 16 columns, while labels, specifications, summaries, and article prose land on repeatable column starts and readable measures.
- Use separate display and text cuts of one variable family; Joby can move from `8rem` campaign statements to `1.2rem` captions without introducing an unrelated visual voice.
- Make the aircraft itself the transition system: fixed full-viewport media and scroll-linked transforms connect flight, engineering, sound, and specifications more memorably than a sequence of independent cards.
- Reduce the mobile composition deliberately: the system changes to 6 columns, halves the gutter, lowers title sizes, and converts overlapping desktop slides into a vertical flow rather than merely shrinking the desktop scene.

## Avoid (1-2 bullets)
- Do not copy the scroll choreography without a linear fallback: key desktop content begins hidden or absolutely positioned and depends on progress variables, while the source supplies separate visible mobile layouts.
- Do not use the `10px` root scale as a fixed global assumption; the source recalculates it from `375`, `1024`, and `2056` design widths, so isolated reuse would distort the extracted rem sizes.
