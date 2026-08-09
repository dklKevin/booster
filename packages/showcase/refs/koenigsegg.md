# Koenigsegg (koenigsegg.com, extracted 2026-08-06, deep pass)

- Black document default (html{background:#000}); three themes only: black, white, hangar green #687c7b. Chrome grays are UI furniture, never content; all dividers are currentColor hairlines at 30% opacity.
- Signal yellow #f6be00 exists ONLY as a 200ms hover underline sweep; never a fill, never text, never at rest. One saturated color, spent entirely on motion.
- Two families: Gustavo condensed uppercase (weight 500, line-height 80-90%, .02em) for display and numbers; Basel Grotesk 400 for body. Fluid root: clamp(10px to 14px), so the whole page scales twice over.
- Scale: heading-1 72-149px (lh 80%) down to copy-5 9px; hero body copy measure-capped per element (24-30rem), no site-wide max-width.
- Signature, the spec ledger row: 5-column grid, value at heading-2 scale (44-121px) spanning two columns, unit 14px at column 3 with optical baseline nudge, label 14px right; all bottom-aligned, closed by a 1.5px rule at 30% opacity. Five stacked rows read as an instrument panel.
- Value-to-label ratio ~4.5:1: the eye lands on "1600" before discovering it means horsepower.
- State each figure twice: once inside prose, once extracted at display scale.
- Split seduction from reference and invert theme between them: model page black, image-led, five stats; technical-specifications page white, chaptered 01/07, zero adjectives. The reachable engineering record makes the spectacle credible.
- Model names are never type: each car ships its own SVG wordmark lockup.
- Motion: two easings only; decelerating .6s for imagery, accelerating .2s for the yellow sweep. Buttons are hairline outlines at 30% opacity, never fills.

Avoid: the giant numeral is loud because 200-400px of silence surrounds it; sub-100% line-height uppercase needs copy-length control at the source (they forbid wrapping outright).
