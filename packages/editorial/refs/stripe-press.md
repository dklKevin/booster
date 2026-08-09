# Stripe Press (press.stripe.com, extracted 2026-08-06)

- Theming: two vars inline on body (--backgroundColor + --color); 30+ component stylesheets consume only these, so each book owns a committed color world at zero added CSS. Hover states invert the pair for free.
- Sample pairs (deliberate value jumps, not tints): #4D1A28/#EBADCB, #FFB55E/#0B1743, #2328A0/#EF9E40; selection inverts.
- Type: one serif superfamily in three optical cuts (Ivar Display/Headline/Text), no sans anywhere; heavy italic for labels and eyebrows.
- Scale: 14/15/16/17/18/21/25, optically tuned (~1.07x steps, no modular scale produces it); line-height moves inversely with size; headings reset to 16px/400 so semantics never leak visual weight.
- Detail: letter-spacing .32px on every link and button; 2px radius everywhere; one 60px x 1px rule reused as the only divider motif.
- Spacing: fluid viewport math (calc(10px + 1vw) margins, 6vw to 14vw gutters); breakpoints set where the layout actually broke (599/811/900/1100/1600).
- Layout intent: one continuous stage re-tinted per piece; navigation reads as the room changing color around you.
- Signature: a draggable real-time 3D book with per-title PBR material data (foil, glitter, buckram bump); the non-WebGL fallback is an authored --coverColor rectangle, designed rather than inherited.

Avoid: the 3D centerpiece pays off because a Stripe Press book is a real foil-stamped object the site exists to sell.
