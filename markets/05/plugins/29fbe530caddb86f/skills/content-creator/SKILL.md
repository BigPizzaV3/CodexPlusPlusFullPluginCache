---
name: content-creator
description: |
  End-to-end social content creation (TikTok, Instagram, Facebook) through the doublespeed MCP. Pulls brand context and performance data from the MCP, generates media, builds slideshow and video drafts, shares review links, and queues posts. Self-improving: persists strategy, creative assets, and feedback to a local client folder so each session compounds. Use when the user mentions social content, creating posts, researching strategy, generating hooks/captions, making slideshows or video drafts, analyzing what's working, or updating content strategy for any doublespeed product.
---

# Content Creator for doublespeed

Orchestrates the full content pipeline over the doublespeed MCP server (`https://doublespeed.ai/api/mcp`): research, strategy, ideation, production, review, and posting. Stateful and self-improving. Every session reads prior work and builds on it.

Format-specific production steps live in focused companion skills; read the one that matches the task:

- `doublespeed://skills/slideshows` - photo carousels: templates, image generation, scene data, rendering, drafts.
- `doublespeed://skills/hook-demo-videos` - hook + demo videos: segments, overlay text, previews, video drafts.
- `doublespeed://skills/ai-video-generation` - AI clip generation: models, text/image-to-video, credits safety.
- `doublespeed://skills/content-remixer` - repurpose winners into new variants and formats.
- `doublespeed://skills/performance-report` - analytics: aggregates, breakdowns, winner/loser calls.
- `doublespeed://skills/account-creator` - account personas: usernames, bios, search terms, branded or unbranded.

## Environment

- **doublespeed MCP tools**: always available. The core pipeline. All tools are scoped to the ACTIVE product; call `whoami` first and `set_product` if the wrong product (or none) is active.
- **Browser** (Playwright, Chrome extension, or any available browser tool): use for TikTok profile research and trend discovery. TikTok's web UI can be flaky, so keep interactions focused (load profile, scan recent posts, extract text, move on).
- **Local shell (ffmpeg)**: available in shell-capable environments (Claude Code, Codex, Gemini CLI). Use for trimming, speed ramping, concatenating clips. Upload results via `prepare_media_upload` + `commit_media_upload`. If no shell is available, skip local processing and work with generated clips directly.

## Best Practices

### Copy

- Don't freestyle hooks, slide text, or captions from your own head - it comes out generic and AI-sounding. Lift and adapt wording from REAL winning posts (your own top performers via `list_posts`, competitor posts via the browser). Your job is to assemble and adapt proven copy, not to write fresh copy.
- When Skip judge pass is enabled, choose concepts directly without copy or visual judges or a scorer. Otherwise, rank every candidate set with `score_slideshow_copy` before picking; it's trained on this platform's real posted outcomes. It judges copy only - pair it with brand rules (`context_get_rules`) and factual checks.
- Default copy style unless the brand guide says otherwise: write like texting a friend; lead with emotional states, not product features; ALL CAPS on 2-3 trigger words per hook; no em dashes; no trailing period; prefer "my"/"this" over "your"; product mentions read as story plot points, not ads.

### Visuals

- Study full posts, not just words: a post's nuance is in its slide-by-slide STRUCTURE. Mirror a specific real post's structure when in doubt.
- Prompt for realism: candid iPhone/amateur photo, real setting, natural light, grain - not a glossy render. Never ask the model to render text (it garbles it); text comes from overlay blocks.
- The reliable way to hit a specific look (or keep a recurring person consistent across slides) is iterative image-to-image via `generate_image` `image_url`/`image_urls` references, not one-shot text-to-image.
- Never reuse the identical image on multiple slides unless that repetition IS the format.

### Operating discipline

- Distribution is noisy: a good post can flop by chance, and formats often need several reps before the algorithm catches. Read engagement rate (likes/saves/comments relative to views), not just raw views, before killing a format.
- Always preview (`render_slides` / `render_video_preview`) and actually look at the output before saving a draft or posting. Fix weak slides and re-render.
- Attach trending audio when posting slideshows (`music_link` from a winning post in the same lane; staff sessions can also use `search_trending_audio`) - it materially affects reach.
- Repeat review links and hosted media URLs in your reply text as short descriptive markdown links; some clients can't open links from result cards.
- Batch where the API lets you: `generate_images` for all slides at once, `scenes` array in `render_slides`, `variant_ids` in `patch_draft`, `create_posts_bulk` for many posts.

## Client Data (local state)

Client files: `~/Shared drives/doublespeed/doublespeed-clients/{client-name}/`

If the shared drive isn't mounted, tell the user and work from MCP data alone.

### Strategy Files

Each client has a `_strategy/` folder with three files:

```
client-name/
├── _strategy/
│   ├── strategy.md        # Research, content strategy, learnings, performance patterns
│   ├── creative-bank.md   # Proven hooks, prompts, caption patterns
│   └── feedback.md        # Raw user feedback log (dated, categorized)
├── brand docs, briefs...
```

**With account groups** (only when a product has 3+ distinct groups OR the user explicitly works by group): add `group--{name}/` subfolders under `_strategy/`, each with its own three files. Folder naming: `group--{name}` (lowercased, hyphens for spaces). Don't pre-create group folders; create them when the user first works on a specific group.

**strategy.md** combines research, strategy, and learnings in dated sections (`## 2026-03-30` → `### Research`, `### Strategy Updates`, `### Learnings`).

**creative-bank.md** stores proven hooks (grouped by style: stat, bold claim, question, story), image prompts, and video prompts.

**feedback.md** is the raw, dated log: `- hooks: "too aggressive, tone it down" (re: stat hooks batch)`. When feedback repeats 3+ times, promote it to a rule in strategy.md - and if the user wants it enforced, add it as a live guardrail via `context_add_rule`.

### State Rules

1. **Read before you write.** Check `_strategy/` before generating anything.
2. **Append, don't overwrite.** Add dated sections. Mark stale findings explicitly.
3. **Save after meaningful work.** Don't wait until end of session.
4. **Scale effort to the ask.** Quick task = read creative-bank.md + go. Full session = load everything.

## Workflow

### Startup (always)

1. Call `whoami` to see the active product. If it's wrong or missing, `list_products` (use `search`; prefer `recommended: true` when titles duplicate, avoid `isEmpty` shells) then `set_product`. Never switch products on your own initiative afterward.
2. Scale state loading to the task:
   - **Quick task** ("make 3 hooks", "generate an image"): call `get_product` for brand context, read `creative-bank.md` if it exists, proceed.
   - **Content session** ("plan next week's content", "create a batch"): read all `_strategy/` files, call `get_product` + `get_post_metrics`. If using groups, call `list_accounts` to map accounts to groups.
   - **Research/analysis** ("what's working?", "audit our accounts"): full state load + browser research if available.
3. Call `context_get_rules` once per session before producing anything the user may publish. These are live guardrails; they always win over local files.
4. If `_strategy/` doesn't exist, create it as you produce work.

### Research (when needed)

Skip if existing research is fresh and the user isn't asking for new research.

- **Via MCP**: `get_post_metrics` for exact aggregates (totals, averages, per-account performance - no pagination needed). `list_posts` sorted by `viewsCount` (or `list_account_posts` for one account) to study winners and losers; pass `include_scene_data`/`include_image_urls` only when you need slide content. `get_product` for brand state. Staff sessions only: `search_trending_audio` for what sounds are moving (scope `songs` for the ranked chart, `niches` to discover sound niches).
- **Via browser**: visit `tiktok.com/@username` for owned accounts and competitors.
- **Save**: update `strategy.md` with a dated research section.

#### Interpreting post data

Posts carry a type (slideshow vs video). Slideshow rows expose slide text through scene data; videos made in doublespeed carry overlay text in their segments. A video with no overlay text (or created outside doublespeed) is invisible to the MCP - use the browser: open the post, describe visual style, transitions, pacing, on-screen text, and music, and record it in `strategy.md` / `creative-bank.md` as visual references. This is common for celeb-edit and other visual-first accounts; their creative bank should emphasize visual references and mood descriptions over text hooks.

### Content Ideation

1. Start from `creative-bank.md`. Evolve proven hooks/prompts rather than inventing from nothing.
2. Use `get_product` for brand voice and `get_post_metrics` / `list_posts` to see which formats and hooks actually perform.
3. Generate hooks in varied styles (stat, bold claim, question, story) and captions with relevant hashtags.
4. **Choose candidates.** When Skip judge pass is enabled, choose directly without a scoring pass. Otherwise, rank candidates with `score_slideshow_copy`. Send ALL candidate copy sets (slide texts + caption) in ONE call - scores are comparative within the submitted set. Pick from the top, then apply editorial judgment for brand rules and factual accuracy (the scorer knows neither).
5. Check drafts against guardrails with `context_check_content` before presenting them as final.
6. Update `creative-bank.md` with new hooks and prompts.

### Production

Follow the matching companion skill for the full step-by-step:

- **Slideshows** (templates → `generate_images` → `render_slides` → `upsert_slideshow_draft` → `queue_post`): `doublespeed://skills/slideshows`.
- **Hook + demo videos** (segments → overlay text → `render_video_preview` → `upsert_video_draft` → `queue_post`): `doublespeed://skills/hook-demo-videos`.
- **AI clip generation** (`list_models` → `generate_video` → `check_generation_status`, credits safety): `doublespeed://skills/ai-video-generation`.
- **Images**: prefer existing collections (`browse_media`; public pools via `visibility: public`), else `generate_images` for batches / `generate_image` with `image_url`/`image_urls` references for image-to-image consistency. Store keepers with `create_image_collection` + `prepare_media_upload`/`commit_media_upload`.

### Review handoffs

If the user pastes an "Edit with Claude" code from a review page, call `redeem_review_handoff` FIRST (codes are single-use, 10-minute expiry), then edit with `patch_draft` using the returned token.

### Posting

- **From a draft** (preferred - keeps provenance): `queue_post` with the draft's `group_id` or review-link `token` (+ `variant_id` when the draft has several). It uses ONLY the variant's own data; if something's missing, fix the variant with `patch_draft` first.
- **Direct from URLs**: `create_post` with `account_username`, `caption`, and `image_urls` (slideshow) or `video_url` (video); optional `music_link`, `logo_url` (video watermark). For batches, `create_posts_bulk` (≤50 per call).
- Default status `scheduled` queues it into the account's next open slot; these tools cannot pin an exact publish time (only the posting REST API's scheduledAt can, within the account's scheduling rules). Use `draft` if the user wants to review in-app first. Edit caption/account later with `update_post`.
- **Order and timing**: `list_posting_queue` shows each account's queued posts in firing order with their expected `scheduled_at`; `reorder_posting_queue` with the post ids in the wanted order swaps their slots (unnamed posts keep theirs).
- Run `context_check_content` before queueing when the product has guardrail rules.

### Feedback Loop

When the user gives feedback:

1. **Log it** in `feedback.md` with date and category (hooks, overlays, visuals, strategy, general).
2. **Apply it** to the current session immediately.
3. **Promote patterns** to `strategy.md` when the same feedback appears 3+ times.
4. **Make it enforceable** when the user asks for a rule ("never show X", "captions must always Y"): call `context_add_rule` - it goes live immediately. Never route a requested rule through `context_propose_fact` (that only queues a candidate for review).
5. **Update creative-bank.md** if feedback changes what hooks/prompts to use or avoid.

When reviewing performance in a later session:

- `get_post_metrics` for exact aggregates; `list_posts` sorted by views, segmented per account via `account_id` or `list_account_posts`.
- Update `strategy.md` with what over/underperformed and why.
- Periodically push key insights to the product via `update_product` (`notes`, `hook_custom_prompt`, brand-guide fields).

## Tool Reference

| Tool                                                  | Purpose                                                              |
| ----------------------------------------------------- | -------------------------------------------------------------------- |
| `whoami`                                              | Identity, permissions, active product                                |
| `list_products` / `set_product`                       | Find and select the active product                                   |
| `get_product` / `update_product`                      | Brand guide, audience, hooks context; write back insights            |
| `list_accounts` / `get_account` / `update_account`    | Accounts, groups, bios, personas                                     |
| `list_posts` / `list_account_posts`                   | Post rows with views/likes/comments, sortable                        |
| `get_post_metrics`                                    | Exact aggregate performance (totals, averages, per-account)          |
| `search_trending_audio`                               | Ranked trending-sound chart + niche discovery (staff sessions only)  |
| `score_slideshow_copy`                                | Rank candidate slideshow copy when judging is enabled                 |
| `list_models`                                         | Image/video generation models, params, pricing                       |
| `generate_image` / `generate_images`                  | AI images (text-to-image, image-to-image); costs credits             |
| `generate_video` / `check_generation_status`          | Async video generation + polling                                     |
| `list_templates` / `get_template` / `create_template` | Slideshow/video scene templates                                      |
| `list_style_presets`                                  | Canonical text style presets (video: tiktok-sans/tiktok-stroke only) |
| `render_slides`                                       | Preview slides from sceneData (up to 8 scenes per call)              |
| `render_video_preview` / `render_video`               | Baked video preview / full Remotion render                           |
| `upsert_slideshow_draft` / `upsert_video_draft`       | Persist drafts, `createShareLink` for reviewUrl                      |
| `get_draft` / `patch_draft`                           | Inspect and surgically edit draft variants                           |
| `redeem_review_handoff`                               | Open a draft from an "Edit with Claude" code                         |
| `create_review_link`                                  | Separate review-link step (prefer createShareLink)                   |
| `create_combined_review_link`                         | One review link covering 2-25 saved drafts                           |
| `queue_post`                                          | Queue a draft variant as a post                                      |
| `create_post` / `create_posts_bulk` / `update_post`   | Direct posting from URLs; edit/reschedule                            |
| `browse_media` / `create_image_collection`            | Media library folders and files                                      |
| `prepare_media_upload` / `commit_media_upload`        | Upload local files (SAS PUT flow, batches supported)                 |
| `import_media_url`                                    | Import a direct media URL; `probe_only` just reads its metadata      |
| `context_get_rules` / `context_check_content`         | Guardrails: read rules, pre-publish check                            |
| `context_add_rule`                                    | Add a LIVE guardrail rule when the user asks for one                 |
