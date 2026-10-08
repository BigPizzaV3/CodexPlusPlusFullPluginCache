---
name: slideshows
description: |
  Build slideshow (photo carousel) posts for TikTok, Instagram, and Facebook through the doublespeed MCP: pick a template, generate images, edit scene data, render previews, save a draft with a review link, and queue the post. Use when the user asks for slides, carousels, slideshows, or image posts.
---

# Slideshows via doublespeed

## Setup

1. `whoami` to confirm the active product; `list_products` + `set_product` if wrong or missing. Never switch products on your own initiative afterward.
2. `context_get_rules` once per session before producing anything the user may publish; check final copy with `context_check_content`.
3. `get_product` for the brand guide and voice.

## Workflow

1. **Pick a template.** `list_templates` to browse, `get_template` for the winner's `scene_data` and variables. Prefer templates that performed well historically (`list_posts` sorted by `viewsCount`). To preview all its slides, pass its scene_data to `render_slides`.
2. **Generate images.** `generate_images` (plural - all slides in ONE parallel call, `async: true`), then poll `check_generation_status`. Check `list_models` for image models. Or reuse library images via `browse_media` (public pools via `visibility: public`).
   - Prompt for realism: candid iPhone/amateur photo, natural light, grain - not a glossy render. Never ask the model to render text; text comes from overlay blocks.
   - To keep a recurring person or match a specific look across slides, use iterative image-to-image via `generate_image` with `image_url`/`image_urls` references.
   - Never reuse the identical image on multiple slides unless that repetition IS the format.
3. **Edit the template's sceneData in place.** Change only text content, image `src`, and per-slide `color`/`bounds`. Keep the template's fontFamily/fontWeight/fontSize/lineHeight/letterSpacing exactly as fetched - drafts from a template product are rejected otherwise. Style text blocks by naming a preset (`style.stylePreset` from `list_style_presets`; usually `tiktok-stroke` or `tiktok-bg`), never by restating the preset's own values. Keep text inside the platform safe area (on 1080x1920: x 46-1033, y 115-1545, clear of the action rail).
4. **Choose the copy.** When Skip judge pass is enabled, choose directly without copy or visual judges or a scorer. Otherwise, send ALL candidate copy sets (slide texts + caption) to `score_slideshow_copy` in ONE call - scores are comparative within the submitted set. Pick from the top, then apply brand rules and factual checks (the scorer knows neither). Lift and adapt wording from real winning posts rather than freestyling.
5. **Preview.** `render_slides` with the sceneData (or `scenes` array for up to 8 variants in one call). Treat `warnings` as unreadable slides; fix and re-render. Actually look at the output: does slide 1 stop the scroll?
6. **Save the draft.** `upsert_slideshow_draft` with the SAME sceneData, `sourceTemplateId` (required lineage when the product has templates), and `createShareLink: true` to get the `reviewUrl` in one call. Omit `groupId` to create; include it to update.
7. **Iterate.** `get_draft` (summary mode) to read blocks, `patch_draft` with `block_edits` (text, images, styling, position) or `structure_edits` (add/remove/reorder pages). Prefer these narrow helpers over resending sceneData; use `variant_ids` to apply one edit across many variants in a single call.
8. **Post.** `queue_post` with the draft's `group_id` or review-link `token` (+ `variant_id` when several). Audio must already be on the draft (see Audio). Run `context_check_content` before queueing when the product has rules.

## Audio

Every slideshow should ship with trending audio; it materially affects reach and no tool adds it for you.

1. Find a track: copy the `music_link` from a winning post in the same lane (`list_posts` sorted by `viewsCount`). Staff sessions can also use `search_trending_audio` (scope `songs` for the ranked chart, `niches` for sound niches).
2. Attach it: `music_link` on `upsert_slideshow_draft`, or `patch_draft` with `music_link` on an existing draft. The link must be a TikTok or Instagram share URL matching the account's platform.
3. `queue_post` returns a `warnings` entry when a slideshow has no audio. Treat it as a blocker unless the user said no music.

## Notes

- Repeat the reviewUrl and hosted media URLs in your reply text as short descriptive markdown links; some clients can't open links from result cards.
- If the user pastes an "Edit with Claude" code from a review page, call `redeem_review_handoff` FIRST (single-use, 10-minute expiry), then edit with `patch_draft` using the returned token.
- For research, strategy files, and the feedback loop, read `doublespeed://skills/content-creator`.
