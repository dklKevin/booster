# https://my.clevelandclinic.org (sector: hospital, sweep: mode, fetched 2026-08-06)
status: full-css

## Default patterns observed (5-8 bullets)
- Hero: a 2880x1740 photo of a smiling uniformed caregiver and patient beside an imaging scanner, used as a cover background from 600px upward; a bottom dark gradient supports a centered white reassurance headline, “We're here when you need us - for every care in the world.” The title is bold and reaches 70px/75px at 900px; there is no hero CTA in the fetched markup.
- Palette: institutional blue drives links and buttons (#0078bf and #007bc2), with a blue gradient hero fallback (#0078bf to #0088d9), dark navy hover/emphasis (#1b477b), orange “strong” appointment buttons (#f08122), green utility emphasis (#00843d; the third CTA heading is #249c3d), pale blue icon fields (#f1faff), pale gray bands (#f5f5f5), and charcoal text (#363636/#4a4a4a).
- Type: the page requests Roboto (400/500/700/900) and Roboto Condensed, while the bundled CSS also embeds Source Sans Pro. General headings use Source Sans Pro with News Cycle fallback, but homepage story, CTA, spotlight, and content panels use Roboto; the result is a mixed legacy/new sans-serif system with bold, oversized section headings and underlined blue text links.
- Layout: a long modular stack moves from a three-card care-entry carousel (Providers, Locations, Appointments) to two image/text highlight splits, three utility CTA cards, a four-item “Why Choose” grid, a Health Library widget, a seven-location image carousel, an eight-link provider resource grid, an asynchronously loaded news section, and a fixed-style contact ribbon.
- Imagery: the hero uses bright, high-key clinical photography showing friendly human interaction and visible medical equipment; the three primary task cards instead use flat pastel illustrations (doctor with five stars, map pin, checked calendar). Lower location cards use facility/campus photography, while utility and trust sections use small medical/service SVG icons.
- Trust signals: credibility is staged as a “Why Choose Cleveland Clinic?” four-card icon grid - Patient-centered care, National recognition, Collaborative providers, and Innovation and research - plus “300+ locations” in the location CTA. No accreditation badge or named ranking/statistic is present in the fetched homepage markup.
- CTA and footer weight: actions repeat as blue underlined links and compact uppercase buttons, with an orange “Request an Appointment” button in the contact ribbon beside the appointment and questions phone numbers. The footer is heavy: a gray social strip followed by four navigation columns (Actions; Blog, News & Apps; About; Site Information & Policies) and a bordered legal/copyright row.

## Tells (3 one-liners)
- A warm caregiver-patient hero is immediately followed by the triad “find a provider / locations / appointments.”
- Blue-and-white utility cards divide care access, wellness content, and administrative help into separate funnels.
- Repeated phone numbers and an orange appointment button persist just above a four-column institutional footer.
