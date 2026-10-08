---
name: session-chronicle
description: Reconstruct a conference, symposium, seminar, workshop, panel, forum, roundtable, presentation, or Q&A transcript as a faithful professional narrative. Use by default when a transcript is supplied without another requested output, and for CHRONICLE, OUTLINE, or HELP commands.
---

# Session Chronicle

Turn the supplied transcript into a readable, source-grounded record. Do not ask intake questions unless the source is genuinely unusable; make cautious editorial decisions and state material uncertainty.

## Routing

- A transcript with no further instruction means `CHRONICLE`.
- `OUTLINE` produces a structured plan rather than full prose.
- `HELP` briefly lists supported outcomes and routes the user's next request. Preserve slash-prefixed or plain command aliases, case-insensitively.
- Route EXPAND, SUMMARISE/SUMMARIZE, PUBLISH, and HIGHLIGHTS to `session-publish`; multi-session comparison to `session-compare`; INFOGRAPHIC and other visual requests to `session-visuals`.

## Workflow

1. Assess transcript quality and boundaries. Read [transcript quality guidance](../../references/transcript-quality-guidance.md) when the source is noisy, incomplete, or poorly labeled.
2. Detect the session format: presentation, interview, panel, roundtable, moderated Q&A, workshop, or mixed. Identify speakers only to the degree supported by the source.
3. Map chronology, themes, transitions, questions, responses, agreements, disagreements, examples, and conclusions.
4. Draft in professional prose using the fitting pattern in [narrative patterns](../../references/narrative-patterns.md). Prefer thematic organization within the actual progression of the session.
5. Apply [attribution guidance](../../references/attribution-guidance.md), then check every substantive claim against the source.

## Fidelity rules

- Preserve meaning, nuance, speaker intent, material distinctions, and the sequence needed to understand the discussion.
- Improve grammar and flow without silently strengthening claims or resolving ambiguity.
- Never invent names, roles, motives, quotations, consensus, conclusions, context, or facts.
- Paraphrase by default. Use direct quotations only when wording is clear and worth preserving.
- Mark uncertainty locally and proportionately. Do not let minor transcript noise dominate the narrative.
- Add external context only when the user requests it or it is necessary to identify a clearly referenced item; label it separately and cite its source.

For `OUTLINE`, follow the relevant session shape, listing proposed sections, principal points, supported speaker attribution, and unresolved ambiguities. Do not draft the full chronicle.
