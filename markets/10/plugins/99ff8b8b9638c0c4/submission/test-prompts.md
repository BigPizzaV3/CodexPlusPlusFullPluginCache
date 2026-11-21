# Eight reviewer test prompts

Prerequisite: TARS has prepared the three named synthetic lists, including at
least one item in Weekly Groceries. Start connected with all four scopes.
Resolve actual list/item IDs from read results, never guess them. Every write
needs a new `idempotency_key`; use the same key and identical arguments only
for retries. These are expected scenarios, not evidence of live execution.

| # | Prompt | Expected tool call(s) | Expected result |
| --- | --- | --- | --- |
| 1 | Show my LystBot lists. | `list_lists({})` | Includes Movie Night, Weekly Groceries and Weekend Trip; no foreign lists. Additional reviewer-created lists may appear. |
| 2 | Show the items in Weekly Groceries. | `list_lists({})` if IDs are unknown, then `get_list({list_id})` | Returns that list and its items, including text and checked status. |
| 3 | Add oat milk and apples to Weekly Groceries. | `add_items({list_id, items:[{text:"oat milk"},{text:"apples"}], idempotency_key})` | Two items created atomically. Retrying identical arguments with the same key returns the stored result without duplicates. |
| 4 | Mark the oat milk item as done. | `get_list({list_id})` as needed, then `update_item({list_id, item_id, text:null, checked:true, idempotency_key})` | Selected item becomes checked; text is preserved. |
| 5 | Create a packing list called Review Packing. | `create_list({title:"Review Packing", type:"packing", emoji:"", idempotency_key})` | Returns a new empty list owned by the connected demo device. |
| 6 | Remind me tomorrow at 9 AM Europe/Berlin to pack for the weekend, then show my reminders. | `create_reminder({title:"Pack for the weekend", scheduled_at:"<tomorrow YYYY-MM-DD>T09:00:00", timezone:"Europe/Berlin", repeat:"none", idempotency_key})`, then `list_reminders({})` | Reminder is stored with the resolved future time and appears in the device's reminders. Actual push delivery requires a registered push token and operational scheduler; this demo deliberately has no push token. |
| 7 | Read LystBot list ID review-inaccessible-list. | `get_list({list_id:"review-inaccessible-list"})` | Tool reports `List not accessible` with `isError:true`, without returning any list content. |
| 8 | Disconnect LystBot from ChatGPT. | No MCP tool exists. Explain connection-management steps; reviewer disconnects manually. | After token revocation/device unlink, previous bearer tokens no longer authorize MCP access. Lists and previous chat content remain. |

For an additional scope failure, a connection without `lists:write` receives
HTTP 403 `Insufficient scope` on write calls. No delete or sharing tools exist.
Evidence: MCP discovery/dispatch and write receipts in `McpController.php`,
OAuth checks in `OAuthAuthorizationService.php`, and local MCP/OAuth tests.
