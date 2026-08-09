# https://www.cloudflare.com (sector: cybersecurity, sweep: excellence, fetched 2026-08-06)
status: full-css

## Token block (~10 lines)
- Core light palette: accent/orange `#ff5e1f`, accent hover `#ff7038`, canvas `#ffffff`, raised canvas `#fdfdfc`, soft section canvas `#f9f7f6`.
- Light text and rules: primary `#262626`, secondary `#707070`, tertiary `#727272`, soft rule `#f0f0f0`, dotted decoration `#ebebeb`.
- Dark sections: canvas `#151414`, raised `#191817`, soft surface `#2a2927`, text `#f0e3de`, secondary text `#9a9390`, translucent rule/dots `#f0e3de20`.
- Product accents exposed in CSS: compute `#0a95ff`, storage `#ee0ddb`, AI `#00bd7d`, media `#9616ff`, security `#b52831`, SASE `#0d9488`.
- Primary type pairing: `"FT Kunst Grotesk", sans-serif` (400/500) with `"Apercu Mono Pro", monospace` (400) for code/monospace; the structurally different Developer Platform page uses `Inter, sans-serif`.
- Default type scale: H1 `40px` mobile / `56px` desktop at `.99` line-height and 500; H2 `32px` / `56px` at `1`; H3 `32px` / `48px` at `1`; paragraph `16px` at `1.2`.
- Hero scale: H1 `44px` mobile / `64px` desktop; H2 `36px` / `56px`; paragraph `16.8px` / `18px`; headings track at `-0.025em`.
- Spacing rhythm: `4px` base token, repeatedly composed as `8`, `12`, `16`, `24`, `32`, and `48px`; navigation is `54px` high mobile and `72px` desktop.
- Layout intent: a centered `1200px` primary content rail sits inside a `1480px` decorative/navigation frame; hero copy is capped at `1080px` and supporting copy at `700px`.
- Signature element: Cloudflare orange fields are overlaid with pale `12px × 12px` dot patterns and long dashed rules (`16,16`), including vertical guide rails repeating every `32px`, turning network infrastructure into the page grid itself.

## Lessons (3-5 bullets)
- Make the infrastructure metaphor structural: the dotted network field and dashed guide rails organize sections and communicate connectivity without adding literal cybersecurity stock imagery.
- Reserve the saturated orange for decisive brand fields and actions, then let near-white canvases and hairline-gray rules carry dense product explanation; this keeps a broad platform legible.
- Use one compact, medium-weight grotesk scale with near-solid headline leading (`.99–1`) and a monospace companion; the contrast feels technical without making body copy resemble a terminal.
- Constrain most content to `1200px` while allowing the decorative system to reach `1480px`; this creates visual scale without letting line lengths or card grids sprawl.

## Avoid (1-2 bullets)
- Do not copy the orange hero, dots, and dashed rails as independent decoration; without the shared `1200px`/`1480px` alignment they become visual noise rather than a coherent network grid.
- Do not assume every interior page shares the homepage system: the fetched Developer Platform page uses a separate Inter-based, two-column treatment, so naive reuse would expose typography and layout drift.
