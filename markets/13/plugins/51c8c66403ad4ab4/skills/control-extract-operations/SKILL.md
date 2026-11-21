---
name: control-extract-operations
description: Manage Extract inventory, account health, schedules, enabled state and user-requested runs. Hand off setup to the setup skill, failures to diagnostics and business metrics to analysis.
---

# Control Extract Operations

Use this skill when the user asks about Extract account status, configured
connectors, sources, destinations, pipelines, connection details, or recent run
history, schedules, enabled state, or explicitly requested runs.

Use the shared Extract MCP server:

- `extract` at `https://api.extract.to/mcp`, displayed as Extract.

Extract documentation: https://docs.extract.to/

## Tools

Use these `account_*` tools:

- `account_summary` - summarize account connectors and connections.
- `account_list_connectors` - list all account connectors, sources, and destinations.
- `account_search_connectors` - filter account connectors by name, type, or platform.
- `account_get_connector` - inspect one configured connector.
- `account_list_connections` - list pipelines.
- `account_search_connections` - find pipelines by source, destination, or status.
- `account_get_connection` - inspect one pipeline.
- `account_list_connection_runs` - list recent runs for a pipeline.
- `account_update_connection_schedule` - change confirmed schedules or enabled state.
- `account_trigger_run` - start an explicitly confirmed run.

## Workflows

### Account Health

Use the `account_summary` tool on `extract` for account status, pipeline health,
active connections, disabled connections, and error counts.

### Connector Inventory

Use the `account_list_connectors` tool on `extract` for a broad source/destination inventory.
Use the `account_search_connectors` tool on `extract` when the user provides a connector name,
type, or platform filter.

### Pipeline Details

Use the `account_list_connections` tool on `extract` for broad pipeline discovery. Use
the `account_search_connections` tool on `extract` when the user provides a source,
destination, status, or name filter. Then call the `account_get_connection` tool
on `extract`
before answering detailed questions about one pipeline.

### Run History

Use the `account_list_connection_runs` tool on `extract` after identifying the connection.

## Safety Rules

- Do not expose credentials, tokens, secrets, or unnecessary PII.
- Do not guess connector ids or connection ids.
- If multiple connectors or connections match, ask the user to choose one.
- Use the setup skill for creating sources, destinations, connections, stream
  selection, configuration, or sample data.
- Hand off SQL analysis and warehouse schema discovery to the analysis skill
  on this same connection; do not initiate another login.
- Confirm the exact schedule/enabled-state change before writing. For a manual
  run, show the connection name, source, destination and current status and obtain
  explicit confirmation of the exact connection before `account_trigger_run`.

## Routing and handoffs

Use when the request concerns inventory, account health, schedules, enablement and requested runs. Handoff to setup for configuration; diagnostics for failure investigation.
“Show failing pipelines” starts with inventory; “why did this sync fail?” belongs to diagnostics.

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
