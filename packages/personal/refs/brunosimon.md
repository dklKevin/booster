# brunosimon (bruno-simon.com, extracted 2026-08-07)
status: full-css

- Neutrals: #251f2b to #1d1721 radial ground for the document, menus, modals, and map; #fff primary text/borders, #fffc default button text becoming #fff on hover, and #555 disabled/input chrome.
- Accents: #ffceca marks active progress, valid inputs, and framed calls to action; #d5ff95 means achieved/success/connected; #ffc67b means music; #ff6a7c means danger/disconnected; #c21515 to #46123b is reserved for edge-mounted menu/map/close controls.
- Type: Nunito, sans-serif 400 is UI/body at a 20px root (18px <=520px, 16px <=440px), with 700 for labels/progress and 900 for the 30px race time; Amatic SC, sans-serif 700 sets 2.5rem titles and 64px touch actions (48px <=520px); explicit 1em line-height appears on notification titles, otherwise line-height is unverified.
- Space: no global grid token; recurring 10px gaps and 20/30/40px inset steps; radii 4px keys, 6px tabs/tooltips, 8px buttons/inputs, 15px gamepad glyph; menu caps at 1000x600px inside 60px gutters, becoming a 600px portrait stack; breakpoints 1100/870/800/520/440/360px plus portrait and 620/540px height cuts.
- Motion: opacity/transform transitions use .15s and .3s; notifications enter in .6s cubic-bezier(.4,1.6,.65,1) and leave in .45s cubic-bezier(.42,0,.47,-.55); map labels use .3s cubic-bezier(.65,-1,.45,1), switching on reveal to cubic-bezier(.49,2.2,.53,.75); player marker bounce is 1s after .5s.
- Structure: a fixed 100vw x 100vh WebGL canvas is the page; HTML UI floats above it as edge triggers, notifications, touch actions, square map, and a centered menu split 50/50 preview-content, changing to 30/70 vertically in portrait; there are no interior document routes.
- Signature: navigation is embodied as driving a vehicle through a WebGL portfolio world whose bundle names Projects, Lab, Career, distance/jump/honk achievements, a timed Circuit, respawns, whispers, and a location map, so exploration itself replaces the project grid.

Avoid: copying the plum game HUD without building the navigable world makes the shell feel like cosplay. Its compact overlays depend on the canvas carrying the portfolio, while pink, green, orange, and red keep single state meanings.
