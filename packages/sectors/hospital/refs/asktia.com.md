# https://www.asktia.com (sector: hospital, sweep: excellence, fetched 2026-08-06)
status: full-css

## Token block (~10 lines)
- Core palette: warm cream `#fcf4e9` (body/header background), near-black `#282725` (text, borders), and white `#ffffff` (cards/reversed text).
- Primary action palette: poppy `#f95647` (join buttons/metrics), hot pink `#ef308d` (secondary accent/hover), and burgundy `#831a4a` (primary dark buttons/links).
- Supporting palette: blush `#ecdccd` (mobile menu, borders), muted brown `#765454` (secondary copy), dusty rose `#be9191`, coral `#f5907a`, rust `#c45138`, sage `#d6deba`, and amber `#f9b146`.
- Type pairing: `inferi-normal, serif` for H1/H3 display copy (with `inferi-normal-italic` for emphasis); `basis-grotesque-regular, serif` for body and H2; Basis Grotesque bold and mono cuts for buttons/labels.
- Base type scale: body `15px` mobile / `18px` from 800px; H1 `36px` / `40px` at 800px / `47px` at 1000px; hero H1 `60px` from 81.25em.
- Supporting type scale: H2 `34px` / `44px` from 800px; H3 `25px` / `30px`; H4 `20px` / `21px`; H5 `14px` / `16px` from 37.5em.
- Spacing rhythm: component gaps center on `8px`, `16px`, `24px`, and `32px`; section Y presets are `16/32/40/56px` mobile and `24/56/72/96px` from 800px.
- Gutters and radii: page gutter `24px`, increasing to `60px` from 75em; common radii `8px`, `10px`, and `20px`, with pill buttons at `26px`, `32px`, or `90px`.
- Layout intent: fluid 12-column utilities from 48rem inside named containers (`600`, `800`, `1000`, `1100→1340`, and `1440px` maxima), with single-column mobile sections and 24px default item gaps.
- Signature element: opposing-direction marquee rows of outlined, rounded labels - `32px/33.6px`, `8px 24px` padding, `16px` gaps - moving for `120s` on desktop and `70s` on mobile.

## Lessons (3-5 bullets)
- Pair a warm, low-contrast clinical canvas (`#fcf4e9`) with near-black text and a tightly rationed poppy CTA; healthcare can feel welcoming without sacrificing action hierarchy.
- Separate emotional and operational voices typographically: Inferi carries large human-centered statements, while Basis Grotesque handles navigation, explanations, forms, and controls.
- Use a small repeated spacing vocabulary for components, then widen only the section cadence at desktop (`24/56/72/96px`); this preserves density inside modules while creating a calm page rhythm.
- Let proof feel editorial rather than institutional: the source makes metrics oversized (`96px` Inferi in `#f95647`) and pairs them with quieter `16px/20px` muted-brown summaries.
- Keep complex care content responsive through explicit systems: 12-column desktop utilities, named max-width containers, and single-column mobile fallbacks rather than bespoke widths per block.

## Avoid (1-2 bullets)
- Do not reproduce every accent color at equal prominence; the stylesheet contains a broad supporting palette, but the recurring foundation is cream, near-black, poppy, blush, burgundy, and muted brown.
- Do not copy the marquee motion without a reduced-motion treatment; the fetched CSS verifies continuous `120s`/`70s` animation but no marquee-specific `prefers-reduced-motion` override.
