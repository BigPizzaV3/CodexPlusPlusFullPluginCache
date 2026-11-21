---
name: workflow-designer
description: Design, inspect, clone or edit Reteno workflows using live account references and the workflow SDK executed by Reteno MCP. Creates paused workflows and verifies graph, configuration and saved state. Use for workflow structure, timers, branches, triggers and inactive prototypes. Does not send, schedule or activate campaigns.
---

# Workflow Designer

For one unambiguous existing relative Timer duration edit, use the
[focused timer procedure](references/focused-timer-edit.md) and Clock catalog only. If the
request changes timer mode, topology, triggers, settings or activation, use the full procedure.

For other work, read [OPERATING_MANUAL.md](OPERATING_MANUAL.md), then the specific block/config catalogs and
[SDK reference](references/client/SDK_API_REFERENCE.md) needed for the task. The plugin prepares
files and requests locally. Reteno MCP runs the remote editor, performs guarded persistence and
read-back. No local browser integration, publisher proxy or external agent is required.

1. Resolve the selected organization and referenced messages, segments, events, applications
   and tags through live MCP. Clarify only missing choices that materially affect the request.
2. For an existing workflow, call `get_workflow_export`, download its JSON artifact through
   `<plugin-root>/scripts/transfer.py`, and retain `modelHash`. Preserve unrelated branches and
   start/stop settings. For a new workflow, call `create_workflow` once, retain its ID and export
   the paused shell before preparing its graph. An empty shell is not a completed workflow.
3. Write SDK code ending with `sdk.finish()`. Prepare an `update_workflow` request with the
   local helper in the manual. Call its tool through the selected authenticated MCP connection.
4. Verify the save using the helper's `verify` command, then inspect a fresh export for the
   intended trigger, messages, timers, branches, end blocks and start/stop settings. New
   workflows must remain paused. Return the workflow ID and verified/unresolved status.

On `workflow_conflict`, re-read and reconcile; never swap in a new hash and blindly replay old
code. On `commitStatus=unknown`, inspect the retained ID before another mutation. On
`workflow_editor_at_capacity`, wait `error.retryAfterSeconds` and retry the same arguments once.
MCP may already perform one editor bootstrap recovery. A response with the expected workflow ID,
`updated:false`, `failurePhase:"editor"`, `commitStatus:"not_committed"` and `retrySafe:true`
establishes a pre-save failure; permit at most one client retry. Without all of that evidence,
re-export before any retry and reconcile the saved state. Do not loop editor restarts.
Do not retry an ambiguous create. Keep the ID and describe incomplete steps for continuation.

Use `reteno-analytics` / `segment-designer` count mode for audience estimates without creating
a segment. Counts are matching contacts, not predicted sends or trigger volume.

Only Reteno is supported. Viber/Telegram blocks and custom tasks are excluded. Never invent
entity IDs or replace missing messages with unrelated assets. Do not send, activate or
schedule a workflow as part of editing; proposed schedules are saved configuration only.
