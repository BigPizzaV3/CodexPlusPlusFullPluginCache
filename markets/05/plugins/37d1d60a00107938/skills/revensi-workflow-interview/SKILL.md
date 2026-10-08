---
name: revensi-workflow-interview
description: Interview an operator, review a complete workflow draft in the conversation, and save it to Revensi once approved. Use when the user asks to map a new process through questions; do not use for reviewing an existing saved map.
---

# Revensi Workflow Interview

This skill guides a new workflow interview in the conversation. Keep the working draft in conversation context; do not create a Revensi record or local file for each answer. Revensi owns persistence and authorization through one final `add_workflow` call. An unfinished conversation draft is not saved and may not survive an interrupted or new conversation.

1. Before creating a record, ask whether someone does this work today, even roughly (`existing`), or nobody gets to it yet (`new`). Do not assume the answer from a goal statement. If the user already supplied it, do not re-ask.
2. Check for an apparent duplicate with `list_workflows` before saving. If that tool is unavailable, say duplicate checking is unavailable; do not assume the workflow is new.
3. Ask the next useful question, usually one at a time, and maintain the draft from the user's answers. Preserve important detail. Do not infer missing answers or re-ask questions the user explicitly deferred.
4. Cover the trigger and rules, inputs, capabilities/tools, ordered steps, decisions and outcomes, exceptions, handoffs, human review, outputs and destination, frequency, and hands-on minutes per run. For work that does not run today, do not invent current roles or handoffs. For work that does, preserve who does it now and where the handoffs lose context.
5. A step owner describes the proposed workflow: `automation` for routine movement/calculation, `ai` for reading/judgment/drafting, and `human` for accountable decisions, conversations, physical actions, or signatures. Human sign-off belongs in review. These are mapping conventions, not a promise that the automation exists.
6. Name specific services only when the user or evidence identifies them. Keep unknowns open. Do not invent savings, scores, build size, access grants, or citations.
7. Present the complete proposed workflow map and its open or deferred questions to the user. Ask for approval to save it; apply requested corrections in the conversation draft first. If the user has already supplied a complete map and explicitly approved saving that map, do not ask for approval again. Do not call `add_workflow` for a preview or without that approval.
8. On approval, call `add_workflow` once with a fresh UUID `requestId`, name, origin, the user-confirmed map layers, and any known purpose, department, effort, or open questions. Save deferred questions in `openQuestions` too; this tool does not persist a separate deferred state, so explain that they remain open in the saved draft. Each map layer is a complete list; use zero-based `stepIndex` only when a decision or handoff belongs to a specific step. Reuse the same request ID only to retry the identical payload. Do not send a transcript, workspace ID, computed scores, status, or other server-owned fields. The server validates the model and resolves the workspace selected during OAuth. If the write tool is missing, say the draft cannot be saved; do not substitute a web request, local file, or another tool.
9. Report the saved name, draft status, and link/ID only from the tool response. Distinguish confirmed facts from open questions. Never mark it live, publish it, or connect a service as part of this skill.

A timed-out save has an unknown outcome. Check `list_workflows` before retrying or claiming success; if retrying the identical payload, reuse its original `requestId` rather than creating another draft.

A save succeeds only when `add_workflow` returns its ID and link.
