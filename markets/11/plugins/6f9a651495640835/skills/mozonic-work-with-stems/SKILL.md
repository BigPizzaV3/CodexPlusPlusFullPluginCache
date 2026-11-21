---
name: mozonic-work-with-stems
description: Use when the user has multiple stem files (drums, bass, vocals, …) or a folder/ZIP of stems and wants Mozonic to analyze them or render a mixed (optionally mastered) bounce.
---

# Work with stems in Mozonic

## 1. Find an existing stem session

The directory plugin works with stem sessions already created in the Mozonic
app. For local stem files or a ZIP, direct the user to upload and create the
session at https://app.mozonic.com first. Then find it with
`mozonic_list_stem_sessions` and inspect it with
`mozonic_get_stem_session(session_id=...)`.

## 2. Render

When analysis is done:
`mozonic_render_stem_session(session_id=..., output_mode=...)`

- `output_mode="mix"` — balanced stereo bounce
- `output_mode="mastered_mix"` — bounce + mastering; add `target_profile`
  (streaming_default, loud_streaming, club_loud, podcast, commercial_loud)

Also async — poll, then fetch artifacts with
`mozonic_download_stem_session(session_id=...)`.
