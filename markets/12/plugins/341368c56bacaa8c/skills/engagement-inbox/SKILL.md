---
name: engagement-inbox
description: Work through social media engagement with Postproxy - find comments, direct messages, and Google Business reviews that are waiting for a reply, read them in context, and send replies the user approves. Use when the user asks what needs a reply, wants to answer comments or DMs, or wants to respond to reviews.
---

# Engagement inbox

Help the user see what is waiting on them and reply, one approved message at a time.

## 1. Find what needs attention

Start with `summary_get` (default 24h window, or the window the user asks for). Its `awaiting_reply` section counts comments, reviews, and chats with no reply from the user over the last 30 days, regardless of the window. Present those counts by network, and flag chats close to the end of their 24-hour messaging window first. Then open the specific items with the tools below (use `history_list` to find recent posts whose comments to check).

## 2. Read in context

- Post comments: `comments_list` with the post ID and profile ID. Not every network supports comments. Comment tools work on Instagram, Facebook, Threads, YouTube, and LinkedIn.
- Google Business reviews: `profile_comments_list` with the Google Business profile ID (and `placement_id` for one location). Reviews sync twice a day, so a very recent review may not appear yet.
- Direct messages: `dm_chats_list` for the profile, then `dm_messages_list` for a chat. DMs work on Facebook, Instagram, Telegram, Bluesky, and WhatsApp.

## 3. Draft and confirm replies

- Draft a reply that matches the brand's tone and answers what was actually asked. Don't promise refunds, discounts, or policies the user hasn't stated.
- Show the draft and send it only after the user approves it. Every reply is posted publicly or delivered to a real person.
- Comment or review reply: `comments_create` with `parent_id` set to the comment, or `profile_comments_create` for a review.
- Direct message: `dm_message_send` with `chat_id` and `body`.

## Messaging window rules

- Facebook and Instagram: free-form replies are allowed within 24 hours of the person's last message. After that, `tag: "HUMAN_AGENT"` is allowed only when a person is replying to that customer's own question. Never use it for promotional or automated messages.
- WhatsApp: outside the 24-hour window, only an approved template (`whatsapp_templates_list`, then `template` in `dm_message_send`) can reopen the conversation. Explain this instead of retrying a free-form message that fails.

## Moderation

`comments_hide` and `comments_delete` affect what the public sees. Confirm before using them and prefer hiding over deleting unless the user asks to delete.
