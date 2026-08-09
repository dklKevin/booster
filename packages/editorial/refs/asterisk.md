# asterisk (asteriskmag.com, extracted 2026-08-07)
status: full-css

- Neutrals: #faf8f0 paper ground with #000000 text and rules; #d7d6cd footer field, #99999a muted captions/archive controls, and #404040 input placeholders; ordinary links step from black to the primary blue on hover.
- Accents: #2d90cf carries editorial and interaction emphasis in openers, progress, links, and hover-revealed marks; #abd3ec is its soft field for selection, forms, and active/hover states; #f0eca8 belongs specifically to Issue 15's fixed metadata flap.
- Type: Noe Text is the 18px reading serif, Noe Standard the display serif, and Atlas Grotesk the label/UI sans; source tokens compute to 10.8/14.58/16.2/18/21.6/28.8/33.3/86.4px, with 1.0 opener and 1.2 display/title line-heights; article titles deliberately permute serif/sans, roman/italic, and 100/400/600-700/900 weights.
- Space: rem steps are 4.5/9/18/36/54/90px from an 18px root; radii are 0; reading width is 750px, body max 1380px, and the desktop issue flap 420px; major sections use 36px padding and 90px page offsets, with 1300/1024/768px layout breaks plus 1520/640px local breaks.
- Motion: links/buttons 0.2s ease-in-out; default controls 0.25s ease-in-out; menu opacity/translate 0.25s ease-in-out; header 0.5s ease-in-out after 0.25s; progress opacity 0.1s linear; asterisk logo 1.5s steps(12) infinite.
- Structure: the issue landing is a fixed 86.5vh cover beside a fixed 420px information flap, then a scrolling table of contents; articles collapse to a centered 750px reading column with an offset oversized opener and a fixed left-edge progress rail.
- Signature: one issue-specific irregular asterisk drawing propagates through the favicon/logo, a 50px article-row hover reveal, archive-cover hover masks, and a 12-frame sprite animation on the article logo.

Avoid: Randomly mixing its faces and weights loses the content-coded contrast and reads as typographic noise. The asterisk system depends on distinct commissioned issue marks and cover art, so repeating one generic star or copying the fixed-flap anatomy misses the premise.
