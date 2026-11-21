---
name: control-extract-setup
description: Use Control Extract to create sources, destinations, and connections, configure credentials and parameters, map fields, select streams, retrieve source sample data, and direct users to Extract account creation or invite pages.
---

# Control Extract Setup

Use this skill when the user wants to create or configure Extract sources,
destinations, connections, stream selections, source sample data, an
Extract account, or user access to their current Extract account.

All skills share the unified Extract MCP server:

- `extract` at `https://api.extract.to/mcp`, displayed as Extract.

Extract documentation: https://docs.extract.to/

Account access links:

- Create a new Extract account: https://app.extract.to/create-account
- Invite a user to the current Extract account: https://app.extract.to/users/new

## Tools

Use these `account_*` tools:

- `account_list_connectors` - find existing sources and destinations before setup.
- `account_search_connectors` - filter sources and destinations by name, type, or platform.
- `account_get_connector` - inspect one configured source or destination.
- `account_create_source` - create a source in setup status and return a setup URL.
- `account_create_destination` - create a destination in setup status and return a setup URL.
- `account_create_connection` - create a connection in setup status and return a setup URL.
- `account_get_configuration_form` - render a shared ChatGPT/Claude settings card, or return its non-secret schemas for other clients.
- `account_request_configuration_inputs` - use native MCP form elicitation when supported; otherwise return a guided-question schema. Returns a draft only.
- `account_submit_configuration_form` - validate and save user-supplied non-secret draft changes; check `remaining_inputs` afterward.
- `account_get_configuration_choices` - refresh dynamic dropdown choices after authentication and saving dependencies.
- `account_get_connector_configuration` - discover parameter scopes, required inputs, conditions, defaults and saved non-secret values.
- `account_add_source_dataset` - append a dataset or SQL query to an existing BigQuery/warehouse source, preserving other datasets and rejecting name conflicts.
- `account_update_connector_configuration` - patch account connector names, enabled state and non-secret parameters; credentials require secure browser or OAuth setup.
- `account_start_connector_oauth` - present an Authenticate card/link for new provider consent.
- `account_get_connector_oauth_status` - check that specific authorization attempt.
- `account_authenticate_connector` - validate saved credentials and discover the source catalog.
- `account_get_setup_task_status` - poll authentication or catalog refresh without exposing task payloads.
- `account_get_connector_parameter_options` - discover dynamic choices, optionally scoped to a connection and stream.
- `account_refresh_connection_catalog` - discover connection streams and destination data contracts.
- `account_get_connection_configuration` - inspect source fields, contracts, scoped parameters and mappings.
- `account_update_connection_configuration` - patch connection/stream parameters, stream settings and field mappings.
- `account_get_connection` - inspect a connection before configuration changes.
- `account_search_connections` - find existing connections by source and destination; verify exact source IDs and follow pagination.
- `account_trigger_run` - run an explicitly requested connection after configuration is verified.
- `account_list_connection_runs` - check the resulting run status; queued is not completed.
- `account_update_connection_schedule` - update schedule, custom cron, or enabled state.
- `account_select_connection_streams` - enable exact streams and disable all others.
- `account_create_sample_data` - start a source sample-data task for a stream.
- `account_get_sample_data` - poll sample-data status and return CSV content when ready.

## Workflows

### Create An Account

When the user wants a new Extract account, direct them to
https://app.extract.to/create-account.

If they are connecting Codex or Claude for the first time, explain that they can
create the account in the browser, then return to the Codex plugin or Claude
connector authorization flow after signing in.

### Invite A User

When the user wants to invite another person to their current Extract account,
direct them to https://app.extract.to/users/new.

Tell the user to open the link while signed in to the Extract account they want
to invite the person into. Do not collect invitee email addresses or other
personal details in chat unless the user explicitly asks for help drafting an
invite message.

### Create A Source Or Destination

Before calling `account_create_source` or `account_create_destination`, confirm the connector
platform and display name with the user. Read `account_get_connector_configuration`,
then explicitly ask for missing required inputs and inputs enabled by parameter
conditions. Direct credential entry to the authenticated Extract settings page; never ask
for passwords, keys or tokens in chat or form elicitation. The
returned `setup_url` handles credential entry; ordinary settings stay in MCP.
Save non-secret inputs with `account_update_connector_configuration`, authenticate, and poll
`account_get_setup_task_status` until success before continuing. Report failure rather
than treating a queued task as successful authentication.

### Create A Connection

Use `account_list_connectors` or `account_search_connectors` to identify the source and
destination. If multiple matches exist, ask the user to choose one. Confirm the
exact source and destination before calling `account_create_connection`. Configure
connection parameters, refresh the catalog and poll completion, then use
`account_get_connection_configuration` (follow `next_page_token` or target `stream_ids`)
and `account_update_connection_configuration` to configure
streams and mappings entirely through MCP. Parameter objects are scoped as
`{"source": {"name": "value"}, "destination": {"name": "value"}}`.
Omitted fields/streams are preserved; supplied lists replace the whole list.
Read existing values before modifying a dataset list or field mapping.

### Add A SQL Dataset To An Existing Source

Use `account_search_connectors` to resolve the requested source and
`account_get_connector_configuration` to inspect its `datasets` parameter and
`custom_object_parameters`. For a BigQuery source, ask for the dataset **name** and
**SQL query** if they are missing. Offer optional primary-key, incremental timestamp,
and view-materialization settings only when declared in its metadata and relevant
to the user's request. Do not invent these values.

Call `account_add_source_dataset(source_connector_id=..., dataset={"name": ..., "sql": ...})`.
This adds an Extract source dataset; it does not create a physical BigQuery dataset.
Existing entries are preserved. Identical retries do nothing; a name conflict must
be resolved explicitly instead of overwriting or renaming an existing entry.
The same tool uses metadata for other sources with an editable `datasets` list.

After adding, call `account_authenticate_connector` and poll `account_get_setup_task_status` to
validate access and rediscover source streams. If the dataset should feed an
existing connection, refresh that connection's catalog and configure its new stream
and mappings. Saving the entry alone does not validate the SQL or run a sync.

Dataset/SQL edits are supported through MCP and do not require browser automation.
If `account_add_source_dataset` is absent but `account_update_connector_configuration` is available,
read and preserve the existing dataset list before adding through that tool (it
replaces the whole list). If neither write tool is available, explain that the
connected server/tool list needs deployment or refresh. Do not describe dataset
editing as an unsupported Extract capability or silently switch to browser automation.

### Add A Dataset To Existing Audience Connections And Run

For requests such as “add `lapsed_7d` with this SQL to BigQuery Audiences Source,
enable it in my Meta Audiences connections, select Mobile Audience, walk me through
mapping, then run,” use this sequence:

1. Resolve the exact source and add the supplied name and SQL using the dataset
   workflow above. Wait for successful source authentication/catalog discovery.
2. Use `account_search_connections` with source and destination names, following every
   page. Verify each result's source connector ID against the resolved source;
   partial name matches alone are insufficient. Show the matching connections
   and resolve ambiguities. Do not create a new connection for this request.
3. For each intended connection, call `account_refresh_connection_catalog`, poll its task
   to success, and read `account_get_connection_configuration`. Resolve `lapsed_7d` to
   its actual stream ID in each connection. Never reuse stream or contract IDs
   from another connection.
4. Resolve the requested contract from `data_contracts`. If “Mobile Audience” is
   not an exact name, ask the user to choose from the discovered contracts. The
   bundled Meta contract is named “Mobile Advertiser ID custom audience”; do not
   silently assume it is the requested contract.
5. Present the connection configuration form or guided mapping questions. Show
   source columns alongside the chosen contract's required fields and descriptions.
   Ask which source column supplies the mobile advertiser ID, and collect other
   required stream parameters. Explain and confirm hashing, load mode and change
   detection. For `diff_result`, use automatic change detection when agreed;
   otherwise ask for a source column or an allowed static value such as `Added`.
   Never invent a column or silently choose audience add/remove behavior.
6. Save the selected contract, complete field mapping and `sync_enabled=true`
   together using `account_submit_configuration_form` or `account_update_connection_configuration`.
   Patch only the requested stream and preserve other streams and settings.
   Do not use `account_select_connection_streams` with just the new name: it disables all
   other streams. Check `remaining_inputs` and reload the saved configuration.
7. Once mapping is accepted and saved, honor an explicit “run connection” request
   with `account_trigger_run` for each intended connection. If disabled, resolve enabling
   it first. A connection run includes all its enabled streams; explain that when
   summarizing the run scope. Poll `account_list_connection_runs` for the returned run ID
   and report completion or failure; never equate queued with success or blindly
   retry a trigger whose outcome is unknown.

An explicit request authorizes the named changes and run; do not ask the user to
repeat that permission. Missing SQL, ambiguous targets and mapping choices still
require user input. A failed discovery or save must stop the dependent run.

### Configure Any Source And Destination

1. Discover or create the requested source and destination. Read each connector's
   `account_get_connector_configuration`, including descriptions, parameter scopes,
   conditions, types, defaults, nested `custom_object_parameters`, authentication
   method and documentation link. Do not infer fields from a platform name.
2. Prefer `account_get_configuration_form(target="connector"|"connection", target_id=...)`
   to present an embedded form on MCP Apps clients, including ChatGPT and Claude.
   On other clients, call `account_request_configuration_inputs` with a group ID for native
   elicitation. If unavailable, explicitly ask using the returned schema. Complex
   object rows and mappings use the card or guided questions. Never assume every
   OpenAI or Claude agent runtime can render widgets or elicitation.
   Submit accepted drafts through `account_submit_configuration_form`; do not submit after
   cancel/decline. Save only edited properties and inspect `remaining_inputs`.
   Explicitly ask for each missing required input by its display name and explain
   the expected format. Resolve conditional choices first, then collect their
   dependent fields. For object lists, collect the required fields of every item.
   Preserve existing list entries unless the user wants to replace them.
3. Collect passwords, API keys, and service-account keys only on the authenticated
   Extract page linked by `setup_url` / Open secure settings. Never ask for secrets
   in chat, native elicitation, or the embedded form. Reload after browser edits.
   Save ordinary parameters through `account_submit_configuration_form`.
   For OAuth authorization call
   `account_start_connector_oauth`. Present its Authenticate
   card or the returned `authorization_url` as a clickable link. The user approves
   access on the provider page; never ask them to copy a code or token into chat.
   They must use the same Extract user/account in the browser (sign-in is offered
   when needed). Poll `account_get_connector_oauth_status` with that attempt ID, not the
   connector's previous authenticated state. Stop on `AUTHORIZED`, `FAILED` or
   `EXPIRED`; restart authorization after failure/expiry if the user wants to retry.
   Once authorized, continue with `account_authenticate_connector` to verify provider access.
   The card's Continue setup button sends a follow-up to the agent; a completed
   authorization alone does not run the pipeline.
   Use `setup_url` for SSH setup or other special authentication. Secret
   stream parameters currently have no supported write path; report this limitation.
4. Authenticate both connectors and poll successful completion before proceeding.
   Saving credentials alone does not prove authentication worked.
5. Create the connection. Read its configuration and collect required connection
   parameters. Discover dynamic choices with `account_get_connector_parameter_options`;
   include `connection_id` and `stream_id` when the options depend on that context.
6. Save connection parameters, refresh the catalog and poll completion. Read actual
   stream IDs, source fields, destination contracts and supported load modes.
7. Ask which streams to sync and collect their required scoped parameters. When a
   destination uses contracts, select a contract and map its required fields using
   source columns or user-chosen static values. Ask about hashing and change
   detection when relevant; do not assume either behavior. Choose a supported
   load mode. Disable unselected streams explicitly.
8. Verify the saved configuration, then set the agreed schedule. Trigger an initial
   run only after explicit confirmation, using the operations handoff. Setup does
   not prove a successful sync.

These steps apply to all connector platforms. The parameter definitions and
provider authentication requirements determine the actual questions and values.

### Initial Schedule Or Enabled State

Set the initial schedule as part of setup. Hand off subsequent standalone schedule
or enabled-state requests to operations. Use `account_get_connection` to confirm the target connection. Confirm the exact
schedule, custom cron expression when `schedule="CUSTOM"`, and enabled state
before calling `account_update_connection_schedule`.

### Select Streams

Use `account_get_connection` to confirm the target connection, then confirm the exact
stream names before calling `account_select_connection_streams`. This tool disables all
streams that are not listed in `stream_names`.

### Get Source Sample Data

Use `account_create_sample_data` with the source account connector id and exact stream
name. Immediately poll `account_get_sample_data` with the returned sample data id until
the status is complete or failed. When `csv_content` is returned, save the full
CSV content to a local file using the returned `suggested_filename`; do not
summarize, truncate, filter columns, or paste the CSV into chat.

## Safety Rules

- Always confirm before creating a source, destination, or connection.
- Always confirm before changing a schedule, enabled state, or stream selection.
- Do not claim an account was created or an invite was sent unless the user
  confirms they completed it in Extract.
- Never expose credentials, tokens, secrets, setup URLs with sensitive query
  parameters, or unnecessary PII.
- Do not ask for Extract login passwords, OAuth authorization codes or invite
  tokens. Direct connector credential entry to the secure Extract settings page.
- If the user asks to invite someone to a different account, tell them to switch
  accounts in Extract first, then open the invite link.
- Do not guess connector ids, connection ids, or stream names.
- Treat `account_select_connection_streams` as a write operation because it changes sync
  configuration.
- For sample data, the local CSV file is the deliverable; keep chat output brief.

## Routing and handoffs

Use when the request concerns connector authentication, configuration, streams, mappings and connection setup. Handoff to diagnostics for failed executions; operations for ongoing schedules and inventory.
“Connect Google Ads to Snowflake” starts here; hand off a failed execution to diagnostics.

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
