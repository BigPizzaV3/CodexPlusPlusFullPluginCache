---
name: gilmos-storyboards
description: "Prepare gilmOS scene breakdowns, shot lists and storyboard boards, or create the next shot with narrative and visual continuity. Use for scene-to-shot planning; media generation is a separate operation."
---

# Turn a scene into shots and a storyboard

Read the project and the actual target scene, using paginated `gilmos_read_resources` if it is outside the bounded context. Match “scene 3” by `scene_num=3`; filter shots by that scene's UUID and order by `sort_order`/`shot_num`. Inspect existing descriptions, current prompts, selected asset versions and approved media before making “the next shot.”

The user's explicit names, characters, places and previous creative choices take priority. Preserve continuity of action, eyelines, screen direction, geography, lighting and props. A useful shot description specifies its dramatic purpose, action, framing, lens where meaningful, movement, duration and sound. `stillPrompt` describes the still; `dynamicPrompt` describes movement over time. Use exact project asset tags for characters/locations/props in those prompts.

## Persist a shot list or scene change

Use `gilmos_create_plans` with the scene ID and a `payload.plans` array. It appends shots; it does not replace the existing list. Keep the requested count, and inspect existing shots after an uncertain response before retrying. Use `gilmos_update_plan` for an existing shot description, and `gilmos_update_scene` for the requested scene title/text. These tools do not rewrite individual shot-version prompts.

Use `gilmos_create_scenes` only for production scenes that do not already exist, and `gilmos_create_sequences` for sequence structure. Do not create duplicate scenes after a screenplay save that already synchronized them. Respect the tool's per-call limits and work in coherent batches when necessary.

When the request is only an image of the next shot, creating a shot record is optional and depends on the user's intended destination. `gilmos_generate_media` creates a global sandbox item; it does not attach that image to a shot version. State the actual destination and do not claim a link that was not saved.

## Delegate a persistent breakdown/storyboard batch

Use `gilmos_start_scene_storyboard_workflow` once for the explicitly selected scenes. Prefer exact `resourceIds`; `sceneNumbers` is available when unambiguous. Omitting selectors can include the whole project, so never omit them for a single-scene request.

Choose `payload.steps` deliberately:

- `breakdown`: technical breakdown only, without storyboard image generation.
- `storyboard`: boards from existing breakdowns.
- `both`: breakdown followed by storyboard generation.

Preserve model, resolution, language and instruction when supplied. Storyboard images consume credits; an explicit request for a stated batch authorizes that batch, not additional scenes or repeated variants. Clarify an unspecified batch scope before launching it.

Track the returned job with `gilmos_get_alfred_workflow_status`; use `gilmos_stop_alfred_workflow` if the user asks to stop. Read back the relevant scene versions and returned result after completion. A storyboard board is scene output, not proof that separate shot images/videos were generated. Its technical storage fields can still contain `storygrid`; call the product a storyboard board, not a narrative Story Grid analysis.

Read [examples.json](references/examples.json) when constructing exact shot-list or workflow arguments. Finish with the actual scene number, saved shots/versions, and state of any active workflow.
