# VDClip: create clips with AI

Turn a source video URL into clips (or a captioned cut) through the VDClip AI pipeline.
This job **consumes credits** and runs async — quote the cost, get approval, then poll.

## Non-negotiable rules

- Estimate cost and confirm with the user before `create_project`. Never start a paid job unasked.
- Ask for the missing inputs instead of guessing: content category and desired clip length change the output materially.
- `language` is required for `clipping`/`captions` and must match the spoken audio, not the user's chat language.
- Never invent a `project_id`, `clip_id`, or `preset_id`. They come from tool results.
- Poll `get_project_status` with bounded backoff. Stop on a terminal status; never loop indefinitely.
- Report `credits_consumed` and `credits_remaining` after creation.

## Workflow

### 1. Check the account

`get_account` returns `plan`, `credits` (spendable now), and `first_name` for greeting.
Call `get_capabilities` when plan limits or scopes are unclear.

### 2. Quote the cost

`estimate_cost({ type, video_url })` — or pass `duration_seconds` if you already know it.

- `type: "clipping"` costs **1 credit per minute**; `type: "captions"` costs **2 per minute**.
- `type: "editor"` is billed at render time, not at creation — see [rendering.md](rendering.md).
- Returns `cost`, `balance`, `affordable`.
- If `affordable` is false, stop and tell the user how short they are. Do not call `create_project`.

### 3. Collect the options

Before creating, ask the user for anything you do not already know. See
[project-options.md](project-options.md) for the full enums.

- `category` — improves cut selection. Ask if unknown.
- `clip_durations` — desired length buckets (clipping only).
- template — call `list_templates` first and pass its id as `preset_id`.

### 4. Create

```
create_project({ type, video_url, language, category?, aspect_ratio?, clip_durations?, preset_id? })
```

Returns `project_id`, `credits_consumed`, `credits_remaining`, `plan_tier`.

`type: "editor"` is a different branch: no AI, no credits, sources must be the user's own
`uploads.vdclip.com` URLs (or none at all for a blank canvas), and `language` is refused.
It opens the editor widget directly instead of starting a pipeline.

### 5. Poll until done

`get_project_status({ project_id })` returns `status`, `step` (pipeline stage index),
`title`, `duration`, `ai_type`, and `error_code` on failure.

Stop on `completed` or `failed`. On failure, map the code before retrying — most are not
retryable as-is:

| `error_code` | Meaning |
| --- | --- |
| `CONCURRENT_PROCESSING_LIMIT` | Too many jobs running; wait for one to finish |
| `EMAIL_NOT_VERIFIED` | User must verify their email |
| `PROVIDER_DISABLED` | Source provider unavailable |
| `PLAN_RESTRICTED` | Plan does not allow this job |
| `PROJECT_PROCESSING_ERROR` | Pipeline failure; retry once, then escalate |
| `VIDEO_DURATION_TOO_SHORT` / `VIDEO_DURATION_TOO_LONG` | Source outside allowed length |

`get_project_status` is the AI-job poller. `get_project` is a different tool — it opens an
editable clip in the editor widget. Do not use it to poll.

### 6. Review the clips

`list_clips({ project_id, cursor?, limit? })` returns per clip: `clip_id`, `title`,
`description`, `duration`, `score` (0–100 virality — **sort descending to pick the best**),
`liked`/`disliked`, `status`, `rendering_status`, `thumbnail`, `highlight_tags`.

- `list_projects({ cursor?, limit? })` finds earlier work. Rows carry `status`
  (`pending`/`processing`/`completed`/`failed`/`limited`/`expired`) and `expiration_date`.
- `rate_clip({ result_id, rating })` records `like` or `dislike` — feedback only, it does not
  edit or delete the clip.

## Next steps

- To read what a clip says and when: [transcript.md](transcript.md).
- To change a clip: [editing.md](editing.md).
- To export an MP4: [rendering.md](rendering.md). To post it: [publishing.md](publishing.md).
- To share a read-only link: `get_project_share({ project_id })` to check current state, then
  `set_project_share({ project_id, visibility })` with `public` or `private`.

## Response style

Lead with the outcome and the cost. State credits consumed and remaining. Surface any
failed clips or `error_code` plainly. Offer at most three next actions.
