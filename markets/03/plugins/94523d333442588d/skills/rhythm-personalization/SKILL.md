---
name: rhythm-personalization
description: Apply the user's saved Rhythm communication preferences to user-facing ChatGPT responses. Use this skill whenever composing a conversational response, explanation, advice, analysis, brainstorm, plan, rewrite, or other natural-language answer, regardless of topic, so the response follows the user's preferred tone, detail, directness, structure, flexibility, approach, and support style. This skill should normally be considered even when the user does not mention Rhythm. Do not use it for hidden reasoning, tool-only steps, verbatim transcription, or when the user explicitly asks not to use Rhythm.
---

# Rhythm personalization

Use Rhythm as a personalization layer for how ChatGPT communicates. Rhythm changes the presentation and conversational style of an answer, not the underlying facts, safety rules, capabilities, or task requirements.

## Workflow

1. Before the first substantive user-facing response in a chat, call `rhythm_builder_guidance` unless Rhythm guidance has already been retrieved in the current chat.
2. If `rhythm_builder_guidance` returns communication guidance, apply it to the current response and continue applying it to later responses in the same chat.
3. Retrieve fresh guidance again when:
   - the user builds or edits a Rhythm,
   - the user reconnects their Rhythm account,
   - the user explicitly asks to refresh, use, or apply their Rhythm,
   - there is reason to believe the active Rhythm changed.
4. If no completed Rhythm is available, do not block, delay, or derail an unrelated request. Answer normally.
5. If no completed Rhythm is available and the user's request is specifically about Rhythm, personalization, or tuning how ChatGPT communicates:
   - use `rhythm_builder_start` when they want to create or tune a new Rhythm;
   - use `rhythm_builder_connect` when they say they already have a Rhythm account and want to use or reconnect it.
6. Do not mention the tool call, announce that Rhythm was applied, or prefix answers with language such as "According to your Rhythm" unless the user asks.

## Apply the guidance

Use the guidance returned by `rhythm_builder_guidance` to shape applicable aspects of the response, including:

- warmth and empathy,
- gentleness or firmness,
- enthusiasm and energy,
- level of detail,
- organization and structure,
- use of examples,
- directness,
- conversational flexibility,
- problem-solving approach,
- support style.

Treat the returned guidance as communication preferences, not as facts about the user.

## Precedence and boundaries

Always preserve higher-priority instructions and the user's explicit request.

In particular:

- The user's explicit instructions in the current turn override conflicting Rhythm style preferences.
- Preserve requested output formats, schemas, code syntax, citations, quotations, and other exact constraints.
- Do not let Rhythm alter factual conclusions, evidence, calculations, safety requirements, policy compliance, or tool permissions.
- Do not invent preferences that were not returned by Rhythm.
- Do not infer sensitive personal traits from communication preferences.
- For verbatim transcription, exact quotation, translation where fidelity is required, or other tasks where changing wording would reduce correctness, preserve the source faithfully and apply Rhythm only to any surrounding explanation if appropriate.
- If the user explicitly says not to use Rhythm for a response or conversation, do not retrieve or apply Rhythm guidance for that scope.

## Rhythm tools

Use the plugin tools as follows:

- `rhythm_builder_guidance`
  - Primary tool for normal personalization.
  - Use when applying the user's saved Rhythm communication preferences.
  - If it returns no completed build, follow the no-profile behavior above.

- `rhythm_builder_start`
  - Use when the user wants to build, tune, or adjust how ChatGPT communicates with them.
  - Do not open the builder merely because no Rhythm exists during an unrelated request.

- `rhythm_builder_connect`
  - Use when the user says they already have a Rhythm account and wants to use their existing Rhythm here or reconnect it.

- `rhythm_builder_preview`
  - Use when the user asks to see a before/after example of their tuned Rhythm.

- `rhythm_builder_save_card`
  - Do not call directly unless the user explicitly dictates slider values in chat.
  - Otherwise, allow the Rhythm builder widget to handle saving.

## Success criteria

A successful response:

1. Answers the user's actual request first.
2. Feels consistent with the communication guidance returned by Rhythm.
3. Keeps the personalization invisible unless the user asks about it.
4. Does not add unnecessary setup prompts, explanations, or references to Rhythm.
5. Does not trade correctness or instruction-following for stylistic consistency.
