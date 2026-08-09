# https://tailwindcss.com (sector: opensource, sweep: excellence, fetched 2026-08-06)
status: full-css

## Token block (~10 lines)
- Light canvas is white `#fff`; dark canvas is gray-950 `#030712`; primary light text is gray-950 `#030712`, and primary dark text is white `#fff`.
- Supporting copy uses gray-600 `#4a5565` on light and gray-400 `#99a1af` on dark; stronger documentation copy uses gray-700 `#364153` / gray-300 `#d1d5dc`.
- Brand and interactive accent is sky: sky-500 `#00a5ef` for light inline code, sky-400 `#00bcfe` for dark inline code and the logo fill, with sky-300 `#77d4ff` for fine borders/handles.
- Display and body type use Inter Variable (`inter`, `inter Fallback`, then `system-ui`); code and utility labels use IBM Plex Mono (`plexMono`, `plexMono Fallback`, then `monospace`).
- Extracted type scale is 12, 14, 16, 18, 20, 24, 30, 36, 48, 60, 72, 96, and 128px; the home H1 responds 36 → 48 → 60 → 96px, while docs H1 is 30px.
- Body patterns pair 14px with 24/28px line-height, 16px with 28px, and 18px with 28px; headings commonly use `tracking-tight` or `tracking-tighter` and medium weight.
- Spacing is a 4px base (`--spacing: .25rem`), heavily composing 8, 16, 24, 32, and 40px gaps/padding; major section separation commonly uses 64px and 96px.
- The fixed header is 56px tall with 16px horizontal padding, rising to 24px at the small breakpoint; content begins at 57px (`pt-14.25`).
- Layout intent: a centered responsive grid caps the homepage at the 96rem/1536px `2xl` breakpoint with 40px gutters; docs switch at 64rem to a 288px sidebar + 40px gutter + fluid article, whose inner widths cap at 42rem/672px and 64rem/1024px.
- Signature element: content is visibly placed on a drafting grid—full-bleed 1px rules, dashed sky selection boxes/handles, and tiny monospace utility-class labels make the framework's own primitives the visual language.

## Lessons (3-5 bullets)
- Turn the product's core abstraction into the interface ornament: Tailwind labels spacing and typography with real utility names, so decoration simultaneously teaches the API.
- Keep dense technical material calm with a nearly monochrome gray system, then reserve the `#00a5ef`/`#00bcfe` sky accent for code, selection states, and brand recognition.
- Let marketing and reference content share tokens but change structure: the homepage uses a wide 1536px demonstration canvas, while docs narrow prose to 672px inside a stable sidebar shell.
- Use large responsive display type (36–96px) with restrained medium weight and tight tracking, then anchor explanations in 16–18px text with 28px line-height.
- Make spacing legible through repetition: 4px-derived gaps plus recurring 1px rules create rhythm even when examples, code, and prose vary dramatically.

## Avoid (1-2 bullets)
- Copying the drafting-grid rules and utility labels without a product concept that they explain would turn meaningful self-demonstration into visual noise.
- Applying the 96px marketing scale or wide demonstration canvas to documentation would undermine the source site's deliberate 30px heading and 672px prose measure.
