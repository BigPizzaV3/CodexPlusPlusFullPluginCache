---
name: saleslumen-workflows
description: >-
  Build and run Saleslumen workflows via MCP: create and update structural
  drafts, publish, activate, and manage executions. Use when the user wants a
  workflow graph, a version, or a workflow run. Do not use for inbox email,
  campaigns, or naming a script function or marketplace operation inside the
  graph.
---

# Saleslumen Workflows

Use the Saleslumen MCP connector to define structural graphs and run workflows that already exist. Keep the conversation natural; push workflow JSON and manage executions with tools.

## Concepts

A workflow has metadata and append-only versions. Create seeds the first version. Update appends a draft. Publish makes a version current. Revert copies a past published definition into a new draft.

Executions pin a version and run asynchronously. Status is a number: `1` ACTIVE, `2` PAUSED, `3` COMPLETED, `4` ERROR, `5` CANCELLED.

`workflows_create` and `workflows_update` accept structural nodes and connections. They reject a node that names a script function or a marketplace operation. Do not put either in the graph. Author those calls in Saleslumen, then start the saved workflow by id.

`agent` and `wait` pause the run. Resume continues at the main-flow successor; it does not re-execute the pause node.

## Workflow

1. Clarify the goal (design, publish, activate, run, resume, cancel, or inspect).
2. Read with `workflows_list` / `workflows_get` before you change a graph.
3. Ship a structural draft with create or update, then publish, then activate, then `workflows_start_execution`.
4. Confirm with the user before publish, activate/deactivate, start/resume/cancel, and delete.
5. Poll with `workflows_get_execution` or `workflows_list_executions`. Resume only when status is `2`.

## Tools

| Task | Tools |
| --- | --- |
| Definitions | `workflows_list`, `workflows_get`, `workflows_create`, `workflows_update`, `workflows_delete` |
| Versions | `workflows_publish`, `workflows_revert_version`, `workflows_get_history`, `workflows_get_version` |
| Lifecycle | `workflows_activate`, `workflows_deactivate` |
| Executions | `workflows_start_execution`, `workflows_resume_execution`, `workflows_cancel_execution`, `workflows_get_execution`, `workflows_list_executions` |

## Guidance

- Default start (no `version_id`) requires Publish then Activate. `version_id` is a preview and may run a draft while inactive.
- Keep graphs acyclic and include `start` and `end`.
- Edit Script source with the Apps Script skill. Do not name a script function or a marketplace operation in a workflow node.
