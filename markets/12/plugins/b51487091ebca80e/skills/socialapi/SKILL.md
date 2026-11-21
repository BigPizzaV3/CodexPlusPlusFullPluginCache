---
name: socialapi
description: Operates the SocialAPI MCP tools (social_api_*) to read and answer comments, DMs, reviews and mentions, and to draft, validate, schedule and publish posts across Instagram, Facebook, Threads, TikTok, X, YouTube, LinkedIn, Google Business Profile, Pinterest, WhatsApp, Telegram, Zalo and Bluesky. Use when the user asks what came into their social inbox, which comments, DMs or reviews still need a reply, wants to answer one, check mentions, write, check or schedule a post, look at post or account analytics, set up comment or DM Automations, manage brands and connected accounts, or debug webhook deliveries.
---

# SocialAPI

Every tool name starts with `social_api_`. The short names below drop that prefix.

## First call: list_accounts

`list_accounts` returns each connected account: `id` (the `account_id` almost every other tool needs), `platform`, `username`, `brand_id`, `status`. Never guess an id or reuse one from an earlier conversation.

- **No accounts**: say plainly that no social account is connected yet, so there is nothing to read, and offer `connect_account`. Never invent comments, messages, reviews or posts.
- **`status` other than `active`**: that account needs reconnecting before anything works on it. Say so and offer `connect_account` for its platform.
- `connect_account` returns an `auth_url` for the user to open. The account connects by itself once they approve, no further call needed.
- Several businesses or clients: `list_brands`, then pass `brand_id` to `list_accounts`, `list_inbox_posts`, `list_conversations` and `list_posts`.

## What came in, and what still needs a reply

Turn the user's window ("overnight", "today") into an RFC3339 start time such as `2026-10-12T18:00:00Z`, and compare it with each comment's or message's own timestamp.

Comments:
1. `list_inbox_posts` with `min_comments: 1` and `limit: 100` (add `account_id` or `platform` to narrow it). It returns the most recently published posts that have comments. Do not pass `since` here: it filters on the post's publish date, so it would hide new comments on older posts. Each post `id` is a platform post id.
2. For each post, `list_post_comments` with `inbox_post_id` (that `id`) and `account_id`. The order depends on the platform, so follow `next_cursor` until it is empty and filter on `created_at`.
3. Keep comments with `created_at` inside the window and `is_owner: false`. `has_replies: false` means nobody has answered. When `has_replies` is true, a reply row (`parent_id` set to that comment) or `get_comment_replies` shows whether one of the replies is the account's own (`Author.IsOwner`).

DMs:
1. `list_conversations` lists the most recently active first. Stop paging once `last_message_at` is before the window.
2. A conversation needs a reply when its newest message is from the other person: `list_messages` returns newest first, so check the first message's `direction` (`incoming` or `outgoing`). `unread_count` above 0 is a quick hint.

Report by account, quote what people wrote, and draft replies. Send nothing until the user approves a specific text.

## Reviews

1. `list_review_accounts` (optionally `platform: google`). Use the accounts whose `Status` is `ok`. This tool and the review tools return capitalised keys: `AccountID`, `Name`, `Status`, `Summary`.
2. `get_reviews` with `account_id` set to that `AccountID` and `order: newest`. Each review has `ID`, `Rating`, `Text`, `Author`, `CreatedAt` and `Reply`, which is null when the business has not answered.
3. Draft each answer in the chat. Call `reply_to_review` (`account_id`, `review_id` set to the review `ID`, `text` up to 2200 characters) only for the replies the user approves. Google may return `state: PENDING` while it checks the reply: that is a success.

A Google review has one business reply, so calling `reply_to_review` again replaces it (and costs another credit). A reply cannot be deleted through these tools.

## Drafting and checking a post

1. `list_accounts` to find the account for each platform the user named.
2. `validate_post` with `account_ids` (preferred over `platforms`: it runs each account's own checks), `text`, any `media`, and the same `platform_data` you would publish with. Instagram needs `{"instagram": {"content_type": "feed"}}`, or `reel`, `stories` or `carousel`.
3. Report `errors` (blocking) and `warnings` (advisory), each with its `platform`, `field` and `message`. `get_constraints` gives the raw limits (text length, media count, file types and sizes) when the user asks for them.
4. Instagram cannot publish text alone: every Instagram post needs an image or video, and `validate_post` does not flag a missing one. When the user gave no media, say an image or video is needed for Instagram before anything is published.
5. Save or publish only when asked: `create_post` (see Publishing).

## Publishing

- `create_post` always takes `text` and one entry in `targets` per account, with `page_id` for a specific Facebook Page and `board_id` on every Pinterest target (`list_pinterest_boards` gives the board ids). `publish_now: true` publishes, `scheduled_at` (RFC3339) schedules, neither saves a free draft. `publish_post` publishes a draft later.
- Publishing finishes in the background: the call returns status `publishing`. Check `get_post` until it reads `published`, `partial` or `failed` before saying it worked. `retry_post` resends the failed targets of a `failed` or `partial` post.
- Media: a public file goes in as `{"source_type": "url", "source": "https://..."}`. `get_media_upload_url` returns an address that only accepts the file's bytes by HTTP PUT within 15 minutes, which a chat cannot send. Use it only when you can run HTTP requests yourself, then `verify_media_upload` and pass `{"source_type": "media_id", "source": "<media_id>"}`. Otherwise ask the user for a public link.
- Figures: `get_post_metrics` for a post's current numbers, `get_post_analytics`, `get_account_analytics` and `get_brand_analytics` for daily history.

## Credits

One interaction credit: `reply_to_comment`, `send_dm`, `reply_to_review`, `reply_to_mention`. One post credit: `create_post` when it publishes or schedules, `publish_post`, `retry_post`. Everything else is free, including drafts, reads, `private_reply_to_comment`, hiding, liking and deleting comments, and managing Automations. The free plan allows 10 posts and 50 interactions a month, paid plans are unlimited. `get_usage` shows what is left, where -1 means unlimited.

## Confirm first

- Anything public or that reaches a person: show the exact text and wait for a yes before `reply_to_comment`, `private_reply_to_comment`, `send_dm`, `reply_to_review`, `reply_to_mention`, `create_post` with `publish_now` or `scheduled_at`, `publish_post`, and `create_automation`.
- Irreversible: `delete_comment`, `delete_post`, `unpublish_post`, `delete_media`, `delete_brand` (disconnects all its accounts), `disconnect_account`, `delete_automation`, `delete_webhook`, `revoke_key`, `revoke_invite`. Name what disappears and wait for a yes.

## When a tool returns an error

A failed call returns `{"error": "...", "code": "..."}` with extra fields, or a plain sentence. Read it out rather than guessing.

| `code` | Meaning and what to do |
|---|---|
| `resource.not_supported`, or the sentence "Operation not supported for this platform" | The platform cannot do this. Do not retry. Say which platform, and check [references/platforms.md](references/platforms.md) for one that can. |
| `billing.platform_not_available` | That platform or account type is not open to this account. |
| `account.reconnection_required`, `platform.<name>.auth`, `platform.<name>.insufficient_scope` | The account must be reconnected: `connect_account`. |
| `platform.<name>.window_closed` | Instagram and Facebook only accept a DM within 24 hours of the person's last message. On Instagram, `message_tag: HUMAN_AGENT` extends that to 7 days; otherwise say the window has closed. |
| `platform.<name>.private_reply_ineligible` | A private reply was already sent for that comment, or the comment is older than 7 days. |
| `validation.post_limit_exhausted`, `validation.interaction_limit_exhausted` | Monthly plan limit reached. `get_usage` shows when it resets. |
| `ratelimit.exceeded`, `publishing.velocity_limit`, `messaging.velocity_limit`, `platform.<name>.rate_limit`, `platform.<name>.throttled` | Too many calls. Wait `retry_after_seconds` when present, then retry once. |
| `validation.*` | A field is wrong: the message and `field` say which. When `create_post` refuses a post, `issues` lists each problem with its platform and field. |

For anything unexplained, `list_events` filtered by `account_id` or `resource_id` shows what the platform answered.

References: [references/tools.md](references/tools.md) (every tool, ids, pagination, response shapes, Automations, webhooks) and [references/platforms.md](references/platforms.md) (what each platform supports).
