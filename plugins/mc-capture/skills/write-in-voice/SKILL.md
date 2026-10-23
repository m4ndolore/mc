---
name: write-in-voice
description: Draft or rewrite capture writing (proposal sections, abstracts, white papers, capability statements, emails to a program office or TPOC, LinkedIn posts) in the user's own voice, and build that voice profile from their writing samples. Also sets the voice for the plugin's own briefings and summaries. Use when someone asks to write, rewrite, tighten or "make this sound like us", or wants a voice profile for their company.
---

# Write in voice

Two voices exist here. Never mix them up.

| Voice | Used for | Source |
|---|---|---|
| **The user's voice** | Anything the user will send or submit under their own name or their company's | Their voice profile (below) |
| **MC voice** | This plugin's own output: opportunity briefings, review summaries, digests of findings | [references/mc-voice.md](references/mc-voice.md) |

A proposal written in Merge Combinator's voice reads as if MC wrote it. Use the user's voice for their documents unless they explicitly ask for MC's.

## The user's voice profile

1. **Find it.** In Claude Code, look for `voice-profile.md` in the project root or `docs/`. In other clients, ask the user to paste it. If they have none, offer to build one.
2. **Build it** from 3–5 samples the user wrote themselves: past proposals, a website, emails, posts. Fill in [references/voice-profile-template.md](references/voice-profile-template.md). Quote the samples as evidence for each rule. Show the draft profile and ask what is wrong before you use it.
3. **Save it.** In Claude Code, write it to `voice-profile.md` with the user's permission. Elsewhere, give it back as a block they can save and paste next time.
4. **Learn from edits.** When the user rewrites your draft, name the pattern in one line ("you cut every adjective before a noun") and offer to add it to the profile's learned rules. Learned rules override the general profile.

## Drafting

1. **Compliance first.** For a proposal, the solicitation's structure, page limits, required headings and evaluation criteria come before voice. Mirror the criteria's language in headings so the evaluator can find each answer.
2. **Lead with the claim.** The first sentence of each section states the answer to the criterion.
3. **Ground every claim** in a test result, deployment, operator, program or number. If the user has not given you one, leave a bracketed placeholder such as `[test result: detection range]`. Never invent evidence.
4. **Then apply the voice:** sentence length, vocabulary, what they never say.
5. **Check** each sentence against the profile's never-list and against [references/mc-voice.md](references/mc-voice.md#plain-writing-rules), which applies in both voices.

## Rules

- Never fabricate a capability, result, customer, quote or past performance.
- Keep classification and export-control markings exactly as the user provides them. Do not add CUI, ITAR or proprietary content to anything the user says will be public.
- Write for the reader who scores or acts on it: an evaluator, a contracting officer, an operator. A founder's excitement does not persuade them. Evidence does.
