---
name: use-buildory
description: Inspect, explain and maintain live Buildory project data through Buildory MCP tools. Use when a user asks about Buildory projects, progress, risks, tasks, parts or BOM items, build logs, knowledge, photo captions, linked resources, blockers, next steps, or explicitly asks to record or update supported project information.
---

# Use Buildory

Use Buildory as the source of truth for the connected user's project facts. Keep factual findings separate from recommendations and distinguish proposed changes from completed writes.

## Choose a read tool

- Call `buildory_list_projects` when the project is not unambiguous or the user asks across projects.
- Call `buildory_project_summary` for status, structure, totals, recent activity, or a general progress review.
- Call `buildory_search_project` for a topic, component, phrase, supplier, linked resource, problem, or cross-section question.
- Call `buildory_get_section` for detailed child sections, tasks, parts, logs, knowledge, photos, and linked resources in one section.
- Call `buildory_get_execution_brief` when the user wants a focused technical handoff for one existing task or section. Treat the returned brief as bounded project context, not as authorization to execute work or mutate Buildory.
- Call `buildory_get_project_activity` when the user asks what changed, when it changed, or whether a change came from a human, MCP client, Codex return, API, or automation.
- When available, call `buildory_list_project_items` before a precise update, archive, restore, or typed inventory request; call `buildory_get_project_item` for one exact returned record.
- When available, use `buildory_list_artifacts` for a file inventory and `buildory_get_artifact` only when full revision history, links, or a temporary download URL is needed.

Use project and section identifiers returned by Buildory. Do not invent identifiers or guess access to projects that were not returned.

## Choose a write tool

- Call `buildory_create_task` to add an agreed task to a specific existing section.
- Call `buildory_update_task` to change an existing task's content, status, priority, or due date.
- Call `buildory_create_bom_item` to record a candidate part or material.
- Call `buildory_update_bom_item` to refine, move, select, order, receive, reject, or obsolete a part.
- Call `buildory_create_knowledge` to preserve a note, decision, research result, specification, or reference.
- Call `buildory_create_build_log` only for work or observations that actually happened, not future plans.

When the connected server exposes the additive Buildory 2.0 tools:

- Call `buildory_update_project` only for supported metadata or active lifecycle changes; it cannot change visibility, publication, billing, MCP settings, or archive state.
- Call `buildory_create_section` or `buildory_update_section` for an explicitly requested section, hierarchy move, or sibling ordering change.
- Call `buildory_manage_task` for blocked state, execution details, or moving an existing task; keep the published `buildory_update_task` behavior unchanged.
- Call `buildory_update_knowledge` or `buildory_update_build_log` only for a genuine correction and include the user's reason. Prefer a new superseding knowledge item for a newer conclusion.
- Call `buildory_create_resource` or `buildory_update_resource` for external references and their project or section placement.
- Use the artifact prepare → direct upload → finalize sequence for versioned deliverable files. Never send file bytes as base64 in tool arguments.
- Call `buildory_archive_items` only for exact records after explicit user intent. Archive is reversible, not permanent deletion. Call `buildory_restore_items` for exact archived records and restore archived parent sections first.

After external execution, use the existing update-task, create-build-log, or create-knowledge tools only when the user asks to return the result to Buildory. Keep the stored outcome concise and preserve Buildory as the authoritative project record.

There are no tools for creating or deleting projects, permanently deleting records, changing project visibility, publishing projects, or changing membership. Section creation and reversible project-item archive/restore are available only when the connected server exposes the additive Buildory 2.0 tools.

Published MCP tools are immutable contracts: extend the toolset, but do not reinterpret existing inputs, outputs, or side effects.

## Review project progress

1. Resolve the intended project. Ask a brief clarification only when multiple returned projects are plausible.
2. Fetch the project summary.
3. Search or inspect a section only when the question needs more detail.
4. Report the current state, evidence, risks, and concrete next steps.
5. Label advice and inferred risks as recommendations rather than stored Buildory facts.

For a general health review, prefer this compact structure:

- Current state
- What needs attention
- Recommended next three steps
- Missing information that would improve the assessment

Do not treat missing activity, dates, priorities, or blockers as proof that the project is healthy. State that the information has not been recorded.

## Write safely

- Write only when the user explicitly asks to record or change something in Buildory. A request to advise, review, brainstorm, or propose does not authorize a write.
- When the user approves a clearly listed set of changes, execute that set without asking for a second redundant confirmation.
- Read first when a write needs a project, section, task, or BOM ID that is not already known.
- Before creating several similar items, inspect existing content when practical to avoid duplicates.
- Before moving, correcting, archiving, or restoring content, resolve exact records and their project first. Never substitute archive when the user asked for permanent deletion; permanent deletion is unavailable.
- Include only fields the user supplied or clearly approved. Do not silently invent dates, prices, statuses, suppliers, or decisions.
- After writing, report exactly what was created or updated and surface any structured Buildory error.
- If write access is unavailable, explain whether the connection is read-only, the workspace needs Pro or Creator, or the workspace itself is locked read-only.
- Never claim a write succeeded unless the tool returned the created or updated record.

## Handle data carefully

- Use only data returned for the authenticated user.
- Avoid reproducing internal identifiers unless they help disambiguate a project or section.
- Do not expose unrelated project details when answering a narrow question.
- Match the user's language.
- Say clearly when no matching information was found.
