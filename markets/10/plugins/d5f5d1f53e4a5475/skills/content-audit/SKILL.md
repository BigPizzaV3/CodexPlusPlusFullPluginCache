---
name: content-audit
description: Review a WordPress site's content and list what needs attention, such as posts without a category, featured image or excerpt, old drafts, or pending comments. Use when the user asks for an audit, a cleanup, or what to fix on their site.
---

# Auditing content

1. Get the overall picture with `wp_count_posts` (by status) and `wp_count_media`.
2. Read posts in pages of 20 with `wp_get_posts`, and use `wp_get_post_snapshot` for the details you need (terms, featured image, excerpt).
3. Check, and report as short lists with post titles and links:
   - published posts with no category other than the default, or no tags (`wp_get_post_terms`)
   - posts without a featured image
   - drafts not touched for a long time
   - comments waiting for moderation (`wp_get_comments` with status hold)
4. End with the three fixes that matter most, and offer to do them one at a time.

This skill only reads. Change nothing until the user picks a fix.
