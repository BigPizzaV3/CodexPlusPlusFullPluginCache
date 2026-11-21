---
name: save-material
description: Add selected text or authorized files to an existing Contexta project, using an approved plan that generates sessions only for the new material. Use for add/import-to-project requests; creating a new project uses create-project.
---

# Add to a Contexta project

Keep the reply focused on the learner’s result and next action. Do not show phrase, task, operation or request IDs, raw status fields, or tool/rendering diagnostics. Use titles and returned website links. Do not announce that a native widget was rendered or reopened; the widget already presents the result.

Native Contexta UI is required when available: render the append-only preview and addition receipt as specified in the shared workflow. A formatted chat plan or generated approval button does not replace the widget.

Use the same material planning flow as the website. Read and apply [the shared workflow](../../references/workflow.md) before replying or calling the service. The skill's technical name remains `save-material` for compatibility; its user-facing action is **Add to Project**.

## Select the source and destination

An explicit request to add selected material authorizes its transfer for planning. Send only that selected text or authorized attachments, never the whole conversation. Preserve pasted whitespace, punctuation, negation and line endings; do not summarize or translate it. For files use real host-provided `files` objects with `download_url` and `file_id`, optionally `mime_type` and `file_name`. Never invent URLs or substitute a summary for an original file. If access is unavailable, offer exact pasted text or website import.

Discover owned projects with `list_practice_projects`; use bounded pagination when needed. Match a named project exactly, resolving genuine ambiguity. If no destination was named, ask the learner to choose an existing project or create a new one with `create-project`. Do not silently create an Inbox or an unrelated project.

Pass `id_format="website"` to project/material discovery, preview, status, creation and widget calls. Keep returned encoded project and pack references unchanged.

Default to new packs within the selected project. Only when an existing pack is explicitly selected, call `list_material_destinations(project_id=...)` and use its actual website-encoded `pack_id`. The pack must belong to this project and be available. Do not guess IDs or create a fallback after a destination error.

## Preview and approve only the addition

Call `preview_practice_plan` with the actual `project_id`, optional selected `pack_id`, exact new `source_text` and/or authorized `files`, a stable `idempotency_key`, and any supplied source title. Do not send old project sources or sessions. The service inherits the existing project's scenario, material level, goal, intensity and text adaptation settings; do not override them in chat.

Poll the returned `operation_id` at the supplied interval within a bounded wait. At `plan_ready`, require `plan.update_mode="append_only"` and the chosen destination before offering approval. Show the actual destination, inherited wording mode, new source count, added session/pack counts and ordered new plan. Existing materials, sessions, answers, audio and results stay unchanged, including unfinished sessions. A selected existing pack receives the new sessions at its end.

Render `show_practice_widget(entry="project", operation_id=...)` when supported. Opening it does not approve the plan. On clear approval, call `create_practice_from_plan(operation_id=...)` with that frozen handle only. Never resend an edited plan or fall back to legacy project-wide replanning. Reuse the operation after uncertain responses; changed material/destination needs a fresh preview.

Report the actual pending/failed/ready result and its exact owned website link. Only `ready` means the first new session is usable. File originals remain private; disclose returned extraction limitations. Do not claim perfect PDF layout, completed assessment, a new trial or new project creation. Legacy raw capture and existing Inbox data remain accessible through their old contracts, but they are not the primary material-addition workflow.
