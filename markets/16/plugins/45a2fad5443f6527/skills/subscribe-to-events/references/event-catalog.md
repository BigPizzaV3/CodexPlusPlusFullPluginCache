# monday CRM event catalog

## 1. AI suggestion event (Path A, primary)

Delivered through ChatGPT event monitoring (MCP Events), not a monday webhook. Check that ChatGPT lists it for this plugin before promising it.

| Field | Value |
|---|---|
| Event name | `crm.ai_suggestion_created` |
| Fires when | monday CRM creates a new AI suggestion for the connected user (as in My Focus) that is still open and the user can access the item |
| `task_type` values | `fulfill_commitment` (a promised follow-up), `resolve_blocker`, `answer_question`, `client_went_silent` |
| Payload | `task_id`, `item_id`, `item_name`, `task_type`, `action_text`, `score` (summary only; read the rest through tools) |
| Filters | `task_types`: non-empty unique array of supported types; omit for all. No item-type, board, or item filter in the released schema; those require post-delivery checks and may still trigger notifications |
| Lifetime | Subscriptions last up to 24 h; ChatGPT refreshes them. Up to 10 live subscriptions per user |
| Companion tools | `show-ai-suggestion-event` (card, by `task_id`; follow-up cards offer Draft reply), `extract_signals` (evidence, by `item_id`), `get-timeline-items`, `search-crm-recipients`, `show-mass-emails-draft` (draft widget; the user sends), `create-timeline-item` / `create-timeline-note`, `update_task_occurrence_status` (mark done, if exposed) |
| Eligibility and delivery | Trial accounts do not receive deliveries. Delivery is best effort with no retry; do not assume every suggestion arrives. |
| Polling fallback | `get_account_task_rollup` (open suggestions by priority) in a scheduled task |

## 2. Board-change events (fallback paths B, C, D)

Source: monday platform API, *Webhooks* reference (https://developer.monday.com/api-reference/reference/webhooks), checked Nov 2, 2026. Webhooks are **board-scoped**. There are no account-wide or user-wide webhooks.

| User says | Webhook `event` | `config` | Activity-log filter for polling (Path C) |
|---|---|---|---|
| New deal / lead / contact created | `create_item` | — | `event_types: ["create_pulse"]` |
| Deal stage / status changed (any value) | `change_status_column_value` | `{"columnId":"<stage col>","columnValue":{"$any$":true}}` | `event_types: ["update_column_value"]` + filter column = stage |
| Stage changed **to** a specific label | `change_status_column_value` | `{"columnId":"<stage col>","columnValue":{"index":<label index>}}` | as above, then filter new label |
| Deal reassigned / owner changed | `change_specific_column_value` | `{"columnId":"<owner people col>"}` | `update_column_value` on the owner column |
| Specific field changed (amount, close date…) | `change_specific_column_value` | `{"columnId":"<col>"}` | `update_column_value` on that column |
| Any field changed | `change_column_value` | — | `update_column_value` |
| Deal renamed | `change_name` | — | ⚠️ event type name not verified; use `include_data` and check |
| Deal moved to a group (e.g. "Won") | `item_moved_to_specific_group` | `{"groupId":"<group id>"}` | ⚠️ verify event type in activity log |
| Deal moved to any group | `item_moved_to_any_group` | — | ⚠️ verify |
| Update / comment posted on a deal | `create_update` | — | `entities: ["update"]` |
| Update edited / deleted | `edit_update` / `delete_update` | — | `entities: ["update"]` |
| Deal archived / deleted / restored | `item_archived` / `item_deleted` / `item_restored` | — | `delete_pulse` etc. ⚠️ verify |
| Subitem events | `create_subitem`, `change_subitem_column_value`, `change_subitem_name`, `move_subitem`, `subitem_archived`, `subitem_deleted`, `create_subitem_update` | Use the **parent** board ID | — |
| New column added | `create_column` | — | — |

Notes:
- `change_specific_column_value` can't watch subitem columns.
- Status `index` values come from `get_board_info` (the status column's label settings). Never guess them.
- The webhook URL is limited to 255 characters. A query parameter can tag events (e.g. `?sub=deal-stage`).
- Payloads include `event.type`, `boardId`, `pulseId` (item), `columnId`, `value`, `previousValue`, `userId`, `triggerTime`, `triggerUuid`. Use `triggerUuid` to de-duplicate retries.
