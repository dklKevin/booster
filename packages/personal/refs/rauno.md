# Rauno Freiberg (rauno.me, extracted 2026-08-06)

- Neutrals: Radix gray ramp; light bg #FCFCFC/text #171717, dark bg #161616/text #EDEDED; hover moves one step up the ramp, 100-150ms ease-out.
- Accents have exactly one meaning each: #FFFF02 yellow only ever means "you are here" (nav tracker fill, text selection); six others live only inside code and demos.
- Type: single-weight sans (400 and 500 alias the same font file); prose 16/28; the essay h1 is 16px secondary gray, identical to body, and still reads because live demos are the visual payload.
- Space: hard 8px grid (8-88); radii 4/8/16/9999; 720px prose column; figures escape to 960px via 100vw translate trick without reflow.
- Motion: one spring (stiffness 620, damping 45, mass 0.2) lives in the app shell, never unmounted; many elements derive from its live value, so mid-flight interruption stays correct.
- The only transform anywhere is scale(0.96) on button press; focus is one global 2px outline contract.
- Signature: 20-hairline minimap at page top that is also the nav; each line computes opacity from the tracker's live position, erasing lines it passes over mid-spring.

Avoid: the minimap as decoration is noise; its lines carry information. The gray-on-gray restraint works only because essays carry live interactive components as visual payload.
