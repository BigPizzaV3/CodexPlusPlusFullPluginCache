---
name: make-a-beat
description: Make a new beat or song in CookUp from an idea, genre, mood, reference or tempo, for example "make a dark trap beat at 140" or "a mellow lo-fi loop with warm keys". Use for new music, not for changing an existing session (edit-a-session) or for sampling a song (flip-a-sample).
---

# Make a beat

Explicit user instructions always take priority over these guidelines.

## Input
- The idea: genre, mood, tempo, key, instruments, length, references.
- If the user gives only a vague request ("make a beat"), make reasonable choices and say what you chose. Ask only when a required fact is missing and guessing would waste the result, such as a session the user asked you to add to but did not name.

## Steps
1. **Quick build** (the user wants something fast, or gives a short prompt): call `create_beat` with the prompt and a full `plan`:
   - bpm, tonic and mode;
   - chord degrees for 8 bars, with bars 5–8 developing bars 1–4;
   - one memorable melody motif with rests;
   - bass on chord roots that answers the kick;
   - a one-bar drum pocket that fits the genre.

   Use `plan.bars` for the requested length (default 32).
2. **Produced build** (a substantial or detailed request):
   1. Call `prepare_production`.
   2. Write a few short private ideas and compare them with `review_production_draft`. Send the full cumulative commands each time.
   3. Develop the strongest idea.
   4. Save the final batch once with `apply_session_edit`.
3. Choose sounds as in the choose-sounds skill: the user's own kits first, and audition the kick, snare or clap, 808 or bass, and lead before committing them.
4. If the host can receive audio, render with `render_audio_preview`, then listen with `listen_audio_preview` before describing how it sounds.
5. End with one `open_session` call so the user can press Play.

## Output
- Session name and code.
- Tempo and key.
- The parts you made.
- Anything CookUp substituted or could not do.

## Never
- Invent sound IDs, session codes or edit results.
- Say the beat sounds good, mixed or finished unless you listened to returned audio. Say it is ready to audition instead.
- Claim the beat was saved before `create_beat` or `apply_session_edit` confirms it.
