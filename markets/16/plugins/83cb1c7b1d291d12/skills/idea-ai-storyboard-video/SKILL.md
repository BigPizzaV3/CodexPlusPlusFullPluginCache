---
name: idea-ai-storyboard-video
description: "Turn a creative brief into a storyboard, approved keyframes, and individual generated video shots with idea.ai."
---

# Storyboard to video clips

Read [the shared MCP workflow](../../references/mcp-workflow.md) before calling tools. It defines discovery, file handling, cost authorization, waiting, and delivery for this skill.

## MCP operation

Use `create_image` or `edit_image` for keyframes, then `create_video` for each approved shot or extension. The operation selects text versus media mode from the supplied files; it does not take a `modality` parameter.

## Plan the shots

Translate the brief into a shot list with action, subject, framing, camera motion, intended duration, aspect ratio, and audio requirements. Preserve approved character/product references and continuity. Distinguish an individual clip from an assembled finished film.

Create or reuse keyframes before animating when they materially improve control. Get approval for an unsettled visual direction before generating the remaining shots. Include keyframe creation and each video shot in the budget.

## Choose valid video inputs

Inspect video models with `get_model`. Seedance 2.5 (`seedance_v2_5`) supports either first/last-frame inputs or named image/audio/video references; its inspected cross-role rules make those groups mutually exclusive. A last frame requires a first frame. Runway Gen-4.5 (`runway_gen4_5`) exposes a first-frame input.

Use the chosen model's actual duration, resolution, and aspect-ratio controls. Do not combine incompatible input groups or assume that adding sound references creates a complete mixed soundtrack. Seedance's Extend variant (`seedance_v2_5_video_extended`) has a combined source-plus-extension duration limit; inspect it before proposing an extension.

## Generate and review shots

Keep each prompt focused on the shot's visible action and camera behavior. Reuse approved source images by URL. Review subject identity, product fidelity, continuity, requested motion, framing, timing, and artifacts. Revise the affected shot rather than regenerating the entire storyboard.

Deliver numbered clips with the shot list, durations, keyframes, and editing notes. The exposed tools do not include a general timeline-assembly or editing-project export tool. If a finished edited film is requested, explain which assembly step needs additional tooling instead of claiming that independent clips are a completed edit.
