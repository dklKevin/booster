# remarkable (remarkable.com, extracted 2026-08-07)
status: full-css

- Neutrals: light-neutral sections use paper #fcfbf8 with ink #211e1c and stepped papers #f3efe7/#e7e1d5; dark-neutral reverses to #211e1c/#fcfbf8, while applied green sections use #1c211c/#f7f8f7 and red-tinted light sections #f8f7f6/#231a1a.
- Accents: #2559f4 is the sole primary-action blue, moving to #1142d4 on hover and #003bb2 active/focus; #e9f2ff and #cce1ff are its subtle ground and hover step.
- Type: reMarkableSerif, "Book Antiqua", Georgia, serif carries headings at variable weights 325-400; reMarkableSans, Helvetica, sans-serif carries body/UI at 400-500. Fluid body runs clamp(.875rem,.069vw + .854rem,.938rem) through clamp(1.5rem,.969vw + 1.212rem,2.375rem), line-height 1.4; headings run clamp(1.5rem,.969vw + 1.212rem,2.375rem)/1.2 to clamp(2.75rem,4.152vw + 1.517rem,6.5rem)/1.
- Space: base increments are .125/.25/.375/.5/.75/1/1.5/2/3/4/5/8rem; responsive 1x/2x expand 1/2rem -> 1.5/3rem at 475px -> 2/4rem at 768px -> 4/8rem at 1024px -> 5/10rem at 1440px. Corners are mostly 2px, with full pills; content uses paired side margins, article measure clamp(min(100%,420px),60%,880px), page max 2560px, and side rails become 12.5% at 90rem and 15% at 120rem.
- Motion: grid entrances use .5s cubic-bezier(.5,1,.89,1); exits .6s; repeated content opacity transitions are .1s and navigation color transitions .3s cubic-bezier(.4,0,.2,1). Motion-reduce variants remove transform/will-change behavior.
- Structure: long image-led chapters alternate full/default/wide containers on a 12-column responsive grid; the product page adds configuration and accordion modules, while articles collapse prose to the centered 420-880px measure with wider media breakouts.
- Signature: a 1px vertical "paper margin" sits at the responsive side inset through successive color-themed sections, paired with a 3px (4px from 48rem) inset cursor rule and oversized low-weight serif copy; it turns the whole scroll into one continuous notebook surface.

Avoid: Copying only the warm off-white, blue buttons, and serif headings produces generic premium hardware. The identity depends on the margin/cursor geometry, unusually square 2px controls, fluid low-weight type, and photography/diagram choreography working together; do not transplant the rail without similarly deliberate sectional alignment.
