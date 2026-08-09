# https://foundersfund.com (sector: vc, sweep: excellence, fetched 2026-08-06)
status: full-css

## Token block (~10 lines)
- Palette / primary surfaces: #ffffff page, header, menu, and portfolio tiles; #202223 primary dark text and 95%-opacity dark overlay.
- Palette / dark and soft surfaces: #181818 team-page ground; #f7eae8 article-content ground; #f2f2f2 header and subnav rules.
- Palette / supporting roles: #555555 long-form copy and secondary links; #333333 default dark utility text; #cccccc dark-detail icon; #fc120b small red arrow accent.
- Active type family: `proxima-nova, sans-serif`; Adobe CSS supplies weights 400, 700, 800, and 900 plus italics. Playfair Display and Helvetica Neue Light are imported in the override CSS, but their application rules are commented out.
- Root scale: 23px at >=1920px, 21px below 1920, 19px below 1600, 18px below 1440, 17px below 1141, 16px below 1065, 15px below 961, 14px below 901, 12px below 585, and 11px below 321.
- Type scale: desktop body 1rem/1.41; mobile body 1.33333rem/1.41; H1/H2 3rem, H3 2.5rem/1, H4 2rem/1.15; detail hero 3.54167rem rising to 5.20833rem at 40em; CTA 1.16667rem weight 600.
- Spacing rhythm: utility steps .58rem, 2.32rem, 3.33333rem, and 5.83333rem; fixed header uses 1.5rem vertical padding, homepage header 2.5rem top at >=40em, and desktop body offset 4.625rem.
- Widths: homepage slide copy max-width 40rem (override from 27.91667rem); long-form content max-width 1500px and 90%; other extracted caps include 24rem, 1024px, and 1440px.
- Layout intent: full-viewport homepage; percentage grid at 40/52/64em breakpoints; team and portfolio tiles move from 2 to 3 to 4 columns, remain square, and center portfolio logos inside 25% insets.
- Signature element: a 100vh portfolio-film slider with white bottom-left headlines/CTAs over full-bleed video, plus directional title transitions using 10% translations and opacity.

## Lessons (3-5 bullets)
- Let portfolio evidence carry the brand: one company story fills the viewport while the firm identity and navigation stay quiet and transparent above it.
- Use a single well-stocked sans family and create hierarchy through a large 2rem/2.5rem/3rem/5.20833rem scale, rather than adding decorative typefaces without a structural job.
- Make dense VC inventories feel systematic: square logo and portrait tiles on the same 2/3/4-column responsive grid allow very different content sets to share one visual grammar.
- Keep editorial depth structurally distinct but token-related: full-bleed 90-100vh story heroes hand off to a constrained 1500px/90% reading field using the same spacing and type system.
- Treat motion as navigation feedback: the slider's short .3-.5s transitions and directional 10% offsets explain movement without adding interface chrome.

## Avoid (1-2 bullets)
- Do not copy every color found in the legacy bundle: later overrides replace red/greyscale tile backgrounds with #ffffff, so ignoring cascade order would produce a materially different site.
- Do not pair the imported Playfair Display or Helvetica Neue Light with Proxima Nova on the evidence of imports alone; the source rules that would apply them are commented out.
