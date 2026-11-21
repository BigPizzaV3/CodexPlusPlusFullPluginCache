---
name: saleslumen-emails
description: >-
  Manage Saleslumen email via MCP: messages, threads, drafts, labels, accounts,
  and address discovery. Use when the user wants to read, send, draft, trash,
  label, or find email in Saleslumen. Do not use for campaigns, workflows, or
  Apps Script.
---

# Saleslumen Emails

Use the Saleslumen MCP connector for mailbox work. Keep the conversation natural; call tools to act.

## Concepts

Tool arguments are snake_case. Fields inside a message, draft, or label object stay Emails JSON: `accountId`, `threadId`, `labelIds`, `payload`, `raw`, and `scheduleTime`.

A thread is a conversation. A draft wraps an unsent message. Labels categorize messages and threads.

An account is an org mailbox. `emails_list_accounts` tells you which mailboxes exist. Put the chosen account id in the message `accountId`.

`emails_discover` takes `domain` and `name`. Report what the tool returns; do not invent addresses.

## Workflow

1. Clarify the goal (read, reply, draft, send, label, trash, discover, or account lookup).
2. Resolve identifiers with list/get before you change anything. Filter lists with `account_ids`, `query`, or `label_ids`.
3. For replies and forwards, call `emails_generate_quoted_content` with `reply_to_message_id` and `quote_type` (`reply` or `forward`), then draft or send.
4. When composing, pass a `message` object and a `request_id` UUID. Inside the message set `accountId`, and `payload` or `raw`. Set `scheduleTime` (epoch milliseconds) on that message only if the user asks to schedule. `emails_send_draft` takes the same `request_id`. Reuse it on a retry.
5. Confirm with the user before send and before permanent delete.
6. Summarize the result in plain language.

## Tools

| Task | Tools |
| --- | --- |
| Messages | `emails_list_messages`, `emails_get_message`, `emails_get_attachment` |
| Send | `emails_send_message`, `emails_generate_quoted_content` |
| Message lifecycle | `emails_trash_message`, `emails_untrash_message`, `emails_delete_message`, `emails_modify_message` |
| Threads | `emails_list_threads`, `emails_get_thread`, `emails_trash_thread`, `emails_untrash_thread`, `emails_modify_thread`, `emails_delete_thread` |
| Labels | `emails_list_labels`, `emails_get_label`, `emails_create_label`, `emails_update_label`, `emails_delete_label` |
| Drafts | `emails_list_drafts`, `emails_get_draft`, `emails_create_draft`, `emails_update_draft`, `emails_send_draft`, `emails_delete_draft` |
| Accounts | `emails_list_accounts`, `emails_get_account`, `emails_create_account`, `emails_update_account`, `emails_delete_account` |
| Discovery | `emails_discover` |

## Guidance

- `emails_update_label` renames a label. There is no separate patch tool.
- Prefer trash over permanent delete unless the user asks to purge.
- Stay in the Emails tools for this skill.
