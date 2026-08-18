---
name: booster-questions
description: Interview-first design-pack routing for the Booster design library. Use whenever the user invokes booster-questions, is unsure what a site should communicate, wants an interview before a design direction, or when the brief itself remains ambiguous after Booster's workspace and asset intake. Asks a short interview, then recommends form and sector packs and refs.
---

# Booster questions: interview, then route

Same destination as the `booster` skill (a pack + refs recommendation), reached through a short interview instead of a repo scan.
Use this when the brief is thin or ambiguous after the sibling `booster` skill has established the workspace and scanned available business materials. An empty or new project alone does not require a full interview.

Before the interview, follow Booster Step 0. Resolve whether the user has an existing folder or wants a new one, accept a blank folder name, scan available business files and images, and offer image generation only when the active agent actually provides the `imagegen` capability.

## The interview

Ask ONE question at a time and wait for the answer before the next.
Use the active agent's structured question tool when available, with concrete options plus room for free text.
Ask at most 5; stop early the moment routing is unambiguous. For a normal website build, aim for one material question before the first shot.

1. Subject: what is this page/site actually about, in one sentence?
2. Job: what should a visitor do or feel: operate a tool, be persuaded, read deeply, meet a person, browse images, or want an object? (This maps directly to the form packs.)
3. Audience/industry: who is this for, and does it live in an industry? (Maps to the installed `packages/sectors/`; "no sector" is a fine answer.)
4. Pole: should it sit quiet-and-precise or loud-and-committed? Warm or technical? (Guides which refs span the right range.)
5. Anchors: any sites they already love for this, or past artifacts of ours that landed? (A named site may join the refs; a new one is also a candidate for the library.)

Do not ask what the interview already answered, and never ask all five as a block.

## Then route

Read the sibling `booster/SKILL.md` from the active skill installation and follow it from Step 2, using the interview answers as the scanned context. If sibling resolution is unavailable, try `~/.agents/skills/booster/SKILL.md` for Codex, then `~/.claude/skills/booster/SKILL.md` for Claude, then `~/.grok/skills/booster/SKILL.md` for Grok.
For routing-only work, deliver the identical "Booster recommendation" block. When the user asked for a website, continue into the build instead of stopping for approval of internal refs or directions unless the answer would materially change the business outcome. If question 5 surfaced a site not yet in the library, note it as a candidate for the library owner to approve into the matching refs/ folder.
