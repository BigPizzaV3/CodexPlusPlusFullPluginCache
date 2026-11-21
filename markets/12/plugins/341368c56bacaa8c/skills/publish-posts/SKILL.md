---
name: publish-posts
description: Draft, publish, schedule, queue, edit, and track social media posts with Postproxy across Instagram, Facebook, TikTok, LinkedIn, YouTube, X, Threads, Pinterest, Bluesky, Telegram, and Google Business. Use when the user wants to post something, schedule content, save a draft, add a post to a queue, change or reschedule a scheduled post, or check whether a post went out.
---

# Publish posts with Postproxy

Turn the user's request into a correct post on the right profiles, confirm before anything goes live, then report where it landed.

## 1. Pick the profiles

- Call `profiles_list` to resolve the target profiles. Use the returned profile IDs. If the user names only a network and they have several profiles on it (for example, two brands on Instagram), ask which one.
- If the user works with several brands, use `profile_groups_list` to pick the right group first.
- For Facebook, LinkedIn organizations, Pinterest, Telegram, and Google Business, the post may need a placement (page, organization, board, channel, or location). Call `profiles_placements` and pass the chosen ID in `platforms`: Facebook `page_id`, LinkedIn `organization_id`, Pinterest `board_id`, Telegram `chat_id`, Google Business `location_id`.

## 2. Shape the content for each network

- Respect the networks' limits. X allows 280 characters per post, Threads allows 500, and Bluesky allows 300. For longer text on X or Threads, offer a thread using the `thread` parameter, or shorten it.
- Instagram, TikTok, YouTube, and Pinterest need media. Ask for an image or video if none was given.
- Media must be public URLs in `media`. If the user only has a file in the chat, ask them for a public link to it.
- Use `platforms` for network-specific options instead of separate posts: Instagram/Facebook `format` (post, reel, story; stories take no caption), YouTube `title` and `privacy_status`, TikTok `privacy_status`, Instagram `collaborators` and `first_comment`, Google Business `format` (standard, event, offer).

## 3. Decide when it goes out

- Now: no `schedule`, no `queue_id`.
- At a time: pass `schedule` as ISO 8601 with a timezone offset. Resolve relative times ("tomorrow at 9") using the user's timezone; ask if it is unknown. Never schedule in the past.
- Into a queue: call `queues_list`, pass `queue_id` (and optionally `queue_priority`). Don't combine with `schedule`. `queues_next_slot` tells the user when it will go out.
- Not yet: pass `draft: true`. Publish it later with `post_publish_draft`.

## 4. Confirm, then publish

Before calling `post_publish` without `draft: true`, show the user exactly what will happen: the final text per network, attached media, target profiles and placements, and the publish time (or "immediately"). Publish only after they confirm. Saving a draft doesn't need confirmation.

## 5. Report back

- After publishing, call `post_status` with the returned post ID. Report each network's status and the published URL. Publishing is asynchronous, so "pending" or "processing" right after creating the post is normal; offer to check again.
- If a network failed, quote its error and suggest the fix (for example, a missing placement or unsupported media type).

## Edit, reschedule, or remove

- Find the post with `history_list` or the ID the user gives.
- `post_update` works only on drafts and on scheduled posts more than 5 minutes before their publish time. Send only the fields that change. `media`, `profiles`, and `thread` replace the existing values entirely.
- To take a published post down, confirm first, then call `post_delete_on_platform` (keeps the Postproxy record) or `post_delete` with `delete_on_platform: true` (removes both). `post_delete` alone only removes the Postproxy record and leaves the live post up; say so.
