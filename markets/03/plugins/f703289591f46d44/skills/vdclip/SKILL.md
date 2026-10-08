---
name: vdclip
description: Create, render, and publish short-form video with VDClip. Use for "clip this video", "make shorts from this YouTube link", "add captions/subtitles", "find the best moments", reading what a clip says and when, opening a clip in the visual editor, rendering or exporting an MP4, checking credits or plan limits, and posting or scheduling clips to TikTok, Instagram, YouTube or Facebook.
license: MIT
compatibility: Requires the VDClip MCP connector (https://mcp.vdclip.com/mcp) and an authenticated VDClip account.
---

# VDClip

Turn long video into short-form content: generate clips with AI, render them, and publish.
Every job runs against the user's real account — credits get spent and posts go out
publicly, so quote costs and confirm before acting.

## Non-negotiable rules

- **Money and reach need approval.** Quote the credit cost before `create_project` (AI
  types) and before `render_clip` on an editor project. Get explicit approval of
  destination, copy, and time before publishing or scheduling.
- **Never invent an id.** `project_id`, `result_id`/`clip_id`, `preset_id`, `account_id`,
  `connection_id` and `post_id` all come from tool results.
- **Never blind-retry a write.** After a conflict, timeout, or uncertain result, read the
  current state first (`get_clip`, `list_calendar`, `get_project_status`). A blind retry
  double-posts or double-charges.
- **`cancel_post` is irreversible.** A cancelled post cannot be un-cancelled, only
  scheduled again from scratch. Confirm the exact posts first.
- **Timing is in seconds.** Everything the connector returns and accepts is seconds.
  Never send `frame`, `frames`, `fps` or `durationInFrames` in project data.
- **Report reality.** Surface warnings, skipped clips and error codes. Never claim a
  result the tool output does not show.

## Pick the workflow

| User wants | Go to |
| --- | --- |
| Clips or captions from a video URL | [create-clips.md](references/create-clips.md) |
| To know what a clip says, and when | [transcript.md](references/transcript.md) |
| To change an existing clip | [editing.md](references/editing.md) |
| An MP4 file to download | [rendering.md](references/rendering.md) |
| To post or schedule to social | [publishing.md](references/publishing.md) |

### 1. Create — AI pipeline, costs credits

`get_account` (plan, credits) → `estimate_cost` (clipping 1 credit/min, captions 2) →
confirm with the user → `create_project` → poll `get_project_status` → `list_clips`.

Ask for the content category and the clip length before creating; call `list_templates` if
the user wants a style preset and pass its id as `preset_id`. Enums, failure codes and the
credit-free `type: "editor"` branch are in [create-clips.md](references/create-clips.md) and
[project-options.md](references/project-options.md).

### 2. Inspect and edit

`get_project` opens the clip's project in the visual editor widget and returns its summary
(overlays, timing, version tag). `get_project_summary` returns the same summary without
opening the widget. `get_transcript` returns the timed text so you can say what is said and
when.

**Chat-driven editing is paused.** `apply_edits`, `save_project` and `compose_scenes` are
not advertised in `tools/list` and refuse with `feature_paused` if called from memory. Hand
the user off to the full editor — see [editing.md](references/editing.md).

### 3. Render

`render_clip` → poll `get_clip` until the render status is terminal → hand over
`download_url` (signed and time-limited; re-read `get_clip` for a fresh one).

Clipping and captions results were already charged at creation, so re-rendering them is
free. Editor projects bill at render time — call `estimate_cost({ type: "editor" })` first.
`method: "browser"` additionally needs `request_render_upload` → PUT → `confirm_render_upload`.
Details in [rendering.md](references/rendering.md).

### 4. Publish

`list_social_accounts` → confirm with the user → `publish_clip` (one clip) or
`schedule_clips_bulk` (many) → manage via `list_calendar`, `reschedule_post`, `cancel_post`.
Rules and limits in [publishing.md](references/publishing.md) and
[scheduling.md](references/scheduling.md).

For a read-only link instead of a social post: `get_project_share` then `set_project_share`.

## When things fail

[recovery.md](references/recovery.md) has the full error taxonomy. The short version:

- **`insufficient_credits`** — stop and say how short the user is. Do not retry.
- **`plan_gated` / `quota_exceeded`** — name the feature and the tier or limit. Do not work
  around it.
- **`unauthorized` / `forbidden`** — ask the user to reconnect or grant the scope.
- **`conflict`** — re-read the current state before deciding anything.
- **`feature_paused`** — chat editing is off; give the editor link from the error message.
- **Unknown outcome after a write** — read current state before any retry.

## Setup

MCP endpoint `https://mcp.vdclip.com/mcp`; per-host install notes in
[host-setup.md](references/host-setup.md). Authenticate through the host's OAuth flow and
never store tokens in files.

## Response style

Lead with the outcome — name the project and what changed, or the cost about to be spent.
Put warnings and blockers next. Offer at most three concrete next actions.
