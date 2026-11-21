---
name: getting-started
description: Use when the user sets up Pluggzy or asks what is connected - list connected accounts and what each can do, check an account's status and limits, understand what to do when a network is not connected or a plan is blocked, or upload an image or video for a post or message. Never ask for passwords or codes in chat.
---

# Getting started

Read [account access and limits](../../references/account-and-limits.md) before using tools.

## See what is connected

Call `list_accounts`. Report each account's network, name, and `status`, and what its `can` list says it can do. If the result says `limited_to_one`, this connection can use only one account: explain that this must be resolved in the user's existing Pluggzy account outside ChatGPT.

Instagram connects two ways. An `instagram` account uses its login: all its DMs, starting conversations, profiles, and photo posts. An `instagrambusiness` account is a Business or Creator account on Instagram's official access: replies within Instagram's windows, comments, insights, and posts, Reels, carousels, and Stories. The same account can be connected both ways.

## Missing, signed-out, or blocked accounts

This plugin requires an existing Pluggzy account with the social accounts already connected. When the requested network has no connected account, an account is signed out, or the plan is blocked, explain that the user must connect, reconnect, or manage the plan in their existing Pluggzy account outside ChatGPT. Do not offer onboarding, a trial, an upgrade, checkout, or billing management, and do not invent a link. Never ask for passwords, codes, QR codes, recovery codes, or PINs in chat.

## Check status and limits

Call `account_status` with the `account` before planning several actions on one account, and report `blocked_reason`, the remaining allowances, and `ready_in_seconds` for the actions the user plans.

## Upload an image or video

Files attached in the chat can't reach Pluggzy. When the user wants a photo or video in a post, comment, or message and it isn't already at a public `https` link, call `upload_media`: give the user its link, wait until they say the file is uploaded, then pass its `media_id` (`media_ids` on `create_post`, `media_id` on `send_message`, `start_chat`, and `comment`). If you made the file yourself and can run commands with internet access (a code sandbox, a terminal), upload it yourself with the `upload_command` it returns, and use the `media_id` once it answers `ok`.

Each link takes one file: call `upload_media` again for each image of a carousel. Images are JPEG, PNG, or WebP, at most 8 MB. Videos are MP4, MOV, or WebM, at most 5 GB on the upload page (100 MB through `upload_command`), and go only in posts on publishing accounts; messages, comments, and LinkedIn, Instagram, and Facebook posts take images. An upload can be used for 24 hours, in as many posts as needed, and a scheduled post keeps its own copy until it goes out.

## Where to go next

- Messages across networks: [Inbox](../inbox/SKILL.md).
- Posts and the post calendar: [Social publishing](../social-publishing/SKILL.md).
- LinkedIn: [LinkedIn inbox](../linkedin-inbox/SKILL.md), [LinkedIn research](../linkedin-research/SKILL.md), [LinkedIn outreach](../linkedin-outreach/SKILL.md).
- [WhatsApp, Telegram and Instagram](../whatsapp-telegram-instagram/SKILL.md), [Facebook](../facebook/SKILL.md), [Instagram Business](../instagram-business/SKILL.md).
