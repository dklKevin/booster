# https://www.target.com (sector: fortune500, sweep: excellence, fetched 2026-08-06)
status: full-css

## Token block (~10 lines)
- Palette - brand/page: Target red `#cc0000` (brand background, text, border, icon), white `#ffffff` (page/base background).
- Palette - text: `#333333` base, `#666666` subdued/placeholder/disabled, `#f7f7f7` inverse.
- Palette - surfaces/borders: `#f7f7f7` subdued surface, `#e8e8e8` hover/inactive, `#d6d6d6` active/disabled/subdued border, `#888888` base border.
- Palette - brand states: `#aa0000` hover and `#840000` active; subdued brand surface `#fee9e7`.
- Type family: `"Helvetica for Target", HelveticaForTarget, Targetica, "HelveticaNeue for Target", "Helvetica Neue", Helvetica, Arial, sans-serif`; supplied weights 200, 400, 700, 900.
- Type scale: 13, 14, 16, 18, 20, 22, 24, 28, 30, 32, 36, 46, 56, 68px; body line-height 1.4, headline 1.3, display 1.
- Type roles: captions 13px; body 14/16/18px; headlines 18/20/22/24/28px, all headline roles at weight 700.
- Spacing rhythm: 4px base with 4, 8, 12, 16, 20, 24, 32, 40, 48, 56, 80px tokens; section margins map to 8/16/24/32px.
- Layout intent: centered content (`margin: 0 auto`) commonly capped at 1200px; responsive references at 393, 568, 768, 1200, 1464, and 1608px, with grid patterns from 1 to 12 columns.
- Signature element: the bullseye's circular geometry repeats through round category imagery, icon/action controls, and pills (`50%` or 999px radius), against a restrained red/white/gray system.

## Lessons (3-5 bullets)
- Let one brand color own primary actions and identity while neutral grays carry nearly all hierarchy; Target reserves `#cc0000` for brand roles and defines darker hover/active states.
- Use a compact, explicit commerce type ladder: 13–18px covers captions and body content, while 18–28px named headline roles keep dense merchandising readable.
- Build spacing semantically on a 4px foundation: Target maps the same primitives into interactive padding, container padding, text gaps, and section margins.
- Carry the logo idea into component geometry: circular category assets and controls make the bullseye identity recognizable without adding more color or ornament.
- Pair a stable 1200px content cap with named breakpoints and variable column counts so promotional storytelling and product grids can share one responsive frame.

## Avoid (1-2 bullets)
- Do not copy every red tint or circular treatment indiscriminately; without strict role assignment, brand actions, status messaging, and decorative imagery lose hierarchy.
- Do not import the full 13–68px primitive scale into every page; use the smaller named role set for routine commerce UI and reserve display sizes for campaigns.
