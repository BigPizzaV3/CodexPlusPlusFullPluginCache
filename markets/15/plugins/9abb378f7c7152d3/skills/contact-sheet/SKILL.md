---
name: contact-sheet
description: "Decode actual selected short-video frames into labelled PNG contact sheets, bounded PNG thumbnails and exact source PTS/index ZIP exports."
---

# Contact Sheet

Require one actual short H.264 8-bit SDR MP4/MOV attachment or HTTPS reference. Limits: 50 MB, 10 seconds, 2–600 container frames, 1920 pixels per side and 2.1 megapixels. Inspection reads container metadata without proving decode compatibility. Export checks actual timestamps, 8-bit format and pixel aspect; explicit non-square aspect is rejected, unspecified uses a disclosed square default. Choose 2–8 uniform frame-index samples or 1–8 unique explicit zero-based frame_indices, and 1–4 columns. Explicit order is retained even when nonchronological. Sampling is based on container frame indices, not equal time intervals, scene cuts or semantic shot selection. Never infer exact variable-frame-rate indices from average FPS. Labels use actual decoded source PTS, rounded for display; JSON preserves returned numeric PTS. PTS need not start at zero. PNG thumbnails fit within 384x384 without enlargement; do not promise full-resolution or certified source color preservation. Show the real contact sheet and actual ZIP/index downloads. The ZIP includes selected frames, sheet, JSON and readme. Source is downloaded without rehosting; outputs are public. Preserve the ZIP if an optional sheet/index save fails. Reopen exact returned URLs without decoding again. Do not generate substitute frames, storyboards, cuts or descriptions. If tools are unavailable, report that rather than simulating exports.

For inspect/create, preserve the actual returned data as text. After create, call contact_sheet_preview with the returned images[0].imageUrl, or the returned ZIP URL if a standalone PNG is unavailable, to show the real app. Provide exact returned links and do not substitute guessed paths. Avoid duplicate Markdown image thumbnails outside the app.
