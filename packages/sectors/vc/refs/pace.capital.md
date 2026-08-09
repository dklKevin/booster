# https://pace.capital (sector: vc, sweep: excellence, fetched 2026-08-06)
status: full-css

## Token block (~10 lines)
- Palette / canvas and ink: warm off-white `#f3f1ed` background with dark umber `#403326` foreground.
- Palette / dimensional wood: `#ebe8e0` light, `#d9d4c9` base, `#c7bfb3` medium, `#b0a89b` dark, and `#988d81` deep.
- Palette / controls and detail: `#b3a289` primary, `#9d866c` accent, `#ad9c85` border, `#604d39` engraved text, `#4d4033` pegs, `#b3884d` ball, and `#c5b087` ball highlight.
- Type family: `"JetBrains Mono", "Courier New", monospace` throughout; no second display family is present in the fetched source.
- Site-specific type scale: `8px`, `9px`, `10px`, `11px`, and `12px`; company names use `11px` bold, descriptions `9px`, and navigation/actions `12px`, usually uppercase with `0.06em`–`0.15em` tracking.
- Utility type scale retained for exceptional/system screens: `14px`, `16px`, `18px`, `20px`, `24px`, and `36px`.
- Spacing rhythm: a 4px base with recurring `8px`, `16px`, `24px`, `32px`, and `48px`; main shells use `16px` padding, rising to `32px` at 768px, while portfolio rows use `48px` gaps and padding.
- Shape and depth: `8px` base radius; wood uses a five-stop diagonal gradient plus inset highlights/shadows and a `0 8px 24px #32221b66` outer shadow.
- Layout intent: center a fixed `440 × 600px` game object in a full-viewport shell; interior portfolio content switches between a full-width horizontal carousel and a wrapped grid capped at `72rem`.
- Signature element: the entire navigation is a playable, flippable wooden pachinko board—pulling its lever drops a ball, while engraved labels act as links; portfolio companies repeat the metaphor as `240px` wooden balls (`208px` in grid view).

## Lessons (3-5 bullets)
- Turn the investment thesis into the interaction model: “make your own luck” is demonstrated through the pachinko mechanic instead of explained in a conventional hero.
- A deliberately tiny, tracked monospace scale can make a sparse VC site feel like a physical machine label system; consistency across copy, navigation, and portfolio captions is what makes it coherent.
- Reuse the signature material language beyond the homepage: circular wooden portfolio tiles carry the same palette, highlights, perspective, and engraved typography into a structurally different page.
- Keep an expressive homepage bounded and accessible: the board scales below 768px, the page exposes a skip link and screen-reader headings, and reduced-motion behavior is present in the stylesheet.
- Let the portfolio support two browsing modes: a theatrical horizontal procession by default and a practical `72rem` wrapped overview on demand.

## Avoid (1-2 bullets)
- Do not copy the game conceit without a thesis-level reason for it; the mechanism works because the source explicitly connects chance, agency, and investing.
- Do not transplant the `8px`–`12px` typography unchanged into text-heavy pages; here it is paired with very short uppercase labels, generous spacing, and compact captions.
