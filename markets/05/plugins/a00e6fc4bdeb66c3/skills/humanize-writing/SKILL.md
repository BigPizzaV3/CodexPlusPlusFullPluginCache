---
name: humanize-writing
description: Rewrite, edit, or polish text so it sounds natural, specific, credible, varied, and appropriate to a real writer and audience while preserving meaning and factual integrity. Use when a user asks to humanize AI text, remove AI-sounding language, make writing less robotic or generic, match a personal voice, improve natural German or English, rewrite marketing copy, emails, articles, posts, scripts, applications, reports, or messages, or reduce formulaic patterns without making false claims about bypassing AI detectors.
---

# Humanize Writing

Make the text sound like someone had a reason to write it. Do not manufacture typos, fake personal experiences, invented opinions, false anecdotes, or random imperfections as camouflage.

## Workflow

1. Identify purpose, reader, relationship, channel, desired effect, language, degree of formality, and facts that must remain unchanged.
2. If reference writing is supplied, read `references/voice-matching.md`. Derive only observable style features; do not imitate protected living authors on request beyond broad characteristics.
3. Diagnose the current text using `$detect-ai-writing-patterns` when the problems are unclear or the user requests an explanation.
4. Choose an editing level:
   - `light`: retain structure and wording where possible;
   - `standard`: rebuild awkward sentences and remove generic material;
   - `deep`: rewrite structure, rhythm, emphasis, and voice while preserving the message.
5. Apply `references/humanization-method.md` selectively. Prefer specific meaning, natural compression, varied cadence, direct verbs, contextual vocabulary, and socially appropriate tone.
6. Preserve facts, quotations, citations, legal qualifiers, product claims, names, dates, numbers, calls to action, and required keywords unless the user authorizes changes.
7. Never invent evidence, customers, experiences, emotions, credentials, or certainty. Mark any missing specificity that requires user input.
8. Read the result as a whole. Remove new repetition, forced casualness, excessive slang, choppy variation, and inconsistent voice.

## Default output

Return the finished text first. Add a brief change note only when requested or when a material ambiguity, factual risk, or missing personal detail remains.

When useful, provide at most three complete versions labeled by tone, with the best default first.

## Boundaries

- Do not promise that a text is human-authored or undetectable.
- Do not optimize primarily to evade academic, employment, publishing, or platform integrity checks.
- Help the user express their own ideas clearly; preserve attribution and disclosure requirements.
- For high-stakes medical, legal, financial, scientific, or compliance text, prioritize accuracy and qualified review over conversational style.

