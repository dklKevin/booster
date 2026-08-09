# https://www.nvidia.com (sector: bigtech, sweep: excellence, fetched 2026-08-06)
status: full-css

## Token block (~10 lines)
- Brand/action palette: NVIDIA green `#76b900` for CTA fills, link underlines, chevrons, active carousel indicators, and progress bars.
- Light palette: page/card background `#fff`, primary text `#000`, strong content text `#222`, and separators `#ccc`.
- Dark palette: page/card background `#000`, raised dark surface `#0c0c0c`, and foreground `#eee`.
- Supporting neutral tokens: `#f7f7f7`, `#e0e0e0`, `#a7a7a7`, `#898989`, `#757575`, `#636363`, `#4b4b4b`, `#313131`, and `#161616`.
- Type pairing: English uses `NVIDIA-NALA, Arial, Helvetica, Sans-Serif`; UI icons use Font Awesome 6 Pro/Sharp.
- Type weights: 300 light, 400 regular, 500 semibold, 700 bold; default copy is 15px/1.666, large copy 22px/1.75, and CTA text 18px/1.25.
- Heading scale: 60, 48, 36, 28, 24, 20px at desktop, all bold with 1.25 line-height; the largest steps contract to 48/36px on laptop and 36/28px at <=1023px.
- Spacing rhythm: named tokens run 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 56, 64, 72, 80, 96px, with recurring 15px component gutters and 30px grid gaps.
- Layout intent: full-bleed media bands contain centered flex-based 12-column content; capped widths are 650px phone, 660px tablet, 984px laptop, and 990pt (1320px) desktop, with breakpoints at 640, 1024, and 1350px.
- Signature element: vivid `#76b900` motion/navigation accents—especially the 4px timed carousel progress line—cut across image-led black/white sections.

## Lessons (3-5 bullets)
- Reserve one unmistakable brand color for state and action: NVIDIA repeats `#76b900` across CTAs, underlines, arrows, focus borders, carousel state, and loading feedback instead of flooding whole layouts with it.
- Let cinematic, full-width media establish scale while keeping text and controls on a strict centered 12-column system capped at 1320px.
- Encode hierarchy as named responsive steps: the 60px hero drops to 48px and then 36px, while all headings retain weight 700 and 1.25 line-height for continuity.
- Make dark and light themes structural primitives (`#000`/`#eee` and `#fff`/`#000`) so product families can change atmosphere without changing the interaction language.

## Avoid (1-2 bullets)
- Do not imitate the green by applying it decoratively everywhere; its distinctiveness depends on being concentrated in actions, links, and live state.
- Do not copy the 1320px desktop cap without the 984/660/650px responsive caps and collapsing column rules; the wide media/content contrast would otherwise become dense and brittle.
