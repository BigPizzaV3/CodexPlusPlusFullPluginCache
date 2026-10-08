---
name: moknah-dialogue-and-pacing
description: Produce natural dialogue and pacing in Moknah - detect speakers, cast a voice per character, merge consecutive same-speaker lines, and place [break_X] pauses at speaker changes, sentence ends and scene beats. Use when the text contains dialogue, or when rendered audio sounds choppy, rushed, or abruptly cut between voices.
---

# Dialogue and pacing in Moknah

The single biggest quality difference between amateur and professional Moknah
output is **line structure and pause placement**. Voice choice matters less than
this.

## Why line structure decides quality

Each line is rendered as its own TTS request. Every render starts prosody from
scratch: fresh intonation contour, fresh energy, fresh breath. So:

- Splitting one speaker's continuous speech across several lines produces audible
  restarts - the pitch resets mid-thought and the delivery sounds stitched.
- Two adjacent lines with *different* voices butt straight up against each other
  with no gap, so the switch sounds like an edit error rather than a reply.

Both are fixed at the text/segmentation layer, before you spend a single credit.

## Rule 1 - Merge consecutive lines from the same speaker

If two or more consecutive lines belong to the same speaker, **combine them into
one line.** Let the voice run continuously through the whole utterance.

Do this at cleaning time, before `create_project` / `add_line`, or fix it after
with `update_lines`.

```
BAD  (3 lines, same speaker - 3 prosody resets)
  line 1: "ما زلت أذكر ذلك اليوم."
  line 2: "كانت السماء صافية."
  line 3: "ولم يكن أحد يتوقع ما سيحدث."

GOOD (1 line, one continuous delivery)
  line 1: "ما زلت أذكر ذلك اليوم. كانت السماء صافية. ولم يكن أحد يتوقع ما سيحدث."
```

Stop merging when you hit any of these ceilings:

| Limit | Value |
|---|---|
| Characters per request, emotions ON | 3,000 |
| Characters per request, emotions OFF | 10,000 |
| Lines per chapter | 200 |
| Breaks per line | 20 |
| Total pause per line | 30 s |

Never merge across a speaker change. Never merge across a scene break.

## Rule 2 - Always break on a speaker change

When the voice changes, insert a pause at the **end of the outgoing speaker's
line**. Without it the two voices collide and the listener misses the handoff.

**Apply this by default, without being asked.** It is standard house behaviour,
not an option to raise with the user. Every speaker change gets a pause unless
the user has asked otherwise.

```
line 1 (Voice A): "هل انتهيت من العمل؟ [break_0.5]"
line 2 (Voice B): "لم أبدأ بعد."
```

Use **0.4-0.7 s**. Fast exchanges sit at the low end; a considered reply or a
change of tone sits at the high end.

### The one exception - deliberate interruption

Drop the pause only when the user wants the next voice to **cut the current
speaker off**: an argument, an interjection, someone talking over someone else,
overlapping urgency. Then the two lines butt straight together with no gap and
the abruptness is the point.

Never remove the pause on your own judgement - only when the user asks for that
effect.

## Rule 3 - Pause at sentence ends and beats

Punctuation gives a small natural pause on its own. Add an explicit `[break_X]`
only where you want the listener to *feel* the gap - the end of a thought, a
paragraph, a scene, a chapter opening.

Recommended starting values, then tune by ear:

| Position | Duration |
|---|---|
| Between sentences, same speaker (only if the text feels rushed) | 0.3 - 0.5 s |
| End of paragraph / thought | 0.6 - 0.8 s |
| Speaker change in dialogue | 0.4 - 0.7 s |
| Scene or section break | 1.0 - 1.5 s |
| After a chapter title, before the body | 1.0 - 1.5 s |
| Dramatic beat (suspense, revelation) | 1.5 - 2.5 s |

Do not put a break after every sentence. Over-paced narration sounds like a
dictation exercise. Breaks are punctuation for the ear - use them where meaning
turns.

For a standalone pause between blocks, put `[break_X]` on its own line.

## Detecting speakers

Scan for these patterns before segmenting:

- Arabic attribution verbs: `قال فلان:` / `قالت` / `أجاب` / `همس` / `صاح`
- Quotation marks: `"..."` `«...»` `„..."`
- The dialogue dash at line start: `- ...`
- Script format: `NAME: line`

Build a **speakers map** (character -> voice) and keep it consistent for the whole
book. Persist it so later chapters cast identically.

## Casting

- One dedicated voice per recurring character, plus a distinct **narrator** voice.
- Adjacent speakers must be clearly distinguishable - do not cast two similar
  voices for two characters who talk to each other.
- Attribution tags (`قال أحمد`) belong to the **narrator**, not the character,
  unless the user asks otherwise.
- Get casting approved before rendering (this is a gate in every production mode).
- Preview with `play_voice_sample` before the user commits.

### Emotions in dialogue

Turn `emotions_mode` **on** for multi-voice dialogue - utterances are short and
the voice keeps changing, so the variation between generations reads as
performance rather than inconsistency. It is a clear quality gain for dialects in
particular.

Turn it **off** for a single-narrator production, even a dialect one. Over
hundreds of consecutive lines in the same voice that variation becomes an audible
stability problem. See `moknah-voice-settings`.

## Markup syntax - get this right or tags get read aloud

The tag syntax depends on `emotions_mode`:

- `emotions_mode: true` -> square brackets: `[happy]`, `[whispering]`, `[sighs]`
- `emotions_mode: false` -> SSML-style angle brackets `<...>`, used sparingly

**Never mix the two.** With emotions off, `[...]` tags are spoken aloud as text.

`[break_X]` works in both modes. X is seconds, 0.1-10.

Available emotion tags (emotions_mode true): `[laughing] [happy] [excited]
[angry] [shouting] [sad] [crying] [surprised] [afraid] [calm] [serious]
[sarcastic] [curious] [whispering] [sighs] [exhales] [wheezing] [snorts]
[mischievously] [questioning] [confident] [swallows] [gulps]`

Effects: `[applause] [clapping] [gunshot] [explosion]`

**Emotion and effect tags are experimental and not fully reliable.** Tell the user
that up front, and validate on one sample line before applying them book-wide.

A line containing only tags and no real words is skipped. Tags and breaks are not
billed beyond their character count.

## Checklist before rendering dialogue

1. Consecutive same-speaker lines merged.
2. A `[break_]` at every speaker change.
3. Beat pauses at paragraph, scene and chapter boundaries only.
4. Speakers map complete; every speaking character cast to a distinct voice.
5. Tag syntax matches `emotions_mode`.
6. One sample line rendered per voice and approved before the full run.
