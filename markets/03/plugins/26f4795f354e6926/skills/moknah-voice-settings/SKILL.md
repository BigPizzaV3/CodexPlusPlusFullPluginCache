---
name: moknah-voice-settings
description: What every Moknah voice parameter does - voice_id, temperature, similarity, speed, expressiveness, emotions_mode, prerecording - how the server/user/project/line cascade resolves, and which settings to use for Standard Arabic, dialects, non-Arabic and poetry. Use when choosing or tuning voice settings, or when rendered audio sounds wrong.
---

# Moknah voice settings

## The cascade

Settings resolve from the most general to the most specific:

```
server default  <  user default  <  project  <  line
```

A `null` at any level means **inherit from the level above**. Set the project
voice once; override individual lines only by exception. Do not stamp the same
value onto 200 lines - that is what the project level is for.

- `set_project_voice` - the book's default voice and settings
- `set_line_voice_settings` - one line's override
- `update_lines` - batch overrides, up to 200 lines in a single call

## The parameters

### `voice_id`
Which voice speaks. Must come from `list_voices` - never invent an id, and only
voices the user actually has access to will work. Premium voices add a
percentage fee on top of the per-character rate, so the same text costs more.

### `prerecording` - the text pre-processing pipeline
This is the highest-impact setting for Arabic. It selects how the text is
prepared *before* synthesis.

| Value | Mode | Use for |
|---|---|---|
| `1` | Normal | Dialects, all non-Arabic languages |
| `2` | Arabic Tashkeel | Standard Arabic (fusha) only - applies contextual diacritics |
| `3` | AI-poet | Poetry and metered verse |

`prerecording: 2` markedly improves fusha pronunciation because Arabic script is
ambiguous without diacritics (`كُتب` vs `كَتب`). **Never use it on dialects or
non-Arabic text** - it will impose fusha diacritics on words that do not take
them and the output gets worse, not better. It is billed at the advanced rate.

### `emotions_mode` - the expressive engine
`true` enables the expressive engine and square-bracket emotion tags. `false`
keeps the standard engine.

It sounds **markedly better for dialects and for dialogue**. But every generation
comes out slightly different, so it carries a real stability cost.

**The deciding question is how many voices the production uses:**

- **Dialogue / multi-voice -> emotions ON.** Utterances are short and the voice
  keeps changing, so variation between lines reads as natural performance.
- **Single narrator ("one man show") -> emotions OFF**, even for dialect. Across
  hundreds of consecutive lines in one voice, that same variation turns into an
  audible inconsistency the listener notices immediately. Stability wins.

This supersedes any blanket "dialects always use emotions" rule: for dialect
content the mode still helps, but only when more than one voice is speaking.

Other consequences:
- Tag syntax flips: `true` -> `[happy]`; `false` -> SSML `<...>`. Mixing them
  makes the tags get read aloud as literal text.
- The per-request character limit drops: **3,000 with emotions on, 10,000 off.**

### `speed`
Delivery rate. Range `0.7` - `1.2`; `1.0` is natural. Leave at 1.0 unless the
user asks. Small moves (0.95, 1.05) are usually enough - anything past ~1.15
starts to sound clipped.

### `similarity`
How closely the output tracks the reference voice's timbre and identity.
Keep it **high** as the default - that is what makes a voice sound like itself
across a whole book. Lower it only when the voice is a clone made from noisy
source audio, where a high value faithfully reproduces the noise and artefacts
along with the voice.

### `temperature`
Variability between renders. Lower = more consistent, steadier, more predictable
delivery. Higher = more variation and life, at the cost of consistency.

**Hard ceiling: never go above 0.75.** Past that the model begins to
**hallucinate** - inventing words, dropping text, mangling phrases. This is not a
"slightly less polished" threshold; it is the point where the output stops being
trustworthy and has to be checked word by word.

- Fusha narration: leave at default. Consistency across hundreds of lines matters
  more than per-line colour.
- Dialect: nudge slightly up - dialect delivery sounds flat when too tightly
  constrained - but stay well below 0.75.

### `expressiveness`
How much prosodic style is applied - emphasis, dynamic range, dramatic contour.

**Keep it at 0. Never raise it on your own initiative.** This parameter is
extremely sensitive - small increases cause hallucination, not merely a livelier
reading.

Raise it only when the user explicitly asks for it, and when they do:

1. **Warn them it risks hallucinated audio.**
2. Render a single sample line and have them check it before applying it anywhere
   else.

If output starts inventing or dropping words, this is the first setting to put
back to 0.

## Settings by scenario

`expressiveness` is `0` in every row - it is never raised except on explicit
user request. `temperature` never exceeds `0.75` in any row.

| Scenario | prerecording | emotions_mode | temperature | expressiveness | speed |
|---|---|---|---|---|---|
| Fusha, single narrator | 2 (Tashkeel) | false | default | 0 | 1.0 |
| Fusha, single-paragraph input | 2 | true | default | 0 | 1.0 |
| Dialect, single narrator | 1 | **false** (stability) | slightly up, < 0.75 | 0 | 1.0 |
| Dialect, dialogue / multi-voice | 1 | **true** | slightly up, < 0.75 | 0 | 1.0 |
| Non-Arabic, single narrator | 1 | false | default | 0 | 1.0 |
| Non-Arabic, dialogue / multi-voice | 1 | **true** | default | 0 | 1.0 |
| Poetry / verse | 3 (AI-poet) | false | default | 0 | 1.0 |

Detect the language from the text itself and apply the matching row - do not ask
the user to specify it if the text makes it obvious.

## Voice choice by content

- **Fusha book** -> a fusha voice. A dialect voice reading fusha sounds livelier
  and is acceptable if the user prefers it.
- **Dialect book** -> the voice *must* match the dialect. Prime it by opening
  with a strongly dialectal word so the voice settles into the register.
- **Dialogue** -> a distinct voice per character plus a separate narrator voice.
  See the `moknah-dialogue-and-pacing` skill.

## Diagnosing bad output

| Symptom | First thing to change |
|---|---|
| **Invented words, dropped or mangled text (hallucination)** | `temperature` is above 0.75, or `expressiveness` is above 0. Put both back down - this is the cause almost every time |
| Arabic words mispronounced / wrong vowels | fusha? set `prerecording: 2`. Dialect? make sure it is `1` |
| Tags read aloud as words | `emotions_mode` is false but `[...]` tags are in the text |
| Delivery inconsistent between lines in one voice | `emotions_mode` is on for a single-narrator book - turn it off; then lower `temperature` |
| Flat, lifeless dialect narration | raise `temperature` slightly (stay < 0.75); turn on `emotions_mode` **only** if multi-voice |
| Voice does not sound like the reference | raise `similarity` |
| Clone reproduces hiss/artefacts | lower `similarity` |
| Choppy, restarting delivery mid-thought | not a settings problem - merge the lines (dialogue skill) |

Change **one** setting at a time and re-render a single line with
`generate_lines`. Do not re-render a chapter to test a hypothesis.

## Cost note

Voice settings are free to change - only rendering costs credits. Iterate on
settings against one short sample line until the user approves, then run the
book. Fixing a setting after a full render costs a full re-render.
