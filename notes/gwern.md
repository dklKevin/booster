# Gwern design reference

Deep reference distilled from gwern.net/design and gwern.net/design-graveyard (fetched 2026-08-06).
Not loaded by default; consult when designing long-form reading experiences.
Token block lives in `../document.md`.

## Documented decisions and their reasoning

- Grayscale-only palette as an experiment in constraint; emphasis carried by dropcaps and small caps rather than hue.
- Dark bg is #161616, never pure black: pure black causes scroll/update jank and poor contrast.
- Sidenotes in both margins because his footnote density was too high for single-margin Tufte layout; references belong at eye level.
- JS never required to read; popups, sorting, sidenotes are all optional enhancements. Pages must survive elinks and phones.
- Semantic zoom: title -> metadata -> abstract -> headers -> margin notes -> body -> collapsed sections -> popups. A page looks short but is an iceberg.
- Annotated link popups are functioning mini-pages (recursive, draggable, pinnable) because readers genuinely dive deep.
- Link icons encode filetype/domain/topic so readers triage without a page load; visual differences should be semantic differences.
- Collapsible sections + lazy transclusion give arbitrarily large virtual pages from plain Markdown.
- Bidirectional backlinks at section level, not just page level.
- Dark mode via explicit widget, with AI classification (InvertOrNot) deciding which images to invert.
- Justified + hyphenated above 650px only; narrow justification produces stretched words and rivers.
- Self-hosted subsetted fonts; cross-domain font caching no longer exists, so font CDNs have no cache benefit.
- Demo mode: LocalStorage use-counts retire newbie affordances after n views.
- Reader mode strips underlines, icons, and most UI as an escape hatch for readers who find the design too much.
- Line-height set in four viewport brackets (1.45/1.50/1.55/1.60) because no one size suits all.

## Graveyard (abandoned, with cause)

- Beeline Reader coloring: A/B showed no improvement, complaints, perf cost. Shorter paragraphs beat gimmick reading aids.
- Pure OS-driven dark mode: readers forgot their setting and blamed the site. Also: a toggle widget is a one-way door; features accrete onto it.
- Auto small-caps for acronyms: doubled compile time, hundreds of DOM nodes, endless regex cases; belongs in the font, not markup.
- q-tag quote highlighting: copy-paste stripped it, browsers silently broke it, manual markup obstructed writing.
- Link screenshot previews: cookie banners defeated headless capture; 10k tiny PNGs to maintain. Replaced with reviewed archives.
- Knuth-Plass line breaking: every route dead-ended; settled for disabling justification on narrow screens.
- AdSense: A/B-measured traffic loss so large the analysis was unnecessary; removed same day.
- Google Fonts, MathJax, Hyphenopoly: all died to one principle, move work to compile time.

## Meta-lessons

- Design pays off multiplicatively, writing additively: polish is rational at scale, irrational below it.
- Test cleverness against readers and believe the result; users won't tell you when it's broken.
- Every ornament needs an off-switch shipped alongside it.
