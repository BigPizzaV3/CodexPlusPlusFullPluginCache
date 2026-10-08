---
name: hook-demo-videos
description: |
  Build hook + demo videos for TikTok, Instagram, and Facebook through the doublespeed MCP: plan segments, source or trim clips, add overlay text, render a baked preview, save an editable video draft with a review link, and queue the post. Use when the user asks for hook videos, demo videos, video edits, or overlay-text videos.
---

# Hook + Demo Videos via doublespeed

A hook-demo video pairs a scroll-stopping opener (the hook) with product/demo footage. It is the most common doublespeed video format and stays editable in the bulk-video table after saving.

## Setup

1. `whoami` to confirm the active product; `list_products` + `set_product` if wrong or missing. Never switch products on your own initiative afterward.
2. `context_get_rules` once per session; check final copy with `context_check_content`.
3. `get_product` for the brand guide and voice.

## Workflow

1. **Plan structure.** Single clip, hook+demo (most common), or multi-segment. Decide per segment whether footage comes from the media library, AI generation (see `doublespeed://skills/ai-video-generation`), or a local file.
2. **Source clips.** Library: `browse_media`. Local files or ffmpeg output (trims, speed ramps, concatenation in shell-capable environments): `prepare_media_upload` → HTTP PUT the bytes to the SAS URL → `commit_media_upload` for the durable URL. Always 9:16.
3. **Write overlay text.** Lift and adapt hooks from real winning posts (`list_posts` sorted by `viewsCount`), not from your own head. Default style unless the brand guide says otherwise: texting-a-friend voice, emotional states over features, ALL CAPS on 2-3 trigger words, no trailing period, "my"/"this" over "your".
4. **Preview.** `render_video_preview` with `videoUrl` (or `clips`), `textBlocks`, and `editorDimensions: 1080x1920`. Video overlay text may ONLY use `stylePreset` `tiktok-sans` or `tiktok-stroke`. Watch the output before saving: readable text, clean pacing, hook lands in the first second.
5. **Save the draft.** `upsert_video_draft` with `videos` (review rows), `hookDemoState` (rows, segments, text blocks - the editable source of truth), and `createShareLink: true` for the reviewUrl.
6. **Iterate.** `get_draft` → `patch_draft` with `segment_edits` (text, styling, overlays, filters, trim/speed), `text_block_inserts` to ADD overlay text, plus leaf fields (`caption`, `music_link`, `mute_music`, `account_id`).
7. **Post.** `queue_post` with the draft's `group_id` or review-link `token` (+ `variant_id` when several). Or post directly from a URL with `create_post` (`video_url`, optional `music_link`, `logo_url` watermark); batches via `create_posts_bulk` (≤50).

## Audio

Trending audio helps videos too. Reuse a winning post's `music_link` (staff sessions can also use `search_trending_audio`); attach it with `music_link` on `upsert_video_draft`/`patch_draft` (or `create_post`). Use `mute_music`/`music_volume`/`video_volume` via `patch_draft` to balance it against the clip's own sound.

## Notes

- `render_video` does a full Remotion composition render; prefer `render_video_preview` + `upsert_video_draft` when the video should stay editable.
- Repeat the reviewUrl in your reply text as a short descriptive markdown link.
- If the user pastes an "Edit with Claude" code, call `redeem_review_handoff` FIRST (single-use, 10-minute expiry), then `patch_draft` with the returned token.
- For research, strategy files, and the feedback loop, read `doublespeed://skills/content-creator`.
