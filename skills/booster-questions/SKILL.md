---
name: booster-questions
description: Interview-first design-pack routing for Kevin's design library. Use whenever the user invokes /booster-questions, is unsure what design direction a project should take, wants to be interviewed before getting a pack recommendation, or when /booster's repo scan would be ambiguous (new empty project, multi-purpose repo, no clear brief). Asks a short interview, then recommends form/sector packs and refs.
---

# Booster questions: interview, then route

Same destination as `/booster` (a pack + refs recommendation), reached through a short interview instead of a repo scan.
Use this when the context is thin or ambiguous; the interview replaces Step 1.

## The interview

Ask ONE question at a time and wait for the answer before the next: Kevin works strictly this way.
Use the AskUserQuestion tool when available, with concrete options plus room for free text.
Ask at most 5; stop early the moment routing is unambiguous.

1. Subject: what is this page/site actually about, in one sentence?
2. Job: what should a visitor do or feel: operate a tool, be persuaded, read deeply, meet a person, browse images, or want an object? (This maps directly to the form packs.)
3. Audience/industry: who is this for, and does it live in an industry? (Maps to `~/.claude/design/packages/sectors/`; "no sector" is a fine answer.)
4. Pole: should it sit quiet-and-precise or loud-and-committed? Warm or technical? (Guides which refs span the right range.)
5. Anchors: any sites they already love for this, or past artifacts of ours that landed? (A named site may join the refs; a new one is also a candidate for the library.)

Do not ask what the interview already answered, and never ask all five as a block.

## Then route

Read `~/.claude/skills/booster/SKILL.md` and follow it from Step 2, using the interview answers as the scanned context.
Deliver the identical "Booster recommendation" block, offer to load the files and start the derive step, and if question 5 surfaced a site not yet in the library, note it as a candidate for Kevin to bless into the matching refs/ folder.
