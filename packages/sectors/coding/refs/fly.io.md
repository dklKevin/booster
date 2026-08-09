# https://fly.io (sector: coding, sweep: excellence, fetched 2026-08-06)
status: full-css

## Token block (~10 lines)
- Palette - primary action/link violet `#7c3aed`; hover violet `#6d28d9`; brand navy `#281950`; deepest navy `#191034`.
- Palette - primary homepage ink `#2e2e2e`; secondary copy `#686082`; white surface `#ffffff`.
- Palette - hero wash `#f4f6eb`; pale-violet border `#e6e0fe`; stronger card divider `#d5cfef`.
- Type pairing - Fricolage Grotesque for body/UI; Mackinac (500/700, including italics) for headings; Fragment Mono-backed system monospace stack for code.
- Body/UI scale - 12px (`text-xs`), 14.5px (`text-sm`), 17px (`text-base`), 19px (`text-lg`), 20.5px (`text-xl`), 24px (`text-2xl`); body line-height is generally 1.5.
- Display scale - 30px, 36px, and 48px/1.3 for section headings; homepage hero is `clamp(26px, 8.9vw, 80px)`/0.95, then 88px, 104px, and 120px at larger breakpoints.
- Heading treatment - Mackinac at 500 by default, 1.375 line-height, `-0.025em` tracking; hero tightens to `-0.02em` and 0.95 line-height.
- Spacing rhythm - 4px base with recurring 8, 16, 24, 32, 40, 64, and 96px intervals; feature-panel desktop insets expand to 100px vertical and 150px horizontal.
- Layout intent - full-bleed hero followed by generously separated responsive flex/grid sections inside a 1728px max-width shell, with 16–24px mobile gutters and 20px panel radii.
- Signature element - large pale-lavender gradient feature panels overlaid with two offset radial dot fields (`#ffffff` dots at 1.4px/1.5px on an 8px grid), framed by `#e6e0fe` and a soft `0 2px 25px rgba(0,0,0,.1)` shadow.

## Lessons (3-5 bullets)
- Pair a characterful editorial serif for compact, high-impact claims with a variable grotesque for dense product explanation; the contrast makes infrastructure feel approachable without weakening technical clarity.
- Let one accent color do several related jobs - primary CTA, links, numeric proof, focus states - while keeping most content in dark neutral and muted purple-gray.
- Alternate open white sections with bounded, textured feature panels; the 1728px shell and 64–96px section rhythm preserve hierarchy even on very wide developer displays.
- Use unusually tight leading only for short hero copy; restore 1.3–1.5 line-height for headings and explanatory text as density increases.
- Make product mechanics visual through horizontally scrollable 450px cards and three-column feature grids, while retaining 85vw cards and single-column flow on small screens.

## Avoid (1-2 bullets)
- Do not copy the 88–120px, 0.95-leading hero treatment for long or frequently translated headlines; its `white-space: nowrap` depends on very short copy and responsive clamps.
- Do not reuse the dot texture, gradients, large illustrations, and lavender borders all at equal intensity; Fly.io reserves that combination for major feature panels, so indiscriminate use would erase the section hierarchy.
