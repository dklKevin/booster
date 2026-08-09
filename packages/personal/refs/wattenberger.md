# wattenberger (wattenberger.com, extracted 2026-08-07)
status: full-css

- Neutrals: #fff page ground with #0f2b3d body copy; article diagrams tighten ink to #1c2b3a, use #fbfbfb secondary planes and #cbd2dc seams; no applied dark theme verified.
- Accents: #041900 to #8179FF is reserved for the identity-name gradient; #3157d5 marks active article controls and #63acfc the active explanatory step. Topic chips are category-coded, but their applied Tailwind colors are emitted as RGB rather than source hex.
- Type: Parclo, ui-serif, Georgia, Cambria, "Times New Roman", Times, serif carries prose at clamp(1rem, 2vw, 1.25rem)/1.5, computed 400 with 600 emphasis; the name is 12vw/0.73em at 900. Inter, ui-sans-serif, system-ui handles labels at .875rem/1.25rem, uppercase with .1em tracking; article h1 reaches 4.5rem/1 at 1280px.
- Space: Tailwind's .25rem unit underlies spacing; homepage sections use 5rem vertical padding, 9rem top and 15rem bottom pauses, a max-width of 80em, and project gaps of 3rem collapsing to 1.5rem at 1024px; reading measure is 44em. Pills are 9999px; article prompt boxes use 1.25rem.
- Motion: homepage badge transform uses .15s cubic-bezier(.4,0,.2,1); article state changes use .3s cubic-bezier(.22,1,.36,1), marks arrive in .42s, and the caret blinks at .8s step-end infinite; reduced-motion rules remove these transitions/animations.
- Structure: A viewport-height identity hero leads to narrow thought lists, then an 80em one-to-three-column project ledger and repeated 2fr/1fr work rows; articles switch to a seven-track grid centered on a 44em text column, with full-width interactive/scrollytelling figures.
- Signature: The name is a 90%-wide, two-line SVG text clip at 12vw, filled by a bottom-right hue-traveling #041900-to-#8179FF gradient; a small “Hi, I’m” line sits offset left and rotated -10deg, making the introduction feel drawn across the viewport.

Avoid: Do not reduce this to a generic serif portfolio with pastel pills. Its effect depends on the oversized clipped name, deliberately skewed offsets, dense experimental artifacts, and the sharp Parclo/Inter division; copying the category colors without that authored content becomes framework boilerplate.
