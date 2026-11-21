---
name: make-a-music-video
description: Take a song from upload to a compiled AI music video in PulseJet AI, in the order the pipeline enforces, confirming cost before every step that spends credits.
---

Use the PulseJet AI MCP tools in this order. Each stage is a real server-side gate: a later step fails until the earlier one is complete, so do not skip ahead.

1. **Find or create the project.** `list_projects` to see what exists; `create_project` for a new one. Note the project id; every later call needs it.
2. **Get the song in.** For a file the customer has, call `upload_song` with `filename` and `contentType` to receive an `uploadUrl` and `stagingKey`, have the customer PUT the file to that URL, then call `upload_song` again with the `stagingKey`. `trim_song` if only part of the track should be covered.
3. **Analyse.** `analyze_song` (free, but refused on a zero balance), then poll `get_analysis` until it reports BPM, key, sections and lyrics. Offer `update_transcript_line` for any mis-heard lyric, because lyrics feed the script.
4. **Creative direction.** `get_narrative_suggestions` or `brainstorm` for ideas, `list_themes` for the visual style, `update_project` to set them, then `approve_creative_direction`.
5. **Script and shot plan.** `generate_script`, review with `get_scenes` (edit with `update_scenes`), then `generate_shot_plan` and review with `get_shots`.
6. **Stills, then video.** Call `generate` with `stage: "thumbnails"` and `estimate: true`, read the quote (creditsNeeded, creditsAvailable, shortfall, shotsToGenerate) to the customer in plain words, and only on their yes call `generate` with `stage: "thumbnails"`. Check `get_thumbnails`, then `approve_thumbnails`. Repeat the same two calls with `stage: "videos"`: estimate first, state the numbers, wait for a yes, then start. Poll `get_generation_progress` with the returned `runId`; use `render_shot` for one shot that needs another pass. If the estimate says `outOfCredits`, say so and stop; do not start a run the balance cannot cover.
7. **Compile and review.** `compile_video` (this step does not spend credits), then `get_project` for the finished download link. Let the customer review the result. For a shot they want to change, use `get_shots` and the `review-and-fix-shots` skill; do not assign a numerical quality score.

Only five tools currently debit credits: `generate`, `render_shot`, `render_all_pending_videos`, `regenerate_shot_image` and `generate_image_candidate`. `analyze_song`, `generate_script`, `generate_shot_plan`, `generate_scene_thumbnails`, `get_narrative_suggestions`, `brainstorm` and `compile_video` do not (`analyze_song` and `generate_scene_thumbnails` are refused on a zero balance but charge nothing). `generate_scene_thumbnails` nevertheless requires the OAuth spend permission: it starts provider-backed image generation and its planned per-scene debit must not become a scope bypass. Before every step that debits credits: tell the customer what the step costs in plain words and wait for an explicit yes. For `generate` the numbers come from `generate` with `estimate: true` (it starts nothing); for every other spending step call `get_credit_balance` and `get_project`, whose `creditState` says whether the pending work is affordable. Never start a credit-spending step on an assumption.

Never invent project state. Read it with `get_project` or `get_shots` and report what the tool returned.

## Reporting a problem

When a step fails, a result looks wrong, or the customer is unhappy and it is not clear they want it passed on, offer to report it in one sentence rather than filing silently or letting it drop. Read back a one-sentence summary, and once they agree file it with `submit_feedback`, keeping their own words in `message` and passing the project id, the `shotId` and any `errorCode` the failing call returned, so nobody has to ask them for those later. The result carries the ticket key to quote back to them.

Whenever something goes wrong, let the customer know a problem or an idea can be reported from this conversation with `submit_feedback`; there is no form to find.
