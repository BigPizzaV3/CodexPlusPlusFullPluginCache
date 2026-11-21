---
name: voiceover-for-a-script
description: Use this when someone wants spoken audio, such as a voiceover, narration, a read of a script, an announcer line, background music or a sound effect. Trigger on voiceover, narrate this, read this out, VO, announcer, background track, sound effect. Do not use it to make video, and do not use it to clone the voice of a real person.
---

# Voiceover for a script

Turn written words into a finished audio file, or make the music and effects that sit under a clip.

## When to trigger

Trigger on "record this", "narrate this", "I need a voiceover", "give me an announcer read", "put some music under it", "I need a whoosh".

Do not trigger when the person wants a talking character on screen. That is video, so use make-a-video.

## Ask for this first

Ask once, bundled:

1. The exact words to be spoken. If they have not written them, offer to draft the script first and get it approved before you record anything.
2. The voice: warm, bright, deep, calm, energetic, the age range, and the accent.
3. The pace and roughly how long it should run.
4. What it sits under, so the read matches, for example a product ad, a documentary, a channel intro.
5. For music or effects instead of speech, what the scene is and how long the bed needs to be.

## Steps

1. Call `nolgia_list_models` and look at the audio models, so you pick one that covers speech, or music, or effects, whichever this is.
2. Call `nolgia_text_to_audio`. For a read, put the exact approved words in `prompt` and describe the delivery in `voice`. For music or an effect, describe the sound in `prompt` and set `duration_seconds` to the length the scene needs. Set `format` if they asked for a particular file type.
3. Audio comes straight back. Call `nolgia_get_asset` if you need a fresh link later.
4. If this is going under a clip you already made, call `nolgia_add_project_assets` so the read and the picture live in the same project.

## What to return

The audio file, the exact words as recorded, and the length. Offer one alternative read at a different pace or in a different voice, since the first take is rarely the keeper.

Never name a model and never discuss what anything cost.

## When to stop or decline

- The script is not approved: get the words right first. Re-recording is wasteful and annoying.
- The person asks for the voice of a named real person, living or dead: decline, and offer to describe the qualities they are after instead.
- The words are a claim the person cannot make, such as a medical or financial promise: flag it before you record, not after.
