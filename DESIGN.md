# Design invariants

Read this before designing any UI, page, artifact, or visual deliverable.
Constraints here are outcomes, not process.
Design freely within them.

## Ban list (the mode, excised by name)

Never use any of the following.
They are the statistical default of every model and mark output as generic on sight.

- **B001** Inter, Poppins, Montserrat, Roboto, or Open Sans as a display face.
- **B002** Purple-to-blue (or any) gradient hero backgrounds, and gradient text headlines.
- **B003** Glassmorphism: frosted panels, backdrop-blur cards, translucent white overlays.
- **B004** The centered single-column hero: badge pill, big headline, subhead, two buttons.
- **B005** Card grids of rounded-xl boxes with soft shadows, icon top-left, title, blurb.
- **B006** Emoji as icons or bullets, sparkle and rocket motifs.
- **B007** The default SaaS palettes: indigo/violet on white, teal on navy, cream plus terracotta.
- **B008** Three-column feature sections with identical cards.
- **B009** Decorative blob shapes, dot grids, and floating abstract gradients.
- **B010** "Delve/unlock/elevate/seamless" marketing voice in interface copy.
- **B011** Em dashes in copy; use plain dashes. (Observed failure: appeared in every A/B run, 2026-08-06.)
- **B012** The accent-colored italic serif word inside a roman headline. (Observed failure: 7 sightings across every high-effort run, 2026-08-06 to 2026-08-08; survived the spec repeatedly.)
- **B013** A full-width mustard or ochre accent band as the page's closing section. (Observed failure: three consecutive website builds, 2026-08-08.)
- **B014** The one-scroll website anatomy: hero, proof-stat strip, numbered service ledger, team roster, request form, colored closing band, footer. If two builds could swap outlines, the outline is the mode. (Observed failure: every 2026-08 website build shared it.)
- **B015** Deep forest or spruce green as the anchor palette. (Observed failure: seven consecutive builds across three subjects, with and without the spec, 2026-08-07 to 2026-08-09.)
- **B016** The numbered hairline service ledger: 01/02/03 rows separated by rules. (Observed failure: five consecutive website builds, 2026-08-07 to 2026-08-09.)
- **B017** AI-cadence copy: contrast-frame lines built as "X, not Y" ("a plan, not a pitch"), and demonstrative or prepositional scaffolding ("This means...", "These are...", "Through this...") carrying sentence after sentence. Say the thing directly, in the voice the organization's own front desk would use. (Observed failure: every 2026-08 build's copy leaned on these, 2026-08-09.)
- **B018** Aphorism headlines: the two-beat fragment pair ("Forty tanks. Plenty to ask.") and koan-style section titles ("Three systems, one careful routine."). When a plain label does the job, the plain label wins: "Contact" beats "Tell us what the tank needs to do." Voice lives in body copy, sparingly; headings and navigation are wayfinding. (Observed failure: every heading of a 2026-08-09 build.)

If a choice would appear unchanged in a hundred other AI-generated pages, it is banned even if not listed.

## Hard floors (non-negotiable)

- Text contrast: 4.5:1 minimum for body, 3:1 for large text, in both themes.
- Every flow is keyboard-operable, uses semantic controls, and preserves a logical focus order. Every interactive element has a visible focus state.
- Touch targets are at least 44 by 44 CSS pixels on mobile. Mobile text inputs render at 16px or larger, and browser zoom is never disabled.
- Animation respects prefers-reduced-motion.
- Theme count is a derived decision: ship the single theme the audience and register call for (patient-facing, print-register, and trust-heavy pages usually commit to light; terminal-register pages may commit to dark). Never add a second theme a sector would not use. When both themes ship, each is deliberately styled, never one inverted from the other.
- No horizontal body scroll; wide content scrolls inside its own container.
- Applicable empty, sparse, dense, loading, success, and error states are designed. Every dead end includes a useful next action or recovery path.
- Never invent customers, metrics, testimonials, certifications, availability, or product behavior. Missing proof remains missing.

## Design packages

Reference material lives in the installed design library (`~/.claude/design/packages/` or `~/.grok/design/packages/`), one package per situation, each holding a `PACK.md` (cross-site lessons) and a `refs/` folder (one distilled site per file).

- `packages/interface`: product and tool UI, apps, dashboards, anything with controls.
- `packages/editorial`: presentation pages built on ideas; landing pages, pitch docs, book-like pages.
- `packages/document`: research docs, study guides, reviews, long-form reading.
- `packages/personal`: the repository's personal website style, portfolio, and identity pages.
- `packages/gallery`: imagery-first pages where the interface recedes.
- `packages/showcase`: physical-object pages; cars, hardware, anything that must be desired.

A second axis lives in `packages/sectors/` (16 sectors: aviation, bigtech, biosecurity, coding, cybersecurity, defense, fortune500, hair-salon, hospital, law, opensource, pharma, retail, startup, supplements, and vc; growing).
Form packages say how a page is built; sector packages say what credibility and register mean in that industry, including the sector's own mode to avoid.

Loading rule: read the matching form package's `PACK.md`, the sector package's `PACK.md` when the brief belongs to an industry, plus 2-3 refs total chosen for the brief.
Never load a whole refs folder; the library is wide so that no single ref can dominate.
Packages grow as the library owner approves new sites; they record that owner's taste, so do not edit them unprompted.

## Evidence lifecycle

The stable ban IDs above are audit handles, not a license to grow the list speculatively.
Record explicit rejected patterns in `evidence/observations.json` with the subject, model, build or artifact, screenshot when available, date, and the user's exact wording.
The tooling may surface repeated candidates, but it never promotes one automatically.
A new ban still requires repeat independent evidence and explicit library-owner confirmation.
Legacy bans whose original runs predate the structured ledger remain marked as legacy evidence instead of receiving invented provenance.

## Derive step (per artifact, before building)

Read the project's existing design tokens, components, brand assets, and design documents before reaching for the library. Preserve established project language unless the brief explicitly calls for a redesign.
Ground the design in the subject itself: its era, material, discipline, or mood.
From that grounding produce a palette with roles, a type pairing, a layout intent, an imagery plan, and one signature element, honoring the bans above.
A signature element appears with restraint, in the one or two places it means something; stamped on every image or section it becomes a watermark.
The imagery plan is not optional in photography-led registers (care, travel, food, objects, places, people): decide what photography the real organization would have, where it sits, and how it is treated.
When real photos are unavailable, art-direct placeholders that hold photography's exact place: inline SVG scenes, treated compositions, real aspect ratios. A type-only page in a photographic register is its own kind of generic, and a gray box is not a placeholder.
When the deliverable is an organization's website, the information architecture is part of the derive: the page structure should match the organization's real jobs and audiences, with plain-named navigation and working links.
One endless scroll is its own mode; so is a set of pages that all share one template stack.
A real organization's website is mostly operational surface: the unglamorous content its users actually come for (the exact set derives from the sector).
Build that surface and let the craft live in how clearly it works; a site that keeps only the photogenic fifth of the organization reads as a brochure mockup, not the organization.
Sketch three materially different directions before committing. Give each direction a compact ASCII wireframe plus palette roles, type roles, layout intent, imagery plan, and one signature element.
The first direction that comes to mind is the mode; discard any two directions that share a family (ground hue, display voice, anchor accent), then commit to one that serves the audience.
Run the counterfactual before selecting: if a similar prompt for a different subject would produce the same direction, discard it.
Refs are range markers that teach how to think, never what to build.
This is a free-form design task, not a form to fill out.
Four gates before building:
- Uniqueness: if this plan - palette, signature element, or page outline - could appear for a different subject, redo it.
- No cloning: if this plan recognizably reproduces a ref's signature element or anatomy, redo it.
- Category legibility: if a first-time visitor could not tell what kind of organization this is within one viewport (a clinic, a store, a magazine), redo it. Escape the sector's mode, never the sector itself.
- Believability: would this organization actually ship this site? If it would sit better in a design portfolio than in the organization's everyday reality, the craft is pointed at the wrong target; redo it.

## Photography integration (when the page carries photos)

Outcomes, not process:
- No undecided edges: every photo's boundary is a deliberate design decision, never a default rectangle floating on the ground.
- One grade: photos and page share a palette; a photo's whitepoint and shadows agree with the page's ground and ink.
- Photography and layout are designed together; a photo dropped into a finished layout reads as dropped.
Art-directing at generation time (environments and light that already carry the palette) beats correcting afterward.

## Judge step (after building)

Render the result and screenshot it at mobile (~375), tablet when the layout changes materially, laptop (~1440), and wide (~1920); users zoom, and layouts are judged at the widths where they fall apart.
Exercise every applicable content and interaction state, including keyboard focus and reduced motion, instead of reviewing only the happy-path first paint.
A section that mixes width-capped content with viewport-bleed content must decide what fills the difference on wide screens; if one side pins to the viewport edge while the other pins to the content cap, the empty remainder reads as a broken layout.
Evaluate the screenshot against the ban list and the derived plan as a separate pass.
Fix what fails, then look again.
Green builds are not evidence; the screenshot is.
