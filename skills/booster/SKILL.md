---
name: booster
description: Build a distinctive UI, page, or website from a brief, business materials, or a new empty workspace by routing to the right Booster packs and references before implementation. Use when the user invokes Booster, starts a visual build, has only a business name and description, needs a new website folder, lacks imagery, or wants a result grounded in the library instead of a preset.
---

# Booster: design-pack routing

You are routing a brief to the right slice of the Booster design library so the build derives from evidence instead of the mode.
The library is two-axis: form packages (how a page is built) and sector packages (what credibility means in an industry).
Loading narrow matters: 2-3 refs total, chosen for the brief, so no single site can dominate the generation.

The default product is a one- or two-shot website build. Keep routing machinery behind the result when the user asked to build. Ask only for missing facts that materially block a credible site, and never turn normal intake into a design questionnaire.

## Step 0: Establish the workspace and asset path

If a usable project or repository is already open, use it and do not ask a folder question.

If no usable project is open, ask one question:

> Do you already have a folder with files about the business, or should I create a new website folder?

- **Existing folder:** ask for its path or for the user to attach/open it, then inspect it read-only before changing anything.
- **New folder:** ask, "What should the folder be called? You can leave this blank if you do not know yet."
- If the folder name is blank, derive a safe slug from the known business name. If the business name is also unknown, use `website-draft-YYYYMMDD` and tell the user it can be renamed later.
- Create the folder only inside a user-authorized writable project location. If no safe parent location is known, ask where to put it instead of writing into the home directory or filesystem root.
- Framework selection belongs to the active builder and project instructions. Ask about it only when the choice would materially change the requested result.

Scan the selected folder for business material before asking for facts: README and notes, PDFs, menus, copy, logos, brand files, existing source, and raster images (`jpg`, `jpeg`, `png`, `webp`, `avif`, `heic`). Never invent an address, hours, price, menu item, translation, testimonial, award, staff member, or business history. Use clearly labeled placeholders when the user prefers a first draft without those facts.

### When no usable photographs exist

Detect the active agent's actual image-generation capability. Do not infer capability from the phrase "OpenAI account" or from the agent's brand.

- If the built-in image-generation tool and `imagegen` skill are available, say: "I did not find usable business photos. Image generation is available here. Would you like me to generate an art-directed website image set, build with art-directed placeholders that can be replaced later, or create an imagery-light direction?"
- If the user chooses generation, invoke `imagegen` and generate only the assets the chosen direction needs. Save selected final assets into the project's established asset directory and update the website to use those project-local files.
- Treat generated images as concept or brand imagery. For a real business, never portray a generated storefront, interior, employee, customer, dish, product, credential, or event as documentary evidence of what exists. Label generated assets for replacement before publication when they could be mistaken for factual business photography.
- Ground generation in supplied facts. Do not fabricate logos, signage, Korean or other translated text, menu items, prices, people, or claims.
- If the capability is unavailable, say: "I did not find usable business photos, and image generation is not available in this agent. I can still build an imagery-light site, build with art-directed image spaces and save a generation brief for later, or wait for you to upload photos."
- Do not make unavailable image generation sound like an error or block the first shot. An imagery-light direction must be deliberately complete. An art-directed placeholder must hold the exact aspect ratio, crop behavior, boundary treatment, responsive role, and visual weight of the future asset instead of appearing as a gray box.
- When the user chooses art-directed spaces for later generation, save a concise image brief in the project's existing design-doc location or `docs/booster-image-brief.md`. For each asset record its intended filename, page placement, aspect ratio, factual inputs, generation prompt, avoid list, and whether it is illustrative or must be replaced with real business photography. If the project is later opened in an agent with image generation, use that brief without redesigning the page, save the generated files into the project, and re-run the rendered audit.
- Mention an API/CLI fallback only when the user explicitly asks for it. Never pressure a user on Claude or another agent to switch products merely to complete the website.
- If usable photographs already exist, prefer them and do not generate replacements unless the user asks.

## Step 1: Scan for context

Gather only what identifies the subject, audience, job, and existing visual language. Usual sources, cheapest first:
- The conversation itself: if the user already described what they're building, that outranks everything on disk.
- Project design documents, CSS variables, Tailwind or theme configuration, shared components, and brand assets. Preserve an established system unless the brief calls for a redesign.
- README.md, package.json (name/description/dependencies), site copy in src/pages or app/ routes, marketing strings.
- Domain keywords that signal a sector (patients/clinical, flights/fleet, contributors/license, reps/scoops, funds/portfolio...).

Do not deep-read the codebase; this is a routing decision, not a review. A minute of scanning is the budget.

Resolve the Booster library in this order, then use that root for DESIGN.md, packages, and `tools/booster.py`:
1. `$BOOSTER_HOME` if it contains `tools/booster.py` or `DESIGN.md`
2. `~/.claude/design` if it contains `tools/booster.py`
3. `~/.grok/design` if it contains `tools/booster.py`
4. the current checkout when `DESIGN.md` and `tools/booster.py` are present

## Step 2: Pick the form package

One of `<library-root>/packages/`: interface (tool/app UI with controls), editorial (idea-led presentation and landing pages), document (long-form reading), personal (identity and portfolio pages), gallery (imagery-first, interface recedes), showcase (a physical object that must be desired).
Pick by the page's job, not its industry.

## Step 3: Pick the sector package, if one applies

List `<library-root>/packages/sectors/` for the current list; match the brief's industry.
Many briefs have no sector: that is a normal outcome, not a failure. Never force a sector fit.
If the brief names an uncovered industry in DESIGN.md or `evidence/uncovered.json` (civic, education, food/hospitality, hospitality, religion, sports), set sector to none. Do not search. Do not force a nearby pack.

## Step 4: Choose refs

Name the form and sector first. Search is retrieval after that decision, never the decision itself.
Read the chosen packages' PACK.md range maps, then pick refs that SPAN a range relevant to the brief (two different poles beat two similar sites).
Cross-package borrowing is legitimate: a hospital dashboard might take one interface ref and one hospital ref.
Prefer offering FOUR pole-spanning candidate paths from the PACK maps or search index, with the instruction to choose two and name the choices. Treat those four as a shortlist, not four loaded references: open no more than 2-3 ref files total. A builder that picks its own range markers derives more and clones less.
Rotate refs between builds on the same subject; feeding the same trio every time re-converges the results.

If no sector applies, set sector to none and do not search the catalog. Pick poles from the form PACK.md range map.

If a sector applies and the search tool is installed, search only with both `--form` and `--sector` set:

```sh
python3 <library-root>/tools/booster.py search "<brief terms>" --form <form> --sector <sector> --limit 4
```

If search returns empty, read the `reason` field and open the chosen PACK.md range map. Never retry unfiltered. Never broaden the query to force a hit.
Treat ranking as retrieval evidence, not a design decision. Read the returned PACK files, then open only the 2-3 candidate refs most relevant to the brief before recommending the shortlist. Never open all four merely because search returned them. Reject a shortlist whose candidates share the same ground hue, display voice, anchor accent, or page anatomy.

## Step 5: Deliver the recommendation

For a routing-only request, use this exact shape:

```
## Booster recommendation

Form: packages/<name> - [one line: why this is the page's job]
Sector: packages/sectors/<name> - [one line] (or "none: [reason]")
Refs (offer these; builder chooses two and names them):
- <path> - [the pole it covers for this brief]
- <path> - [the pole it covers for this brief]
- <path> - [the pole it covers for this brief]
- <path> - [the pole it covers for this brief]

Reminders: DESIGN.md ban list + hard floors apply; commit one chosen direction;
all four gates are live (uniqueness including page outline, no cloning, category legibility,
believability: would this organization actually ship it?).
```

For an implementation request, do not stop and make the user operate the routing machinery. Choose and name two refs from the shortlist, load no more than 2-3 ref files total, continue through derive and implementation, and summarize the chosen form, sector, refs, and subject grounding with the completed build.

Ask the user to choose between refs or directions only when the available facts support materially different businesses or outcomes. Otherwise make the best grounded choice and preserve the one- or two-shot workflow.

If the scan leaves you genuinely unsure between two form packs or two sectors, say so in one line and recommend the `booster-questions` skill (`$booster-questions` in Codex) instead of guessing.

## Step 6: Derive when the build is proceeding

Default path: choose one direction, give it a compact ASCII wireframe, then build. Screenshot mobile and laptop, then stop unless the user asks for `booster-audit`.
Keep three-direction thinking in your head. Persist one chosen direction, not three full records, unless the user invoked `booster-questions` or the directions imply different businesses.

When three directions are required, read [references/direction-record.md](references/direction-record.md) and produce that record before substantial implementation. Otherwise record subject grounding, palette roles, type roles, layout intent, imagery plan, and one signature element for the chosen direction only.

Run both rejection checks before selecting:

1. Family collision: discard directions that share a ground hue, display voice, anchor accent, or page anatomy.
2. Counterfactual: discard any direction that a similar prompt for a different subject would also produce.

The chosen direction still passes DESIGN.md's uniqueness, no-cloning, category-legibility, and believability gates.
