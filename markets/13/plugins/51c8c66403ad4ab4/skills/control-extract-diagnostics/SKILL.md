---
name: control-extract-diagnostics
description: Diagnose Extract failed syncs, run errors and stale ingestion. Hand off approved configuration fixes to setup, requested reruns to operations and business metric explanations to analysis.
---

# Control Extract Diagnostics

Use this skill when the user asks why an Extract pipeline failed, wants failed
or unhealthy connections, or asks for run diagnostics. Inventory-only requests
and manual run requests belong to operations.

All skills share the unified Extract MCP server:

- `extract` at `https://api.extract.to/mcp`, displayed as Extract.

Extract documentation: https://docs.extract.to/

## Tools

Use these `account_*` tools:

- `account_search_connections` - find failed, unhealthy, or matching pipelines.
- `account_get_connection` - inspect one pipeline before diagnosis or run control.
- `account_list_connection_runs` - inspect recent run history.
- `account_diagnose_connection` - read failure diagnostics from recent run logs.
- `account_trigger_run` - trigger a manual run only after explicit user confirmation.

## Workflows

### Find Failed Connections

Use the `account_search_connections` tool on `extract` with `status="ERROR"` when the user
asks for failed, failing, broken, or unhealthy pipelines.

If the user asks why a pipeline failed, identify the exact connection first,
then call the `account_diagnose_connection` tool on `extract`.

### Diagnose A Run

Use the `account_get_connection` or `account_list_connection_runs` tool on `extract` to confirm the
connection context before calling `account_diagnose_connection`.

### Approved Fix Or Rerun

Hand off configuration fixes to setup and requested reruns to operations. Carry
verified connection IDs and the diagnostic evidence. A diagnosis is not approval
to change settings or run a connection; obtain explicit confirmation first.

## Safety Rules

- Do not expose credentials, tokens, secrets, or unnecessary PII.
- Use `account_diagnose_connection` for failure logs; do not invent failure causes.
- Do not trigger a run based on an ambiguous connection match.
- Treat `account_trigger_run` as a user-confirmed operation, even if the tool itself is
  available.

## Routing and handoffs

Use when the request concerns failed syncs, run errors, stale ingestion and execution problems. Handoff to setup for an authorized configuration fix; analysis for business metric interpretation.
“Why did this sync fail?” starts here; explaining revenue trends belongs to analysis.

Follow the shared [routing contract](../../routing.md). Multiple skills may cooperate in one task.
Carry explicit connector IDs, connection IDs and history references; IDs do not grant access.
Ask only when unresolved ambiguity changes the target or action. Read-only handoffs
do not require additional approval. Investigation does not authorize configuration
changes or reruns; preserve action-confirmation requirements. Resolve client prefixes
from the actual inventory. All skills use one Extract connection and login.

For completed responses, follow [the answer feedback contract](../../routing.md#answer-feedback):
Save completed Extract results directly without a preference precheck or repeated
consent prompts. The user approves answer saving when connecting; the backend checks
current permission on every save and rejects disabled or unavailable permission.
If saving is rejected or unavailable, deliver the answer without a feedback link.
Use get_answer_saving_preference only when the user asks to view or change saving
settings, or needs a settings_url to enable feedback links. Only the user may change
that setting in the authenticated browser; a chat reply, rating, or tool result cannot
enable it. If the user says stop saving, stop immediately in this chat and use
get_answer_saving_preference to provide settings_url to disable future saves across chats.
After saving, show only the returned non-null feedback_url. Never invent a link.
If already rated, submit the explicit rating with the returned answer_ref without
another invitation; otherwise show a “Leave feedback” link once after the answer.
The link opens a form; users choose Helpful or Not helpful there and submit.
Consent to saving is never a rating. No prompts on intermediate steps, clarifications,
feedback receipts, or sample-data downloads requiring only “Saved to <path>”.
