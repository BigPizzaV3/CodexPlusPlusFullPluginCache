---
name: idea-ai-asset-restoration
description: "Enhance or upscale existing images and video, or clean source audio, using idea.ai models selected for the source and requested improvement."
---

# Asset restoration

Read [the shared MCP workflow](../../references/mcp-workflow.md) before calling tools. It defines discovery, file handling, cost authorization, waiting, and delivery for this skill.

## MCP operation

Use `edit_image` for image enhancement, `create_video` for footage enhancement, and `create_audio` for audio cleanup. Upload and validate the source before pricing; request only the desired restoration operation.

## Assess the source and goal

Determine whether the user needs image upscaling, footage enhancement, frame-rate conversion, or audio cleanup. Use actual source metadata and inspect representative content when possible. Ask for a target resolution, frame rate, or loudness only when it affects the choice; avoid inventing detail that was not captured.

## Match the source to a model

Inspect current model constraints. Real-ESRGAN (`real_esrgan`) exposes `upscale_factor` and `output_format`, but its inspected source-image limit is 1024 by 1024 pixels. Topaz Proteus (`topaz_proteus`) exposes video `resolution` and `fps` with its own duration, dimension, and aspect-ratio limits.

VEED Clean Audio (`fal_veed_clean_audio_v1`) accepts either source video or source audio, with a combined maximum of one file; it exposes `strength`, `normalize_loudness`, `target_lufs`, and output format. Quote the selected source role with actual measured duration. Explain current reserve-and-settle guidance, including any source-role maximum reserved for URL-sourced audio, before spending. A quote is not automatically a hard spending cap. Cleaning a video's audio produces an audio asset, not necessarily a newly muxed video.

Reject an incompatible plan before upload or quoting. Use a supported alternative or a separately authorized preprocessing step rather than silently submitting a source outside the model's limits.

## Compare with the original

Assess halos, oversharpening, altered faces/textures, motion artifacts, unnatural interpolation, clipped sound, and excessive cleanup. Preserve the original. A larger file is not proof of added detail, and interpolation does not recover real captured frames.

Deliver the enhanced assets with actual returned metadata, selected settings, and any remaining defects. Reattaching cleaned audio or assembling outputs requires a tool that explicitly supports it.
