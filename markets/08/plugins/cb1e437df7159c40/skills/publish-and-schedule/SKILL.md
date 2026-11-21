---
name: publish-and-schedule
description: Publish or schedule Instagram posts, reels, carousels and stories, and plan when to post. Use when the user wants to post, schedule, queue or reschedule something on Instagram, turn slides or images into a carousel, or asks when they should post this week.
---

# Publish and schedule

## Pick the time

If the user hasn't given a time, call `ig_best_times` with their IANA time zone and suggest the best slots. Send `when` as ISO 8601 with the time zone offset (for example `2026-10-01T18:00:00+02:00`), or `"now"`. Posts can be scheduled up to 75 days ahead.

## Get the media

Instagram fetches media from a link. It must be a public https link to the file itself, not a link to an Instagram post.

- If the file is on the user's computer and you can run commands (Claude Code, Cowork, Codex, Cursor), call `ig_media_upload` with the file name, run the upload command it returns, then pass its `media_ref` to `ig_publish`.
- In a chat where you can't run commands, ask for a public link to the file instead.
- Carousels take 2–10 images or videos in the order they should appear. Keep them the same aspect ratio: Instagram crops the rest to match the first.

## Publish

1. Call `ig_publish` without `confirm_code`: `type` (reel, image, carousel or story), `media`, `caption` and `when`. Nothing is posted yet; you get a preview that checks the links, the account and Instagram's 24-hour publishing limit.
2. Show the preview, including the exact caption, and ask for a clear yes.
3. Only after the user agrees, call again with exactly the same arguments plus `confirm_code`.
4. Publishing runs in the background. Tell the user it's queued, then check `ig_schedule` for the outcome and the post's link.

Published posts cannot be deleted through Instagram's API, so read the caption back before confirming.

## Move or cancel

`ig_schedule` lists what's queued with job ids. `ig_schedule_change` moves a queued post to a new `when` or cancels it, with the same preview and yes. Posts that have started publishing can't be changed.
