# panic (panic.com, extracted 2026-08-07)
status: full-css

- Neutrals: homepage content ground #ebebeb over a #1c1c1c body; support steps to #171717 with #808080 copy; hover popovers invert to #fff with #444 copy, while the footer recedes to #666.
- Accents: rgba(120,0,255,1) identifies section headings; rgba(68,185,208,1) marks follow/social; rgba(255,205,63,1) marks support and Playdate; #9844f6 is the default popover action, while #a12e32 and #0852ff stay product-local to Herdling and Ratcheteer.
- Type: homepage uses "Booton", system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif at 4rem/1.3 (40/52px capped), weight 300; section heads are 4.2rem/4.5rem, popovers 1.6rem/2rem, support 2.4rem/4.6rem, with 600 for actions; interiors deliberately swap to space-mono/Saans (Prompt) and "BootonVF", sans-serif (Transmit).
- Space: 1rem equals 1vw from 240-999px then caps at 10px; the icon rail maxes at 105rem with 22rem square targets, sections recur every 3rem, the takeover reserves 72rem, and popovers use 2rem padding with a 1rem radius.
- Motion: hero titles scale over .4s ease-in; takeover swaps fade 350ms linear; icons lift from scale(.9) to scale(1) over .15s ease-in-out; speech bubbles rise and fade over .5s ease-in-out; the Despelote ball runs 1000ms ease-out.
- Structure: a full-bleed, product-themed takeover ends in a 120vw x 6vw wedge rotated -3deg, then app, game, console, and follow icon groups share one centered rail before a dark support/footer block; Prompt instead uses a 42ch terminal grid and Transmit 84.5rem chevron sections.
- Signature: 22rem product/game icons behave like a visual launcher - each scales up and translates -1rem on hover while a white, shadowed speech bubble moves 5rem upward from behind it, exposing product-specific title art, copy, platform, and action color.

Avoid: Do not collapse the route-specific palettes, fonts, and title art into one tidy brand system; the coherence depends on a neutral shell and repeated icon proportions while each product keeps its own voice. The 1vw rem scaling and 40px body cap suit sparse labels and large art, not dense interface copy.
