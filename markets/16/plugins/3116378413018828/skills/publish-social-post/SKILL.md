---
name: publish-social-post
description: Use when the user wants to publish or schedule an image, video or carousel on social media (Instagram, Facebook, LinkedIn, TikTok, YouTube) for one of their brands, including a Canva design. Prepares the content and creates the post in Abency.
---

Follow this flow to publish an image, a video or a carousel. The server is organization-scoped: ALWAYS resolve the brand first and pass `brand_id` in every call. Reply in the user's language.

1. Call `list_brands` and confirm the brand with the user (unless they already named it). Call `get_brand` to learn its sector, tone and identity before writing the copy.
2. Call `get_connections` with that `brand_id` and find the `connection_id` of each target network.
3. Get the visual content in one of these ways:
   - **Canva design:** `canva_list_designs` (filter by title with `query`), then `canva_export_design` with the `design_id` and the format (`png`, `jpg`, `mp4` or `gif`). It returns a `media_path` ready to use.
   - **The user's own files, if your environment can make HTTP requests:** `get_media_upload_url` with the ARRAY of ALL file names in a single call; upload each file to its signed URL and keep each returned `media_path`.
   - **If you cannot upload files** (for example in ChatGPT): ask the user to upload the images in the Abency composer, or create the post as a draft with the copy so they can add the image there.
4. Write the copy in the brand's tone and confirm it with the user, together with the images, networks and date and time.
5. Call `create_post` with `connection_ids`, the copy and the media:
   - 1 image or video → `media_path` = the path.
   - Carousel → `media_type = "carousel"` and `media_path` = a JSON array of paths in order `["uploads/a.jpg", "uploads/b.jpg"]`.
   - To schedule, pass `scheduled_at` in ISO 8601 with a time zone (e.g. `2026-11-05T10:00:00+01:00`). **Without `scheduled_at` the post stays as a draft and is never published**: tell the user.
6. Call `get_post_status` and report the result. If a network fails, explain why (`platforms[].error_message`).

Rules:
- Publishing is public and cannot be undone from here: confirm copy, images, networks and date BEFORE calling `create_post`.
- Never send images as base64 inside a call; use Canva or the signed upload.
- Make MCP calls one at a time, not in parallel.
- To change an already scheduled post use `update_post` (only while it is not being published); changing only the date keeps the copy.
