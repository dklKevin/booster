# https://www.crowdstrike.com (sector: cybersecurity, sweep: mode, fetched 2026-08-06)
status: full-css

## Default patterns observed (5-8 bullets)
- Hero pattern: an autoplay three-slide promotional carousel (`8500ms` delay) pairs report/event/AI-security headlines with one red CTA each over wide responsive background art; it is followed by a dark textured platform statement, “The Agentic Security Platform,” and a large Falcon platform graphic.
- Palette: black `#000` and white `#fff` are the dominant surfaces/type pair; signal red `#EC0000` drives primary CTAs and emphasis, darkens to `#D30000` on hover, and occasionally runs into electric blue `#0024FF` in separators/gradients; pale `#F8F8F8` and gray `#707070` support secondary surfaces and controls.
- Type: Neue Haas Grotesk Display Pro is the base/body, link, and much heading face; CrowdStrike Sharp Sans is the heavier display/component face used for prominent titles, cards, accordions, and forms, with Helvetica/Arial fallbacks. Desktop CSS sets body at 24/32px, H1 at 56/64px, and H2 at 48/56px.
- Layout: the homepage stacks a rotating hero, a centered platform proclamation and product diagram, a three-part “Future of Security” feature set, analyst-recognition cards, a bundle/pricing card grid, a testimonial-video carousel, and a final solution-card section.
- Imagery: fetched assets verify black-and-red geometric hero art with glowing nested chevrons, dark gradient/texture backgrounds, and dense branded platform diagrams composed of concentric arcs, agent icons, labels, and red-to-teal gradients; stock-photo use was unverified in the inspected homepage assets.
- Trust signals: proof is staged in dedicated bands—“Recognition by trusted analysts” presents two Gartner Leader claims and an IDC MarketScape Leader claim, while “Customers trust CrowdStrike” uses three named-role testimonial videos and a link to all customer stories; the event hero also cites “10,000+ security leaders.”
- CTA/footer pattern: `#EC0000` filled buttons with white text and arrow icons repeat as “Start free trial,” report/event actions, “Contact sales,” and “Schedule a demo,” often paired with white outlined secondary actions. The footer opens with a full-width red-gradient “Try CrowdStrike free for 15 days” banner, three CTAs, then five accordion/link groups plus social and legal navigation (57 footer links in fetched HTML).

## Tells (3 one-liners)
- A black field cut by luminous red geometric threat-tech shapes, capped with a red arrow CTA.
- “Unified platform” messaging made literal as a dense concentric security architecture diagram.
- Analyst Leader cards, named security-leader testimonials, and a free-trial CTA repeated before a link-heavy enterprise footer.
