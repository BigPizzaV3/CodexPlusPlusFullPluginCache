---
name: inbox-triage
description: Triage the social inbox with the SocialAPI app. Collect new comments, DMs, Google reviews and mentions across every connected account, rank what still needs a reply, draft answers in the brand's voice, and send only the replies the user approves. Use when the user says "what came in", "what needs a reply", "check my inbox", "answer my comments", "reply to my reviews", "any new DMs", "overnight", "today's messages", "clear my inbox", or asks for customer replies on social media.
---

# Inbox triage

Requires the SocialAPI app in ChatGPT. Every tool name starts with `social_api_`. The `socialapi` skill holds the parameters, ids, pagination rules, platform support and error codes: follow it for every call.

## 1. Set the scope

- Turn the user's window into an RFC3339 start time. With no window given, use the last 24 hours and say so.
- `list_accounts`. No account: say nothing is connected, offer `connect_account`, and stop. An account whose `status` is not `active` goes in the report as "needs reconnecting" and is skipped.
- Several brands: cover all of them, grouped by brand, unless the user named one.

## 2. Collect

Follow the `socialapi` skill's "What came in, and what still needs a reply" and "Reviews" sections:

- Comments: `list_inbox_posts` with `min_comments: 1`, then `list_post_comments` per post, filtered on `created_at` and `is_owner: false`.
- DMs: `list_conversations`, then `list_messages`. A conversation needs a reply when its newest message is `incoming`.
- Reviews: `list_review_accounts`, then `get_reviews` with `order: newest`. `Reply: null` means unanswered.
- Mentions: `get_mentions` with `since` on Instagram, Facebook, Threads, Bluesky and X.

Skip platforms that have no comments or DMs (see the platform table in the `socialapi` skill) without reporting them as errors.

## 3. Rank

Sort every item that needs a reply into one of three groups:

1. **Reply now**: complaints, 1 or 2 star reviews, order, booking or payment problems, and Instagram, Facebook or WhatsApp DMs whose last incoming message is more than 20 hours old (those platforms refuse a reply 24 hours after the person's last message; on Instagram, `message_tag: HUMAN_AGENT` extends that to 7 days).
2. **Needs a reply**: questions, unanswered positive reviews, leads asking about price or availability.
3. **No reply needed**: praise with no question, emoji-only comments, and spam (offer to hide spam, which is free).

## 4. Report

Start with the totals per group, then one table per account: platform, who, what they wrote (quoted), when, group, and a draft reply. Never invent an item: an empty inbox is a valid answer.

## 5. Draft and send

- Write in the account's voice. When unsure, read the account's own earlier replies (comments with `is_owner: true`, `outgoing` messages) and match them.
- Never promise a refund, discount, date or fact the user has not given. Leave a `[placeholder]` instead and point it out.
- Limits: comment and review replies up to 2200 characters, DMs and private replies up to 1000.
- Send nothing until the user approves a specific text. Then send each approved reply with its own call (`reply_to_comment`, `send_dm`, `reply_to_review`, `reply_to_mention`). Each costs 1 interaction credit, a private reply is free. Before sending many, check `get_usage`.
- Afterwards, list what was sent and what failed, with the meaning of each error code.
