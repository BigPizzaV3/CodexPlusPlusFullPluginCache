# Perisclaw public plugin tool annotations

This is the reviewer-facing justification for every tool advertised by
`https://api.perisclaw.com/mcp/plugin` with Read + write access. The direct
`/mcp` connector has a broader private-client surface and is not the directory
submission target.

`readOnlyHint` means the call cannot mutate state. `destructiveHint` is true when
the call can send, delete, overwrite, change access, or activate durable
behavior. `openWorldHint` is true when the call reaches beyond Perisclaw: it
communicates with people, changes state in the user's WhatsApp account or Google
Contacts, or fetches from WhatsApp's media servers.

| Tool | Read only | Destructive | Open world | Justification |
| --- | --- | --- | --- | --- |
| `get_profile` | true | false | false | Identifies the connected WhatsApp account. |
| `workspace_open` | true | false | false | Renders the catch-up card; does not mark messages read. |
| `workspace_conversation` | true | false | false | Renders one permitted chat and an unsent draft; sending happens only from the card's Send button through `reply_prepare`/`reply_send`. |
| `reply_prepare` | false | false | false | Saves private reply text; sends nothing. |
| `reply_send` | false | true | true | Sends the approved draft to WhatsApp at most once. |
| `reply_status` | true | false | false | Reads a draft's durable outcome without retrying it. |
| `monitor_list` | true | false | false | Lists this connection's ChatGPT event subscriptions (listed only where watching is enabled). |
| `monitor_stop` | false | true | false | Cancels one of this connection's event subscriptions (listed only where watching is enabled). |
| `search_messages` | true | false | false | Searches the connected account's stored message index. |
| `get_messages` | true | false | false | Reads message history for one permitted chat. |
| `search_contacts` | true | false | false | Searches stored contacts without changing them. |
| `search_chats` | true | false | false | Searches the connected account's chats. |
| `chats_recent` | true | false | false | Lists recent permitted chats. |
| `contacts_get_batch` | true | false | false | Reads several stored contacts in one call. |
| `contact_get` | true | false | false | Reads one contact and its saved enrichment. |
| `chat_settings_get` | true | false | false | Reads settings for one chat. |
| `chat_settings_list` | true | false | false | Lists saved chat settings. |
| `get_group_invite` | true | false | false | Reads the current invite metadata without changing membership. |
| `media_download` | true | false | true | Reads media already present in the connected account; fetches the file from WhatsApp's media servers. |
| `media_upload` | false | false | false | Returns a one-time private upload URL for a file the user chose to send; sends nothing until `message_send`. |
| `automation_list` | true | false | false | Lists saved Automations. |
| `automation_get` | true | false | false | Reads one saved Automation. |
| `automation_runs` | true | false | false | Reads Automation execution history. |
| `message_send` | false | true | true | Sends text, media, polls, locations, contact cards, events or buttons; text goes through the reply receipt and sends at most once per `request_id`. |
| `react_to_message` | false | false | true | Adds a visible reaction to a WhatsApp message. |
| `mark_read` | false | true | true | Changes shared WhatsApp read state and may emit a read receipt. |
| `mark_unread` | false | false | true | Changes the chat's unread marker in the connected WhatsApp account. |
| `forward_message` | false | true | true | Sends an existing message to another chat. |
| `pin_message` | false | false | true | Changes message state visible in the WhatsApp chat. |
| `edit_message` | false | true | true | Overwrites previously sent content visible to recipients. |
| `delete_message` | false | true | true | Deletes a message and can affect other participants. |
| `pin_chat` | false | false | true | Changes chat-list organization in the connected WhatsApp account. |
| `mute_chat` | false | false | true | Changes notification behavior in the connected WhatsApp account. |
| `archive_chat` | false | false | true | Changes chat-list organization in the connected WhatsApp account. |
| `delete_chat` | false | true | true | Deletes chat history from the connected WhatsApp account. |
| `add_chat_label` | false | false | true | Applies a WhatsApp label to a chat in the connected account. |
| `remove_chat_label` | false | false | true | Removes a WhatsApp label from a chat in the connected account. |
| `add_label` | false | false | true | Creates a WhatsApp Business label in the connected account. |
| `create_group` | false | true | true | Creates a WhatsApp group and adds participants. |
| `group_add` | false | true | true | Adds people to a group and changes their access. |
| `group_remove` | false | true | true | Removes people from a group and changes their access. |
| `group_promote` | false | true | true | Grants group-administrator access. |
| `group_demote` | false | true | true | Removes group-administrator access. |
| `group_settings` | false | true | true | Changes settings shared by group participants. |
| `leave_group` | false | true | true | Removes the connected account from a group. |
| `edit_contact` | false | true | true | Overwrites a contact's name in WhatsApp and, if connected, Google Contacts. |
| `update_contact_metadata` | false | true | false | Overwrites structured private contact metadata. |
| `contact_enrich` | false | true | true | Persists additional facts on a contact, which can sync to Google Contacts. |
| `contact_forget` | false | true | true | Deletes saved enrichment for a contact, which can sync to Google Contacts. |
| `automation_set_enabled` | false | true | true | Activates or disables durable behavior, including scheduled sends. |
| `automation_delete` | false | true | true | Permanently removes durable behavior and stops future external effects. |
| `automation_run_control` | false | true | true | Starts, resumes, pauses, or cancels runs that may have external effects. |

The public plugin intentionally excludes raw database access (`wa_db_query`),
Perisclaw-internal wiki, mission, note and template primitives, and Automation
authoring; it manages existing Automations only. Read-only OAuth connections
receive the same profile without WhatsApp-mutating tools; they keep
`monitor_stop`, which only ends their own ChatGPT subscription.
