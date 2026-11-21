---
name: scene-by-scene-video
description: Design a video with Crealix scene by scene, choosing each scene's narration, length, image or clip, AI model (Veo, Kling, Seedance, Sora…), camera move and transition, with the user's own media too. Use when the user wants full control, a specific video model, their own images or clips, or an ad, a product demo or a trailer.
---

# Scene-by-scene video (from scratch)

No template in between: you design each scene and Crealix executes it, with
any image or video model, the user's own media, or both. Nothing is spent until
the scenes' media is generated.

## 1. Read the guide

Call `get_creation_guide('from_scratch', durationSec, language)`: the scene
fields, the suggested number of scenes and seconds per scene for this length,
the narration pace of the voice, and prices (voice and image per scene;
clips by model).

## 2. Design the scenes

For each scene:
- `text`: what the narrator says (and the captions show). Within the pace the
  guide gives for its duration. Leave it empty for a silent shot.
- `durationSec`: at least as long as its narration.
- `mediaPrompt`: what the image or clip shows, in English and concrete:
  subject, action, setting, how the light falls, framing. No text or logos in
  the picture, no style words (the visual style is added), no names (describe
  the person).
- `movementType` for a camera move on images, `transitionType` into the next
  scene.
- The user's own image or clip in a scene: it must be in Crealix first
  (`import_media_from_url`, or `upload_media`), then it goes on that scene.

Write it like the best short-form: the hook in scene 1, one idea per scene, a
payoff at the end. Describe light on surfaces (warm side light, pale dawn), not
lamps or beams, unless the scene really has the source.

## 3. Cast it

From the guide's cast, choose what suits this video: voice and delivery,
visual style (or none, to follow the prompts alone), captions and music, plus
`cover` for short-form. The models: Crealix's recommended ones unless the user
names one; `show_options('video_models')` only if they want to compare.

## 4. Propose and create

`check_plan` with the scenes until it is valid, then one `validate_plan` (the card
shows the scenes, the cast and the cost) with two or three lines of why. On a
yes, `create_project_from_scratch` with the same fields and the `proposalId`
(free), then `generate_scene_media` for scenes `all` with voice and image: the cost
the proposal showed.

## 5. Bring it to life

- Suggest which scenes deserve motion (the hook, the key moments), not all of
  them. `animate_scenes` first returns each clip's model, length, quality and
  price: tell the user all four, say which ones Crealix picked, and animate
  only after they agree, with its `confirmationId`.
- Add a hook overlay on scene 1 and a few text overlays where they help
  (`add_text_overlays`), and sound effects on real moments only
  (`add_sound_effects`). No ticking clocks unless asked.
- Fine-tune with `update_project` and `update_captions`; `undo_last_change`
  reverses an edit.
- Render only when they ask: the card's Render button, or `render_project`.
