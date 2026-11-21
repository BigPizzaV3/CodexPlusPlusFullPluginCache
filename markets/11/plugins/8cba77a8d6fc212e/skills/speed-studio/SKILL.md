---
name: speed-studio
description: Speed up or slow down a short video with matching audio tempo. Choose 0.5, 0.75, 1.25, 1.5 or 2 times playback speed. Preview and download the completed MP4 inline.
---

Use the connected Firemoon Speed Studio tools. Call speed_studio_retime using rate and an actual video attachment reference or user-supplied HTTPS URL. Do not guess inaccessible local file paths, fabricate IDs, or substitute native generation. Ask for missing edit settings.

Sources may be up to ten seconds and 50 MB. The editor file picker accepts up to 2 MB; use chat attachments for larger files when the host supplies a downloadable reference.

Return the actual inline media widget with fullscreen and download controls. Open speed_studio_open only for the dedicated editing controls. For a saved result that no longer loads, call speed_studio_preview with the original job_id, never create another edit.

Keep one stable request_id for identical inputs and settings. After interruption recover that same request; do not start an automatic duplicate. Preserve partial results and report failures accurately.

Media is processed by Firemoon. Anyone holding an output link can access it. Do not download or execute outside code.
