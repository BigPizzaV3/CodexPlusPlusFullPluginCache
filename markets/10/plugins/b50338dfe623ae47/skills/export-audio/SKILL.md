---
name: export-audio
description: Give the user a downloadable WAV or MP3 of a saved CookUp session, for example "export this as a WAV", "send me an MP3" or "bounce the beat". Use for finished audio files, not for listening to drafts while composing.
---

# Export audio

Explicit user instructions always take priority over these guidelines.

## Steps
1. **Which session.** Use the session in use, or the one the user names. Read its current version with `get_edit_context` or `get_session`.
2. **Format.** Call `export_session_audio` with the code, `expectedVersion` and format:
   - `wav`: stereo 16-bit;
   - `mp3`: 320 kbps.

   If the user didn't say, use WAV.
3. **Get the file.**
   - If the status is `server-render-queued`, call `get_audio_export` with the returned `previewId` and the same `expectedVersion`. It waits for the file.
   - Otherwise the CookUp panel renders it: call `open_session` once if no panel is open, tell the user to tap Render export if asked, then call `get_audio_export`.
4. **Finish.** `get_audio_export` shows the file card with playback and save controls. Make it the last card; do not call `open_session` after it.

## Limits
- Exports cover the saved arrangement, up to 10 minutes.
- Built-in effects, buses, sends and automation are included. External VST plugins are not.

## Never
- Say a file is ready while the export is pending.
- Send the user to the website for the download.
- Call `listen_audio_preview` on an export.
