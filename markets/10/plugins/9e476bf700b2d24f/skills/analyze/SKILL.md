---
name: analyze
description: Analyze one or more videos
---
Analyze these videos: $ARGUMENTS

Use the `analyze_video` tool. For a single video, pass it as the `url` (TikTok, Instagram, or YouTube Shorts) or as a `video_uuid` if it looks like a UUID. The tool queues the analysis and never returns it, so call `get_video_details` about 30 seconds later, then every 30 seconds until the analysis is complete, and summarize it covering the hook, format, narrative structure, topic, and any other key components.

For more than one video, pass them all in a single call as `videos` instead of calling once per video. Then tell the user how many were queued, list any that were skipped with the reason, and let them know the analyses will be ready in a few minutes rather than checking each one.

If `$ARGUMENTS` is empty, ask the user which videos they want analyzed.
