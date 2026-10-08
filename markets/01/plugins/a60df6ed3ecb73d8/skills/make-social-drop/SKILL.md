---
name: make-social-drop
description: >
  Creates and exports a Hyperhuman social drop from a workout, program, or exercise.
  Use when the user asks for Reels, Shorts, TikTok clips, captions, covers, or social drop export.
  Requires OAuth. Not for direct posting to social networks, pricing, checkout, embeds, or medical advice.
---

# Make a social drop

## Goal

Produce a channel-ready drop package (video variants, cover, copy) and export it.

## Steps

1. Confirm OAuth. If missing, stop and ask the user to connect Hyperhuman.
2. Identify source: workout, program, exercise, or exercise group id. Browse with `list_team_workouts`, `list_team_programs`, or `list_team_exercises` if needed.
3. Call `create_drop` with `source_type` and source id(s).
4. Wait for ready state; use `list_team_drops` / status fields from tool results. Do not claim Ready if the tool says Processing.
5. On request: `regenerate_drop_copy` and/or `regenerate_drop_cover`.
6. Call `export_drop` when the user wants downloadable assets.
7. Summarize: drop id, channel presets, export links/copy pack, quota note if returned.

## Output

- Drop id + status
- What was generated (ratios / durations / copy)
- Clear note: export does not auto-post to Instagram/TikTok/YouTube/Facebook

## Guardrails

- Explicit invocation preferred (writes + publish-adjacent).
- `export_drop` records usage; it does not schedule Automate social publish.
- No pricing or checkout.
- See [references/drop-flow.md](references/drop-flow.md).
