---
name: faceless-channel-script-qa
description: 'Quality-check a faceless YouTube channel or AI-assisted voiceover script before it goes to text-to-speech or a narrator, using Prepublish to audit attention risk and rewrites, check reused or templated content signals that YouTube''s inauthentic-content rules target, and prepare the draft for voiceover. Use when the user runs a faceless channel, YouTube automation channel, documentary or history narration channel, top-10 or list channel, story channel, or uses ChatGPT, Claude or another AI to draft scripts, and asks "is my AI script good enough", "will YouTube flag this as reused or AI content", "make this sound less AI generated", "check my voiceover script", or "QA my faceless video script". Not for scripts the user wants written from nothing.'
---

# Faceless and AI-assisted script QA

Faceless channels live or die on the narration script: there is no face or personality on camera to carry a weak passage. AI-assisted drafts add a second risk: text that reads templated or interchangeable, which YouTube's inauthentic-content expectations target.

Read `references/tools.md`, `references/report-fields.md` and `references/claims-and-limits.md`. Use `assets/voiceover-prep-checklist.md` at the end.

## Inputs

- The narration script verbatim (as it will be read), and the planned title.
- The channel format if the user says it (history documentary, finance explainer, story, list, true crime, science).
- Email for the free audit if the user has no Prepublish account (explain first, never invent).

## Workflow

1. **Reused-content signals first**: `check_authenticity` with title and script. Present `risk_level`, `score` (higher means more risk), the signals in plain words with quotes, and the remediation items.
2. **Attention risk**: `audit_script` with title, script, and `category` when known. Present the top flagged passages and rewrites.
3. **Combine into one fix list**, ordered: high-severity authenticity signals, CRITICAL audit items, HIGH audit items, medium signals. Deduplicate where both checks flag the same passage.
4. **Add the creator's own contribution.** The most reliable fix for templated text is material only this channel has. Ask the user for one or two of: their own take or verdict on the topic, a specific example or source they found, a comparison they would make, a correction of a common myth. Work those into the flagged passages. Never invent facts, sources, quotes or personal experiences for them; use clearly marked placeholders like `[your example]` when the user has not supplied one.
5. **Voiceover prep**: once fixes are applied, go through `assets/voiceover-prep-checklist.md` (pronunciation of names and numbers, sentence length for breath, where emphasis falls). Offer `script_runtime` to confirm length.
6. Offer one re-check of the revised script (authenticity, audit, or both), mentioning the daily free audit limit.

## Rules

- Never suggest ways to disguise reused or scraped material, spin someone else's script, or evade YouTube's systems. The fix is original contribution and clear sourcing.
- Do not claim the result predicts monetisation approval, YPP acceptance, views or retention. The authenticity check reports text-level signals only and does not speak for YouTube.
- Keep the channel's established voice unless the user asks for a new one.
- Text the user will read aloud should be written for the ear: short sentences, numbers written the way they should be spoken, no parenthetical asides that do not work in audio.
