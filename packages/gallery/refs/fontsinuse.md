# fontsinuse (fontsinuse.com, extracted 2026-08-07)
status: full-css

- Neutrals: #FFFFFF page/main ground and overlay text; #000000 body text and mobile rule; #F0F0F0 image placeholders/sample dividers, #DDDDDD and #CCCCCC borders, #999999/#666666/#444444 metadata steps; tile hover is rgba(0,0,0,0.8).
- Accents: #FF4B33 is the sole front-facing signal red for link hover/active, errors, and alerts; #FFF380 and #339933/#77CC77 exist as source tokens but their public gallery role is unverified.
- Type: BentonSansRE, Verdana, sans-serif body at 14px/1.6 (22.4px); RelayCond, Arial, serif headlines at 48/36/30/24px with line-height 1, bold for h1-h3; gallery overlay h4 is regular and drops to 16px at 20-44.99em, captions are 12px/1.25, contributor text 10px/1.2.
- Space: 10px base unit with 5/15/20/30/40px derivatives; gallery gap 20px and cell bottom rhythm 30px, header/main rhythm 20px; containers max at 700/940/1180/1420px, desktop tiles target 220px; gallery tiles have no radius rule.
- Motion: masonry cells use `opacity 0.2s, margin-top 0.2s`; sponsor opacity uses 250ms; the full-tile hover detail swaps by `display` with no transition; loader spins use 400ms linear infinite.
- Structure: a 240px brand column precedes the archive/search header; the gallery steps through 2/3/4/5/6 equal columns at 20/30/60/76.25/91.25em, while use pages pair a 700px article with a 220px metadata rail and 20px gap, collapsing below 60em.
- Signature: every square artwork tile reveals a full-surface rgba(0,0,0,0.8) title/date/designer/contributor panel, then continues below as one or more monochrome font-specimen image strips (minimum 46px high at desktop) separated by 1px #F0F0F0 rules.

Avoid: Copying only the tiny typography, dense taxonomy, or hover veil reads dated and hides essential context. The effect depends on strong artwork, real specimen-strip assets, and the image-to-typeface relationship; without those, the 220px archival grid becomes generic thumbnail inventory.
