---
name: inbox
description: Use when the user wants to check messages across LinkedIn, WhatsApp, Telegram, Instagram, Instagram Business, or Facebook Messenger, find unread conversations or replies they owe on any of these networks, read a conversation, draft replies, start a conversation, or mark chats read. Send only with user approval. This skill handles these networks' direct messages, not email.
---

# Inbox across networks

Read [account access and limits](../../references/account-and-limits.md) before using tools.

## Find conversations needing attention

Call `list_chats` to list conversations from every connected account, Instagram Business included, merged and most recent first. Pass `provider` to stay on one network, or `account` for one account. Start with `unread: true` for unread triage. For replies the user owes, also inspect recent conversations without the unread filter. A read conversation can still need a reply.

Each item has `chat_id`, `account_id`, `provider`, and `person_id` for one-to-one chats. On Facebook, the default listing is the personal Messenger inbox: a Page's inbox (`page_id`) and message requests (`requests: true`) are separate listings, described in [Facebook](../facebook/SKILL.md). Check them too when the user asks for everything waiting. Follow `next_cursor` within the requested scope. The cursor keeps the first page's `limit` and `unread` filter. Pages from several accounts can hold fewer items than `limit` to keep the order. Report `skipped` accounts (signed out or restricted) and `errors` with their next step, and do not claim the whole inbox was checked when accounts were skipped or more pages remain.

Use `get_messages` with the chat's `chat_id` and its `account_id` as `account`. Messages arrive most recent first, and `from` is `me` or `them`. Check who sent the latest message and read the exchange in chronological order. An unread count or snippet alone does not prove the user owes a reply. `get_messages` shows you the page's three most recent images with the result (their attachments say `shown_below: true`); open any other image with `get_attachment` (`chat_id`, `message_id`, `attachment_id`). Videos, voice notes and documents can't be opened by you, but every attachment has a `url` the user can open or download for 24 hours: give it to them when they want the file. Instagram Business and Facebook Pages messages give an image's link instead. On Instagram Business, the first page also returns `reply_window`: check it before drafting, as described in [Instagram Business](../instagram-business/SKILL.md).

Present the network, the person or group name, the latest inbound request, its timestamp, and a suggested next action. Group the summary by network when several are involved. State the number of conversations inspected.

## Draft and send replies

Draft replies from the conversation's facts and the user's requested tone, in the register of that network: chat apps are usually shorter and less formal than LinkedIn. Keep commitments, dates, and claims grounded in the conversation or the user's instructions.

Show the network, the recipient or group, and the exact text before calling `send_message` with `chat_id`, `account`, and `text`. Send only after the user authorizes that reply. If they already approved that exact draft, proceed without another approval request. In a group chat, the reply goes to every member: say so when it matters. To send an image with the message (one per message), add `image_url`, a public `https` link to a JPEG, PNG, or WebP image of at most 8 MB, or `media_id` from `upload_media` for an image on the user's device or attached in the chat, as described in [Getting started](../getting-started/SKILL.md). Show the image with the text before sending.

Instagram Business allows replies only within Instagram's windows: never set `user_written: true` on text the user hasn't written or approved word for word.

Confirm success from the tool result. If the outcome is uncertain, inspect the conversation with a fresh read before retrying.

## Start a conversation

Use `start_chat` with `to`, `text`, and `account` (or `provider` when one account of that network is connected) only when the user asks to message someone they have no conversation with. `to` is a LinkedIn `person_id`, a WhatsApp phone number in international format with its country code, or a Telegram, Instagram, or Facebook user id (a chat's `person_id`, a group member's or friend's `user_id`, or from `get_profile`). Starting chats has a low daily limit, about 10 a day on WhatsApp, Telegram, Instagram, and Facebook. These networks restrict accounts that message strangers, and WhatsApp bans new accounts after two or three cold messages, so only message people who expect it, and show the recipient and exact text first. An Instagram Business account can't start conversations. For LinkedIn InMail, invitations, or batches, use [LinkedIn outreach](../linkedin-outreach/SKILL.md).

## Read state

Reading or summarizing does not authorize `mark_read`. Use it when the user asks to mark a conversation read, or unread with `read: false`, with the chat's `account`.

## Network-specific guidance

The same tools work on every network. For network details, use:

- [LinkedIn inbox](../linkedin-inbox/SKILL.md) for LinkedIn-only triage.
- [WhatsApp, Telegram and Instagram](../whatsapp-telegram-instagram/SKILL.md) for recipients, reactions, profiles, and group members on those networks.
- [Facebook](../facebook/SKILL.md) for Pages, message requests, posts, comments, and friends.
- [Instagram Business](../instagram-business/SKILL.md) for reply windows, comments, private replies, and insights.

To act on new messages as they arrive instead of checking on request ("when a message comes in from X, draft a reply"), use [Automations](../automations/SKILL.md).
