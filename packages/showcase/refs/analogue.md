# analogue (analogue.co, extracted 2026-08-07)
status: full-css

- Neutrals: Homepage ground #EAEAEA with #000000 type; product chapters/catalog invert between #000000/#ffffff and object-specific greys #D7D7D7, #B8B8B8, #D5D5D5, #E4E6E5; editorial panels are #F2F2F2 with secondary copy #686868, while index links move #aeaeae to #595959 on hover.
- Accents: #6A69D1 belongs only to the Analogue Duo catalog tile; #26B33D is the article's mobile back-to-announcements bar; #F90000 text and #F95A00 icon are reserved for newsletter errors.
- Type: CircularXx with "circularXx Fallback" (Arial-derived), feature setting ss08; weights 400/450/500/600. Fluid scale runs nav 12px/3.75vw mobile to 9px/.918vw desktop, body 18px/5.625vw to 18px/1.837vw, and hero 27px/8.438vw to 36px/3.673vw, mostly line-height 1-1.2 with negative tracking.
- Space: Two viewport units encode nominal pixels: fm1=.3125vw and f1=.102vw; at 48rem the full-width wrapper changes from 3.75vw to 2.041vw side padding and gains 16 columns with .408vw gaps. Hero art caps at 86%, manifesto copy at 64%; radii range from .408vw editorial panels to 2.857vw desktop chapter seams (mobile 2.5vw and 4.489vw).
- Motion: Applied defaults are .15s cubic-bezier(.4, 0, .2, 1); mobile menu expansion and review-card opacity use .3s (the latter cubic-bezier(0, 0, .2, 1)); the homepage news strip is a 40s linear infinite marquee.
- Structure: A sticky transparent header sits over full-bleed product-image chapters; catalog cards form one column then two, while navigation, footer, and editorial content align to the 16-column desktop grid and collapse at 48rem.
- Signature: Museum-scale isolated hardware renders fill monochrome/color-field chapters, with tightly tracked product names and tiny outlined availability pills anchored to the lower edge; rounded section seams make each object read as a discrete exhibit.

Avoid: Copying only the black/white palette and oversized type produces an empty luxury-tech shell. The restraint depends on immaculate purpose-shot product renders, per-product ground colors, and viewport-calibrated cropping; without those assets, its sparse chapters lose their hierarchy.
