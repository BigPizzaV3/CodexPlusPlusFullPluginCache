---
name: diagnose-pe-readiness
description: Diagnose a student's Civil, Mechanical, or Electrical PE study readiness using reviewed PE Prep Pro practice sets. Use when a student asks what to study, wants a baseline drill, or needs weak topics prioritized without storing answer history.
---

# Diagnose PE Readiness

Use the PE Prep Pro Agent Hub to run a short, transparent diagnostic. This is study guidance, not a prediction of passing or a substitute for the current NCEES exam specification.

## Workflow

1. Ask for the target discipline if it is not clear.
2. Call `list_disciplines` and use only returned topic names and concept IDs.
3. Choose up to three representative topics. Run separate `create_practice_set` calls with one or two items per topic.
4. Present each returned question exactly as supplied. Do not solve, hint at, or reveal an answer before the student commits.
5. Call `grade_practice_set` only with the signed token and the student's explicit answers.
6. Summarize strengths and gaps from this session only. Do not imply persistent tracking.
7. Recommend at most three next topics, tying each recommendation to observed evidence and the returned explanation or reference starting points.

## Guardrails

- Never alter question wording, options, citations, reviewer, or revision metadata.
- Never claim a readiness percentage from fewer than 10 answered items.
- Label small samples as directional.
- If a tool reports no matching content, call `list_disciplines`; do not invent a topic or item.
- If content appears wrong or ambiguous, use `report_content_issue` with the student's permission and omit personal information.
