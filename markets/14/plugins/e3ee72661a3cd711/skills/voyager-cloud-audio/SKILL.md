---
name: voyager-cloud-audio
description: "Cloud: generate narration with premade or existing Voyager voices, music and sound effects."
---

# Speech, music and sound effects

Follow `voyager-cloud` (read it with `load_skill` if it isn't loaded) for account,
models, costs and jobs. Audio jobs run
in the background: poll `get_job` and present the player and download when done.

## Narration

1. `list_voices` lists premade voices. Choose one that fits the script's audience
   and tone, or the voice the user names; offer two or three when the voice is
   open and it matters.
2. `list_voices` with `source` set to `mine` lists the user's existing cloned
   voices, if they have any. This plugin never creates,
   records or re-records a voice clone; if the user wants one, say it is made in
   the Voyager app, where they give their own consent.
3. Write the script for the ear: short sentences, numbers and names written as
   spoken. Then `generate_speech` with the text, voice and the
   speech model chosen as `voyager-cloud` describes.
4. Listen-check claims honestly: report what you heard only if you could check it.

## Direct the delivery

- Emotion written as narration ("she said sadly") is spoken aloud. Direct delivery
  with the markup the chosen speech model supports, such as bracketed tags
  (`[whispering, playful]`), only where `list_models` or the model's description
  says it accepts them; otherwise write the line so its wording carries the tone.
- Ellipses add a pause and weight; capitals add emphasis. Don't use SSML.
- Delivery works best when the voice already has it; a calm narrator will not
  shout well.

## Music

Describe genre, tempo, instruments, mood and structure in the prompt, and whether
it is instrumental (a bed under speech or picture should be). Narrate the
arrangement ("start with just piano, then bring in drums"). Never ask for a
particular song's melody, lyrics or an artist's voice. Exact cue timing is never
guaranteed. Call `generate_music` with a duration that fits the
use and the limits `list_models` reports for the chosen model.

## Sound effects

- One sound per prompt. Write a short sequence in order ("footsteps on gravel,
  then a metal door opens"); make longer scenes as several cues.
- Name the sound's kind: impact, whoosh, ambience, one-shot, loop, braam, glitch,
  drone, plus tempo and key for musical hits.
- Set a duration or looping only when `list_models` reports that setting and its
  range for the model; otherwise let the model choose.
- Deliver the format the job returns and name it in your reply; this plugin does
  not convert or mix audio.

Generate each cue with `generate_sound_effect`, named by cue (`reveal-hit`,
`ui-click-01`), and list the delivered files with their intended cue times.
