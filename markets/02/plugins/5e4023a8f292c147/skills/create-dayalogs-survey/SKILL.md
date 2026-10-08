---
name: create-dayalogs-survey
description: Create, revise, validate, and preview Dayalogs surveys through the Dayalogs MCP. Use when a user wants to turn requirements, questions, a questionnaire, or a research brief into a new survey or a deliberate new survey version. Covers targeted authoring help, validation, explicit create/update intent, optimistic concurrency, and preview-first review.
---

# Create A Dayalogs Survey

Build a valid survey without guessing the schema or silently changing an existing survey.

## Workflow

1. Establish the survey's purpose, audience, source language, question content, required logic, and intended delivery channel. Ask only for information that materially changes the design.
2. Call `survey_authoring_help` with an empty path only when topic discovery is needed. Then request the smallest relevant paths for the question types, logic, assessment, embed, or operational behavior being used.
3. Draft the survey from those current server-side contracts. Do not rely on remembered field names when targeted help is available.
4. Call `validate_survey`. Resolve every schema and semantic error before importing.
5. Determine import intent explicitly:
   - New survey: use `import_survey` with `mode=create`.
   - Existing survey revision: first read the survey, then use `mode=update` with the stable `survey_id` and observed current `version_id` as `expected_version_id`.
   - Never use a slug collision as an implicit update instruction.
6. If the server returns `version_conflict`, stop. Tell the user who changed the survey, when it changed, and the bounded change summary returned by Dayalogs. Reconcile deliberately and obtain a fresh version before retrying. Never auto-retry by merely replacing `expected_version_id`.
7. Use `get_preview_url` and give the user the preview, not a respondent collection link. Summarize important design choices and any assumptions that still need review.
8. Revise through focused patch/append tools when appropriate, preserving the same expected-version guard. Revalidate after material structural changes.

## Safety

- Keep the survey in draft until the user explicitly asks to start collection.
- Do not call `go_live_survey` without explicit publication confirmation.
- Do not create a real share link unless the user explicitly asks for one and confirms it when required.
- Treat destructive operations, response deletion, review decisions, sends, and irreversible state changes as separate user-approved work.
- Do not expose grading answer keys or hidden respondent logic in respondent-facing copy.

## Quality Bar

- Prefer the simplest question type that preserves the user's analytical intent.
- Keep mobile completion practical: concise labels, bounded option counts, and no unnecessary introductory steps.
- Ensure conditions refer to values available before they are evaluated.
- Keep randomized blocks free of internal dependencies and repeats unless current authoring help explicitly supports them.
- For embedded surveys, consult the embedded-survey authoring guidance and design for one focused interaction per step.

## Completion

Return the survey title, stable survey id, current version id, draft status, validation result, and preview URL. Mention unresolved assumptions plainly. Never imply that a preview is live collection.
