# Editing a source video and using a video reference are different tasks

Sources checked on 2026-09-07. Seedance 2.5, Gemini Omni and SwitchX have different operations
and vendor contracts. First check the exact selected mode in the current Givon catalog; a
description of the model family does not grant new capabilities.

## Choose the right action

- **Editing the source video:** keep the clip itself and change the named part: an object, the
  background, the light or another supported element.
- **Video reference:** take motion, camera, style or other explicitly named traits from the clip
  to create a new video. This does not promise to keep all the source frames, the duration or
  the audio.
- **Extension:** add events after the end of the clip. It needs its own supported operation; the
  word «продолжи» ("continue") does not turn a reference into an extension.

For a local edit, name one change and a specific object. List the identity, pose, camera,
background and light to keep only as far as needed. When replacing a background, state
separately that perspective, contact shadows and silhouette edges must match. Do not rewrite
the character's action when the user changes only the surroundings.

## Model specifics

How a particular model words an edit, reads a mask or a reference, and where its edit mode ends
is in that model's current prompting guide. A feature documented for
a model elsewhere is not necessarily available in the mode selected in Givon.

## Example of a local edit

```text
Edit the supplied source video. Replace only the background with a quiet blue
studio cyclorama. Preserve the person's face, hair, clothing, walking performance,
framing and camera movement from the source. Match the original perspective and
key-light direction, preserve soft contact shadows, and keep silhouette edges
clean. Do not introduce new actions, people, dialogue or on-screen text.
```

This text applies only to a supported source-edit operation. A reference-only task cannot
promise the same result. After generation, check not only how good the background looks but
also the source motion, the face, the edges and the sound, when it had to be kept.

## Sources

- Google Gemini Omni: https://ai.google.dev/gemini-api/docs/omni
- BytePlus capability scope: https://docs.byteplus.com/en/docs/byteplus_las/video_gen_enhanced
- Beeble SwitchX: https://docs.beeble.ai/beeble/switchx
