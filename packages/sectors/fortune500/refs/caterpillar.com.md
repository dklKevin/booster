# https://www.caterpillar.com (sector: fortune500, sweep: excellence, fetched 2026-08-06)
status: wayback

## Token block (~10 lines)
- Palette — brand/action/focus yellow `#ffcd11`; primary CTA uses yellow fill, black text, and yellow border.
- Palette — structural black `#000000` for the global navigation, search, hero fallback, dark teasers, and footer-like panels; white `#ffffff` for reversed hero text and light surfaces.
- Palette — soft section/table surface `#f8f8f8`, card/divider gray `#cccccc`, and darker UI gray `#3f3f3f` for hover states.
- Palette — functional link blues `#2679b8` and `#0067b8`; both occur in link/action rules, with `#0067B8` also used by editorial-card chevrons.
- Type pairing — headings: `"Roboto Condensed Bold", Arial, "Helvetica Neue", Helvetica, sans-serif`, weight 700, line-height 1; general paragraphs: `Arial, "Helvetica Neue", Helvetica, sans-serif`, line-height 1.45; hero supporting copy: `"Noto Sans Regular", Arial, "Helvetica Neue", Helvetica, sans-serif`.
- Type scale — desktop H1 58px, H2/H3 26px, H4 22px, H5 20px, H6 14px; hero headline 54px/54px; mobile H1 and hero headline 30px, while mobile H3/H4 are 16px and H5 is 14px.
- Spacing rhythm — primary sections use 60px top/100px bottom; no-top/no-bottom variants preserve the opposite value; mobile sections compress to 42px/42px. Subsection gaps are 54px, and title gaps shift from 44px to 36px on mobile.
- Component spacing — containers have 10px side padding (15px below 768px); hero copy uses 12px below headings, a 22px gap after the accent bar, and 27px above its CTA; editorial cards use 12px horizontal gutters and 16px internal padding.
- Layout intent — responsive 12-column grid with container maxima 719px at 576px, 720px at 768px, 960px at 992px, and 1140px at 1200px; three-column editorial cards are 33.33333% each and collapse at smaller breakpoints.
- Signature element — the `#ffcd11` accent bar is exactly 40px × 5px and recurs beneath titles and hero copy, tying full-bleed photographic/gradient heroes to restrained black-and-white content sections.

## Lessons (3-5 bullets)
- Let one tightly specified brand primitive do repeated work: the 40px × 5px yellow bar marks hierarchy without turning every surface yellow.
- Pair condensed, uppercase display typography with plainer body copy; the 58px-to-26px headline drop creates an industrial, high-authority voice while body text remains readable at a 1.45 line-height.
- Use full-bleed photography selectively, then protect overlaid messaging with a source-defined black-to-transparent gradient and a copy column capped at 55% rather than relying on image choice alone.
- Make dense corporate navigation feel intentional by reserving `#000000` for the global frame and `#ffcd11` for active, hover, focus, and CTA states; the same state color teaches interaction across components.
- Preserve a generous desktop section cadence (60px entry, 100px exit) but explicitly compress it to 42px on mobile instead of scaling every gap independently.

## Avoid (1-2 bullets)
- Do not copy the yellow at high coverage: the source uses it as a narrow accent, state signal, or CTA fill against dominant black, white, and `#f8f8f8` surfaces.
- Do not transplant the 54px condensed hero type without the 55% copy constraint and gradient/image treatment; it would become visually heavy and lose contrast on arbitrary imagery.
