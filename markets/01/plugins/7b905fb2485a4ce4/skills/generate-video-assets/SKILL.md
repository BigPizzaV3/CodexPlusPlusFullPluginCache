---
name: generate-video-assets
description: "Generation: create a complete vertical video from an idea or script, or generate one image, video clip, voiceover, music track, or sound effect with BlitzReels."
---

# Generation

Choose one generation branch, confirm material cost or likeness choices, and return verified results.

## 1. Route the request

- Preserve the user's prompt, script, narration, and aspect ratio.
- Call `generation_options_list` when model, duration, voice, style, or aspect ratio remains unresolved.
- Ask one focused question when a missing choice changes the output or cost.
- For a reusable visual system, inspect it with `story_kits_list` and `story_kits_get`.
- For an existing character, inspect it with `characters_list` and `characters_get`; call `characters_apply` after
  the user confirms the rights and likeness consent required by the tool.

Completion: one supported branch with every material input resolved.

## 2. Complete-video branch

- Call `generation_plan_brief` to convert the idea or script into a production brief.
- Call `generation_plan_validate`; surface every warning, required choice, and cost before generation.
- Call `generation_faceless_create` once for the approved brief.
- Preserve the returned project, revision, and job IDs.

Completion: one accepted full-video job tied to a verified project and revision.

## 3. Single-asset branch

- Select exactly one matching tool: `generation_image_create`, `generation_video_create`,
  `generation_voiceover_create`, `generation_music_create`, or `generation_sound_create`.
- Generate only the requested asset type with the resolved inputs.

Completion: one accepted asset job with every returned identifier retained.

## 4. Follow and deliver

- Follow an active job with `generation_jobs_get` within its returned polling guidance.
- Call `generation_jobs_cancel` when the user explicitly asks to cancel that job.
- After an ambiguous timeout, inspect the existing job before deciding whether another creation is needed.
- Return verified project, revision, job, and asset IDs; status; warnings; preview or download URLs; and the next
  available action.

Completion: a verified terminal result or the latest explicit active or blocked state.
