---
name: lmnts-campaign-handoff
description: Move a social media campaign plan into lmnts as reviewable drafts. Use when the user has planned posts (copy, platforms, dates, images or videos) in this conversation and wants them built in lmnts, or asks to send, push, or hand off a campaign, calendar, or batch of posts to lmnts.
---

# Hand a campaign to lmnts

lmnts holds a client's social content as posts. Each post has a caption, one or more platforms, a scheduled day and time per platform, and attached media. Everything you create here is a draft that a person reviews in lmnts before anything goes live. Never claim something was published.

## Before you create anything

1. Call `list_clients` and match the campaign to one client by name. If the user has one client, use it. If several could match, ask which one. Never guess.
2. Read that client's `connected_platforms` from the result. A post can only carry platforms the client has connected. If the plan names a platform that is not connected, tell the user which posts are affected and ask whether to drop that platform or keep the post for the others.
3. Confirm the plan with the user in one short table: post title, platforms, date, time, and which asset goes with it. Times are wall-clock in the client's timezone (America/New_York). Post nothing until they say go.

## Build it

For each planned post, in order:

1. `create_post` with `client_id`, a short internal `title`, the final `content` (the caption), the `platforms` list, `scheduled_date` (YYYY-MM-DD) and `scheduled_time` (HH:MM, 24 hour). Always pass the time the user stated. Pass a `post_id` you generate (a UUID) so a retry never creates a duplicate.
2. If the plan has an image or video for that post: `upload_asset` with the file (or its URL) and the `client_id`, then `attach_asset_to_post` with the returned `asset_id`. Upload each asset once; reuse the same `asset_id` if the plan uses it on several posts. For a carousel, attach the assets in the order they should appear.
3. Keep the post id, title, and lmnts `url` from each result.

Do not call `mark_post_ready_for_review`, `approve_post`, or `schedule_post` unless the user explicitly asks for that step, and only after every draft is built. If those tools are absent, the user connected with draft-only permission; say so once instead of retrying.

## Finish

1. Optionally call `ask_sprk` once per client with a short instruction such as "Review the drafts created today for consistency of tone and hashtags, and flag anything over a platform limit." Report Sprk's reply.
2. Give the user a compact summary: one line per post with the lmnts link, plus anything skipped and why (platform not connected, asset failed to upload, caption over a platform limit).

## Rules

- One draft per planned post. Do not merge or split posts without asking.
- Keep captions exactly as the user approved them. Do not add hashtags, emoji, or calls to action they did not write.
- If a tool returns an error, fix the input if it is obvious (a bad date, a platform not connected) and retry once; otherwise stop and tell the user which post failed and why.
- `client_id` is the lmnts client. Do not confuse it with any other id.
