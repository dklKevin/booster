# samwho (samwho.dev, extracted 2026-08-07)
status: full-css

- Neutrals: light ground #fff with main text oklch(0.21 0.034 264.665) and highlight oklch(0.967 0.003 264.542); `?theme=dark` switches to ground oklch(0.13 0.028 261.692), text oklch(0.872 0.01 258.338), highlight oklch(0.278 0.033 256.848); homepage cards stay #fff with #333 labels.
- Accents: #4ba69d, #a0d9d3, #f29e38, #f27405, #bf4904 appear in order only as the five equal segments of the 0.7rem identity bar atop every page; dark mode mixes each with 20% black.
- Type: body Seravek, "Gill Sans Nova", Ubuntu, Calibri, "DejaVu Sans", source-sans-pro, sans-serif at 14pt/1.5; headings "Iowan Old Style", "Palatino Linotype", "URW Palladio L", P052, serif at 3rem/2rem/1.5rem and 1.2 line-height; code uses ui-monospace, "Cascadia Code", "Source Code Pro", Menlo, Consolas, "DejaVu Sans Mono", monospace.
- Space: repeated 1rem unit; 780px article plus 1rem inset, headings get 2rem top space and prose 0.8rem above/below; card grid is auto-fill minmax(180px, 1fr) with 1rem gaps; radii 8px cards, 1rem code/speech bubbles; margin notes are 17vw and fold inline at 1300px.
- Motion: cards change shadow in 0.3s cubic-bezier(0.67, 0.86, 0.25, 1); hero keys scale to 0.95 hover/0.90 active in 0.1s ease-out; footer signature draws for 0.9s ease, then 1.5s ease-out after 0.9s, then 0.4s ease after 2.4s; reduced motion forces 0.01ms.
- Structure: a centered single 780px article stacks emoji-titled autobiographical sections, with a responsive essay-card grid; interior essays retain the same bar and column but replace the homepage hero with wide custom teaching components, code blocks, and 17vw outer margin notes.
- Signature: a large inline keyboard SVG spells SAM over WHO; each key is independently pressable, scaling on hover/active, so the masthead itself demonstrates the tactile, bottom-up interactivity used throughout the essays.

Avoid: copying the emoji headings, five-color strip, and white card grid alone reduces this to a generic developer homepage; its character depends on the custom keyboard masthead and topic-specific interactive diagrams doing real explanatory work.
