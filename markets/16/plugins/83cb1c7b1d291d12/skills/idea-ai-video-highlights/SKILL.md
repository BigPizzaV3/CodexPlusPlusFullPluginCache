---
name: idea-ai-video-highlights
description: "Extract highlights from longer footage with idea.ai using an editorial scoring brief and requested clip durations."
---

# Highlight clips

Read [the shared MCP workflow](../../references/mcp-workflow.md) before calling tools. It defines discovery, file handling, cost authorization, waiting, and delivery for this skill.

## MCP operation

Use `create_video` for highlight clipping after the free source upload is ready and its measured duration has been quoted. Optional transcription uses a separate, authorized `extract_text_from_media` operation on a model supporting `mediaToText`.

## Define what makes a highlight

Identify the source footage, audience, desired number of clips, duration targets, and editorial criteria. Use a supplied transcript or timecodes when available, but do not claim to have watched or transcribed footage the host cannot inspect.

Write a concrete scoring brief: the moments to favor, necessary context, and content to avoid cutting mid-action. Keep extraction separate from captioning, reframing, soundtrack changes, or publishing.

## Validate the clipping model

Inspect BytePlus Highlight Clipping (`byteplus_video_highlights_v1`). Its inspected contract accepts source video from 10 seconds to three hours and up to five `targetDurations`, each 1–600 seconds. It also exposes `scoringPrompt`; its only named preset is `football`, so do not invent other preset values or assume that preset fits every genre.

Check current file-size and format limits. Quote using the actual source duration and requested `targetDurations`. Use the free upload flow to obtain measured duration before quoting; do not guess a clip's length for billing.

## Review the selected moments

Check that returned clips match the scoring intent, include enough context, begin and end coherently, and meet the requested durations. Report when semantic relevance cannot be reviewed. If the result misses the brief, explain the specific mismatch before an authorized revision.

Deliver the actual clips and returned timing information. Do not fabricate source timecodes, assume multiple outputs from a successful status, or claim social publication. Captioning and format adaptation are optional additional steps with their own tools and costs.
