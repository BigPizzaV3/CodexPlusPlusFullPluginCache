---
name: stele
description: Use Stele as durable, shared project memory and work tracking. Apply this skill when the user wants to recall project context, trace decisions and provenance, save knowledge, inspect or coordinate tasks, organize a roadmap, or leave a handoff for another agent or teammate.
---

# Stele shared project memory

Stele stores decisions, lessons, risks, documents, components, objectives, and tasks in a shared project knowledge graph. Use the Stele tools when the user's request depends on persistent project context or should leave durable context for future work.

Do not use Stele for unrelated requests such as general code generation, calendar access, email, or web research unless the user also asks to retrieve, save, or coordinate project context.

## Establish the project

The hosted server is stateless. Every project-scoped call must include `project_slug`.

- Use a project slug explicitly named by the user.
- If the project is not clear, call `list` with `what: "projects"` and ask the user to choose when more than one project is plausible.
- Never guess a slug or carry an implicit active project between calls.

## Read before acting

Before a non-trivial write, check what the project already knows so you do not duplicate or contradict current records.

- Use `recall` for a broad, ranked context bundle about a question or topic.
- Use `search` for a keyword, exact-term, or document-scoped lookup.
- Use `list_tasks` for the current work board and `list` for other collections.
- Use `fetch` when a result's full body and edges matter.
- Use `inspect` with `action: "context"` for a node's neighborhood or `action: "provenance"` to explain why it exists and what it superseded.

Search and recall results are summaries. Fetch the relevant node before relying on detailed wording, lifecycle state, or links.

## Preserve evidence and uncertainty

Answer from recorded graph evidence. Name the relevant record with a short human-readable gloss and its shareable ID, such as “the retry-backoff decision (`KNOW-12`)” or “the telemetry task (`TASK-8`)”. When useful, link it as:

`https://app.stele-ai.dev/p/<project_slug>/nodes/<SHAREABLE-ID>`

Clearly distinguish recorded facts from your inference. If the graph is incomplete or conflicting, say so and ask whether the user wants the missing context recorded.

## Capture durable knowledge

Use `knowledge` with `action: "create"` for a decision, architecture fact, lesson, risk, goal, gap, opportunity, priority, or FYI that should survive this conversation.

1. Search for an existing record first; update it with `node` rather than creating a duplicate when it represents the same fact.
2. Choose the category that describes what the information is, not merely where it was discussed.
3. Record enough context to remain useful later: what happened or was chosen, why, consequences, and concrete triggers or evidence.
4. Supply the lifecycle fields requested by the schema. Use `null` deliberately when the knowledge should not expire, is not tied to a resolving task, and needs no review date.
5. Add links with `node` and `action: "link"` when they explain causality, support, supersession, ownership, or fulfillment.

Use `knowledge` with `action: "review"` only after checking the node against current reality.

## Coordinate tasks through the lifecycle tool

Use `task` for task lifecycle changes. Never simulate a lifecycle transition by editing a task status with `node`.

- `create`: include a clear outcome, reason, and success criteria.
- `claim`: claim work before beginning when the user asks the agent to perform it.
- `complete`: complete only when the outcome and success criteria are genuinely satisfied; summarize what changed and verification performed.
- `release`: release work that is intentionally being handed back.
- `reopen`: reopen completed work only when more work is actually required.

Use `list_tasks`, `fetch`, and `inspect` to understand task state and linked context before changing it. Consequential task actions such as cancellation and force-claiming are in `destructive`.

## Edit and organize carefully

- Use `node` to update content, move a node, or add a typed link.
- Use `objective` to create objectives and milestones, place tasks, set targets, reorder work, or mark an objective achieved.
- Use `comment` for discussion attached to a node.
- Use `document` for long-form plans, specifications, imported material, or diagrams.
- Use `organize` for durable project components, topic renames, feedback, or supported context-injection controls.
- Use `workspace` only for persistent workspace records. Hosted requests do not retain an activated workspace between calls, so do not rely on activation or deactivation as session state.

Use the exact action-specific arguments advertised by each tool schema. Do not send fields from another action branch.

## Destructive operations

The `destructive` tool contains consequential operations such as cancelling tasks, force-claiming, removing links, restoring old versions, retiring or archiving records, and merging data.

- Explain the exact effect and target first.
- Obtain explicit confirmation immediately before the call.
- Keep the confirmed scope narrow; do not batch additional destructive changes into the request.
- If the action is unavailable on hosted MCP, report that limitation instead of substituting another mutation.

Read-only candidate discovery such as `action: "dedupe_knowledge"` may be used to inspect possible duplicates, but any merge still requires confirmation.

## Finish with a useful handoff

After writes, report what changed with titles and shareable IDs, mention important links or lifecycle state, and identify any remaining uncertainty or follow-up. Do not expose raw internal UUIDs.
