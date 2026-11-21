---
name: bandicam-text-to-video
description: Create a video from a text prompt with Bandicam AI. Use for text-only video creation, model selection, or cost estimates; use image-to-video or motion control when the request supplies those references.
---

# Bandicam AI text-to-video

Use this workflow for text-only video requests. For a supplied starting image or motion-reference video, use the corresponding image-to-video or motion-control workflow. Use the connected Bandicam AI MCP tools for live model information, prices, account access, and generation. Do not invent model IDs, supported options, credit costs, job states, or result URLs.

1. Turn the user's idea into a concise video prompt. Preserve the requested subject, action, setting, mood, and format. Ask only for a detail that is necessary to choose a supported model or submit the job; otherwise use the user's wording.
2. Call `list_models` with `category: "video"`, then with the chosen `model` ID to read full defaults, controls, and capabilities. Choose a text-to-video model that supports the request. If the user names a model, match it to a returned ID; if unavailable, explain the mismatch and offer a supported option. Use actual control `field` names and supported values; the category list alone does not include full options.
3. Call `quote_job` with that model ID and the intended options when the user wants a price first or sets a credit ceiling. Report it as an estimate. Stop for an estimate-only request, an unverifiable budget, or an estimate above the budget. Otherwise generation returns its own credit information, so a separate quote is unnecessary. Stop on insufficient credits without purchase or checkout suggestions.
4. If the user requested only an idea, comparison, or estimate, stop after providing that information. If the user asked to create the video, call `generate_video` once with the chosen model, prompt, and supported options, matching any quote. Do not submit multiple variants unless requested or insert another cost-confirmation question.

## Results and recovery

- Let displayed cards track progress. Use `wait_for_job` for dependent steps, requested completion checks, or clients without cards. Keep polling the same ID through `running`, `processing`, or `deadline_reached`, within host limits; disclose unfinished work.
- Never resubmit an uncertain job. For `recovery_required`, call `resume_generation` with its ID. Without an ID, disclose uncertainty. Stop on failure or insufficient credits without purchase suggestions.
- `credits_quoted` is an estimate; `reserved` is not consumed. Report final `credits_cost` with `credit_status` for usage/refunds.
- Do not duplicate cards or call `show_creations` for new jobs. Otherwise use returned previews/`view_urls`; refresh expired links with `get_creation`. Claim content quality only after inspection, not from `completed` status alone.
