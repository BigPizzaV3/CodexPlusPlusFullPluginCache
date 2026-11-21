---
name: facebook
description: Use when the user wants to work on Facebook specifically - read or reply to Messenger chats or a Facebook Page's inbox, handle message requests, list, publish, schedule, edit, or share posts as the profile or a Page, read or write comments, react to posts, or manage friends, friend requests, and follows. Sends, comments, reactions, posts, and friend requests require user approval.
---

# Facebook

Read [account access and limits](../../references/account-and-limits.md) before using tools. If `list_accounts` shows no Facebook account, connect one as described in [Getting started](../getting-started/SKILL.md).

Every tool below takes an optional `account`. A listed chat carries its `account_id`: pass it as `account` to the other tools for that chat, and use the same account for a post's comments and reactions.

## Messenger

The personal Messenger inbox uses the same tools as the other networks: `list_chats` with `provider: "facebook"` (every Facebook account merged unless `account` is given), `get_messages`, `send_message`, `mark_read`, and `start_chat`. This default listing doesn't include the inboxes of the user's Pages or message requests: check those separately when the user asks for everything waiting on Facebook. Follow [Inbox](../inbox/SKILL.md) for triage, reading order, drafting, and reply approval.

Personal chats are end-to-end encrypted. If the user skipped unlocking their Messenger history when connecting, older messages are missing and a thread can seem to start midway: say so rather than inferring what came before. New messages come through either way.

Show the recipient or group and the exact text before any send. In a group, a message reaches every member.

To message someone with no conversation yet, use `start_chat` with the Facebook account and, as `to`, the user id from a chat's `person_id`, `facebook_list_friends`, or `get_profile`. It always sends from the personal profile. Messages to people who aren't friends land in their message requests, and Facebook restricts accounts that message strangers, so only message people who expect it. New conversations have a low daily limit: check `account_status` before planning several, and never spread messages across accounts to get around it. Facebook has no scheduled batch tool.

`react` adds an emoji reaction to a Messenger message (`chat_id`, `message_id` from `get_messages`, `reaction`). For posts and comments, use `facebook_react_post`. `get_profile` with the Facebook account takes a Facebook id or vanity name (the part after `facebook.com/`) of a person or Page as `user_id`, or `me`, and counts as a profile view. `list_group_members` lists a group chat's members with their `user_id`. Group membership is not consent to be contacted: do not start chats with members unless the user names them and confirms.

## Pages

A Page is not an account of its own: it comes with the Facebook account that manages it. `facebook_list_pages` returns the Pages activated when the account connected, with their `page_id`. A Page missing there was not activated: reconnecting the Facebook account, as described in [Getting started](../getting-started/SKILL.md), offers every Page again.

`list_chats` with a `page_id` lists the Page's Messenger conversations, with `unread: true` for triage and `next_cursor` for more. Their `chat_id` values start with `PAGE_<page_id>_`: `get_messages`, `send_message`, and `mark_read` on them read and answer as the Page, and `from: "me"` is the Page. A Page can only answer: it cannot start a conversation.

Pass `as_page` with a `page_id` to post, comment, or react as that Page instead of the personal profile. Before any reply, post, comment, or reaction, say whether it goes out as the user's profile or as which Page, and get approval for that identity.

## Message requests

`list_chats` with the Facebook account and `requests: true` lists conversations started by people the account isn't friends with. Read them with `get_messages`. `accept_message_request` moves one to the main inbox, and the sender sees that it was accepted: use it only when the user asks.

## Posts

`list_posts` with the Facebook account lists its own posts by default, a Page's with its `page_id` as `user_id`, or anyone's by Facebook id or vanity name. Facebook returns at most 3 posts a page: follow `next_cursor` when the user needs more, and do not present one page as the whole feed. Report text, dates, likes, comments, and shares as returned.

`create_post` with the Facebook account publishes `text` (up to 10000 characters), optionally with one image as `image_urls` or `media_ids` (see [Social publishing](../social-publishing/SKILL.md) for uploads and scheduling). `visibility` is `anyone` (public, the default) or `relations_only` (friends). A Page's posts are always public: leave `visibility` out with `as_page`. To share an existing post, pass its `share_post_id`, with optional text and no image; a share keeps the shared post's audience and can't be scheduled. Mention someone with `@` followed by their Facebook id or vanity name. Show the exact text, any image, the audience, and the identity before publishing, and publish only after approval. Add `publish_at` to schedule a post instead, after confirming the time in the user's time zone. Report success and the post link only when the tool returns them.

`facebook_edit_post` replaces the text of a post the account or one of its Pages published. It keeps the image and audience. Show the current and the new text and edit only after approval. This plugin cannot delete a Facebook post.

## Comments and reactions

`list_comments` lists a post's comments, or with `comment_id` the replies to one comment, 10 a page. `comment` comments on a post, or answers a comment with `reply_to`, with text and optionally one image (`image_url` or `media_id`), as the profile or a Page (`as_page`). Comments are public: show the post, the exact text, and the identity before commenting.

`facebook_react_post` reacts to a post, or to a comment with `comment_id`: `like`, `love`, `care`, `haha`, `wow`, `sad`, or `angry`, optionally as a Page. `remove: true` takes a reaction back, with the same reaction and `as_page` as when it was added. Reactions are visible, so react only when the user asks.

## Friends and follows

`facebook_list_friends` lists the account's own friends (Facebook shows no one else's), up to 50 a page. With `requests: "received"` or `requests: "sent"`, it lists pending friend requests instead, each with its `request_id`. `facebook_friend_request` with `action: "accept"` and the `request_id` accepts a received request; `action: "decline"` refuses a received request or cancels a sent one. Answer only as the user decides.

`facebook_friend_request` with `action: "send"` and a `user_id` sends a friend request, which carries no message. Confirm the exact person first, for example with the name and link from `get_profile`, and check sent requests so nobody is asked twice. `facebook_follow` follows a person or Page without being friends. Friend requests and follows share a low daily and weekly allowance, because Facebook blocks accounts that send many: check `account_status` before planning several, and never spread them across accounts.
