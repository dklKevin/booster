# https://www.palantir.com (sector: defense, sweep: excellence, fetched 2026-08-06)
status: full-css

## Token block (~10 lines)
- Light palette: canvas #FFFFFF; raised/alternate surfaces #F3F3F3 and #F9F9F9; primary text #1E2124; secondary text #636363; tertiary text #767676.
- Dark palette: canvas #1E2124; alternate surfaces #2F3234 and #494A4B; primary text #FFFFFF; secondary text #B9B9B9; tertiary text #9B9B9B.
- Accents: default green #2B5945 on light; blue #4E8AF7 on dark/light-blue themes; theme variants salmon #F2C4BF, mint #A6F2CC, and gold #8C7847; error #FF4136.
- Type pairing: Alliance No.1 for body/base display and Alliance No.2 (falling back to Alliance No.1, then system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Oxygen, Ubuntu, Cantarell, Fira Sans, Droid Sans, Helvetica Neue, Helvetica, Arial, sans-serif) for large headlines, captions, and earmarks; supplied at 400/700 with italics.
- Body scale at the extracted 18px root: 16px/1.4286, 18px/1.3889, 20px/1.3, and 34px/1.1765; captions are 10px/1.6 with 0.05em tracking and uppercase treatment.
- Responsive headline scale: 34px mobile; at 560px, 40px and 50px tiers; at 960px, 50px, 72px, and 100px tiers, with -0.02em tracking on large display text.
- Homepage hero type is a separate 30px mobile / 80px desktop display treatment; another interior hero scales 42px / 96px / 140px at 760px and 1200px breakpoints.
- Spacing rhythm is 10px-centered: 3px tiny, 10px XS, 20px S; gutters step 10px → 15px → 30px, horizontal page padding 20px → 30px, and section padding 60px → 80px → 100px.
- Layout intent: a fluid 12-column grid with 10/15/30px responsive gaps, content capped at 80rem (1440px at the 18px root), and asymmetric column spans used to keep copy narrow beside expansive media.
- Signature element: a fixed full-viewport video hero with an 80px desktop headline whose words reveal upward from clipped masks (`clip-path: inset(0 0 100% 0)`) in `mix-blend-mode: difference`, followed by a flickering, bouncing arrow.

## Lessons (3-5 bullets)
- Make the restrained black/white/gray system carry most of the interface, then assign accent colors by theme or content context instead of scattering brand color across every component.
- Build authority through a rigorous 12-column editorial grid and deliberately narrow text spans; let mission imagery and video consume the remaining columns rather than compressing both into equal halves.
- Separate utilitarian reading typography from expressive display typography: Alliance No.1 keeps dense material calm while Alliance No.2, tight tracking, and sharply larger tiers create campaign-level emphasis.
- Treat motion as a small number of identifiable system gestures: the clipped word reveal in the hero and the extracted fixed 28-degree gray page wipe with centered Palantir mark are more memorable than many unrelated micro-animations.

## Avoid (1-2 bullets)
- Copying the 80px blended headline over arbitrary footage can destroy legibility; the extracted treatment depends on full-viewport media, high contrast, clipping, and carefully limited text.
- Reusing every available accent at once would erase the hierarchy: the source defines green, blue, salmon, mint, and gold as theme variants, not a simultaneous rainbow palette.
