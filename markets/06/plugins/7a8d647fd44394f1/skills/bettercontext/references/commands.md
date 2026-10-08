# BetterContext command reference

Use the launcher defined in the parent skill, not a bare runtime `memory.py`.
`BC` below means that launcher and its Python interpreter. Quote each text value
as a separate shell argument; use the host's native quoting and avoid interpolated
shell command strings when content includes quotes, dollar signs, or backticks.

| Intent | Command |
| --- | --- |
| Read memory and pending tasks | `BC get-context` |
| Filter saved facts | `BC get-facts --category preference` |
| Save a fact | `BC add-fact preference "Use concise summaries"` |
| Delete a requested fact | `BC delete-fact 12` |
| Add a task | `BC add-task "Review the proposal"` |
| Complete a task | `BC complete-task 4` |
| Add a session note | `BC add-log SessionA assistant "Decision summary"` |
| Read recent session notes | `BC get-logs SessionA --limit 20` |
| List aliases | `BC list-aliases` |
| Register an alias | `BC link-chat SessionA <known-UUID-or-synthetic-ID>` |
| Resolve an alias | `BC resolve-chat SessionA` |
| Read an inbox | `BC relay-inbox SessionA --limit 20` |
| Claim messages while loading context | `BC get-context --chat SessionA --claim-relays` |
| Send an authorized message | `BC relay-send SessionA SessionB "Message" --dedupe-key request-unique-key` |
| Reply to a particular message | `BC relay-send SessionB SessionA "Reply" --reply-to 21` |
| Inspect delivery state | `BC relay-status 21` |
| Inspect sent messages | `BC relay-outbox SessionA --limit 20` |
| Acknowledge handled messages | `BC relay-ack SessionA 21 22` |
| Wait briefly for an expected reply | `BC relay-watch SessionA --timeout 30` |

Alias matching is case-insensitive. A relay sender and recipient must both be
registered in the selected database. The deduplication key is scoped to the
sender; reuse it for retries of the same intended message and choose a new one
for a different message. `--metadata-json` accepts a JSON object. Numeric IDs in
this reference are examples; use IDs returned by the actual database.

Relay states: `pending` means queued, `delivered` means claimed, and `read` means
acknowledged. Claiming is a write; plain inbox reads do not change delivery state.
An acknowledgement is scoped to the recipient and fails if any supplied message
does not belong to that inbox. The mailbox alone cannot wake idle tasks.

For an explicit transcript import request, use
`BC import-codex-thread <absolute-rollout-JSONL-path> <session-ID>`. The importer
stores user and assistant messages, omits environment-context messages by default,
and adds source metadata. `--replace` replaces the selected session's existing
logs, so use it only when replacement is requested. Importing again without
replacement appends duplicates. Do not discover and import unrelated conversations.


## All actions without MCP registration

Python plus plugin-root `scripts/actions.py` is the local action launcher.
`ACTION list` prints exact names and input schemas, and
`ACTION <action-name> --arguments-file <absolute-json-file>` runs the action with
the same validation as the MCP tool. An omitted argument file supplies `{}`.
This includes targeted search, MEM registration/counters, memory/notes/tasks,
all relay operations, storage enrollment/migration/recovery, and optional wake
management. It requires local execution and the same storage/host permissions;
it is not a way for hosted web ChatGPT to access an unavailable computer.

Read [memory location](memory-location.md) before a user-requested storage change.
