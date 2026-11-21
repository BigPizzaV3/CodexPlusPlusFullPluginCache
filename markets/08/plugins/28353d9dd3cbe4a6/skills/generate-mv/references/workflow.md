# Tool return field quick reference

No tool accepts `user_id`; the server takes it from the login state. The billing credential `example` is selected by the server according to quality and does not appear in inputs or returns.

## `mv_list_models()`

```jsonc
{
  "count": 2,
  "default_model": "2.7",   // Used when model is omitted
  "models": [ { "model": "2.7", "model_id": 168, "model_name": "...", "qualities": [...], "ratios": [...],
                "credits": { ... }, ... } ]   // Same fields as mv_get_options, without gate fields
}
```

Pass `models[].model` as `model` to `mv_get_options` and `mv_create_story`. The model is fixed when the task is created.

## `mv_get_options(model?, audio_duration_sec?)`

```jsonc
{
  "model": "2.7", "model_id": 168, "model_name": "...",
  "qualities": [
    { "value": 2, "display": "720P", "credit_per_second": 20, "time_sec_unit": 1,
      "estimated_production_credit": 3600 }   // Present only when audio_duration_sec was passed
  ],
  "ratios": ["16:9", "9:16", "1:1"],
  "required_image_count": 1,
  "min_audio_duration_sec": 0, "max_audio_duration_sec": 0,
  "prompt_limit_length": 0,
  "credits": { "story_creation": 20, "cover_regenerate": 10, "role_regenerate": 10,
               "production": "Billed by audio duration; see qualities[].credit_per_second" },
  // Mandatory confirmation gate 1 (always present)
  "requires_user_confirmation": true,
  "confirmation_gate": "plan_and_credit",
  "blocked_until_user_confirms": ["mv_create_story"],
  "user_confirmation_prompt": "GATE 1 of 3 - STOP AND ASK THE USER. ...",
  "step_credit": { "step": "story_creation", "charged_by": "per task", "credit": 20,
                   "charged_when": "mv_create_story is called", "note": "..." },
  "next_step": "..."
}
```

Pass `qualities[].value` as the `quality` input (for example `2`=720P, `4`=1080P). If omitted, the default quality is used.

**Confirmation gate.** This call always reports gate 1. List every parameter you intend to pass to
`mv_create_story` plus `step_credit.credit` (the story-creation cost) and the estimated production
cost, then **end the turn**; `mv_create_story` is forbidden until the user confirms.

## `mv_create_story(...)`

Inputs: `audio_urls` (required, list), `image_urls` (required, list), `prompt?`, `ratio?`, `quality?`, `model?` (from `mv_list_models`; defaults to `default_model`).

Returns: `{ task_id, task_status, model, model_name, quality, credit_cost, next_step }`

## `mv_get_story(task_id)`

```jsonc
{
  "task_id": "...",
  "task_status": ..., "current_stage": ..., "current_step": ..., "quality": 2,
  "audio_urls": ["..."],
  "story_outline": "...",           "story_outline_status": "success",
  "cover_url": "...",  "cover_prompt": "...", "cover_status": "success",
  "role_url": "...",   "role_prompt": "...",  "role_status": "success",
  // Per-item details for roles/props/scenes; each item is { id, url, prompt, status, error_code }
  "role_list":   [ { "id": "...", "url": "...", "prompt": "...", "status": "success", "error_code": null } ],
  "object_list": [ ... ], "object_status": "success",
  "scene_list":  [ ... ], "scene_status": "success",
  "can_both_edit": true,
  "storyline": [ { "index": 0, "section_id": "...", "start_time": 0.0, "end_time": 4.5, "script": "..." } ],
  "storyline_status": "success",
  "lyrics": [ { "start_time": 0.0, "end_time": 4.5, "text": "..." } ],
  "lyrics_status": "success",
  "partial": false,
  // Mandatory confirmation gate (see below)
  "requires_user_confirmation": true,
  "confirmation_gate": "story_assets" | null,
  "blocked_until_user_confirms": ["mv_submit_production"],
  "user_confirmation_prompt": "GATE 2 of 3 - STOP AND ASK THE USER. ...",
  "step_credit": { "step": "storyboard_production", "charged_by": "audio duration", "credit": 150,
                   "credit_per_time_unit": 30, "time_sec_unit": 1,
                   "estimated_audio_duration_sec": 5, "note": "..." },
  "next_step": "..."
}
```

Each `*_status` value is `doing` / `success` / `fail`. Only when outline, cover, role, storyline, and lyrics are all `success`
can you proceed to stage two; `object_status` / `scene_status` only have values when upstream returns prop/scene assets.
`role_url` / `role_prompt` / `role_status` are compatibility views of the first item in `role_list`; when there are multiple roles, look at `role_list`.

**Confirmation gate.** `confirmation_gate` becomes `story_assets` once outline, cover, lyrics, and
storyline are **all** `success`; before that it stays `null` and you just keep polling. While
`requires_user_confirmation` is `true`, show the cover, outline, lyrics, and storyline, state
`step_credit.credit` (the shot-production cost), ask the user the question in
`user_confirmation_prompt`, and **end the turn**; every tool listed in `blocked_until_user_confirms`
(in particular `mv_submit_production`) is forbidden until the user replies.

## `mv_update_storyline(task_id, storyline)`

Pass the **complete list** as `storyline`; each item is `{ index, start_time, end_time, script }` (seconds, float).
Return the `section_id` from `mv_get_story` as-is; the server uses it to match shots.
Method: first call `mv_get_story` to obtain `storyline`, modify the whole list, then write it back as-is. Returns `{ task_id, updated, segment_count }`.

## `mv_update_lyrics(task_id, lyrics)`

Pass the **complete list** as `lyrics`; each item is `{ start_time, end_time, text }`. Returns `{ task_id, updated, line_count }`.

## `mv_regenerate_asset(task_id, asset_type, prompt?)`

`asset_type` can only be `role` or `cover`. Returns `{ task_id, asset_type, submitted, credit_cost, next_step }`;
then poll `role_status` / `cover_status` from `mv_get_story`.

## `mv_submit_production(task_id, compose_only=false)`

- `compose_only=false`: first submission of shot production, charged by audio duration.
- `compose_only=true`: only re-compose, no credits charged; use only after single-shot regeneration completes.

Returns `{ task_id, submitted, compose_only, next_step }`.

## `mv_get_production(task_id)`

Query tool; **calling it never charges credits at any time**. Step 5 uses it to poll shots, and step 7 uses it to retrieve the final video.

```jsonc
{
  "task_id": "...",
  "task_status": ..., "total_shots": 12, "result_url": "https://.../mv.mp4", "error_code": null,
  "segments": [
    { "index": 0, "start_time": 0.0, "end_time": 4.5,
      "image_prompt": "...", "video_prompt": "...",
      "image_status": 2, "image_url": "...",
      "video_status": 2, "video_url": "...", "error_code": null }
  ],
  "status_legend": { "image_status/video_status": "0-pending, 1-generating, 2-success, 3-failed" },
  // Mandatory confirmation gate
  "requires_user_confirmation": true,
  "confirmation_gate": "segments" | null,
  "blocked_until_user_confirms": ["deliver result_url to the user"],
  "user_confirmation_prompt": "GATE 3 of 3 - STOP AND ASK THE USER. ...",
  "step_credit": { "step": "final_compose", "charged_by": "per task", "credit": 0, "note": "..." },
  "next_step": "..."
}
```

**Confirmation gate.** Once every `segments[].image_status == 2`, `confirmation_gate` becomes
`segments`: show the shot images, state `step_credit` (accepting them is free, regenerating a shot
is charged), ask whether to regenerate any of them, and **end the turn**.
`result_url` must not be delivered before the user accepts the shots, even if it is already filled in.

Determine shot readiness (for display in step 5): all `segments[].image_status == 2`.
Determine final video readiness (for retrieval in step 7): all `segments[].video_status == 2` and `result_url` is non-empty.
If `video_status == 3` or `error_code` is non-empty, stop polling, report it to the user, and offer the option to regenerate that shot.

## `mv_regenerate_segment(task_id, segment_index, image_prompt?, video_prompt?)`

Take `segment_index` from `segments[].index` in `mv_get_production`. Returns `{ task_id, segment_index, submitted, next_step }`.
After regeneration completes, you must call `mv_submit_production(task_id, compose_only=true)` again to refresh `result_url`,
then retrieve the new final video in step 7 with `mv_get_production` (that step is free).

## Helper tools

- `get_user_profile(include_member_items=false)` → query the user overview in real time:
  `{ user_id, nickname, email, avatar, register_time, credit, is_member, member_level,
     member_level_name, member_source, expire_time, purchase_time, product_id, subscription_type }`
  - `credit` is the current credit balance; use it for balance checks before charged operations
  - When `include_member_items=true`, `member_items` is included (a list of membership information items for each endpoint)
  - This API queries in real time and does not persist to the database; it errors directly when not logged in and can be used as a login-state self-check
- `create_upload_url()` → `{ upload_url, method, content_type, form_field: "file", headers, response_hint, notice }`
