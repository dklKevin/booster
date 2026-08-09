# https://material.security (sector: cybersecurity, sweep: excellence, fetched 2026-08-06)
status: full-css

## Token block (~10 lines)
- Homepage palette: warm canvas #E4E3E0, light panel #F5F5F5, and primary text/dark controls #383E41.
- Homepage accents: security/data blue #007DB8, alert-node coral #FF7B7B, and CTA yellow #E8A800.
- Interior token palette: light-gray background #EFEFEF, text #333333, primary blue #4F87B8, light blue #6CAFD9, red #E16464, green #A3B98A, teal #78ABAC, and purple #816189.
- Homepage type: "sofia-pro-variable", Arial, sans-serif for display/body/UI; "logic-monospace", ui-monospace, SFMono-Regular, Menlo, Consolas, monospace for uppercase eyebrows; "sentinel", Georgia, "Times New Roman", serif for the announcement.
- Homepage scale: hero 80px/weight 500 (76px, 72px, 68px at narrower desktop breakpoints; 48px mobile); body 20–24px; eyebrow 15–17px with .14em tracking; buttons 16px.
- Interior scale: "Brown LL", Arial, sans-serif; H1 60/66px, H2 48/55.2px, H3 32/41.6px, H4 26/32.5px, H5 20/28px, H6 18/27px; body 18px at 1.45 line-height.
- Spacing rhythm: 2, 4, 8, 16, 24, 32, 40, 48, 80, 128, and 192px tokens; homepage commonly uses fluid clamp() gutters and 32–56px component padding.
- Layout frame: homepage width min(1728px, viewport minus two 40–96px fluid gutters); interiors use a centered 1200px container with 64px desktop side padding and 768/1024/1200/1280px max-width utilities.
- Layout intent: editorial asymmetry—homepage hero splits at two-thirds/one-third, while interior heroes and feature rivers use balanced two-column grids before collapsing to one column.
- Signature element: a full-viewport, scroll-reactive hero drawn as an architectural grid—warm/light panels meet a saturated #007DB8 graph field whose fine solid/dashed lines and #FF7B7B nodes visualize an attack network.

## Lessons (3-5 bullets)
- Turn the security model into the composition itself: the hero's grid tracks, connecting lines, and nodes communicate systems and attack paths without relying on generic shield imagery.
- Keep dense technical storytelling approachable by anchoring it in warm neutrals, then reserve saturated blue, coral, and yellow for state, risk, and action.
- Use typography by information role: a humanist variable sans for the main narrative, tracked monospace for telemetry-like labels, and a restrained serif for editorial/news moments.
- Let long-form pages become quieter than the campaign homepage: the article template returns to a 768px reading column and smaller Brown LL hierarchy while retaining the same spacing and color vocabulary.
- Build responsiveness into the concept: the asymmetric desktop hero becomes a stacked mobile sequence, but preserves its graph cells, strong color field, and action hierarchy.

## Avoid (1-2 bullets)
- Do not copy the graph motif as surface decoration; without meaningful nodes, paths, and staged interaction it will read as arbitrary cyber-tech wallpaper.
- Do not reproduce both homepage and legacy interior typography indiscriminately; Sofia Pro, logic-monospace, Sentinel, and Brown LL need explicit page/role boundaries to avoid a fragmented system.
