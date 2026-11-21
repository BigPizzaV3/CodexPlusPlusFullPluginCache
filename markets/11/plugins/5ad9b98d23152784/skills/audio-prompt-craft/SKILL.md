---
name: audio-prompt-craft
description: "For a generation-ready music, sound-design or speech prompt, turn the audio goal and selected model contract into creative direction and separate literal lyrics or spoken text. Not needed for a question about audio models or for editing a script's words without preparing a generation."
metadata:
  version: skill-render-ea6bd93365667f6d
---

# Preparing an audio prompt professionally

First define the meaning of the result: music, a jingle, a sound bed, sound design or a
voiceover. These tasks use different fields and must not collapse into one universal prompt.

## General order

1. Pin down the purpose: an ad, background for a clip, an intro, a podcast, a character's voice.
2. Take into account the confirmed inputs and settings of the chosen model.
3. Keep the explicit genre, mood, instruments, voice, language, text and exclusions.
4. Decide minor details yourself — tempo, dynamics, structure, density of the arrangement,
   character of the performance — when they follow from the task.
5. Do not ask a question about every parameter, and do not invent lyrics, lines, brand claims
   or the voice of a specific person.

Pass duration, variant, language or voice id and other execution controls in the typed settings
or provider options. The prompt contains only the creative brief, and the literal content goes
in the field meant for it.

## Music and jingles

A full brief contains the relevant elements:

- the function of the track and its place in the content;
- genre and era, without unlawfully copying a specific composition;
- mood and emotional arc;
- tempo, rhythm and energy;
- lead and supporting instruments;
- structure over time: intro, build, peak, outro;
- density, space and production character;
- vocals and lyrics only if requested and supported;
- what must not be heard, when the exclusion really matters.

Example:

```text
A 15-second energetic electronic jingle for a short ad for a sports app. A fast, bouncy beat,
a short three-note synth hook, a tight bass pulse and one bright hit on the final logo.
Structure: an instant hook, a build toward the 10th second, a clean final accent with a short
tail. Modern polished production, no vocals, no long intro and no aggressive distortion.
```

Do not add generic `cinematic`, `epic` or a list of genres unless they serve the task.

## Voiceover

The text to be spoken is a separate literal input. It is kept word for word, including names,
numbers and punctuation. Tone, pace, emotion, pauses and pronunciation belong to the delivery
controls or to a separate instruction field, if the schema supports one.

Never put service phrases into the literal spoken-text field, such as «[говорит энергично]»
("speaks energetically"), «мужской голос» ("male voice") or «пауза 2 секунды» ("2-second
pause"): many models will say them out loud.

Before you prepare the generation, check that:

- all of the user's text is kept word for word;
- the language and voice are compatible with the model;
- difficult names have confirmed pronunciation guidance, if it is needed;
- the delivery does not change the meaning of the text;
- the length of the text is realistic for the chosen duration;
- no instructions will end up in the speech as words.

## Sound design for video

Tie each sound to its source and moment: a footstep, the click of a lid, rustling fabric, city
ambience, a transition or a final sonic logo. Do not list abstract "high-quality sounds". If the
native audio of the chosen video model is not enough, prepare a separate sound layer instead of
a video prompt that asks the model for audio it cannot produce.
