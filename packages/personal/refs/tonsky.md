# Tonsky (tonsky.me, extracted 2026-08-06)

- Palette is one hue doing all the work: bg #FDDB29, text #000, and every gray is an alpha of black (.4/.2/.06) so it tints with the background. No second color. Seasonal swap to #6ADCFF in winter.
- Spacing derives from the font: gap = IBM Plex Sans cap height (12.5px), font-size = cap/0.698, radius = gap/3; type and rhythm are the same variable, so text optically sits on the grid.
- Type: IBM Plex Sans 400/600 only; 575px single centered column; ~12KB hand-written CSS, no frameworks, semantic tags instead of classes.
- Commitment lives where nobody budgets: six semantic bitmap cursors with pressed states (hand on links, I-beam on prose, arrow that depresses on :active); photo blended into the yellow via multiply with a hover frame.
- The joke dark mode (mouse-tracking flashlight over black) is fully engineered: fade states, 400-day cookie, saved mouse position on beforeunload. The bit is a bit; the implementation is not.
- Editorial vocabulary over visual classes: .loud, .note, .foot, .starred.

Avoid: copying #FDDB29 gets a loud page, not this page; the color works only because every gray is an alpha of black over it, there is no competing accent, and a 575px column limits how much yellow is in view. Partial cursor sets read as bugs.
