---
name: practice-progress
description: Summarize measured Contexta patterns and owned project progress, or return the next full website session. Use for saved evidence and continuation, not grading chat answers, inventing learning trends, or administering account limits.
---

# Practice progress

Keep the reply focused on the learner’s result and next action. Do not show phrase, task, operation or request IDs, raw status fields, or tool/rendering diagnostics. Use titles and returned website links. Do not announce that a native widget was rendered or reopened; the widget already presents the result.

Answer from saved Contexta evidence, with one useful next action. Read and apply [the shared workflow](../../references/workflow.md) before replying or calling the service.

## Open the progress view first

For a progress or next-practice request, use `show_practice_widget(entry="progress", id_format="website")` as the primary read when available. It returns the canonical measured patterns and actual next website action together, with the native Contexta interface. Do not collect summary-tool results first and then build a replacement table, dashboard, card or action button in chat.

For a named project, resolve its owned website reference from this conversation or `list_practice_projects`, clarify genuine ambiguity, then include that `project_id` in the progress-view call. For account-wide progress, omit `project_id`; no project discovery is needed. Pass `id_format="website"` on supported discovery and progress calls so references match website URLs.

The returned component is the complete answer to a progress or next-session request. Do not append a second summary, table, card, project heading, count list, website link or action button for the same result. In particular, do not generate a separate “Start next session” button: the real component already provides “Continue on website”. No additional prose is needed unless there is a relevant warning absent from the component or the learner asked a separate question.

A successful UI call is not proof of visible rendering. If the host fails to display it, explain that limitation and use the fallback below instead of claiming the chat response is the widget. Do not repeat a successful render merely to confirm it.

## Fallback and additional detail

Use `get_pattern_map_summary`, `get_practice_project_summary` and `get_next_practice` when the progress-view tool is unavailable or failed, or when the learner asks for specific detail absent from that view. These are additional reads or a truthful text fallback, not prerequisites for opening progress. Use `response_version=2` for next-practice reads when supported and `id_format="website"` for project/pack references.

Keep account-wide evidence separate from project-scoped evidence. Any text fallback or requested extra detail must preserve actual counts, freshness and limitations supplied by the service. A not-ready or insufficient-data result supports no diagnosis. The progress view adds no aggregate score, assessed-completion count or trend window. Project/material readiness does not imply completed assessment.

For a text fallback or requested extra detail, state the actual ready, preparing, assessment-pending, blocked, unavailable or completed condition. A completed project has no invented next session and must not be called still generating. Link to the exact returned website action only in that fallback; do not execute all four portal exercises in ChatGPT.

Do not claim improvement without comparable repeated measured evidence. Viewing a phrase, a successful save, a single score or a retry alone is not a trend. Do not double-count the same speech attempt and its portal history projection. Conversational language suggestions are separate from saved assessment.

In a text fallback, explain insufficient evidence plainly and suggest one relevant real practice action. The component already presents its own insufficient-evidence message and next action; do not repeat them. Do not use an empty result to diagnose the learner, force a plan, or create a reminder without a separate request.
