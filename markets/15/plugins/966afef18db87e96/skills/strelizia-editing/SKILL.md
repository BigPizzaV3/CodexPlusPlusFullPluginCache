---
name: strelizia-editing
description: How to drive the Strelizia desktop editor through its tools — open sessions, pick highlights, cut shorts, edit the timeline, export.
---

# Working in Strelizia

Strelizia tools run inside the user's running desktop app. If a tool answers "앱이 꺼져 있습니다" (app offline), ask the user to open Strelizia, sign in, and turn on Cloud connection in Settings → Integrations → AI assistant, then retry.

## Ground rules
- All times are milliseconds. Timeline times refer to the active sequence; session times refer to the stream video.
- When the user says open, show or go to something, navigate the app: `open_project` for editor projects, `open_session` for analysis sessions, then `seek_session` / `play_session`. Do not only read data.
- Read `get_timeline` before editing and after a batch of edits. Every write tool is exactly one undo step; use `undo` to revert.
- Tools whose description says "크레딧이 차감됩니다" spend the user's credits (speech subtitles, shorts cutting, post-processing, session questions). Tell the user before calling them unless they already asked for exactly that.
- Destructive tools (delete, ripple, silence cuts, export, restore) prompt for confirmation; prefer them only when the user asked.

## Typical flows
1. **From a stream to shorts**: `list_sessions` → `open_session` → `get_chat_peaks` / `search_transcript` / `recommend_hot_clips` → `add_to_pick_board` for each moment → `create_shorts` (one vertical sequence per pick; poll `get_shorts_batch_status`) → `apply_shorts_style` / `set_shorts_subtitles` / `set_shorts_title` → `get_frame` to show the result → `start_export`.
2. **Long-form transcript edit**: `add_to_pick_board` (the part to keep) → `create_longform_edit` → `cut_longform_silence` (dry_run first) → `delete_transcript_range` for unwanted lines → `start_export`.
3. **Timeline edits on an open project**: `get_timeline` → `split_clip` / `trim_clip` / `move_clip` / `delete_clips` / `ripple_delete` → `add_text` / `add_effect` / `set_keyframe` / `apply_anim_preset` → `get_frame` at the changed time to verify.
4. **New footage**: `import_video_session` (local file) → `start_transcription` (poll `get_transcription_status`) → `start_chat_collect` with the VOD URL → `analyze_scenes`.

## Reporting
Answer in the user's language. After edits, say what changed in one or two lines and offer `undo`. Do not paste raw tool JSON.
