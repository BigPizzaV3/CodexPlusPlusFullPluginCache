---
name: create-project
description: Create an English practice project from selected materials with an approved plan, or discover an explicitly requested full ready-made project. Use for interview, presentation/meeting, or work/study projects; additions use save-material. General Try Contexta requests use standalone Speaking through pronunciation-practice.
---

# Create a Contexta project

Keep the reply focused on the learner’s result and next action. Do not show phrase, task, operation or request IDs, raw status fields, or tool/rendering diagnostics. Use titles and returned website links. Do not announce that a native widget was rendered or reopened; the widget already presents the result.

Native Contexta UI is required when available: render the server-held preview and creation receipt as specified in the shared workflow. A formatted chat plan or generated approval button does not replace the widget.

Read and apply [the shared workflow](../../references/workflow.md) before replying or calling the service. Selected materials use an approved server-held plan; an explicitly selected ready-made demo uses the existing template-copy boundary.

Pass `id_format="website"` to project preview, creation, status, starter copying and widget calls; retain the exact returned website IDs and links.

## Distinguish Speaking introduction from project demos

“Try Contexta,” “try the plugin,” “try a short answer” and a demo request without
personal material use the pronunciation-practice skill's standalone Speaking
introduction. Start `start_quick_exercise(mode="speaking", purpose="intro_speaking")`
on that explicit intent. Do not request a résumé, list project templates, preview
a source plan or create a project for this introduction. Opening or describing
the service remains read-only.

For an explicitly requested full ready-made project, discover the actual
`list_demo_practices` catalog with the chosen scenario and level. Only on a
clear project-copy request, copy the actually selected template with
`create_demo_practice` and its stable request identity. Render the owned receipt
using `show_practice_widget(entry="project", operation_id=..., id_format="website")`.
Full project sessions continue on the website and never become the introductory
Speaking exercise.

Existing legacy short demo projects remain owned projects. If the learner
explicitly asks to continue one by title or its website link, resolve that owned
project and open `show_practice_widget(entry="project", project_id=..., id_format="website")`.
Preserve its saved attempts and feedback. Never create a replacement project or
convert a saved project into an independent speech task to repair a link.

## Prepare a useful preview

Use the learner's stated goal and selected source. Ask only for essential missing information; do not reproduce the website onboarding questionnaire.

Choose the matching `preview_practice_plan` scenario:

- `interview_preparation`: resume in `source_text`, vacancy in `supporting_source_text`. For authorized files, identify the actual resume/job file IDs with `resume_file_id` and `job_description_file_id`; do not guess roles.
- `presentations_meetings`: the selected notes, slides or talking points, with the supplied audience and goal.
- `work_study_materials`: articles, documents, research or study notes the learner wants to understand, discuss or answer.

For a new Interview project, use `preserve_source_text=false` by default: adapt the resume and vacancy into useful interview practice while retaining the original sources. Use `preserve_source_text=true` only when the learner explicitly asks not to adapt or to preserve the original wording.

For Presentations & Meetings and Work & Study, use `preserve_source_text=true` by default. Use `preserve_source_text=false` only when the learner explicitly requests AI adaptation. State the chosen mode in the plan preview. Explicit wording preferences override these scenario defaults; do not change the mode silently after approval. Supply `target_level` only when the learner chooses it; otherwise let the service use its supported account default. Supply `practice_intent` only when it follows from the learner's stated goal (`understand_remember`, `discuss_present`, or `write_answer`).

Send only the selected text and/or actual host-authorized `files`, plus a stable idempotency key and the supplied goal/title. Never synthesize file URLs or replace a file with a chat summary presented as its original. The service decides source inventory, coverage, sizing and allowances; do not approximate the website wizard with independent formulas.

Explain briefly that the selected material will be sent for a plan preview. An explicit request to create practice from that material provides transfer intent; unrelated attached content does not.

## Import a prepared structure exactly

When the learner asks to import ready-made packs and sessions exactly, call
`preview_practice_plan` with `plan_mode="exact"`, the exact `project_title_hint`,
`preserve_source_text=true`, and `packs`. Each pack has `title` and `sessions`;
each session has `title` and its complete `source_text`. Preserve all supplied
strings and array order. Do not turn this structure into a combined article,
summary, SESSION markers, or an Interview resume/vacancy pair. The scenario
can still describe the learner's purpose; exact import bypasses AI source
analysis, project naming, replanning, chunk allocation and body rewriting.

This mode creates a new project only. Do not combine it with `source_text`,
`supporting_source_text`, files, a source title, resume/job file selectors,
`project_id` or `pack_id`. Use the same preview and approval workflow below.
Never downgrade an unavailable exact mode to automatic planning.

Exact import accepts up to five packs with 1–15 sessions each. Project titles
are at most 50 characters, pack titles 64, session titles 255 and each complete
session text 12,000. Nonblank strings retain whitespace and punctuation.
Account project, storage and session allowances also apply. Pack titles must
be distinct and cannot already exist anywhere in the learner's account;
project titles cannot already exist either. These database name constraints
return an error instead of a suffix. Repeated session titles/texts are allowed.
If any limit or conflict is reported, explain it and let the learner choose
what to change. Never truncate, rename, regroup, split or omit content to make
it fit without the learner explicitly requesting that change and approving
a fresh preview. Preserve returned exact titles when presenting the plan.

## Approval and creation

Poll `get_operation_status` at the returned interval within a bounded wait. At `plan_ready`, show the actual project title, level, source count, preservation/adaptation, ordered plan and any allowance consequences the response supplies. The preview is not an assessment or a created project.

When `show_practice_widget` is available, explicitly render that server-held preview with `entry="project"` and its `operation_id`. The widget displays the authoritative plan and an approval action; opening or polling it does not approve creation. For an explicitly requested new project interface before a preview exists, open `show_practice_widget(entry="project")` for a short instruction to supply the goal and selected material in chat. The widget does not contain a second project editor. Keep the textual preview usable when a host does not render UI.

Ask for approval of that returned plan. On clear approval call `create_practice_from_plan` with its `operation_id`; do not edit or resend the full plan. Reuse the same ID for uncertain retries. A material or goal change needs a fresh preview; an expired preview needs a new one too.

Wait for the actual `ready` response before promising usable practice and link to its exact owner-only URL. Pending or failed preparation remains pending or failed. Keep the existing operation for later continuation rather than making duplicate projects.

After approval, render the receipt through `show_practice_widget(entry="project", operation_id=...)` when available. It reads the same operation and owned project; the first session is usable only at `ready`. If failed or expired preparation already has a project, use its returned website link before proposing another project.

For adding material to an existing project, use the Add to Project skill (`save-material`) and its append-only approved planning flow. If the learner just says “save this article” without a destination, offer the choice of a new project or an existing project; do not silently create an Inbox. This skill creates a new project only; omit `project_id` and `pack_id` here. For explicit ready-made website starter requests, discover with `list_demo_practices` and copy the actually selected template using `create_demo_practice`; never guess a template or substitute a different level. Full listening, reading, writing and speaking sessions remain on the website.
