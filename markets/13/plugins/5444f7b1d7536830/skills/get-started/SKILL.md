---
name: get-started
description: Use when someone first connects Clevera or asks what it can do. Explains how to work with their help center, library and agent jobs through the Clevera tools.
---

# Getting started with Clevera

Clevera turns screen recordings into how-to videos, social clips and help articles, and hosts the help center those articles live in. The Clevera tools act on the workspace the person connected, within the abilities they granted.

## First steps

1. Call `get_me` to see who the connection acts for, the workspace, and which abilities it has. Only offer what those abilities allow.
2. For help-center work, call `list_sites`, then `get_site_tree` for the site the person means.
3. For videos and articles they already made, call `list_library`. For raw screen captures, call `list_recordings`.

## Writing help articles

- Read `get_content_guide` (topic `dialect`) before writing, and check drafts with `preview_markdown`.
- `create_article` saves a draft that is not live. Use `submit_for_review` so a person on the team approves it.
- Before `update_article`, read the page with `get_page` and pass its `base_revision_id`, so a newer edit is never overwritten.
- Only call `mark_page_ready` or `publish_site` when the person explicitly asks for the change to go live.

## Making videos, clips and articles from recordings

These cost credits, so always price them first:

1. Quote with `quote_video` or `quote_clip`. Quotes are free and start nothing.
2. Tell the person the credit range, and start only when they agree (`create_video`, `create_clip`, `create_article_from_recording` or `translate_video`).
3. Follow the job with `wait_for_job`. If it returns `needs_input`, give the person the link: the spend needs their approval in Clevera, and you cannot approve it yourself.

`get_credits` shows the balance and this connection's spending limits.

## Help-center insights

`get_site_insights`, `get_content_gaps` and `get_page_feedback` show what readers search for, what they don't find and which pages they rate poorly. These are useful for suggesting which articles to write or fix next.
