---
name: content-remixer
description: |
  Repurpose winning content into new posts through the doublespeed MCP: find top performers, extract what worked, and remix it into fresh variants and formats (new copy on a proven structure, new imagery on a proven layout, slideshow to video and back). Use when the user asks to remix, repurpose, iterate on a winner, make variants, or "more like this".
---

# Content Remixer via doublespeed

Remixing beats freestyling: a proven structure with fresh skin outperforms a new idea most days. This skill turns one winner into many posts.

## Setup

1. `whoami` to confirm the active product; `list_products` + `set_product` if wrong or missing. Never switch products on your own initiative afterward.
2. `context_get_rules` once per session; check final copy with `context_check_content` before queueing.

## Find the winner

1. `get_post_metrics` for the exact aggregate picture (per-account and per-format performance, engagement rate vs raw views).
2. `list_posts` sorted by `viewsCount` (add a date range to catch recent breakouts); pull the winner's full structure with `include_scene_data`.
3. For outside inspiration, study competitor posts in the browser (staff sessions can also check `search_trending_audio` for what's rising in the niche). Judge winners on engagement rate (likes/saves/comments relative to views), not views alone - one lucky post is not a format.

## Remix moves

Pick the lightest move that produces a genuinely different post:

1. **Same structure, new copy.** Keep the winning post's slide-by-slide structure; swap hook, body text, and caption. Generate several copy sets and adapt wording from other real winners. When Skip judge pass is enabled, choose directly without copy or visual judges or a scorer. Otherwise, rank them ALL in one `score_slideshow_copy` call.
2. **Same copy, new visuals.** Regenerate imagery with `generate_images`; to keep a recurring person or match the original look, use image-to-image via `generate_image` with `image_url`/`image_urls` references to the winner's media (`browse_media` to find it).
3. **Promote the winner to a template.** `create_template` from the winning scene_data (preview with `render_slides` first) so every future draft inherits the structure with proper `sourceTemplateId` lineage.
4. **Cross-format.** Slideshow winner -> video: reuse its hook as video overlay text and generate footage per `doublespeed://skills/ai-video-generation`, then build the draft per `doublespeed://skills/hook-demo-videos`. Video winner -> slideshow: turn its beats into slides per `doublespeed://skills/slideshows`.
5. **Audio refresh.** Re-queue a proven post with new trending audio: the `music_link` from a current winner in the same lane (staff sessions can also use `search_trending_audio`).
6. **Full video recreation.** The REST `/api/v1/clone` endpoint (separate `ds-` API key, not an MCP tool) recreates a source video as a fresh AI generation, optionally featuring the product.

## Ship

1. Preview every remix (`render_slides` / `render_video_preview`) and actually look at it - a remix that reads like a re-upload is wasted.
2. Save with `upsert_slideshow_draft` / `upsert_video_draft` (`createShareLink: true`), iterate with `patch_draft` (use `variant_ids` to apply one edit across many variants).
3. Spread variants across accounts with `queue_post` or `create_posts_bulk`; never post identical content to the same account twice.

## Notes

- Repeat review links and hosted media URLs in your reply as short descriptive markdown links.
- Log which remix moves win into the strategy files described in `doublespeed://skills/content-creator`.
