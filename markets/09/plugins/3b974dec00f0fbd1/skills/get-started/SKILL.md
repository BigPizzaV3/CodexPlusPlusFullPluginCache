---
name: get-started
description: Use when the user wants to draft, schedule or publish social media posts with Content Mill, or check their connected accounts, platform limits, or what has been posted.
---

# Getting started with Content Mill

Content Mill posts to the user's own connected social accounts (X, LinkedIn, Instagram, Facebook, Threads, Bluesky), so be deliberate.

## Recognize the ask
- "post / share / publish / schedule ..." -> publishing; follow the steps below.
- "draft / write me a post / let me review" -> `create_draft`. Nothing goes public.
- "what's scheduled / did it go out / did anything fail" -> `list_posts`, then `get_post`.
- "how long can a post be on ..." -> `get_platform_limits`.
- "cancel / delete that post" -> `delete_post`.

## How to post
1. Call `list_social_accounts`. Offer only accounts whose connection status is Connected. If it is unclear which accounts the user means, ask.
2. Call `get_platform_limits` for the chosen platforms before writing. A post sent to several platforms must satisfy all of them, so write to the strictest.
3. If the post needs an image or video, call `upload_media_from_url` with a public https link. For a file with no link, call `create_media_upload`, send the raw bytes to its upload URL from your shell, then call `finish_media_upload`. Never put a file's contents in a tool argument. If you cannot make an HTTP request, ask for a public link or to add the media in the Content Mill web app.
4. To let the user refine first, use `create_draft` and `update_draft`. Drafts are never published. `update_draft` overwrites the draft's text, accounts and media and does not keep the previous version, so tell the user what will change before calling it.
5. To publish: call `preview_post`, show the user the preview (text, accounts, time), and wait for their approval. Only then call `publish_post` with the preview token and `confirmed: true`. Never publish without showing the preview and getting a go-ahead, and never confirm on the user's behalf. For a change, preview again: a preview is single-use and publishes exactly what was previewed.
6. Publishing is asynchronous. Afterwards call `get_post` to report each platform's result and link.

## Worth knowing
- Only drafts can be edited. A scheduled post is deleted and recreated through a new preview; a published post can't be changed.
- Give times as ISO 8601 with a timezone offset, in the future. If you don't know the user's timezone, ask.
- A post that fails on one platform doesn't stop the others; its status is PartiallyFailed.
