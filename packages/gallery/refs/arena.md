# arena (are.na, extracted 2026-08-07)
status: full-css

- Neutrals: light ground/text #FFF/#000 with steps #F7F7F7, #EDEDED, #DEDEDE, #999, #696969, #333; dark ground/text #000/#FFF with #1A1A1A, #333333, #4F4F4F, #696969, #B2B2B2, #E5E5E5. Inputs move gray1 to gray2 on hover/focus; buttons retain gray1 and gain a gray3 border.
- Accents: focus and draggable dividers use blue #3D46C2 light/#5E6DEE dark; public-channel state uses green #238020/#98DC89; private-channel state uses red #B93D3D/#EB6864; alerts use orange #E15100/#FF7A30.
- Type: custom `areal` WOFF2 with `areal, "areal Fallback", Arial, Helvetica, sans-serif`; token scale 12.5, 14.4, 16, 19.2, 24, 28, 32, 40, 48px. Applied channel header is bold 28px/35px; block captions are 400 12.5px/16.875px; text components use 1.35-1.45 leading and bold is the only emphasis weight.
- Space: 5px base with 5/10/15/20/25/35/45/65/80/100/130px ladder; 3px control radius, circles 50%, pills 9999px. Desktop gutters are 65px and collapse to 15px at 520px; gallery columns are minmax(260px,1fr), minmax(150px,1fr) at 520px; no global content max-width found.
- Motion: hover actions reveal in 50ms; block images fade in over 100ms ease; header and dividers transition 200ms ease-out; skeletons pulse 500ms ease-in-out; the 2px loading rail runs 60s cubic-bezier(0,1,1,1) with 250ms ease-out/125ms delayed ease-in completion. Reduced-motion disables all transitions and animations.
- Structure: a fixed 55px header sits above a 12-column shell that collapses at 900px; channel identity and metadata precede a virtualized auto-fill block grid with 15px gaps, reduced to 5px for the two-up mobile layout.
- Signature: every heterogeneous saved block is normalized to a square 1:1 media well, then a separate 65px caption band after a 10px gap; tiny 12.5px titles and hover-only connect/open controls let images, links, text, and channels read as one continuous visual index.

Avoid: Do not turn this into rounded-card masonry or decorate every tile; most content edges stay square and the 3px radius belongs chiefly to controls/status surfaces. The system depends on dense heterogeneous blocks plus terse metadata, so sparse uniform imagery loses the recognizable archival rhythm.
