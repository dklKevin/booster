# joshwcomeau (joshwcomeau.com, extracted 2026-08-07)
status: full-css

- Neutrals: light ground #fff with text #0a0c10 and gray steps #f1f3f9/#e6e8f0/#d6d8e1/#9295a0/#3d455c/#21232c; dark ground #0d0f12 with text #e3e6e8 and steps #13171b/#1a1f23/#272e35/#75808a/#b9c4d0/#f2f5f7; hovers move to a neighboring theme token, while selection is #ffec8f on #000 in light mode.
- Accents: #4242fa light / #809fff dark is action, link underline, and focus; #e60067 / #ff1981 marks uppercase section labels; #2c0b8e / #e6b3ff marks article headings; #ff9d00 / #fa0 is reserved for warning callouts.
- Type: Wotfard with Verdana-adjusted fallback at 400/500/600; Cartograph CF 400/700 for code; Sriracha 400 for “spicy” display moments. Base is 16px with line-height calc(.95 + .62rem); article prose 18px, tutorial h1 36px/500, article h2 32px, About h1 64px.
- Space: 32px viewport padding, 16px below 35.1875rem; radii concentrate at 4/8/16px plus 1000px pills. Shell max-width is 68.75rem; tutorial grid is 42.875rem prose + 21.875rem rail; homepage uses a 2fr/1fr grid with 64px 96px gaps and collapses at 48rem.
- Motion: theme swap is 350ms cubic-bezier(0.41, 0.1, 0.13, 1); the shared spring is 833ms with a sampled linear() overshoot curve; nav geometry morphs over 666ms with another linear() curve. Entrances, wiggles, and theme layers all provide prefers-reduced-motion fallbacks.
- Structure: a sticky 5rem header sits above an asymmetric article-index grid; interior tutorials use a centered reading track with a right rail and full-bleed demo rows, then every page resolves into a deep illustrated footer.
- Signature: the footer becomes a 192px-deep scene: 5120px-wide theme-colored SVG cloud/ground bands frame a 150×269px light/dark Josh portrait that pops upward on the 833ms spring, turning site chrome into a responsive animated landscape.

Avoid: copying the clouds or mascot alone produces generic “whimsy”; they depend on the paired light/dark ramps, spring language, and dense interactive teaching payload. Do not flatten the many semantic accents into a rainbow applied everywhere.
