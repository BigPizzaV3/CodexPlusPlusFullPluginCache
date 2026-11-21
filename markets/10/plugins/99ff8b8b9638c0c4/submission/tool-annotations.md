# MCP tool annotations

All seven tools operate within LystBot (`openWorldHint:false`). Reads have no
side effects. Writes require `idempotency_key`; the same key and identical
arguments return a persisted receipt rather than repeating the mutation.
A reused key with different arguments is rejected. `update_item` conservatively
retains `destructiveHint:true` because replacing text overwrites existing content.
There are no delete or revoke tools in this register.

| Tool | readOnlyHint | destructiveHint | openWorldHint | idempotentHint | Reason |
| --- | --- | --- | --- | --- | --- |
| list_lists | true | false | false | true | Reads connected-device memberships. |
| get_list | true | false | false | true | Reads one accessible list and its items. |
| list_reminders | true | false | false | true | Reads connected-device reminders. |
| create_list | false | false | false | true | Adds a list; operation receipt prevents duplicate retries. |
| add_items | false | false | false | true | Adds items atomically; receipt prevents duplicate retries. |
| update_item | false | true | false | true | Replaces text or checked status; receipt prevents repeated mutation. |
| create_reminder | false | false | false | true | Adds a reminder; receipt prevents duplicate retries. |

Source: `backend/src/Controllers/McpController.php::tools()` and `write()`.
The package test compares live tool discovery with these annotations.
