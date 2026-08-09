# warp (warp.dev, extracted 2026-08-07)
status: full-css

- Neutrals: light ground/card #fff with body ink #292927; inverted modules use #08090a ground, #eef7fa text, #b8bfc1 body, #9ea4a6 secondary, and #424647 rules; subtle/dim rule fallbacks are #46454166/#46454133, while hover/active surfaces mix text at 5%/10%.
- Accents: #cbb0f7 is the marketing interaction hover; inside the product simulation #00c2ff marks terminal theme/cursor, #238dff active state, #43c251 success, #f6ba00 warning, and #ee343b error.
- Type: display is theFuture/theFuture Fallback at 400/500; body stack is "Matter", system-ui, sans-serif at 16/24; mono is "Azeret Mono", "Azeret Mono Fallback", ui-monospace, monospace at 400/500; hero clamps 56px to 80px with 60px to 90px line-height and -.035em tracking, while the scale runs 12/14/16/18/20/24/30/36/48/60/72/96px.
- Space: 4px grid; named steps 4/8/16/24/32/48/64px, 56px hero/container gap, 24px mobile and 40px desktop gutters; root radius 2px (derived 0.75/1/2/3/4/6/8px), primary buttons 0px; 1280px content/nav rail, 1152px article shell, 896px article measure.
- Motion: fast/normal/slow 100/200/400ms with cubic-bezier(.4,0,.2,1); factory rows reveal in 320ms and exit in 260ms with cubic-bezier(.16,1,.3,1), composer enters in 240ms, pulse is 1.6s ease-in-out, shimmer 1.35s linear, marquee 50s linear; reduced motion removes or pauses these.
- Structure: sticky translucent navigation tops a left-aligned hero and full-rail 760px product simulation; subsequent 1280px sections alternate wide media with a sticky 320px product index, while the article route collapses to an 896px reading column.
- Signature: an oversized, animated “Warp Factory” desktop window directly under the hero: traffic-light chrome, operational sidebar, staged activity rows, and a resizable task-detail pane cycle through agent work with reveal, exit, pulse, and shimmer states.

Avoid: Copying only the pale canvas and giant software window yields the standard developer-tool hero; Warp’s identity depends on unusually accurate operational states, near-square geometry, and restrained color. The hero simulation is client-rendered, so its 760px server placeholder is verified but internal dimensions are unverified.
