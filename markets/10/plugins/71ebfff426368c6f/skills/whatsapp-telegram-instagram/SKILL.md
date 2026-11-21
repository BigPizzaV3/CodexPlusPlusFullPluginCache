---
name: whatsapp-telegram-instagram
description: Use when the user wants to work on WhatsApp, Telegram, or Instagram specifically - read or reply to chats, message a phone number or user, react to a message, look up a contact's profile, list a group's members, or list an Instagram account's posts. Sends and reactions require user approval. For publishing posts use the social-publishing skill; for an Instagram Business account's messages, comments, and insights use the instagram-business skill.
---

# WhatsApp, Telegram and Instagram

Read [account access and limits](../../references/account-and-limits.md) before using tools. These networks use the same tools as every other network; the account says which one. If `list_accounts` shows no account of the network, connect it as described in [Getting started](../getting-started/SKILL.md).

## Chats

Use `list_chats` with `provider` (`whatsapp`, `telegram`, or `instagram`) to merge every account of that network, or `account` for one account. Each item carries its `account_id`: pass it as `account` to `get_messages`, `send_message`, `mark_read`, `react`, and `list_group_members` for that chat. Follow [Inbox](../inbox/SKILL.md) for triage, reading order, drafting, and reply approval.

Show the recipient or group and the exact text before any send. In a group, a message reaches every member. For Facebook Messenger and Pages, use [Facebook](../facebook/SKILL.md). For an Instagram Business account (provider `instagrambusiness`), use [Instagram Business](../instagram-business/SKILL.md).

## Start a conversation

Use `start_chat` with `to`, `text`, and the `account` (or `provider` when one account of that network is connected):

- WhatsApp: `to` is a phone number in international format with its country code, like `+33 6 12 34 56 78`. The tool refuses numbers that may lack a country code: ask the user rather than guessing one. WhatsApp bans accounts that send cold messages, and new accounts after two or three. Only message people who expect it, and never send the same message to many numbers.
- Telegram: `to` is the numeric user id from a chat's `person_id` or from `list_group_members`. Usernames are not accepted here.
- Instagram: `to` is the user id from a chat's `person_id` or `get_profile`. Messages to people who don't follow the account land in their message requests.

New conversations have a low daily limit on these networks, about 10 a day. Check `account_status` before planning several, and never spread messages across accounts to get around a limit. These networks have no scheduled batch tool.

## Reactions

Use `react` with `chat_id`, `message_id` from `get_messages`, `reaction` (one emoji), and `account`. The recipient sees reactions, so react only when the user asks for it. A new reaction replaces the account's previous one on that message. Telegram accepts only its standard reaction emojis (👍 ❤️ 🔥 🎉 😁 👏 and similar). If a reaction is refused, report it rather than trying other emojis on your own.

## Profiles

Use `get_profile` with the `account` (or `provider`) and `user_id`: on WhatsApp a WhatsApp id (a chat's `person_id`, `<digits>@s.whatsapp.net`) or a phone number with its country code, on Telegram a user id, on Instagram a user id or username. Each lookup counts as a profile view. Fields depend on the network and the person's privacy settings: report missing ones as unknown.

## Group members

Use `list_group_members` with a WhatsApp or Telegram group `chat_id` and its `account`, and follow `next_cursor` when the user needs everyone. Members come with their `user_id`, name, and on WhatsApp their phone number. Group membership is not consent to be contacted: do not start chats with members unless the user names them and confirms.

## Instagram posts

`list_posts` with an Instagram `account` lists the account's own posts by default, or another user's with `user_id` (a user id or username). Report captions, dates, likes, and comments as returned.

To publish or schedule a photo post, use `create_post` as described in [Social publishing](../social-publishing/SKILL.md). An Instagram account connected with its login posts one photo (required) with a caption of up to 2200 characters. The post is public and cannot be edited or deleted through this plugin.
