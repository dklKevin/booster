# https://www.sequoiacap.com (sector: vc, sweep: mode, fetched 2026-08-06)
status: full-css

## Default patterns observed (5-8 bullets)
- Hero: a sticky wordmark/navigation header leads into a centered, text-only mission statement, “We help the daring build legendary companies.” The highlighted phrase is ringed by an inline hand-drawn SVG; CSS gives the hero a 22rem minimum height at base and up to 50rem responsively, with 4rem vertical padding.
- Palette: the light-mode page uses warm off-white `#fbf7f0`, near-black `#1b1917` text, and gray `#aeada9` rules. Sequoia green appears as the default tile color `#00a071` and footer/deeper-green tile `#007354`; homepage tiles also explicitly use `#1b1916`, `#1f8ac4`, `#b06300`, and `#fab23a`.
- Type: Rosart is the serif used for the animated hero and newsletter headline; Unica is the sans used in the footer and many card headlines/details; PitchSans is used for uppercase utility text such as card categories/CTAs and the mailing-list eyebrow. All three are self-hosted with CSS `@font-face` declarations.
- Layout: below the hero, one dense 12-column “ink” grid mixes 14 large square tiles and 4 small square tiles. Desktop CSS spans large tiles across 6 columns and small tiles across 3, with 32px gaps and thin `#aeada9` separators; this is followed by a full-width newsletter signup.
- Imagery: every ink tile has a 1:1 aspect ratio and uses cover-cropped media. The fetched homepage contains 14 images, 2 videos, and 2 Lottie animations, mixing portraits, editorial/technology artwork, screenshots, branded graphics, and animated motifs; dark gradient protection is applied behind overlaid white text.
- Trust signals: credibility is staged through founder/company framing (“Our Founders,” “Our Companies,” “idea to IPO and beyond”), named Sequoia authors, company-partnership stories, and an “Explore our companies” tile. Badges, accreditations, and numeric portfolio/performance statistics were not present in the fetched homepage source.
- CTAs and footer: tiles use compact uppercase content-type labels plus verb CTAs—primarily “Read,” with “Listen” and “Watch”—whose CSS reveals the verb on hover. A centered email capture (“Get the best stories from the Sequoia community”) precedes a heavy `#007354` footer with About, Business Entities, Login, motion controls, and copyright columns.

## Tells (3 one-liners)
- An oversized serif founder-myth mission statement, centered in acres of warm off-white and marked with a hand-drawn circle.
- A masonry-like wall of square editorial tiles that turns portfolio authority into a media feed.
- Institutional trust delivered through company/founder names and partner bylines instead of badges or performance numbers.
