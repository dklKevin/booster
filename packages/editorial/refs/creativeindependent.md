# creativeindependent (thecreativeindependent.com, extracted 2026-08-07)
status: full-css

- Neutrals: #fff/white page and article-section grounds with #000/black text and dotted borders; links and controls switch dotted decoration/borders to solid on hover, while `html.dark` verifies #fff text/borders but no alternate ground value.
- Accents: color is assigned per content/story, not as one brand accent: the current lead interview uses #F2F0EA on #548AEA; content-type tokens are #c66026 approaches, #48699B focuses, #f8f8ea guides, #09099b questions, #ffff80 series, #cdddbb tips, and #def4ff transmissions.
- Type: Courier, "Courier New", monospace at 16px; article copy runs 1.3rem line-height, then 1.5 at 535px; titles are 2rem/1.1 and become 3.25rem at 820px, subtitles 2rem there; captions alone use "Georgia", serif at 0.94rem, with bold reserved for prompts/names.
- Space: 1rem body inset and 2rem page-row gap; archive tiles are 100% x 270px below 640px, then 270px square with 0.625rem gaps/padding; articles cap at 640px with 1.5rem paragraph rhythm and 2.5rem figure rhythm; radii are 1.25rem controls, 6px speech bubble, 45px circular submit.
- Motion: filter chevron rotates over 150ms ease; accordion arrows rotate over 0.5s ease; playing audio runs a 2s infinite 0-to-40px gold-tinted box-shadow pulse; other hovers change border style or grayscale with no timing.
- Structure: a pixel-logo/header and wrapping dotted-button taxonomy lead directly into a dense flex-wrapped archive; interiors are stacked accordion sections, with a 14rem floated metadata rail beside the centered 640px text from 535px and dotted section frames from 820px.
- Signature: each story's inline foreground/background pair is mechanically propagated from its square archive tile into the article title field, accordion labels, and optional inline `.highlight` spans; related links introduce their own story pairs inside that field.

Avoid: Copying only the many bright tiles produces an arbitrary rainbow checkerboard; the variety depends on one controlled pair per story, repeated through a severe Courier, dotted-rule, square-module system rather than treated as a reusable global palette.
