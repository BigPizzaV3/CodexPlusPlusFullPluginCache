---
name: linkedin-inbox
description: Use when the user wants to check their LinkedIn inbox specifically, read LinkedIn messages or conversations, find unread LinkedIn messages or replies they owe, and draft responses. Send replies only with user approval. For WhatsApp, Telegram, Instagram, Facebook, or several networks at once, use the inbox skill. This skill handles LinkedIn messaging, not email inboxes.
---

# LinkedIn inbox

Read [account access and limits](../../references/account-and-limits.md) before using tools.

## Find conversations needing attention

Use `list_chats` with `provider: "linkedin"` and follow `next_cursor` within the requested scope. With several LinkedIn accounts, it lists them all merged, most recent first, and each item carries its `account_id`. Pass `account` instead to read one account only. Start with `unread: true` for unread-message triage. For conversations waiting for a reply, also inspect recent conversations without the unread filter. A read conversation can still need a reply.

Use `get_messages` for relevant `chat_id` values, with the chat's `account_id` as `account` when several accounts are connected. Messages arrive most recent first. Check who sent the latest message and interpret the exchange in chronological order. An unread count or chat snippet alone does not prove that the user owes a reply. `get_messages` shows you the page's three most recent images with the result (their attachments say `shown_below: true`); open any other image with `get_attachment` (`chat_id`, `message_id`, `attachment_id`). Videos, voice notes and documents can't be opened by you, but every attachment has a `url` the user can open or download for 24 hours: give it to them when they want the file.

Present the person or conversation name, the latest inbound request, its timestamp, and a suggested next action. State the number of conversations inspected and whether more pages remain. Report accounts listed in `skipped` or `errors` with their next step. Do not claim to have checked the entire inbox after one page.

## Draft and send replies

Draft replies using the conversation's facts and the user's requested tone. Keep commitments, dates, and claims grounded in the conversation or the user's instructions.

Show the recipient and exact text before calling `send_message` with `chat_id`, `text`, and the chat's `account`. Send only after the user authorizes that reply. If they already approved that exact draft, proceed without another approval request. To send an image with the message (one per message), add `image_url`, a public `https` link to a JPEG, PNG, or WebP image of at most 8 MB, or `media_id` from `upload_media` for an image on the user's device or attached in the chat, as described in [Getting started](../getting-started/SKILL.md). Show the image with the text before sending.

Confirm success from the tool result. If the outcome is uncertain, inspect the conversation with a fresh read before retrying. Reading or summarizing does not authorize `mark_read`; use it when the user asks to mark the conversation read or unread.

For several approved replies, use [LinkedIn outreach](../linkedin-outreach/SKILL.md) to schedule the batch. For other networks or a combined inbox, use [Inbox](../inbox/SKILL.md).
