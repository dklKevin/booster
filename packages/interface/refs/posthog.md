# posthog (posthog.com, extracted 2026-08-07)
status: full-css

- Neutrals: light primary ground #FDFDF8, stepped surfaces #EEEFE9/#E5E7E0, ink #111111, secondary #65675E, border #BFC1B7; dark primary #1E1F23, surface #2D2E37, ink #FAFAFA, secondary #AEB3C2, border #3E424F; hover-invert swaps light ground/ink to #4D4F46/#FDFDF8.
- Accents: #2F80FA marks inline emphasis and Product Analytics; #EB9D2A supplies the raised-button underlay; #F7A501 identifies replay, #6AA84F positive states, #F54E00 notifications/errors, #B62AD9 experiments, and #29DBBB workflow/tool identity.
- Type: RoundHog, sans-serif is the 400/500/700/800 UI and display family; Source Code Pro, Menlo, Consolas, monaco, monospace is code at 13px/500. Applied scale is 12/16, 14/20, 16/24, 17/inherited, 20/28, 24/32, 30/36, 36/40; headings are usually 700, body 400/500.
- Space: 4px utility grid; applied radii 4/6/12/16/20px plus 40% desktop icons; reading/media widths 42rem/56rem and broad shell 80rem; sections use 64px or 80px vertical padding. Container stops are 425/482/640/768/900/1024/1160/1280/1536px.
- Motion: state transitions use 100/150/200/300/700ms with cubic-bezier(.4,0,.2,1) or cubic-bezier(0,0,.2,1); windows pop in at 200ms cubic-bezier(.34,1.56,.64,1); the tool ticker is 45s linear infinite and is disabled under reduced motion.
- Structure: a wallpapered desktop with top menubar and icon navigation contains rounded application windows; homepage/product copy uses a responsive ReaderView with two-column hero logic, while articles keep the same app chrome around a 42rem prose column.
- Signature: the whole website is a functioning desktop metaphor: glowing 36px app icons open routes as windows, each window has scheme-aware nested surfaces, scroll areas, title controls, and spring-like open/close motion rather than merely imitating a dashboard screenshot.

Avoid: copying the desktop chrome without PostHog's unusually broad product graph turns it into costume. The many accents work because they label tools, states, and window mechanics; using them decoratively produces noise, and the 40%/20px radii should not leak into every content block.
