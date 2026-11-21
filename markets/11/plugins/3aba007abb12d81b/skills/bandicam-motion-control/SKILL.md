---
name: bandicam-motion-control
description: Transfer movement from a reference video to a character image using Bandicam AI. Use when the user wants a pictured character to follow an existing dance, gesture, or movement clip.
---

# Bandicam AI motion control

This workflow needs a character image and a motion reference video. It does not provide general timeline editing, animated typography, or motion graphics composition.

1. Identify which input is the character image and which is the motion reference. Use supplied URLs or asset IDs, or `get_creation` for a known earlier Bandicam output. If an input is missing, call `show_upload` and wait for its asset ID; do not guess an attachment URL. Preserve both references while collecting the second input. Do not create a substitute reference video unless the user requests it.
2. Call `list_models` with `category: "video"`, find the motion-control presets, then call `list_models` with the chosen full `model` ID. Read its input capabilities, defaults, and controls. Check known file type, dimensions, and duration against those capabilities; do not claim validation of metadata you cannot inspect. If a file is rejected, report the specific limit returned by the server.
3. Use `input_urls` for the character image and reference video. Resolve `variant` from the current `create_motion_control_video` input schema. `quote_job` takes the full model ID; the generation tool accepts the exact strings in its variant enum. Currently the model `ai-motion-control-kling-26` maps to variant `26`, and `ai-motion-control-kling-30` to `30`. Recheck both the catalog and enum before using these examples. Other tools may accept full model IDs as variants, so do not apply this shortening rule to them.
4. Keep optional prompting about the intended character, scene, or motion faithful to the request. Use only options supported by the selected model's controls or defaults. Apply a request about retaining reference audio only if the model exposes that option; do not claim motion transfer also clones a voice or guarantees exact identity.
5. For a cost-first request or stated credit ceiling, call `quote_job` with the exact model, options, and both input references. Costs can depend on the reference video, so do not quote an empty-input job as this job's price. If the requested budget cannot be verified or the quote exceeds it, stop and explain.
6. If the user requested generation and inputs are ready, call `create_motion_control_video` once. If they requested only a feasibility check or estimate, provide that without starting a job. Do not generate extra variants or add an upscaling job automatically.

## Results and recovery

- Let displayed cards track progress. Use `wait_for_job` for dependent steps, requested completion checks, or clients without cards. Keep polling the same ID through `running`, `processing`, or `deadline_reached`, within host limits; disclose unfinished work.
- Never resubmit an uncertain job. For `recovery_required`, call `resume_generation` with its ID. Without an ID, disclose uncertainty. Stop on failure or insufficient credits without purchase suggestions.
- `credits_quoted` is an estimate; `reserved` is not consumed. Report final `credits_cost` with `credit_status` for usage/refunds.
- Do not duplicate cards or call `show_creations` for new jobs. Otherwise use returned previews/`view_urls`; refresh expired links with `get_creation`. Claim content quality only after inspection, not from `completed` status alone.
