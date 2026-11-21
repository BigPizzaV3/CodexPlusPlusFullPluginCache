---
name: send-whatsapp-message
description: Send a WhatsApp message, photo or document to a person or group, forward a message, or edit or delete a sent message, after the user confirms the exact action.
---

# Send a WhatsApp message

Sending reaches real people and cannot reliably be recalled. Confirm before every send, forward, edit, deletion or group change.

## Find the recipient

- Replying in an existing chat: pass its exact `conversationId` from `list_conversations`, `search_messages` or `list_unanswered_conversations`. This picks the right number for you.
- Someone named by the user: find them with `list_contacts`. If several people match, ask which one.
- A number the user typed: send it with the country code (for example +44 7700 900123). If the country is unclear, ask. Do not guess a country code.
- A group: find it with `list_groups` and send with `send_group_message`, passing its exact group ID as `jid`. `send_message` is for one person only. All group members may receive the message, so show the group name when confirming. If no group tools are available, make a draft link with `create_message_draft`.

Confirm which account sends. Use `list_connections` if it is unclear whether the personal (QR) number or the Business number is ready. For `send_message`, pass `channel` when both are connected, and `fromNumber` when the user picks one of several linked numbers. Never switch accounts after a failure without asking.

## Confirm, then send once

1. Show the sending account, the recipient (name and number) and the exact text. Wait for a clear yes.
2. Call the tool once with a new `idempotencyKey` (8 to 128 letters, digits, dots, colons, underscores or hyphens). Never reuse a key with different content or a different recipient. Do not retry an uncertain result on your own; if a retry is clearly safe, keep the original key and exactly the same details.
3. One yes covers one message. For several people, confirm each message separately. Never loop through a list.

## Draft links: the user sends it themselves

`create_message_draft` makes a WhatsApp link with the message filled in. Nothing is sent: the user opens the link and taps Send in their own WhatsApp. Use it when the user wants to send it themselves.

`send_message` and the photo, document, location, contact and poll tools also return a draft (`status: "draft_ready"`, `draft_link`) instead of sending when sending is turned off for the number, or when the number reached today's limit for people it never chatted with. Show `draft_link` as a link and say it was not sent. Never retry a draft as a send. A group draft opens WhatsApp's chat picker, so tell the user to pick the group. Links cannot carry files, so a file goes as its link.

## Read the result

- Accepted is not delivered. For `send_message`, check an unclear result with `get_send_status`, passing the returned `intent_id` as `intentId`. Group sends, photo and document sends, forwards, edits and deletions return an `operation_id`; check those with `get_operation` (`operationId`). Completed does not prove delivery. If there is no ID, report the uncertainty; never resend to be safe.
- Same message to the same person (or group) within an hour: WhatSync refuses it as a duplicate. Pass on what the error says: it either already went, or WhatsApp has not confirmed the earlier one arrived (then say it may have gone and suggest checking the chat). Do not change the wording to get around it.
- Daily limit reached: tell the user the limit and that it resets at midnight UTC (give that in their local time), then stop.
- Too many requests: wait for the returned `retry_after` before the next send. Do not loop, change keys or switch accounts to get around it.
- Recipient not on WhatsApp: tell the user and ask them to check the number.
- WhatsApp not ready: stop sending and tell the user which connection is not ready. Say "not sent" only when the tool rejected the send before trying; otherwise say the outcome is uncertain. Saved messages can usually still be read.
- Access ended: tell the user once, give the dashboard link from the result if there is one, and stop.

## Photos, documents and existing messages (personal number only)

Use these only when the tools are available:

- `send_image`: `phoneNumber` (country code, digits only), a public `https` `url`, optional `caption`.
- `send_document`: the same, plus a required `fileName` and optional `mimeType`.
- `forward_message`: the exact `sourceMessageId` and the destination `phoneNumber`. Confirm what is being forwarded and to whom.
- `edit_message`: the exact `targetMessageId` and the new `text`.
- `delete_message`: the exact `targetMessageId`; confirm it deletes the message for everyone.

Read the exact message first. Forwarding, editing and deleting work only on saved one-to-one messages on the personal number, and editing and deleting only on messages the user sent. Do not promise an edit will succeed. Confirm the exact file and caption before sending, and never upload a private file somewhere public just to get a link.

## Business numbers

For a Business number, call `check_recipient_send_options` for the exact recipient. A free-form reply needs a message from that customer within the last 24 hours. Otherwise use an approved template: find it with `list_business_templates` (`status: "APPROVED"`) and check its name and language with `get_business_template`. Confirm that the recipient agreed to receive messages and the exact filled-in text, then send with `templateName`, `templateLanguage`, `templateParameters` in order and `recipientOptInConfirmed: true`, without `text`. Templates with media headers or buttons that need a value are not supported. Use `expectedPreview` only when copied from a previous WhatSync result.
