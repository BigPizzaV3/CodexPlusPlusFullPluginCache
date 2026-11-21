---
name: footage-transformation-vfx
description: "For editing existing footage or adding VFX to it, use the source video, the requested change and the chosen model's contract to define what stays, what changes and how the effect blends in over time, including the frame-first path for an exact subject from a photo. Not needed for a new scene generated from text or an image."
metadata:
  version: skill-render-ea6bd93365667f6d
---

# VFX transformation of existing footage

This skill applies when the starting point is an existing clip rather than a new scene built
from scratch. Its job is to hold the stated properties of the source and carry out the changes
the user named. It complements `video-prompt-craft`: the general video skill covers motion and
camera, this one covers the footage transformation contract.

## Identify the real input mode

Check the chosen model and its input schema against the current catalog:

- `video_edit` / source-video slot: the model receives the footage as an editable base;
- `video_reference` / video-reference slot: the clip sets motion, composition or the scene, but
  does not promise frame-by-frame preservation of the whole source;
- when preservation accuracy matters more than a particular model, choose a model with
  `video_edit`;
- describe a reference input as control of motion, composition or scene; promise frame-by-frame
  preservation only when the matching capability exists.

Use confirmed facts from the attachment or the asset summary: duration, transcript, whether
there is sound, the described subject and scene. State the FPS, the timecode of a line, the lens
or the light direction only when there is a measurement or an explicit source.

## An exact subject from a photo in existing footage

A video model redraws a subject from its reference, so a pet, a product or a person from a photo
comes out similar, not the same. When the user needs that exact subject in their footage, offer
the frame-first path instead of one edit:

Explain the frame-first trade-off before starting: image editing can preserve the reference
subject more closely, but regenerating motion from that frame does not preserve the original
footage frame by frame. Do not promise exact identity throughout the resulting video.

1. Obtain a suitable frame of the footage. Use host-local frame extraction only when an actual
   available capability can read that footage and the user has authorized the local operation.
   Otherwise ask for a supplied frame or an accessible frame image; do not invent a public frame
   extraction tool, a local path readable by MCP, or an attachment URL.
2. Use `givon_list_models` and `givon_get_model_schema` to select a supported image-edit model
   that accepts both the frame and the subject photo. Upload/import them through the available
   public asset route, bind each returned `assetUri` to its supported input role, and author an
   image-edit prompt preserving the source scene while placing the subject. If the required
   combination is unsupported, explain the gap and agree the alternative before proceeding.
3. Quote the exact image request with `givon_quote_generation`, obtain approval under
   `givon-ai-create`, generate through `givon_generate_content` with quoted `maxTokens` and a
   stable `idempotencyKey`, then check `givon_get_generation_status` and show the resulting frame.
   Obtain the user's approval of that frame before moving to the video stage.
4. Select an active image-to-video model and inspect its live schema. Bind the approved image
   only to the declared start-image field and describe motion, preserving the agreed trade-off.
   Quote and obtain approval for this separate video request, then generate and check status
   through the same public lifecycle. Return the finished clip or its truthful running/failed
   state. Reuse each stage's idempotency key after uncertain acceptance; never launch a duplicate.

Use the CLI equivalents in `givon-ai-create` when shell access is the chosen route. Each stage
has its own supported input, quote and job. Do not replace a requested direct footage edit
with regeneration from a frame without agreeing that loss of source continuity with the user.

## Contract: PRESERVE → CHANGE → INTEGRATE

### 1. PRESERVE

Name only the source invariants that apply:

- character: identity, face, body proportions, wardrobe, expression, performance;
- product: exact geometry, color, material, label and logo shape;
- frame: framing, angle, headroom, horizon, lens character, camera motion;
- scene: objects and parts of the surroundings the user did not ask to change;
- sound: source dialogue and lip-sync, when they need to be kept.

### 2. CHANGE

List the requested changes and how they relate in time or space. Do not merge independent
changes into an invented causal chain. Use the wording `change only`, `replace only`,
`transform only` and `add only` only when the user really limited the change to one element.

### 3. INTEGRATE

The integration approach follows the user's artistic direction. For a realistic or physically
embedded effect, take only the relevant traits:

- matching direction, softness and temperature of the key light;
- contact shadow, environmental bounce, reflections and light cast by the effect;
- parallax and the speed of the world relative to the source camera motion;
- matching depth of field, focus falloff, lens character, grain and atmospheric haze;
- no stray halos or cut-out edges, and consistent depth where objects touch.

For a hand-drawn, graphic, surreal, glitch or otherwise stylized effect, keep exactly the
requested visual logic instead of substituting photorealism.

Describe behaviour over time: where the effect starts, how it spreads, and what it lights,
deforms or refracts. For large creatures and objects, state the scale explicitly relative to a
specific element of the scene.

## References

Use the chosen live schema and `promptAuthoring` / `x-promptAuthoring` reference semantics to
bind every uploaded/imported asset to its role. Use only the aliases the selected model supports:

- numbered tags such as `@Video1`, `@Image1` or `@Audio1` require declared inline-reference
  support and must match the order of the corresponding schema-backed reference collection;
- a dedicated source/start/end slot has its own semantic role; describe "the source video" or
  "the opening frame" instead of inventing a numbered alias;
- never invent a slot, alias, media URL or file-selection status. If a required asset has no
  supported input field, explain the mismatch and agree the alternative with the user.

If a photo is needed only as a texture reference, pin down its role: take the look, fur or
material from it, and keep the background, composition and light of the source scene. Tie each
reference to its role directly in the scene description.

## Timing, lines and duration

For an event on a spoken line, use two anchors, and only when the facts are available:

1. semantic: the exact words of the line;
2. numeric: `at about N seconds`, from a measured or given timecode.

The numeric anchor requires a measured or given timecode. If an intro is added before the
source performance, check the arithmetic: `total runtime - intro = remaining source window`. For
a line that does not fit, increase the total length, remove the pre-roll or state the trim
explicitly.

## Prompt language

Write the prompt in the prompt language set by the chosen model's current prompt-authoring contract; usually that is English. Keep the `@ImageN` /
`@VideoN` / `@AudioN` aliases, names, numbers, brands and exact lines as written. If the user asked for several language versions, prepare a separate,
self-contained variant for each.

## Iterations

For a refinement such as «свет мягче» (softer light), «эффект начинается раньше» (the effect
starts earlier), «существо больше» (a bigger creature) or «камера остаётся исходной» (the camera
stays as in the source), change the named part and keep the rest of the contract, the aliases,
the invariants, the timing and the chosen model stable.

## Final check

- the model's input mode matches the attached video;
- every reference used is named by its alias and role;
- PRESERVE lists only the invariants that are needed;
- CHANGE contains all the requested changes and only them;
- the integration approach matches the requested realism or style;
- no timecodes are invented;
- the duration and the line physically fit;
- the prompt contains only the description of the result and the parameters that affect
  generation.
