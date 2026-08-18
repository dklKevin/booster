# https://tailscale.com (sector: cybersecurity, sweep: excellence, fetched 2026-08-06)
status: full-css

## Token block (~10 lines)
- Canvas and surfaces: neutral-100 `#f9f7f6` (page background), white `#ffffff` (cards), neutral-300 `#eeebea` (borders/dividers).
- Text and dark surfaces: neutral-800 `#2e2d2d` (primary text), neutral-900 `#232222` (primary buttons), neutral-950 `#1f1e1e` (deep dark), neutral-50 `#faf9f8` (light-on-dark text).
- Brand/feature color: blue-500 `#5a82de` to blue-800 `#324994` for the homepage's major product-story gradient; blue-100 `#cedefd` and blue-900 `#253570` support tinted elements.
- Secondary semantic tints: green-100/800 `#cbf4c9`/`#0b3733`, purple-100/800 `#efddfd`/`#502c6b`, red-100/800 `#ffd3cf`/`#760012`, orange-100/800 `#f8e5b9`/`#571f0d`.
- Primary type: `inter`, `inter Fallback`, `ui-sans-serif`, `system-ui`, `sans-serif`; body is 14px rising to 16px at 921px, weight 400, line-height 1.5, tracking -0.01em.
- Technical label type: `mdio`, `mdio Fallback`, `ui-monospace`, `SFMono-Regular`, `Menlo`, `Monaco`, `Consolas`, `monospace`; labels are 12/14px, weight 500, uppercase, line-height 1, tracking 0.05em.
- Display scale: 40/56/64px across 0/641/921px breakpoints; title 2XL is 32/40/48px; both use weight 500, line-height 1.1, tracking -0.01em.
- Supporting scale: title-sm 18/20px at 0/641px (500/1.2); title-xs 16px (500/1.5); body-sm 12/14px and body-md 14/16px at 0/921px (400/1.5).
- Spacing rhythm: named tokens resolve to 2, 4, 8, 12, 16, 20, 24, 28, 32, 36, 48, 64, 72, 96, and 192px; homepage composition repeatedly uses 8/12px gaps, 24/32px grouping, and 64/96px section space.
- Layout intent: centered `1280px` container with 20px gutters, 40px from 64rem; homepage bands extend to `1360px`/`1440px`, while `.container-new` and the product illustration use `1120px` content width.
- Signature element: a large bordered, rounded product-story panel whose blue `#5a82de`→`#324994` header contains role tabs and an `1120×600` network-use illustration, followed by a white three-column proof grid.

## Lessons (3-5 bullets)
- Make the product model concrete: pair the Zero Trust claim with role-specific tabs and a large network illustration instead of relying on abstract security imagery.
- Use a warm near-neutral canvas, hairline neutral borders, and very low shadows (`0 4px 8px #18171705`) so dense UI-like cards remain approachable without losing technical credibility.
- Keep the main hierarchy typographically simple - one variable sans for prose and display, one compact mono for technical labels - then create distinction through scale, case, and tracking.
- Let trust evidence occupy real layout space: the homepage follows its centered claim with a broad customer-logo field and developer testimonials before the final conversion panel.
- Preserve one wide container system while constraining explanatory copy to `768px` and major feature headings to `900px`; this keeps long pages expansive but readable.

## Avoid (1-2 bullets)
- Do not copy every tint at equal strength: the source keeps neutral-800 dominant and reserves colored pairs for categorized accents; indiscriminate use would turn a restrained security system into a rainbow dashboard.
- Do not reuse the 64px display size or 64–96px spacing unchanged on small screens; the fetched CSS steps type at 641/921px and expands gutters only at 64rem.
