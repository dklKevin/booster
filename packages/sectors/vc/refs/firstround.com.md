# https://firstround.com (sector: vc, sweep: excellence, fetched 2026-08-06)
status: full-css

## Token block (~10 lines)
- Base palette: warm canvas `#fbfbf6` (`--color-tan`), near-black ink `#000503`, white `#fff`, secondary grey `#646c7b`, light grey `#d0d0d0`.
- Green roles: light field `#b6f2d8`, vivid accent `#21fbac`, dark field/ink `#243c39`.
- Purple roles: light field `#f8e8ff`, vivid accent `#e4adff`, dark field/ink `#3b1044`.
- Blue roles: light field `#dfe9f7`, vivid accent `#89baff`, dark field/ink `#191f54`.
- Red roles: light field `#ffd0c4`, vivid accent `#ff4d58`, dark field/ink `#56001f`; yellow uses `#f3f0ce`, `#f4cf54`, `#614e39` in the same light/accent/dark roles.
- Type pairing: `store-norske-skandia, sans-serif` for UI, body and display; `store-norske-leif, serif` for narrative subtitles, quotes and callouts.
- Core scale: labels `14px/1`, supporting text `16px/1.4`, body `20px/1.24`, serif lead `24→36px/1.2`, section heading `32→48px`, H1 `40→64px`; hero display reaches `56px/.92` and `120px` on the image hero.
- Spacing rhythm: root page gutters `20px` mobile / `30px` desktop; default section padding `60px` mobile / `120px` desktop; recurring internal gaps and rules use `12`, `20`, `24`, `32`, `40`, `48`, `60` and `80px` steps.
- Layout intent: full-bleed color sections contain centered content capped at `1222px`; global shells cap at `1440px` (absolute max `2560px`), with readable text capped at `60ch` or `760px` and grids switching at `768px`/`1024px`.
- Signature element: a sticky full-viewport “Beginnings” hero (`position: sticky`) arranges portfolio-company tiles around the headline; hover/scroll reveals tinted images, logos and long founder-origin stories while the section background changes through the paired accent schemes.

## Lessons (3-5 bullets)
- Make portfolio proof the opening narrative, not a logo wall: each company is tied to a specific founding insight, while the repeated “Beginnings…” headline gives many stories one memorable frame.
- Use a systematic light/vivid/dark color triad per accent so editorial sections, cards, text and buttons can invert coherently without inventing one-off combinations.
- Separate institutional voice from founder storytelling: compact Skandia handles navigation and high-impact claims, while Leif at `24–36px` gives explanations and quotes a more human editorial cadence.
- Let dense interior pages change structure without changing tokens: the companies page uses featured two-column cards plus a subgrid list, while long-form content stays on a `760px` reading measure inside the same `1222px` section shell.
- Preserve generous pacing around consequential claims: the `60/120px` section defaults and limited text measures make detailed operating content feel deliberate rather than crowded.

## Avoid (1-2 bullets)
- Do not copy the five accent families without enforcing their paired foreground/background roles; arbitrary mixing would lose the contrast logic encoded by the site’s normal and inverted schemes.
- Do not reproduce the sticky, animation-heavy hero as decoration alone: its `100vh`/long-scroll behavior and many hover states need real portfolio stories, reduced-motion handling and careful mobile fallbacks to justify the interaction cost.
