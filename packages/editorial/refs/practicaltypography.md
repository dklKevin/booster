# practicaltypography (practicaltypography.com, extracted 2026-08-07)
status: full-css

- Neutrals: Page text is browser-default black; source-applied tones are #333 for rules/emphatic headings, #667 for sidenotes, #999 for dormant controls, #ccc for callout/table rules, #fcfcfc to #ffffff radial callouts, and #fbf3f3 link-hover grounds; the explicit toolbar ground is #ffffff (body ground itself is unverified).
- Accents: #933 marks ordinary links with a raised degree glyph; #a33 is reserved for specimen/payment actions, brightening to #e33 on hover and falling to #ccc while active.
- Type: Root size is fluid 2.4vw, capped at 24px above 1000px and floored at 18px below 520px; default body is valkyrie-text 0.91rem/1.45, switchable to equity-text 0.98/1.4, century-supra-text 0.93/1.46, concourse-text 1/1.35, heliotrope-text 0.96/1.42, or triplicate-text 0.85/1.45; display topics use advocate-c41 2.3rem/1.1, uppercase with 0.02em tracking.
- Space: A recurring 2.5rem measure drives the article's 12rem left offset, 2.5rem right gutter, list indents, and 7.5rem sidenotes inside a 1000px body; content pads 3rem top/18rem bottom, paragraphs space by 1em, and 520px collapses to 1.5rem margins; radii are 8px on text hovers, 1em on payment pills, and 0.25rem on tooltips.
- Motion: Background, fixed side-border, and switcher-opacity transitions are 0.2s with the browser-default easing; tooltip opacity is 0.3s; no keyframe animation found.
- Structure: Desktop articles are a narrow right-shifted reading column with absolutely positioned left sidenotes, fixed 5rem edge navigation, and a bottom toolbar revealed near the scroll end; the homepage replaces prose with a fixed 9rem cover lockup beside a two-column contents list, collapsing to one column at 520px.
- Signature: A draggable/detachable font palette applies persisted `body-text_*` classes to restyle the whole book among six optically calibrated house families, so the typography itself is the interactive specimen rather than decoration.

Avoid: Copying the red degree-link marks, pale-pink hovers, or eccentric custom elements without the embedded Butterick families turns a working typographic demonstration into mannerism. The font switcher only earns its place because each option has its own tuned size, leading, caps, and numeral behavior.
