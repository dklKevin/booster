---
name: booster-audit
description: Audit an implemented UI, page, site, or visual artifact against Booster's hard floors, stable ban IDs, chosen direction, and four outcome gates. Use after visual implementation, when the user says the result feels generic or AI-made, before calling a design complete, or when asked to diagnose and fix visual quality, responsive, accessibility, state, or reference-cloning problems.
---

# Booster audit

Review evidence in two separate lanes: operational hard floors and aesthetic mode detection. Never let a subjective taste finding hide an objective accessibility or responsive failure.

## 1. Reconstruct intent

Read the artifact, current implementation, project design tokens and components, Booster DESIGN.md, the selected form and sector packs, two or three selected refs, and the direction record when present.
Treat notes and build summaries as claims. Verify the rendered result independently.

If the selected direction or refs are missing, say so and mark the affected gates UNVERIFIED. Do not invent them after seeing the result, and do not PASS while a mandatory gate is unverified.
Compare the implementation with the project's shared tokens and components. Treat an unexplained one-page fork as a finding. If a Booster ban conflicts with an established shared system, report the conflict and return to derive instead of silently replacing or forking the system.

## 2. Capture rendered evidence

Bind the evidence to the reviewed build with a revision, artifact hash, or timestamped URL. Run the real artifact and capture at approximately 375px mobile, 768px, 1440px laptop, and 1920px wide desktop, plus just below and above every CSS or container breakpoint between them.
Exercise every applicable empty, sparse, dense, loading, success, and error state.
Inventory and keyboard-test every interactive control and flow. Inspect focus visibility and order, test reduced motion at runtime, and check horizontal overflow at 100%, 200%, and 400% browser zoom. Any untested control or flow is UNVERIFIED.
Measure contrast in every shipped theme, computed touch-target size, mobile input text size, and viewport zoom configuration. Inventory customer, metric, testimonial, certification, availability, and behavior claims, then tie each one to an authoritative project source or mark it unverified.
For claim provenance, the truth source must be independent of the audited presentation: user-supplied or official organizational material, authoritative backend records, or verified runtime data. Display copy or code introduced by the audited build cannot validate itself.

If no rendered artifact or screenshot is available, the aesthetic lane is provisional and cannot pass. Source inspection can still prove some hard-floor failures.
Source can prove a failure when the failing value or behavior is unavoidable. The mere presence of a focus rule, media query, token, or component cannot prove a runtime pass.

## 3. Classify findings

Use these severities:

- P0: blocks use, hides content, invents proof, or violates a non-negotiable hard floor.
- P1: recognizable mode, broken responsive behavior, missing applicable state, or failed outcome gate.
- P2: localized polish or coherence problem that does not invalidate the direction.

Use high confidence only when pixels, interaction, or source directly prove the finding. Use medium when evidence is partial. Omit low-confidence speculation.

Map mode findings to stable DESIGN.md IDs such as B004. A tell without a ban ID may still fail an artifact-local uniqueness or counterfactual gate when the rendered evidence proves it, but it does not become a global ban. It stays an observation candidate and is never promoted automatically.

Before choosing a verdict, make a coverage matrix. Mark every DESIGN.md hard floor, each of the four gates, design-system conformance, claim provenance, each required viewport, each shipped theme, and every applicable state as PASS, FAIL, UNVERIFIED, or justified N/A. A mandatory UNVERIFIED blocks PASS.

## 4. Report the verdict

Return:

```text
Verdict: PASS | REVISE | FAIL | INCOMPLETE

Evidence reviewed:
- <build identity, viewports, breakpoints, zoom levels, themes, states, interaction checks, source>

Coverage:
| Check | Status | Evidence or N/A rationale |

Findings:
| Severity | Confidence | Lane | Location | Rule or gate | Observable evidence | Bounded correction |

Surviving checks:
- <important hard floors and gates that passed>

Residual uncertainty:
- <anything the available evidence could not prove>
```

PASS requires no P0 or P1 findings, rendered evidence for the aesthetic lane, and no mandatory UNVERIFIED checks. REVISE means the evidence is complete and one or more bounded corrections are required. FAIL means invented proof, direct reference cloning, or a fundamental direction failure requires a new direction rather than a bounded correction. INCOMPLETE means the artifact, access, intent record, or mandatory evidence is unavailable. Do not turn the report into a numeric taste score.

Audits are report-only unless the user separately authorizes implementation or evidence recording. Record an observation only after resolving the DESIGN.md ledger owner and obtaining an explicit rejection of one named pattern. Run `python3 <resolved-Booster-root>/tools/booster.py observe ...` with the exact required subject, model, artifact, date, note, and optional screenshot fields. Preserve the user's exact wording when available, never invent missing provenance, and never promote a candidate.

## 5. Correct without converging

When the user asked for fixes, correct hard-floor failures directly. For aesthetic P1 findings, return to the subject grounding and the three-direction derive record rather than choosing a canned style.
Preserve valid work, make the smallest coherent correction, recapture the affected viewports and states, and audit again.
Stop only when no P0 or P1 findings remain or a concrete blocker is proven.
