---
name: bandicam-thumbnail
description: Create a YouTube thumbnail or vertical video cover with Bandicam AI from a topic and optional reference images. Use for thumbnail concepts, a requested final image, or revisions to an existing cover.
---

# Bandicam AI thumbnail

Create one clear still image for a specific video topic. Use this workflow for a video cover, rather than a product catalog photoshoot or a general image request.

1. Identify the video's real topic and intended surface. Use a supplied title, brief, or reference; ask for the topic if it is missing. Default to a landscape composition for a YouTube thumbnail and portrait for a vertical cover, using only a model-supported aspect ratio. Keep any headline tied to the actual content rather than adding invented claims or events.
2. Choose a readable composition: one focal subject, useful visual contrast, and space for short text only when text is wanted. Preserve the user's headline exactly if supplied. If they ask for concepts, provide concise alternatives without generating each one. Generate one image by default; create additional versions only when requested.
3. For a supplied face, logo, or prior thumbnail, use a usable URL or asset ID as `input_urls`. Resolve an earlier known Bandicam creation with `get_creation` for fresh references. When a chat image cannot be forwarded, call `show_upload` and wait for its asset ID. Do not imply you used a reference that never reached the tool.
4. Call `list_models` with `category: "image"`, then with the selected model ID to read full defaults, controls, and capabilities. Choose a reference-capable model for edits and use only supported controls, taking option keys from their `field` values. Treat a requested pixel size as a constraint to check; do not claim an exact export size that the tool does not support.
5. Prompt for the topic, focal subject, layout, background, lighting, and requested headline. For revisions, keep the original reference and describe the requested changes. Image generation may alter lettering or likeness: do not promise exact logo or text reproduction, editable layers, click-through rates, or deterministic text overlays.
6. Set the model's supported image-count control explicitly in both quote and generation options. For different concepts, use one job per concept with one image per job; for identical-prompt variations, use either a supported batch or individual jobs, not both. Count all outputs toward the requested quantity. If the user requests a price first or supplies a credit ceiling, call `quote_job` with the chosen model, options, and reference inputs and calculate the total for all planned jobs. Stop for an estimate-only request, insufficient credits, an unverified budget, or a total above the budget. Call `generate_image` only when the user requested actual image creation, without an extra confirmation question. For concepts or estimates alone, return that information and stop.

For a requested revision, use the existing image reference and change only the requested elements. It is another paid job. In a set, keep each concept tied to its job ID; retain successful outputs and do not retry the whole set after a partial failure. Check lettering, cropping, and reference consistency when the result can be inspected.

## Results and recovery

- Let displayed cards track progress. Use `wait_for_job` for dependent steps, requested completion checks, or clients without cards. Keep polling the same ID through `running`, `processing`, or `deadline_reached`, within host limits; disclose unfinished work.
- Never resubmit an uncertain job. For `recovery_required`, call `resume_generation` with its ID. Without an ID, disclose uncertainty. Stop on failure or insufficient credits without purchase suggestions.
- `credits_quoted` is an estimate; `reserved` is not consumed. Report final `credits_cost` with `credit_status` for usage/refunds.
- Do not duplicate cards or call `show_creations` for new jobs. Otherwise use returned previews/`view_urls`; refresh expired links with `get_creation`. Claim content quality only after inspection, not from `completed` status alone.
