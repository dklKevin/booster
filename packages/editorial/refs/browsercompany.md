# browsercompany (thebrowser.company, extracted 2026-08-07)
status: full-css

- Neutrals: homepage ground #EEEEE7 with #000000 text at 85% primary / 60% secondary; dark mode switches to #1B1B1B with #FFFFFF primary and #EEEEE7 text, with body color/background stepping over 250ms.
- Accents: #0C50FF is the Internet-blue interaction signal (selection, mobile menu, online dot, live cursor pixels); Values uses #FF4F43 only for annotations/numbers/quote rules, while #F9DA49, #5E2320, #EADFDD, #4C5248, and #DDEDEA identify its successive story chapters.
- Type: homepage/careers use EB Garamond 28px/1.2 headings (400, italic for statements), 24px/1.4 subheads, and 20px/1.4 body; ABCDiatypeMono is 14px uppercase, 400, 2.1px tracking. Values sets IvarText 16px/150% prose and system-ui 32px/130% 700 pull quotes.
- Space: homepage rhythm is 10/20/40/50/75px, with 700px statement, 720-740px footer, and 21ch→28ch headline caps; Careers is 820px with 20px gutters; Values narrows prose to 600px inside 140px/160px sections. Applied editorial/link surfaces are square (0px radius); primary breakpoints are 800/1000px, Values 991/767/479px.
- Motion: border/focus changes run 250ms cubic-bezier(.4,0,.2,1) or cubic-bezier(.77,0,.175,1); page reveal is 400ms cubic-bezier(.77,0,.175,1), logo travel 700ms cubic-bezier(.87,0,.13,1), and the online square pulses 2s cubic-bezier(.4,0,.6,1) infinite.
- Structure: homepage is a centered 100svh logo → italic statement → two CTAs → link footer, with presence/theme controls fixed top-left; Careers becomes an 820px accordion document, while Values is a separate 600px long-read alternating full-width color chapters, images, captions, and margin navigation.
- Signature: a pixelated fixed canvas maps the pointer and simulated concurrent visitors onto a 10px grid in #0C50FF; cells fade in 500ms, simulated paths advance every 175ms, and a live online count plus Show/Hide control makes collective browsing visible over the otherwise spare page.

Avoid: Do not reduce this to cream, serif italics, and dotted links; its identity depends on the live-presence pixel layer, custom animated logo, and unusually quiet composition. Treat the colorful Values essay as a deliberate legacy subworld, not a palette to spread across the homepage.
