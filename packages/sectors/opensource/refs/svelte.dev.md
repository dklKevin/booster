# https://svelte.dev (sector: opensource, sweep: excellence, fetched 2026-08-06)
status: full-css

## Token block (~10 lines)
- Light surfaces: `#fff` page, `#fdfdfd` secondary, `#fafafa` tertiary, `#f2f2f2` raised.
- Light foregrounds: `#141414` strongest, `#262626` body, `#666` muted.
- Brand/action: `#d43008` foreground accent and `#ff3e00` logo; accent background resolves to the foreground accent.
- Lines and states: `#ebebeb` border, `#42b4ff4d` selection, `#71aad033` unfocused selection, `#ff9` highlight.
- Type pairing: `"DM Serif Display", Georgia, serif` headings; `Georgia, serif` body, switching to `"EB Garamond", Georgia, serif` at high pixel density.
- Interface/code: `"Fira Sans", -apple-system, sans-serif` UI and `"Fira Mono", monospace` code; optional readable body mode is `"Atkinson Hyperlegible", sans-serif`.
- Type scale: h1 `3.6rem`/`5.4rem` at 800px+, h2 `3rem`, h3 `2.4rem`, body `1.8rem` (high-density `2.2rem`), small body `1.6rem`, mono `1.4rem`, UI `1.3rem`/`1.6rem`/`3rem`.
- Spacing rhythm: side padding `1.6rem`/`3.2rem`/`4.8rem` at 0/480/800px; page top `6rem` then `8rem`; page bottom `8rem`; sections `6rem` then `10rem` at 900px.
- Layout intent: center prose in a `76rem` content measure; let marketing sections reach `120rem`; docs add a `28rem` minimum left sidebar and a right on-page rail from 1200px.
- Signature element: the responsive, full-width “Svelte machine” hero illustration sits behind a `clamp(60rem, 50vw, 80rem)` headline block and fades into the page with layered gradients.

## Lessons (3-5 bullets)
- Separate reading, interface, and code voices: a display serif and bookish body make long documentation editorial, while Fira Sans and Fira Mono keep navigation and examples unmistakably functional.
- Encode responsive whitespace as a small token progression (`1.6rem` to `3.2rem` to `4.8rem`) and reuse it in navigation, page edges, sections, and side rails.
- Keep documentation readable at `76rem`, then spend width on navigation aids; the left index becomes fixed at 832px and the right “on this page” rail appears only at 1200px.
- Give the homepage one bespoke brand narrative—the Svelte machine—while the blog and docs return to restrained typography and shared tokens.

## Avoid (1-2 bullets)
- Do not copy the three-font-plus-mono stack without disciplined roles; applying the display serif or UI sans everywhere would erase the hierarchy the pairing creates.
- Do not transplant the wide illustrated hero into content pages; its viewport-based height and oversized artwork work because the interior pages revert to a narrow reading measure.
