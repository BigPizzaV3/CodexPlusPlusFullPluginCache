# Composing a tune that works as an alarm

## The speaker

A small speaker in a picture frame. It cannot reproduce deep bass: a note
under about 150 Hz mostly disappears.

| Octave | `c` is | Use |
|---|---|---|
| `o3` | 131 Hz | lowest useful bass (`C` channel) |
| `o4` | 262 Hz | bass that carries, harmony |
| `o5` | 523 Hz | melody |
| `o6` | 1047 Hz | bright melody, bird-like figures |
| `o7` | 2093 Hz | sparingly; with `@0` it is piercing |

Keep the melody in `o5`–`o6` and the bass in `o3`–`o4`. On channel `D`
the note sets how bright the noise is: `o2 c` a thud (kick), `o5 c` a snare,
`o7 c` a hi-hat.

## The shape of an alarm

- **Don't write a crescendo.** The frame already fades the whole tune in
  over `fade_in_seconds` (10 minutes by default). Write it at the level it
  should reach.
- **It loops.** 4 to 16 bars (roughly 8 to 40 s) is right. Make the last
  bar lead back into the first, and don't leave a long silence at the end:
  the loop would stutter.
- **Tempo sets the mood.** 80–110 for a gentle wake-up, 120–160 to get
  someone out of bed.
- The tune repeats for up to an hour. Favour something pleasant heard many
  times over something clever heard once.

## Balance between channels

All four play at once and add up. Starting points:

| Role | Settings |
|---|---|
| Melody `A` | `v12`–`v13`, `@1` or `@2`, `q7` |
| Harmony / arpeggio `B` | `v7`–`v9`, `@0` or `@1`, `s2` for plucked notes |
| Bass `C` | `v12`–`v14`, `@0` (a triangle sounds quieter than a square) |
| Drums `D` | kick `v12 s2 o2 c`, snare `v9 s2 o5 c`, hat `v5 s1 o7 c` |

Commands persist, so a drum pattern sets volume and decay on every hit:
`D l8 [v13 s2 o2 c v5 s1 o7 c v10 s2 o5 c v5 s1 o7 c]4`.

## Game Boy tricks

- **Arpeggio for chords.** A channel plays one note at a time, so cycle the
  chord tones fast: `B o4 l32 [c e g]…` or, slower and softer,
  `B o4 l8 [c e g e]2`.
- **Articulation.** `q4`–`q5` for bouncy, detached notes; `q8` with ties
  for sustained ones. `s1`–`s3` makes each note ring and fade like a pluck
  or a bell.
- **Colour.** Change `@` between sections (`@2` verse, `@1` chorus) for
  variety at no cost.
- **Echo.** Copy the melody to `B` at a lower volume, starting an eighth
  later: `B r8` at the start, and one eighth less at the end so the lengths
  stay equal.

## Counting, so the channels match

1. Choose the metre. In 4/4 every bar is 4 beats: `l4` notes count 1, `l8`
   count ½, a dot adds half.
2. Write each channel bar by bar, separated by `|`, and count each bar.
3. For longer tunes, put one phrase (2–4 bars) per line, in the order
   A, B, C, D, then the next phrase. `tune.py check` prints the beats of
   every line: all lines of one phrase should show the same number.
4. Without a sandbox, list the beats per bar in your head or in a comment
   (`; 4 4 4 4`) before sending.

## Staying under 2048 bytes

- Set a default length (`l8`) and only write lengths that differ from it.
- Use loops for repeated bars: `[c e g e]4`.
- Comments and extra spaces are removed before counting.
