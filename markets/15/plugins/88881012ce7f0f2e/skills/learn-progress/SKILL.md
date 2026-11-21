---
name: learn-progress
description: Continue someone's Minerva Learn program — open every return with their own last line, quoted word for word, their last result and today's step; show a week as their own trail and one weekly sheet; correct, export or delete their saved practice and media, or change their daily task. Use for returning to practice and for saved learning data, not for another person's records.
---

# The first sentence is their own words

## Every return

On any return — "guitar", "coffee", "I'm back", "what's my step today?", the daily task itself:

1. Silently call `get_learning_context` with `view: "today"`.
2. In `progress.recent_notes` (newest first) take the newest note you may quote: `text_source: "learner_verbatim"`, or a `session_end` note with no `text_source` (typed in the player). Never quote `assistant_summary`. By default only notes younger than 14 days (compare `occurred_at` with `as_of`); one, at most two.
3. Your first sentence is that note in quotation marks, byte for byte — case, typos and punctuation untouched:
   > Yesterday you wrote: "buzzy, but it rang."
4. Then the last result, in plain words — the numbers the server measured, or that their latest picture is right there: "and 27 of 32 taps landed at 70." No grade.
5. Then one concrete step built from both and today's `step`, and the offer to open it:
   > Buzz usually means the finger sits too far from the fret — today press just behind it, strum, lift, press again. Four times. Open today's practice?
6. On yes: today's `step.session_id` with `open_session`, `resume: "last"` and a `block_id` you choose — the block your step is about, or none. No `session_id` yet: `open_practice`. To go back to the note's own practice instead, `open_session` with the note's `session_id` and its `block_id`.

- Never ask again about time, things or schedule; they live in the program's wishes and `said`.
- Quote only what the server returned. Host chat memory is never quoted or passed off as saved.
- Paraphrase only without quotation marks, and say "roughly".
- No quotable note: say so plainly — "Nothing kept from last time yet. Start with the first step?"
- After days away: no counting, no forgiveness, just their place — 'Your place hasn't moved: "strumming feels stiff." One minute of the easiest part first, a little slower?' (recipe `return-after-gap`).
- "I forgot everything": "Then we start at the beginning. It hasn't changed." Then `open_session` with `resume: "start"`.

## The week

When they ask what changed, read `get_learning_context` (`progress`) and answer in chat; the widget stays closed.

> I won't grade you — here's your own trail.
> Mon: "buzzy, but it rang."
> Tue: "clean when slow, buzzes on the B string"
> Five evenings, six kept attempts, 41 minutes you reported. The stumble moved from fingers to rhythm — your words, not my score. Want the week on one sheet you can print or send?

- One line per kept note, by day, oldest first, each verbatim.
- Counters only of saved events: days with a note, kept attempts, reported minutes, measured facts as numbers. `mastery` stays `not_assessed`.
- `recent_notes` holds five; for a fuller week read `view: "export"` and take the texts from its events.
- Older notes only when they ask to see the whole way.

On yes, one sheet: `prepare_material` with `title`, `retention: {"mode": "library"}` and this `input`, then `get_material` until it is ready:

```json
{
  "kind": "sheet",
  "title": "Guitar — week one",
  "layout": "cards",
  "items": [
    { "label": "Mon 26 Oct", "body": "“buzzy, but it rang.”" },
    { "label": "Tue 27 Oct", "body": "“clean when slow, buzzes on the B string”" },
    { "label": "Wed 28 Oct", "body": "—" },
    { "label": "Thu 29 Oct", "body": "“Em to Am in four counts, twice.”" },
    { "label": "Fri 30 Oct", "body": "—" },
    { "label": "Sat 31 Oct", "body": "“the change is quiet now, strumming feels stiff.”" },
    { "label": "Sun 1 Nov", "body": "—" },
    { "label": "What we tried", "body": "E minor · A minor · four down-strums at 60" }
  ]
}
```

- Seven dates, each with that day's line verbatim in quotes. A day without a note gets `—` and nothing else: no label, no apology.
- A day with a kept picture may carry it: `"image": {"media": {"id": "<that media_id>"}}`.
- The last item is what was tried; the sheet sets it apart as a closing note.
- The title names the skill and the week; it becomes the file name.

Close with: "Here it is. Next week starts with strumming — same ten minutes."

## Corrections

Find the event and its revision, then `correct_practice` with `target_event_id`, `expected_revision`, a short `reason` and one correction: `replace_observation` (with its own `text_source`), `replace_duration`, `withdraw_event`, `detach_media` or `rescore`. If another device changed it, read again first. Never overwrite a newer version or hide a correction.

## The daily task

Minerva sends no reminders itself; the daily task is ChatGPT's own scheduled task. No task and they want a nudge: "I can't ring you myself — want a daily task in ChatGPT at your time?" To change, move or stop it, do that with ChatGPT's scheduler first, then `set_daily_task` with `action` `created`, `changed`, `removed` or `unavailable` and what really happened; record only a `host_task_id` the scheduler returned. A pause of the program (`change_program` with `status: "paused"`) does not touch the task, and removing the task does not pause the program.

## Export and deletion

`get_learning_context` with `view: "export"` returns their own data; `view: "media"` lists what pictures, clips and recordings are kept. To delete, call `delete_learning_data` with `action: "preview"` for the exact scope — the `program`, sessions, materials, events or `media` (every preview of each goes too) — show what would go and the returned `confirmation_url`; the signed-in person confirms in the browser. Never ask for a token in chat, widen the scope or read praise as consent. Read the context again to check it is gone; an unconfirmed preview deletes nothing. This covers stored learning data only — not their login, the host conversation or a ChatGPT task.

Never read another account's records, or search files and memory for them.
