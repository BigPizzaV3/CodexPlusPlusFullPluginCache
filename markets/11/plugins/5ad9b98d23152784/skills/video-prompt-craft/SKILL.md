---
name: video-prompt-craft
description: "For a generation-ready video prompt, turn the scene or shot plan and the chosen model's contract into action, camera, timing and sound instructions. Not needed for a storyboard without final wording or for choosing a model."
metadata:
  version: skill-render-ea6bd93365667f6d
---

# Professional video prompt preparation

A video prompt directs change over time. It has to answer not only "what is in the frame" but
also "what happens, how it develops, how the camera behaves and what stays unchanged". A
retelling of the idea without staging decisions is not a finished prompt.

## 1. Define the task and the end result

Distinguish:

- `text-to-video`: the whole scene is built from text;
- `image-to-video`: the image already sets the look and the opening composition;
- `reference-to-video`: separate assets set identity, product, style, motion, camera, effect
  or sound;
- `video edit / transform`: one specific property of the source video changes;
- `extension / transition`: a continuation or a transition between states is needed;
- `single shot`: one continuous scene;
- `multi-shot`: several meaningful shots with transitions and continuity.

An explicit subject, action, order of events, lines, style and exclusions belong to the user.
Do not ask about every setting. When a decision does not change the meaning and the chosen
model supports it, make it yourself: the duration within the available range, framing, camera,
light, the character of the motion and, when the clip has sound, the character of the sound.
Ask a question only for a real blocker.

## 2. Assign a role to every media asset

For each image, video and audio file, state its exact role:

- source, start or end frame;
- character or product identity;
- style, composition or location;
- motion, camera or effect reference;
- dialogue, voice, music or ambience reference.

Use pixels, frames and confirmed metadata within that role. Do not carry appearance over from a
motion reference, motion from a style reference, or a whole interface screenshot into the final
scene. File names help you find the material, but they do not replace its content.

## 3. Follow the chosen model's contract

Use only the confirmed input modes, durations, audio capability, slots and settings. Do not
guess capabilities from the brand or the model name. A video reference does not by itself make
an edit or extension operation available. Start and end frames set the states of a transition,
while references set identity, look, motion, style or audio: do not combine the two when the
contract declares them incompatible, and do not add references to boundary frames on your own.

The chosen model's current prompting guidance owns model-specific syntax;
its live contract owns available fields.
When the task needs one of these general methods, read only the matching reference:

- Editing a source video (for example with Seedance 2.5, Gemini Omni or SwitchX):
  `references/source-video-edit.md`.
- Style transfer or fixing a specific visual defect: `references/style-and-revision.md`.

A reference does not replace the current inputs and settings from the catalog; do not load the
other file in advance.

Duration, aspect ratio, resolution, quality and the audio flag belong to typed settings. The
prompt describes the creative result. If the user asks for a clip longer than one model output,
offer a supported segment and a plan to assemble it from several pieces instead of an error or
a prompt that cannot be executed.

## 4. Build the director's brief

Before writing the final text, decide:

1. **the subject and the observable action**;
2. **starting state → development → end state**;
3. **spatial relationships** and the direction of motion;
4. **framing and camera behaviour**;
5. **setting, light, palette and atmosphere**;
6. **the physical response** of clothing, hair, liquid, smoke, surfaces and objects;
7. **continuity and invariants**;
8. **sound intent**, only when the audio setting is on: the sound the scene produces, plus
   speech or music when the user asked for them.

Make the missing non-essential decisions yourself and tie them into one direction. Do not add a
new main character, product, plot twist, line of dialogue, music, caption or advertising
promise.

## 5. Structures for different inputs

### Text-to-video, single shot

```text
[Subject and starting position]. [One clear action and how it develops].
[Setting and spatial relationships]. [Shot size/angle and one consistent camera move].
[Light, palette, atmosphere]. [Physics and important invariants]. [Sound the scene produces, only when audio is on].
```

Motion has to be observable: instead of "dynamic", describe exactly what speeds up, turns,
opens up, scatters or changes. Do not overload a short shot with several independent events and
conflicting camera moves.

### Image-to-video

The source frame already owns the appearance, the objects, the angle and the opening
composition. So the prompt is built like this:

```text
SOURCE: @Image1 — the opening frame.
MOTION: one feasible motion that fits the source's pose, framing and duration: who or what starts moving and how it develops.
CAMERA: one consistent camera behaviour.
PHYSICS: the natural response of materials and surroundings.
KEEP: identity, product shape, key background, light or composition that must not be lost.
END STATE: the observable state at the end of the shot, if it matters.
SOUND: only the sources that are needed, and only when audio is on.
```

Do not retell the whole source image, and do not invent product properties the image does not
show. Do not demand "complete stillness" from elements that need a slight physical response to
look real.

### Video edit / transform

Name the source video, the exact change, the boundaries of the change and the properties to
keep. If the background changes, do not change the motion or identity; if the clothing changes,
do not rewrite the whole story; if an effect is added, tie it to an object and a moment.

### Reference-to-video

Use the aliases exactly as the host gave them, without renumbering, and state each one's role
explicitly:

```text
@Image1 sets the character's identity.
@Video1 sets only the camera movement.
@Audio1 sets the editing rhythm, not the character's voice.
```

Then describe the new scene. Do not use an alias that does not exist, and do not silently merge
different roles.

## 6. Single-shot and multi-shot are different artifacts

Do not turn a simple scene into a storyboard. A single shot gets one whole action, one camera
move and continuity.

For a genuinely multi-beat result, build a director packet. For each shot, give:

- its purpose or beat;
- the observable action;
- shot size, angle and composition;
- the camera movement;
- light and mood;
- the starting and ending boundary state;
- dialogue, SFX or ambience, when needed and the audio setting is on.

Distribute the shots within the available duration. Hard timestamps are needed only when they
help synchronization or the target model requires them; for a simple gesture, "first… then…" is
enough. Keep identity, product shape, direction of motion, the screen axis, time of day and
colour consistent across shots. A transition has to connect the end state of one shot with the
starting state of the next. Start and end frames reduce drift at the seam between clips, but
they do not guarantee an invisible cut, the same voice or exact geometry.

## 7. Sound follows the audio setting

Whether the clip has sound is the audio setting's call, not the prompt's. Do not ask the user
a separate "with or without sound?" question when the task is clear. The prompt follows the
value the generation runs with: an untouched switch means the model's default, and a model that
generates sound but has no switch always has sound on. When the task clearly calls for silence
(a silent product animation) or for sound (an ad, an atmospheric or talking scene) and the model
has a switch, set the audio setting accordingly instead of writing the wish into the prompt.

- When sound is on, direct the sound the scene produces: ambience and the sounds of visible
  actions and materials. Choose their character yourself.
- Add speech or music only when the user asks for them. Do not invent lines, lyrics or an exact
  voiceover; a voice reference does not license a new line either.
- «Без речи» ("no speech") rules out speech, not necessarily ambience or the sounds of the
  setting.
- When sound is off, leave sound out of the prompt.

If the chosen model's contract cannot produce a sound the user asked for, do not put an
impossible demand into the prompt: plan that sound as a separate sound layer.

## 8. Full examples

### Image-to-video: a sneaker box

```text
SOURCE: @Image1 — the red Nike box and the source close-up composition.
MOTION: a woman's hands enter the frame naturally, carefully untie the gift bow and move the
ribbon aside, then take the edges of the lid and lift it smoothly. The actions follow one
another, without jumps or extra objects.
CAMERA: static vertical close-up, no zoom and no change of angle.
PHYSICS: the ribbon bends softly and settles beside the box; the fingers and hands move with
natural anatomy; the lid keeps its rigid shape and opens on its real hinge axis.
KEEP: the red colour, shape, proportions, material, logo and look of the box; the source
background and light direction.
END STATE: the lid is slightly open, the hands hold it, and the box stays in the centre of the
frame.
SOUND: a quiet rustle of ribbon and cardboard, no speech and no music.
```

When the audio setting is off, leave the last line out of the prompt.

### Text-to-video: a short ad shot

```text
White sneakers stand on a dark matte pedestal. A narrow beam of cool light slides from left to
right along the side, revealing in turn the leather texture, the stitching and the sole; at the
end a warm rim highlight appears on the heel. The camera makes a slow arc of about a quarter
turn at product level, keeping the sneakers centred, with no change of focal length. Dust in the
air reacts faintly to the motion, and the contact shadow stays stable. Minimalist premium
product-film look, a deep background with no text, people or extra objects.
```

This example assumes the audio setting is off. With audio on, end it with the sound the scene
produces.

### Multi-shot packet

```text
Shot 1 — establishing: an empty workshop at dawn, wide static shot; a closed album lies on the
table, cold light comes from the window.
Shot 2 — discovery: medium shot from above, a hand opens the album; the camera moves in
smoothly, the pages turn physically and stop at a photograph.
Shot 3 — reaction: close-up of the heroine from @Image1, her gaze softens; warm light reflected
from the page, a barely noticeable camera move forward.
Continuity: the same heroine, clothing, table, window-light direction and album position.
Audio: a quiet rustle of pages and the morning ambience of the workshop, no music and no speech.
```

When the audio setting is off, leave the Audio line out.

## 9. Final check

- the task matches the input mode;
- the action and its progression over time are visible;
- every asset has an exact role and alias;
- the event load is realistic for the duration;
- the camera does not contradict itself;
- physics and invariants protect what matters without freezing the whole frame;
- sound follows the audio setting: the scene's sound when it is on, speech or music only on
  request, no sound in the prompt when it is off;
- the prompt is not a retelling or a UI instruction;
- settings stay typed fields;
- a single shot is not inflated into a multi-shot, and a multi-shot has continuity;
- when the same defect repeats across results, a stronger lever beats new wording: a reference
  image, one simple action, a shorter clip, a first or last frame, or fewer subjects.

Reference aliases apply only when the chosen model declares inline-reference support.
Bind them to actual reference order and roles; for dedicated source/start/end fields,
use the slot role instead of inventing an alias.
