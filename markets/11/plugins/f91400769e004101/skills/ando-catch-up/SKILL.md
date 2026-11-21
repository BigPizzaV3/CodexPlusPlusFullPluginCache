---
name: ando-catch-up
description: Summarize activity in an Ando channel, project, or bounded time window, including decisions, blockers, and requests. Use for catch-ups, project updates, and what changed since a specified time.
---

# Catch up

Read [Ando basics](../../references/ando-basics.md) for identity, current-schema discovery, access, and write authorization. Discover only tools needed for this request.

Resolve the requested workspace, channels/project, time window, and timezone from context. Ask only when a missing boundary would materially change the result. If using a reasonable default, state it.

Use the current conversation reads and search schemas. Resolve IDs from permitted discovery. Search locates candidate messages; read the relevant messages and thread replies before summarizing. Follow cursors until the requested window is covered, including replies that resolve an earlier blocker. If a tool truncates results, narrow the window and continue rather than claiming complete coverage.

Separate final decisions from proposals, open requests from completed work, and reported blockers from inferred risks. Include owners only when stated or confirmed. Prioritize changes relevant to the user's work; avoid an exhaustive transcript or unnecessary personal details.

Return a concise update with source links for material claims. State the covered window and any inaccessible channels, missing replies, or incomplete pages. Do not send the update, create tasks, or change channel context unless requested. For a specific disputed question, use [Find answers](../ando-find-answers/SKILL.md).

See [shared workflows](../../references/shared-workflows.md) for conversation-read contracts and recovery.
