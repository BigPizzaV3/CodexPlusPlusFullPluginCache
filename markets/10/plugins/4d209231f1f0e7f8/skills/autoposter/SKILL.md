---
name: autoposter
description: Getting started guide for Auto Poster AI social media publishing and scheduling.
---

# Getting Started with Auto Poster AI

Auto Poster AI enables you to draft, schedule, and publish content across 9 major social networks:
LinkedIn, X (Twitter), Instagram, TikTok, YouTube, Threads, Bluesky, Pinterest, and Facebook.

## Recommended Workflow

1. **List Accounts**: Call `autoposter_list_accounts` first to retrieve active connected social channels and their `id`s.
2. **Check Platform Constraints**: Call `autoposter_get_rules` to ensure content respects platform-specific character limits, aspect ratios, and media constraints.
3. **Draft Post**: Call `autoposter_draft_post` with the selected `accountIds` and post copy. If human approval is preferred, keep as draft for dashboard review.
4. **Schedule or Publish**: Use `autoposter_schedule_post` for specific release windows, or `autoposter_publish_draft` for immediate broadcast.
5. **Track Delivery**: Check `autoposter_get_post_status` to view delivery state and live published URLs.
6. **Attach Images and Media**: To attach existing media from the workspace library, call `autoposter_list_media` first and pass the selected media's `id`s in `mediaIds` (or pass CDN URLs in `mediaUrls`). When attaching fresh AI-generated images (such as DALL-E outputs) or chat uploads up to 100MB, upload them using `autoposter_upload_media` or pass them directly in the `files` parameter. For larger files or videos (>100MB), ask the user to provide a direct public file URL or use `autoposter_get_media_upload_url` for direct S3 upload up to 5GB.
7. **Delete / Cancel Posts**: Use `autoposter_delete_post` with `postId` to delete or cancel an existing draft, scheduled, or pending post.
8. **List & Search Posts**: Call `autoposter_list_posts` to view scheduled posts, drafts, or delivery history filtered by state (`scheduled`, `drafts`, `queued`, `posted`) or caption keyword.
9. **Browse Media Library**: Call `autoposter_list_media` to inspect uploaded images and videos stored in the workspace media library with CDN URLs.

