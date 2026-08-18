# https://stripe.com (sector: bigtech, sweep: excellence, fetched 2026-08-06)
status: full-css

## Token block (~10 lines)
- Palette - light surfaces: white `#ffffff`; subdued canvas `#f8fafd`; quiet border `#e5edf5`.
- Palette - content: solid heading/body `#061b31`; softer body `#50617a`; subdued text `#64748d`.
- Palette - brand/action: primary violet `#533afd`; hover violet `#4032c8`; pale action surface `#e8e9ff`; focus/input violet `#665efd`.
- Palette - signature accents: gradient stops `#bdb4ff`, `#643afd`, `#533afd`; stat gradients combine `#ffd601`, `#ee30fb`, and `#635bff`.
- Type pairing: `"sohne-var", "SF Pro Display", sans-serif` for UI/display; `SourceCodePro` at weight 500 for code.
- Body scale: `0.75rem`, `0.875rem`, `1rem`, `1.125rem`, `1.25rem`; body line-height is mostly `1.35–1.45`, generally at weight 300.
- Heading scale: mobile `0.875/1/1.125/1.25/1.375/1.75/2.125rem`; desktop (940px+) `0.875/1/1.375/1.625/2/3/3.5rem`, weight 300 with `-0.01em` to `-0.025em` tracking.
- Homepage headline: responsive English range `2.125rem` → `2.5rem` at 640px → `3rem` at 940px, line-height `1.15` (`1.03` below 640px), capped at `32ch`.
- Spacing rhythm: 4px (`#50`), 8px (`#100`), 12px, 16px, then 8px steps through 200px; common gap/gutter is 16px; section rhythm is 56–96px, depending on viewport and section type.
- Layout intent: centered 1264px maximum-width system, switching from 4 to 8 to 12 equal columns at 640px and 940px; 16px content margin and grid gap keep dense product modules aligned.
- Signature element: a full-bleed animated wave behind two overlaid copies of the hero headline; the foreground copy uses `mix-blend-mode: hard-light` with `rgba(0,14,255,.5)` to fuse type and moving color.

## Lessons (3-5 bullets)
- Scale one grid rather than inventing layouts per page: the same 4/8/12-column, 16px-gutter, 1264px-cap system supports the editorial homepage and denser Payments/Billing modules.
- Give technical products warmth through a restrained neutral foundation plus localized spectral color; Stripe reserves saturated violet and multicolor gradients for actions, data, and hero motion rather than flooding every surface.
- Treat typography as infrastructure: one variable sans spans 300-weight display through compact UI, while a dedicated monospace makes code examples feel native instead of decorative.
- Make the signature moment structurally meaningful: the animated wave intersects the revenue headline through blend mode, connecting the visual behavior to the message instead of adding an unrelated animation.
- Encode responsive hierarchy in tokens: heading sizes, section gaps, and column counts change together at 640px and 940px, preserving density and emphasis across pages.

## Avoid (1-2 bullets)
- Copying the gradients, hard-light headline, and animated canvas without the quiet `#f8fafd`/`#061b31` foundation would produce glare and weaken legibility.
- Reusing the full 12-column density or 56–96px section spacing unchanged on small screens would miss the source system’s deliberate 4-column collapse and responsive type reductions.
