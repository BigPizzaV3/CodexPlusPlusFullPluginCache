---
name: idea-ai-motion-transfer
description: "Animate a supplied character or subject using motion from a reference video through idea.ai motion-control models."
---

# Motion transfer

Read [the shared MCP workflow](../../references/mcp-workflow.md) before calling tools. It defines discovery, file handling, cost authorization, waiting, and delivery for this skill.

## MCP operation

Use free `upload_media` with both motion input slots when the files are on the user’s device, resolve ready uploads and measured metadata, then quote and use `create_video`. Uploading the references does not start animation.

## Establish the two references

Identify the character/subject image and the motion video. Clarify whether the user wants the clip's movement, camera behavior, and original sound preserved; those are separate choices. Inspect the image and clip when available to describe what can be transferred and flag mismatched framing or visibility.

## Validate the model inputs

Inspect Kling V3 Motion Control (`kling_v3_motion_control`) or another available motion-control model. Its inspected schema requires paired `motionImage` and `motionVideo` roles, with a 3–10-second motion video. Validate current duration, format, image dimensions, and size limits before scheduling a generation.

Use the returned `character_orientation`, `keep_original_sound`, and `mode` choices where supported. Do not invent a skeleton, pose track, or character ID. Model controls may not isolate every aspect of motion from camera behavior.

For user-owned files, declare both required inputs in one authorized upload request. For assets already generated through the MCP, reuse their URLs with the correct roles.

## Assess the result

Review movement timing, body/subject proportions, identity, framing, unintended distortions, and the requested sound treatment. Do not claim frame-accurate motion capture or perfect identity preservation from a completed status alone.

If the reference clip is outside the model's limits, ask for a suitable excerpt or use separately authorized trimming tools that are actually available. Do not silently submit unsupported media or repeatedly retry it.

Deliver the result with the source references and a concise account of any motion or identity differences that remain.
