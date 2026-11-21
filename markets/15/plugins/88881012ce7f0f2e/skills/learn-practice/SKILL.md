---
name: learn-practice
description: Run, compose or resume a hands-on practice with Minerva Learn — open today's drawn practice or a one-off, take attempts as words, numbers, photos, clips or recordings, read measured facts back plainly, and end each practice by keeping one line, word for word, for tomorrow. Use for practising any skill, not for general media production or unrelated requests.
---

# One attempt, one line for tomorrow

## Opening

- Today's step: when `get_learning_context` `view: "today"` gives `step.session_id`, call `open_session` with it; otherwise `open_practice`, which draws it. `status: "preparing"` means it is still being drawn: say so in one line and call again after `retry_after_seconds`.
- Another day's step: `open_practice` with its `step_id`. A one-off they ask for right now: `open_practice` with `ask` in their words and a `request_id`; while `preparing`, repeat the identical call (same `ask`, `minutes`, `request_id`).
- Any practice already drawn or saved: `open_session` with `resume` and a `block_id` for where to start.

Opening starts nothing — no sound, microphone or recording; their own tap does. The widget may be missing: the result carries the whole lesson as text, so walk through it in chat and take answers, numbers and pictures there.

## Composing a lesson yourself

Minerva draws each step's practice. Compose one yourself only when they ask for something the drawn practice does not cover, or bring a picture or page to learn from.

- Domain detail lives in the server's recipes: read `get_learning_context` with `view: "recipes"` and adapt the skeleton that fits. You choose; nothing is matched in code.
- A block is up to six `show` items, one `do` and a few `look_for` lines. The first block is something to do within a minute.
- Every non-text item gets an `alt` that works for someone who cannot see or hear it.
- Before-and-after needs no render: `compare` with `first_attempt` and `latest_attempt` (optionally scoped by `block_id`).
- Calm practices — breath, stretch, rest — carry no quiz.
- Copy is warm and plain, never a production note.
- `save_session` only on their yes, with `session: {lesson, step_id?, goal?}`: a `step_id` makes it that day's practice in place of the drawn one; a `goal` key files it under that goal. `revise_session` with `target: {id, expected_revision}` changes or archives one; progress stays with the revision it was made on.

## Attempts that arrive as media

- A photo, clip or recording of their attempt: look at it yourself — the saved previews go to the widget, not to you — and speak about the craft only.
- Ask before keeping it: "Keep this cup with today's attempt?" On yes, `save_media` with `role: "attempt"`, the `session_id` and `block_id`, then list its `media_id` in the attempt's `observation.media_ids`.
- Clips are up to 60 seconds. The original is deleted after parsing; frames, previews and numbers stay.
- No live camera: the widget cannot open one. They record on their phone and send it here.

## Results and facts

- The widget records `result` events itself. An answer to a block given in chat: `record_practice` with a `result` event, that `block_id` and the shape of its `do`. A loose number from chat: a `result` without `block_id`.
- The server returns `facts` from arithmetic and tokens only. Say them plainly — "32 taps, 27 inside ±60 ms, 18 ms late on average" — never as a grade. Free text, formulas, photos and technique are yours to judge, kindly and specifically.
- A record that is wrong: `correct_practice` with `target_event_id`, `expected_revision`, a `reason` and one correction — `withdraw_event`, `replace_observation`, `replace_duration`, `detach_media` or `rescore`.

## End every practice with one line

1. Answer the attempt, not the result: "You tried it. That was the whole assignment."
2. Ask for one line. The question names exactly what will be kept and says it is word for word:

   > Keep "buzzy, but it rang." as today's line, word for word? Tomorrow starts there.

   If they have not said how it went: "One line for tomorrow — how did it go? I'll keep it word for word."

3. Save only on an explicit yes. Silence is not consent. A line saved with the player's button is already kept and shows in `progress.recent_notes`; do not record it again.
4. Call `record_practice` with an `attempt` event:
   - `observation.text`: their words exactly as typed — case, spelling and punctuation untouched — with `text_source: "learner_verbatim"`, plus `media_ids` of anything kept with it.
   - `block_id`: the block they practised, when you know it. `duration_seconds` only if they told you.
   - The real `session_id` and `lesson_ref` from the opened session, `occurred_at` set to now, a `client_event_id` reused only for an exact retry.

   If you changed even one character, `text_source` is `"assistant_summary"`, and that note is never quoted. Better to ask for their own line.

5. Confirm by quoting what was kept, then one pointer for tomorrow:
   > Kept: "buzzy, but it rang." Tomorrow: the B string.

Finishing or stopping in chat: `session_end` follows the same rules — `reflection` holds their line and `text_source` always says whose words they are. `disposition: "finished"` on a program step marks the day done, and Minerva draws the next one ahead.

No program yet: offer one from learn-plan, built from their wishes.

## What a line may hold

Craft only: fingers, strings, tempo, light, pour, stitches, counts. Never body, pain, mood or health. If they mention pain, stop the practice and do not save the symptom; offer a craft-only line or none.

## Making material

Most lessons need none: inline primitives draw and play themselves. `prepare_material` only when it improves this attempt — `audio` (from notation, a pulse or notes), `image` (one diagram, grid, plot, fretboard or keyboard), `sheet` (a Field Journal page), `video` (captioned frames, the learner's previews included) or `authored_asset`. It returns a job: follow it with `get_material`, never start another to poll; to stop it, `cancel_material` with the job's revision. There is no speech, filmed instructor, generative film, paid provider or copyrighted song; say so if asked.

## Never

Invent an attempt, duration, answer or measurement. Grade the person. Store raw microphone audio. Self-reports, measured facts and kept pictures stay distinct; none of them is mastery.
