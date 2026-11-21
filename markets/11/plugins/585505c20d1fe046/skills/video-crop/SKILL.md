---
name: video-crop
description: Center-crop a short video to landscape, portrait or square. Timing and audio are preserved. Review the framing and download the completed MP4 inline.
---

Use the connected Firemoon Video Crop tools. Call video_crop_crop using format and an actual video attachment reference or user-supplied HTTPS URL. Do not guess inaccessible local file paths, fabricate IDs, or substitute native generation. Ask for missing edit settings.

Sources may be up to ten seconds and 50 MB. The editor file picker accepts up to 2 MB; use chat attachments for larger files when the host supplies a downloadable reference.

Return the actual inline media widget with fullscreen and download controls. Open video_crop_open only for the dedicated editing controls. For a saved result that no longer loads, call video_crop_preview with the original job_id, never create another edit.

Keep one stable request_id for identical inputs and settings. After interruption recover that same request; do not start an automatic duplicate. Preserve partial results and report failures accurately.

Media is processed by Firemoon. Anyone holding an output link can access it. Do not download or execute outside code.
