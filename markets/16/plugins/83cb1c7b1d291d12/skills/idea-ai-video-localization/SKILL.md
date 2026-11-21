---
name: idea-ai-video-localization
description: "Create dubbed or subtitled language versions of an existing video with idea.ai while preserving approved terminology and presentation."
---

# Video localization

Read [the shared MCP workflow](../../references/mcp-workflow.md) before calling tools. It defines discovery, file handling, cost authorization, waiting, and delivery for this skill.

## MCP operation

Use `create_video` separately for dubbing and subtitles. If transcription is requested, discover a compatible `mediaToText` model and price `extract_text_from_media` as a separate paid operation; do not silently transcribe just to inspect the source.

## Define the language versions

Identify the source video, source language, target languages, audience, pronunciation needs, and any supplied script, glossary, or SRT. Keep proper names, numbers, product terminology, and approved claims consistent. Separate translation, dubbing, and subtitle styling so each requested operation is explicit.

## Inspect dubbing and subtitle controls

Inspect VEED Dubbing Pro (`veed_dubbing_pro_v1`) or another available dubbing model. Its inspected schema exposes `source_language`, `target_language`, and `voice_cloning_strength`; use only returned language values. Do not assume global plugin availability means that a model supports every language.

Inspect VEED Subtitles (`fal_veed_subtitles_v1`) for captioning. Its contract requires a subtitle `preset` and supports `language`, optional `srt_content`, and style customization. Preserve user-supplied timing and wording unless an adjustment is requested. Confirm current file duration and size limits for each step.

Quote each language version and each subsequent subtitle operation separately. Where an output feeds the next operation, use its generated URL rather than asking for another upload.

## Review the localized versions

Check terminology, pronunciation, translation meaning, timing, voice treatment, subtitle contrast, line breaks, safe placement, and overflow. If the host cannot play audio or inspect target-language content adequately, describe that limit and request a fluent review instead of declaring linguistic accuracy.

Deliver clearly labeled language versions and list the original and translated wording when available. Do not claim to export an editable subtitle file merely because subtitles were burned into a returned video; verify the actual output artifacts.
