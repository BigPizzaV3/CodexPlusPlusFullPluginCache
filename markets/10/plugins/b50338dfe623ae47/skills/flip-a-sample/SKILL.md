---
name: flip-a-sample
description: Sample a song or loop and build a beat around it in CookUp. Use when the user attaches audio and wants it chopped or sampled, or names a song to sample, for example "flip this", "sample Ain't No Sunshine" or "chop the intro of this track".
---

# Flip a sample

Explicit user instructions always take priority over these guidelines.

## Get the audio
- **The user attached a song or loop:** call `flip_attached_audio` with the file. Add `title` and `artist` if known, `code` if a session is in use, and `chops` if the user asked for a number.
  - CookUp finds the tempo, key and best loop on its servers.
  - It saves up to a minute of the song and the chops into the user's library under "Sample Flips/<song>".
- **The user names a song but attached nothing:**
  1. Find the exact title, artist and a link where it plays with web search.
  2. Call `start_sample_flip` with them.
  3. Give the user the `captureUrl`. In the CookUp Sample Lab they record the song from a browser tab (a few seconds up to a minute) or drop a file, and save chops.
  4. Call `get_sample_flip` with the flip id when they say they are done, until its status is `ready`.
  - CookUp never downloads songs from YouTube or other sites. Do not offer to.
- **They want another part of the song:** call `flip_attached_audio` again with `loop` (an index from the returned `loops`), `bars`, or `start` and `end` in seconds.

## Build the beat
1. Use the session from `code`, or create one with `create_session`.
2. Set the tempo to the flip's `bpm`.
3. Put the chop `soundId`s (user-*) on drum-lane pads, one chop per lane, or on a sampled instrument.
4. Write drums and bass in the flip's key that leave room for the sample, with `apply_session_edit` (read `get_edit_context` first).
5. End with one `open_session` call.

## Clearance
- Clearing the sample is the producer's responsibility.
- CookUp records the song, artist, link and the exact seconds of each chop. `get_sample_flip` with the session `code` returns these clearance rows, and the Sample Lab can download them as a CSV.
- Mention this once. Do not refuse or lecture.

## Never
- Invent a link, timestamps, BPM or key: use what the tools returned.
- Claim a flip is ready before `get_sample_flip` (or `flip_attached_audio`) reports chops.
