---
name: edit-and-export-video
description: "Editing: change or export a BlitzReels project. Use for timeline, caption, media, text, audio, transition, layout, or export requests."
---

# Editing

Preview one bounded project change, apply it once, verify the resulting state, and export when requested.

## 1. Resolve the project

- Use `projects_get` when the user identified a project.
- Otherwise call `projects_list`; ask the user only when several plausible projects remain.
- Call `projects_inspect` when the edit needs detailed timeline or caption context.

Completion: one verified project ID and every ID or time range required by the edit.

## 2. Preview the change

- Prefer `timeline_edit_preview` when it supports the requested mutation.
- Prefer `timeline_edit_apply` or `batch_update_timeline_clips` for coordinated edits.
- For one bounded operation, use the matching focused tool: `update_timeline_clip`, `timeline_media_add`,
  `timeline_audio_add`, `add_text_overlay`, `add_transition`, `mute_clip_audio`, or `delete_timeline_items`.
- Resolve media through `media_list` or `media_assets_get`; call `media_assets_preview` when the choice is uncertain.
- Resolve every item ID, time range, and destructive target from tool state or the user's selection.

Completion: a reviewed preview or an unambiguous mutation plan that accounts for every target.

## 3. Apply and verify

- Apply the approved change once.
- Re-read the project or affected timeline state.
- On a stale ID or conflict, discard the pending edit, refresh context, and resolve the target again.
- After an ambiguous response, inspect current state before deciding whether a retry is needed.
- For partial batch failure, account for every item and retry only verified failures.

Completion: every requested change is proven by follow-up state, with receipts and warnings reported.

## 4. Export

- Call `exports_start` when the user requested export or approves it after previewing the edit.
- Follow that export with `exports_list` until its terminal state.
- Return a download URL only when the tool reports it ready.

Completion: verified project and item IDs, changed state, warnings, export status, and available download URL.
