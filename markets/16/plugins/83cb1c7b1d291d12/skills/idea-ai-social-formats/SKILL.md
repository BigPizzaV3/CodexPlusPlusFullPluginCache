---
name: idea-ai-social-formats
description: "Adapt an approved image into multiple social or advertising layouts using idea.ai resizing and outpainting controls."
---

# Social image formats

Read [the shared MCP workflow](../../references/mcp-workflow.md) before calling tools. It defines discovery, file handling, cost authorization, waiting, and delivery for this skill.

## MCP operation

Use `edit_image` with the selected resize or outpaint model. A local source can be uploaded and measured for free before pricing; the adaptation itself is a paid operation.

## Establish the format plan

Use the approved source image and the user's target placements or exact dimensions. Confirm focal subjects, text/logos that must survive, and areas reserved for copy. When dimensions are unspecified, propose aspect ratios as creative choices; do not invent current platform advertising requirements.

## Choose resize versus outpaint

Inspect Smart Resize (`fal_smart_resize`) for an available `targetSize`. Inspect Recraft V3 Outpaint (`recraft_v3_outpaint`) when the image needs additional canvas; it exposes independent expansion directions and `zoom_out_percentage`.

Choose the least disruptive supported operation. Resizing a composition and generating new surrounding content have different effects, so describe which is planned. Validate source dimensions and size limits. Price each output and keep its relationship to the original reference clear.

## Review the adaptations

Check focal-subject visibility, crop boundaries, stretched proportions, text legibility, logo integrity, new visual artifacts, and usable copy space. Compare new surrounding content with the source's lighting, perspective, and style. Keep accepted variants and repair only failed ones.

Do not silently replace exact brand text or treat generated text as an approved final layout. If a placement needs accurate typography or a layout operation not exposed by the tools, identify that finishing step.

Deliver a labeled set with actual returned dimensions and intended placement. These tools create image assets; they do not publish posts, configure ad campaigns, or certify platform approval.
