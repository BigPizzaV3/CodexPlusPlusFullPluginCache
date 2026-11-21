---
name: bandicam-image-to-video
description: Animate a reference image or an earlier Bandicam AI image into a video. Use for requests to bring a photo, illustration, or product image to life with subject or camera motion.
---

# Bandicam AI image to video

Use this workflow when the user supplies a starting image or identifies an earlier creation. For motion transfer from a reference video, use the motion-control workflow instead.

1. Resolve the starting image from a supplied URL or asset ID. For an earlier Bandicam creation, use its known job ID with `get_creation` to obtain fresh references; use `list_creations` only when you need to find the intended image. If several match, ask which one. Do not generate a replacement starting image without a request to do so.
2. Chat attachments are not automatically accessible to the MCP server. If there is no usable reference, call `show_upload` and wait for the asset ID in a follow-up message or context. The upload card handles storage; do not call `create_upload` for that same file or look for the new upload in `show_assets` before it has been used.
3. Call `list_models` with `category: "video"`, then with `model` set to a chosen returned ID to read its defaults, controls, and capabilities. Choose an image-to-video model that accepts the image and requested duration or format. Take option names from the actual control `field` values, not the control group labels. Keep the user's selected model when supported.
4. Write a motion-focused prompt: what moves, how it moves, camera movement, and the desired final state. Preserve the image's subject and style unless the user requested a change. Do not promise exact frame, identity, or text preservation. Pass the image reference in `input_urls`; a description of the image alone is not a reference input.
5. If the user asks for a price first or sets a credit ceiling, use `quote_job` with the selected model ID, intended options, and image input. Treat the result as an estimate. Stop before generating if the user asked only for an estimate, the budget cannot be checked, or the estimate exceeds the budget.
6. For a request to create the video, call `generate_video` once with that model, prompt, image reference, and supported options. Generate only the requested number of clips; default to one when no number is given. A request to create already authorizes the requested generation; do not insert another cost-confirmation question.

## Results and recovery

- Let displayed cards track progress. Use `wait_for_job` for dependent steps, requested completion checks, or clients without cards. Keep polling the same ID through `running`, `processing`, or `deadline_reached`, within host limits; disclose unfinished work.
- Never resubmit an uncertain job. For `recovery_required`, call `resume_generation` with its ID. Without an ID, disclose uncertainty. Stop on failure or insufficient credits without purchase suggestions.
- `credits_quoted` is an estimate; `reserved` is not consumed. Report final `credits_cost` with `credit_status` for usage/refunds.
- Do not duplicate cards or call `show_creations` for new jobs. Otherwise use returned previews/`view_urls`; refresh expired links with `get_creation`. Claim content quality only after inspection, not from `completed` status alone.
