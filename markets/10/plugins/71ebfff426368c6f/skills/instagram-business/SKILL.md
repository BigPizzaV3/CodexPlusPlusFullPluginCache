---
name: instagram-business
description: Use when the user wants to work on an Instagram Business or Creator account connected through Instagram's official access - answer its direct messages within Instagram's reply windows, read, reply to, hide, or delete comments on its posts, reply privately to a commenter, or report its insights (reach, followers, audience, a post's performance). Messages, comments, private replies, and moderation require user approval.
---

# Instagram Business

Read [account access and limits](../../references/account-and-limits.md) before using tools. This skill is for an account with provider `instagrambusiness` in `list_accounts`. An Instagram account connected with its login (provider `instagram`) is covered by [WhatsApp, Telegram and Instagram](../whatsapp-telegram-instagram/SKILL.md). If both are connected, pass the `account` of the right one to every tool.

An Instagram Business account can't start a conversation or look up other people's profiles or posts. To start conversations, the same account can also be connected with its login, as described in [Getting started](../getting-started/SKILL.md).

## Direct messages

Use `list_chats` (it includes Instagram Business, or pass `provider: "instagrambusiness"`), `get_messages`, `send_message`, `mark_read`, and `react` with the chat's `account_id` as `account`. Follow [Inbox](../inbox/SKILL.md) for triage, reading order, drafting, and reply approval. Conversations can't be marked unread.

Instagram lets the account answer only people who wrote to it:

- Within 24 hours of the person's last message, any approved reply can go out: text up to 1000 characters, optionally with one JPEG or PNG image.
- From 24 hours up to 7 days after it, only a reply the user wrote or approved word for word, sent with `user_written: true`. Never set `user_written` on text you wrote on your own or that the user hasn't approved word for word.
- After 7 days, no reply can go out.

`get_messages` without a cursor returns `reply_window`: `open`, `user_written_only`, or `closed`. Check it before drafting and tell the user which window applies. When it is `closed`, say so instead of drafting a reply that cannot be sent.

`react` works within 24 hours of the person's last message, and `remove: true` takes the account's reaction back. React only when the user asks.

## Comments

`list_posts` with the account lists its own posts, Reels, and carousels, at most the 25 most recent, including ones made outside Pluggzy, with their `post_id` and like and comment counts. `list_comments` lists a post's comments, most recent first, or with `comment_id` the replies to one comment. Hidden comments show `hidden: true`, and new comments can take 10 minutes to appear.

`comment` with the `post_id` comments on one of the account's own posts, or answers a comment with `reply_to`: text only, with `@username` mentions. Comments are public: show the post, the comment being answered, and the exact text before commenting.

`private_reply` sends a direct message to the author of a comment, the way to answer a commenter who never messaged the account. Instagram allows one per comment, within 7 days of the comment, and a failed try can use it up: show the exact text first, and don't retry on your own after a failure or an uncertain result. The person's answers arrive in `list_chats`.

`moderate_comment` takes the `post_id`, `comment_id`, and `action`: `hide` (only its author and the account still see it, and the author isn't told), `unhide`, or `delete` (removed for good, whether it is someone else's comment or the account's own). Hiding is the gentler choice: suggest it first. Confirm the exact comment and action with the user before moderating; deleting cannot be undone.

## Insights

`instagrambusiness_get_insights` reports the account as Instagram does, with figures that can lag up to 48 hours. `report` is:

- `overview` (the default): reach, views, accounts engaged, interactions, likes, comments, saves, shares, follows, profile views, and link taps over the last `days`.
- `followers`: the follower count day by day, with followers gained and lost, at most 89 `days`.
- `audience`: followers by age, city, country, and gender. It needs 100 or more followers.
- `post`: one post's reach, views, likes, comments, shares, and saves, with its `post_id` from `list_posts`.

Report a metric listed in `unavailable` as unknown, never as zero. State the period the figures cover.

## Posts

To publish a feed post, a carousel, a Reel, or a Story, use `create_post` with the Instagram Business account, as described in [Social publishing](../social-publishing/SKILL.md).
