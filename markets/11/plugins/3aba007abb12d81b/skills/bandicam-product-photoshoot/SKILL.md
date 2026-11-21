---
name: bandicam-product-photoshoot
description: Create product photos with Bandicam AI from a product description or reference image. Use when the user asks for studio, lifestyle, catalog, or promotional product images, including a small set of visual variations.
---

# Bandicam AI product photoshoot

Create product images with the connected Bandicam AI MCP tools. This skill covers still images, not video ads, website design, or claims of exact product or logo reproduction. Use live catalog and job results; do not invent model IDs, supported options, credit costs, completed outputs, or URLs.

1. Identify the product and the requested image use: clean catalog photo, studio hero shot, lifestyle scene, or promotional concept. Preserve supplied product details, visible branding, colors, and composition requirements. If no reference image is available, describe the result as a concept based on the user's description; do not promise exact packaging or lettering.
2. If the user wants their actual product represented, use a reference image when available. Accept a usable asset ID or image URL. If they need to upload a local image in ChatGPT, call `show_upload` and wait for its returned asset ID in the conversation before generating. Do not call `create_upload` to handle the upload card, and do not assume an upload succeeded.
3. Call `list_models` with `category: "image"`, then with the chosen `model` ID to read full defaults, controls, and capabilities. For a reference image, choose a model that supports image references. For text-only concepts, choose a supported text-to-image model. Use the control `field` values as option keys; the category list alone does not include full options. If the requested feature is unavailable, explain the limitation before starting a job.
4. Draft a prompt for each requested image. Specify subject, camera framing, lighting, background, and intended use without adding unrequested claims about the product. If the user gives no number of images, make one. If they request a set, keep each variation distinct and state the number.
5. When the user wants a price first or sets a credit ceiling, call `quote_job` for each distinct model/options/input combination, including reference `input_urls`. Account for the number of requested images in the estimated total. Stop for an estimate-only request, an unverifiable budget, or a total above that budget. For an authorized generation without a price-first request, use the generation response's credit information. Stop on insufficient credits without purchase or checkout suggestions.
6. If the user asked only for concepts or estimates, stop after that information. If they asked to create images, call `generate_image` once per requested image, using the chosen model, prompt, reference `input_urls`, and supported options, matching any quote. For this one-job-per-image workflow, explicitly set the supported image-count control to 1 in both quotes and submissions (currently `imageCount` for many models). Do not combine N jobs with N images per job. Track the estimated total across the full requested set, including any requested finishing jobs. Do not generate extra variants or insert another cost-confirmation question.
7. Track each shot with its job ID. If part of a set fails, retain successful outputs and stop before starting unsubmitted shots; report completed, failed, and pending shots separately. A later retry must target only the shots the user requests, not regenerate the whole set.

Apply `remove_background` or an image upscaler only when requested, and include these separate jobs in any budget. Verify visible product details before claiming they were preserved.

## Results and recovery

- Let displayed cards track progress. Use `wait_for_job` for dependent steps, requested completion checks, or clients without cards. Keep polling the same ID through `running`, `processing`, or `deadline_reached`, within host limits; disclose unfinished work.
- Never resubmit an uncertain job. For `recovery_required`, call `resume_generation` with its ID. Without an ID, disclose uncertainty. Stop on failure or insufficient credits without purchase suggestions.
- `credits_quoted` is an estimate; `reserved` is not consumed. Report final `credits_cost` with `credit_status` for usage/refunds.
- Do not duplicate cards or call `show_creations` for new jobs. Otherwise use returned previews/`view_urls`; refresh expired links with `get_creation`. Claim content quality only after inspection, not from `completed` status alone.
