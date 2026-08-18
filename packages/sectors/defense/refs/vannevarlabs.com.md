# https://www.vannevarlabs.com (sector: defense, sweep: excellence, fetched 2026-08-06)
status: full-css

## Token block (~10 lines)
- Core palette: ink `#222222`, white `#FFFFFF`, dark gray `#595959`, mid gray `#8D8D8D`, light gray `#B2B2B2`, rule gray `#D4D4D4`, and pale surface `#EFEFEF`.
- Homepage palette: dark hero/body surface `#646463` (hero component also specifies `#646464`, with `#585858` browser fallbacks), acid-green accent/root background `#CEF53D`, and gray copy/navigation `#B2B2B2`.
- Section color coding: AI blue `#3D82FF` with dark `#2733C7` and highlight `#DBF3F8`; mission red `#FE0100` with highlight `#FDDFE9`; company green `#96DA03` / `#26B549`; careers amber `#F5761C` / `#FFDE5A`.
- Primary type: `suisseNeue, "suisseNeue Fallback", sans-serif`, generally weight 300 for uppercase display and weight 300–500 for supporting text; `suisseIntl, "suisseIntl Fallback", serif` is used for selected secondary styles.
- Signature/utility type: `thermochrome, "thermochrome Fallback", monospace`, variable weight 200–900, usually uppercase with `0.05em` tracking; `suisseIntlMono, "suisseIntlMono Fallback", monospace` is also loaded.
- Suisse Neue display scale: h0 `60px → 144px` at `.9` line-height, h1 `40px → 72px` at `1 → .95`, h2 `28px → 60px`, h3 `24px → 44px`; display tracking is `-0.02em` to `-0.025em`.
- Thermochrome display scale: h1 `54px → 82px`, h2 `32px → 66px`, h3 `25.212px → 52px`; body/supporting styles include `10px → 14px` and `14px → 18px`.
- Spacing rhythm: `4px` base token; recurring component gaps/padding are `8, 12, 16, 20, 24, 28, 32, 48, 56, 64px`, expanding to `112–128px` for major section separation.
- Layout: full-viewport themed bands contain flex/grid compositions, switch principally at `48rem` and `64rem`, use `24–32px` responsive page gutters, and cap major content at `1440px` with narrower `672px` and `768px` reading measures.
- Signature element: emphasized words switch from light Suisse Neue to uppercase Thermochrome and sit over an animated color band built as a `103%`-wide, `75%`-high pseudo-element behind the letters.

## Lessons (3-5 bullets)
- Encode product and mission families as a controlled color system - blue for AI, red for mission areas, green for company/homepage, amber for careers - while keeping the same typography and layout grammar across them.
- Pair very light, tightly tracked grotesk headlines with a visibly technical variable face only on emphasized words; this creates a defense-tech voice without turning every label into faux-military UI.
- Use the `4px` spacing base for controls and cards, then make section cadence jump decisively to `112–128px`; the contrast keeps dense information legible while preserving editorial drama.
- Let full-width color fields establish context, but constrain actual compositions to `1440px` and prose to `672–768px`; the system scales from cinematic heroes to readable long-form sections.
- Treat responsive type as part of the identity: the extracted display styles grow roughly `60→144px` and `54→82px`, preserving hierarchy rather than merely shrinking a desktop composition.

## Avoid (1-2 bullets)
- Do not copy the acid green, red, blue, and amber together without the site’s section-level theme rules; simultaneous use would turn deliberate wayfinding into visual noise.
- Do not apply Thermochrome to all copy: its extracted role is emphasis, navigation/CTA, statistics, and technical display, while Suisse Neue carries the reading burden.
