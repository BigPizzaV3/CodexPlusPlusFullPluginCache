---
name: get-started
description: Use when the user wants the metadata of a video page (title, description, thumbnail, tags, date, duration, embed player) or the list of entries on a category or listing page, for example to publish it on their own site.
---

# Embedfinder

Embedfinder turns a video page link into a ready-to-publish entry.

1. For one or more video page URLs (up to 8 at a time), call `extract_video_metadata`. Present the title, thumbnail, description, tags and the embeddable player URLs it returns. The player list is ranked best first.
2. For a category, archive or listing page, call `list_page_entries` to get the URLs of its entries and the next page, then pass the ones the user wants to `extract_video_metadata`.
3. Each URL uses 1 extraction from the account quota. Before large batches, or when the user asks how much is left, call `get_quota`.

Embedfinder only reads public pages. It never downloads, stores or re-hosts videos, and it cannot post, edit or delete anything. If a tool says the quota is used up, tell the user and share the upgrade link it returns; do not retry.
