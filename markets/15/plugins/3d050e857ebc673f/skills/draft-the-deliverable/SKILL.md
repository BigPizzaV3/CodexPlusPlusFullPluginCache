---
name: draft-the-deliverable
description: Draft the deliverable. Use when the user wants a client deliverable (engagement brief, meeting brief, steering committee or status pack, proposal or other templated document) drafted from their Delegent work in their firm's format.
---

# Draft the deliverable

Delegent provides the firm's instructions and the evidence. You build the document with your own tools. Delegent never sends template files.

## 1. Get the instructions

`delegent_get_deliverable_instructions` with the deliverable type, template name if given, and workstream. `delegent_list_templates` shows what exists.

- If no template matched, ask which to use or whether to go without one.
- A template file marked not usable gives a `reason` (still analysing, failed, unsupported). Say so and offer to proceed without it.
- For the file itself, follow `get-template`: `delegent_get_template` with the `template_ref` returns the full instructions and style profile.

## 2. Collect evidence

- `delegent_get_context_for_task` and `delegent_get_source`. A file name or summary alone is not evidence for a number. `delegent_list_files` finds source documents.
- If a decision-critical input is missing or contradictory, show a table (Missing input | Why it matters | Owner to confirm | Required by) and ask before drafting.
- `delegent_search_firm_knowledge` can add anonymised firm-wide patterns when the firm has it enabled. Label them as patterns, not project facts.

## 3. Draft, validate, present

- Answer first, quantify the implication, then the next action. Separate fact, assumption and recommendation.
- Check arithmetic, units, dates, owners and claim-to-source support. Report checks as Passed / Not checked / Needs confirmation.
- Include a source register.
- Present as a draft. Never say it was approved.

## 4. Keep it in Delegent, if asked

- On the user's request, `delegent_save_file` saves the finished file to the workstream with a summary and its text.
- `delegent_capture_work` records follow-up actions or decisions, citing sources.
