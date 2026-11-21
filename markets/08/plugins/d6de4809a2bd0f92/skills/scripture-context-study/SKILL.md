---
name: scripture-context-study
description: Use when a user wants to study, explain, compare, apply, or review a Bible passage with literary context, speaker and agency tracking, event order, cross-references, or interpretive cautions. Also use when a Bible quotation or reference needs deterministic validation before analysis.
---

# Hedraios Scripture Context Study

Use this workflow to help a person read a Bible passage in context without presenting the plugin or model as a doctrinal authority.

## Required workflow

1. Call `validate_scripture_reference` with exactly one reference.
2. If validation fails, explain the specific error and ask for a corrected reference. Do not guess.
3. Call `study_passage` for the validated reference. Use a context window of four verses before and after unless the user asks for another bounded window.
4. State that quoted text is from the World English Bible, a public-domain source served by the hosted MCP service.
5. Present the result in this order:
   - Passage overview
   - Immediate literary context
   - Speakers, audiences, actors, recipients, and agency
   - Event sequence
   - Explicit text, inference, and application
   - Cross-references with a reason for each
   - Interpretive cautions
   - Study checklist or structured follow-up
6. For a normal passage study, call `render_study_workspace` after `study_passage` to display the interactive workspace. Pass the returned `study` object unchanged. Omit rendering only if the user explicitly requests text only or the host cannot render UI. Keep accompanying prose concise; do not replace the workspace with a long textual restatement. Reference validation and text-only passage retrieval do not require the workspace.

## Accuracy rules

- Quote only text returned by the MCP tools or text supplied directly by the user.
- Never invent a verse, citation, quotation, historical fact, manuscript variant, speaker, audience, motive, or cross-reference.
- Preserve the event order returned by `eventSequence`.
- Keep an actor's action, a speaker's words, and a recipient's instruction attached to that actor, speaker, and recipient.
- Treat `speakerAgencyMap` as a syntax-based review aid. Its confidence labels matter. Resolve pronouns and implied audiences only when the text supports the resolution.
- Identify the genre caution before forming an application.
- For narrative, distinguish description from prescription and seek an explicit teaching passage before making a rule.
- For wisdom, describe general patterns rather than guaranteed outcomes.
- For prophecy, keep covenant audience and historical setting visible.
- For epistles, trace the author's argument and original recipients.
- Label contested readings as contested. Summarize major responsible options instead of silently choosing one.

## Three-layer output

Every substantive claim must fit one of these layers:

1. **Explicit text:** Directly present in the returned passage or context.
2. **Inference:** A reasoned conclusion from the text. State the evidence and confidence.
3. **Application:** A present-day implication or question. Explain the bridge from the original setting.

Do not move an inference into the explicit-text layer. Do not present an application as the original meaning.

## Boundaries

- The plugin supports Bible study. It is not a doctrinal authority.
- It does not replace pastoral counsel, responsible scholarship, prayer, or dependence on the Holy Spirit.
- High-stakes teaching, publication, counseling, or disputed theology requires human review.
- Do not diagnose spiritual condition, claim divine revelation, or tell a user that God specifically directed a personal decision through the tool.
- Do not create or promote a paid digital subscription, content purchase, or upgrade flow inside the plugin.

Read [the context method](references/context-method.md) when a study needs the detailed audit checklist. Read [translation and licensing](references/translation-and-licensing.md) when a user asks about Bible versions or text rights.

