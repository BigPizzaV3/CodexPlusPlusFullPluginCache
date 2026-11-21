---
name: wignet-tunes
description: Compose the melody a Écran Papier e-paper frame's alarm clock plays — write it in MML (four Game Boy-style channels), check it, let the owner hear a WAV preview, and set it on the alarm. Use when the owner wants their frame's alarm to play a tune, jingle or melody, or to change, fix or explain an alarm tune.
---

# Écran Papier alarm tunes

Some Écran Papier frames are alarm clocks with a small speaker. An alarm can
ring a WAV built into the frame (`sound`) or play a **tune** you write:
text in MML, a music notation from old computers and game consoles, played
on four Game Boy-style channels and looped for as long as the alarm rings.
This skill covers writing one. Driving the frame in general (links,
connectors, the verify loop) is the `wignet` skill.

## 1. Can this frame play a tune?

`get_capabilities` → `tune` must be `true`. It is only true when the frame's
own firmware says it plays tunes. When it is `false` but `alarm` is `true`,
the alarm works with its built-in sound; setting a tune is refused. Tell the
owner a firmware update is needed. Don't retry.

## 2. The loop

1. `get_alarm_schedule`: pick the alarm by `id` (ask if there are several),
   note its `volume`, `fade_in_seconds` and `max_duration_seconds`.
2. Compose (§3, and `references/composing.md` for what sounds good on this
   speaker). Start from `references/examples.md` when the owner has no
   particular idea.
3. **Check it** if you can run code:
   `python3 scripts/tune.py check tune.mml`. It uses the platform's own
   parser: pass here, pass there. It prints the beats of every line, which is
   how you fix the most common error (§4).
4. **Let the owner listen** before anything changes on the frame:
   `preview_tune` with `{"tune": "<the text>"}` checks it and returns a link
   to a player that runs in the browser, sample for sample what the frame's
   synthesizer plays (minus the fade-in and the speaker). Give the owner the
   link; they press Play. Hosts that show MCP Apps display the player right
   in the conversation. No connector? `python3 scripts/tune.py link tune.mml
   --base https://app.ecranpapier.com` prints the same link, and `tune.py wav tune.mml -o
   tune.wav` makes a file you can hand over.
5. `update_alarm` with `{"id": "<id>", "tune": "<the text>"}`. It keeps the
   alarm's other settings. `"tune": null` goes back to the built-in sound.
   The reply holds the tune as stored (normalized: comments removed,
   commands lowercased).
6. Tell the owner what happens next. The frame picks the change up at its
   next check, within 15 minutes while an alarm is set; an alarm due sooner
   rings its previous sound. At the alarm the volume rises from silence over
   `fade_in_seconds`, then the tune loops for `max_duration_seconds`. Any
   button stops it.

No code sandbox? Skip step 3: `preview_tune` and `update_alarm` both refuse
a tune they cannot play and say where the problem is (§5).

## 3. The notation

```
; A comment. One line per channel; a channel can continue on later lines.
A t120 o5 l8 v12 @2 c e g >c< | g e c r
C o3 l2 c g
```

| Channel | Sound | `@` choices |
|---|---|---|
| `A`, `B` | square wave: melody, harmony | `@0` thin … `@3` full (duty 12.5/25/**50**/75 %) |
| `C` | soft wave: bass, pads | `@0` **triangle**, `@1` sawtooth |
| `D` | noise: drums | `@0` **white**, `@1` metallic |

| Write | Means |
|---|---|
| `c d e f g a b` | a note; `+` or `#` sharp, `-` flat: `f+`, `b-` |
| `r` | a rest |
| `4`, `8.`… after a note or rest | length: `1 2 4 8 16 32 64` (`3 6 12 24 48` for triplets); a dot adds half |
| `c4&c8` | a tie: one note of both lengths, same pitch only |
| `o1`–`o7`, `>` `<` | octave (`o4 c` = middle C), one up, one down |
| `l8` | default length for notes written without one (**`l4`**) |
| `t40`–`t240` | tempo, quarter notes per minute (**120**) |
| `v0`–`v15` | volume (**12**) |
| `s0`–`s7` | decay: each note fades, `s1` fastest; **`s0`** holds |
| `q1`–`q8` | how much of each note sounds, in eighths (**`q7`**; `q8` = legato) |
| `[ … ]3` | repeat 2–16 times (**2**), nests 4 deep |
| `\|` | bar line, ignored: use it to count |

Commands are case-insensitive; the channel letter must be uppercase.

## 4. The rules that trip people

1. **Every channel lasts exactly as long as the others**, counting rests.
   The tune loops, so a short channel would drift. Write in bars (`|`),
   count beats per bar, and pad the end with rests. `tune.py check` shows
   each line's beats.
2. **`t` goes before the channel's first note**, and every channel that sets
   it uses the same value. Setting it on channel A alone is enough.
3. **State carries on.** Octave, length, volume and `@` stay set until
   changed, across lines too. `>` and `<` are relative, so restate `o…` at
   the start of every line; that keeps a mistake from spreading.
4. A loop `[ … ]` opens and closes on one line. A tie joins the same pitch.
5. At most 2048 bytes once normalized and 180 s per loop. Use loops and a
   default length `l…` to stay short.
6. Plain ASCII: no quotes, backslashes or braces.

## 5. When something is refused

The error names the line of your text and quotes the spot, e.g.
`line 3 near "c4 h4": unknown command 'h'`, or
`channel B lasts 15 beats but channel A lasts 16`. Fix that spot only and
send it again. If an alarm rang its old sound, the frame had not synced
yet (§2.6). A frame whose firmware rejects a tune plays its WAV, and failing
that, a beep.

## 6. Melodies from elsewhere

Write original tunes, or arrange melodies in the public domain (folk songs,
classical works whose composers died long ago). For a song still under
copyright, don't transcribe it: write an original tune in its style,
tempo and mood, and say so.
