# https://www.starlux-airlines.com (sector: aviation, sweep: excellence, fetched 2026-08-06)
status: full-css

## Token block (~10 lines)
- Core palette: midnight navy `#0f2d3c` for the page body/header and white `#fff` for reversed navigation and hero text.
- Navy depth: `#0f3244` (light), `#092532` (dim), and `#08202d` (dark) extend the core without changing hue.
- Warm surfaces: `#fff8f2` (lightest cream), `#f7eae1` (pale blush menu surface), and `#e1d3ca` (warm divider).
- Accent palette: `#f9c78b` (champagne), `#b3a05f` (muted gold), `#b08061` (warm bronze), and `#a6924e` (olive-gold gradient end).
- Grounding neutrals: `#4e463f` footer brown, `#413b37` dark brown, `#372828` darkest utility-bar brown, and `#767676` border gray.
- Type family: `Montserrat, Noto Sans TC, Noto Sans JP, Tahoma, Mitr, Sarabun, Bai Jamjuree, Microsoft JhengHei, SF Pro TC, sans-serif`; Google Fonts requests weights 200/300/400/600.
- Type scale: 12, 14, 16, 18, 20, 24, 30, 36, and 64px (`.text-xs` through `.text-6xl`); base line-height is 1.5, with 28px and 36px explicit leading options.
- Spacing rhythm: 4px base steps dominate (`space-x-1` = 4px, `space-x-2` = 8px, `mt-3` = 12px, `px-4` = 16px, `space-y-6` = 24px, `space-y-8` = 32px), with larger section padding such as 128px.
- Layout intent: full-width image-led bands aligned to an auto-centered container with 12px gutters, 24px gutters from 1024px, and max-widths of 640/768/1024/1280/1366px at matching breakpoints.
- Signature element: a full-bleed image carousel under a translucent navy header, using header overlap of `-3.44rem` mobile / `-7.55rem` desktop, black-to-transparent image gradients, white shadowed display text, and a translucent `#372828` action rail at the image foot.

## Lessons (3-5 bullets)
- Build aviation hierarchy by layering the global header and task shortcuts directly over destination imagery; the extracted negative margins and 80%-opacity dark surfaces preserve drama while keeping navigation legible.
- Keep the operational UI restrained: the live source uses 14–16px most often, light 300-weight labels, 8–24px local spacing, and warm dividers instead of oversized controls competing with campaign imagery.
- Use one cool institutional anchor (`#0f2d3c`) and a narrow family of warm creams, browns, and champagne accents; this lets booking, loyalty, and editorial content feel related without making every surface identical.
- Treat localization as part of the type system: the primary Montserrat voice hands off explicitly to Noto Sans TC/JP and Thai-oriented Tahoma/Mitr/Sarabun/Bai Jamjuree fallbacks while retaining the same requested weights.
- Reuse the same responsive container and header/footer shell on editorial interiors; the fetched Inflight Dining and Our Fleet pages load the same global CSS and font stack as the homepage.

## Avoid (1-2 bullets)
- Do not copy the many adjacent gold/bronze tokens without fixed semantic roles; `#b3a05f`, `#f9c78b`, `#b08061`, and `#a6924e` are close enough to become inconsistent decoration when applied ad hoc.
- Do not place light-weight white type on photography without the extracted black gradient/text-shadow and dark translucent layers; the contrast system is what makes the overlap treatment usable.
