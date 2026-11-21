---
name: schedule-social-posts
description: >
  Schedule, edit, and cancel social media posts with PostWing.
  Use when the user wants to post or schedule to Instagram, TikTok, YouTube,
  LinkedIn, X, Facebook, Pinterest, or Threads.
---

# Schedule social posts with PostWing

PostWing is a remote MCP server. Auth is OAuth: the user signs in to PostWing the first time they use a tool.

## Before scheduling

1. Call `get_me` for the user’s timezone.
2. Call `list_accounts` (optionally with `platform`) to get account ids. If the user has more than one account on a platform, ask which one.
3. If nothing is connected, call `connect_account`, have the user finish the login in their browser, then call `sync_accounts`.
4. For Pinterest, call `list_pinterest_boards` and set `options.board_id`.

## Schedule a post

1. Gather the caption, any media, the accounts, and the time (convert it to ISO 8601 with the user’s timezone).
2. Show the user the caption, each account (platform and handle), the media, and the time, and wait for a clear yes.
3. Call `schedule_post` with `caption`, `scheduled_at`, `accounts: [{ id, caption?, options? }]`, and `media: [{ url, type?, cover? }]`.
4. Tell the user it is scheduled and share `dashboard_url`.

## Edit or cancel

- Find posts with `list_posts` (follow `next_offset` while `has_more`) or `get_post`.
- Change a post with `update_post`, sending only the fields that change. For several posts, call it once per post.
- Cancel: `cancel_post`.
- Show the user the change and get a yes before any of these.

## Media

- Prefer `request_media_upload` for in-chat uploads when the host supports it.
- Or `import_media` with public HTTPS URLs. Videos have a size cap.
- Video covers: `cover: { "url": … }` or `cover: { "at_ms": 1500 }`.

## Rules

- Never invent account or post ids. Use values from PostWing tools.
- Never schedule, change, or cancel without showing the user and getting a clear yes.
- On an error, read `error.code` and `error.field` and fix that field, or tell the user `error.message`.
- Do not claim analytics or inbox features. PostWing schedules and publishes only.
- An active PostWing subscription is required.
