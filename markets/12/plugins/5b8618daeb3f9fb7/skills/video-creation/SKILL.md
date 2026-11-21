---
name: video-creation
description: Generate product promotion, UGC-style and close-up videos through Designkit's
  unified designkit_create_task tool, then check progress and actual video media with
  designkit_get_artifacts. Also use for video briefs, scripts and shot plans; a planning
  request alone does not authorize generation.
---

# Video creation

Designkit generates images and videos through the same `designkit_create_task` entrypoint. For a video-production request, specify video output, duration, aspect ratio and available references in the task brief, then follow `designkit_get_artifacts`. A dedicated video-generation or video-export tool is not required. `designkit_get_profile` returns account identity only; it does not enumerate capabilities or prove that upstream generation login is healthy.

Use this expert when the user wants a product promotion video, a UGC-style product video, or a product close-up. Support both a complete brief and an early idea that needs a short script or shot plan. A request for ideas or a script alone does not authorize paid video production.

Read the [bundled video presets](references/presets.json), choose the one that fits the user's intent, then read [the video workflow](references/video-workflow.md) and [the MCP workflow](references/mcp-workflow.md). Local preset aliases are conversational shorthand, not registered host commands or server-side IDs.

Reuse the supplied material, product facts, language, duration, ratio and creative choices. Ask only for missing information that affects the requested result. When the user explicitly requests a fictional product concept, do not require a nonexistent product photograph. When accurate depiction of an actual product matters, obtain usable source material.

For production, hand the brief to the existing Designkit task tools using their actual schemas. Do not invent a video-generation tool, a model route, a preset-resolver API or a dedicated voice/character parameter. Follow real server questions and account requirements. A successful submission is not a completed video.

Return the actual video artifact and available playback/download links. If the backend returns only a storyboard, image, script, question or error, identify that result accurately instead of claiming the video is finished. Do not silently substitute an image for the requested video.
