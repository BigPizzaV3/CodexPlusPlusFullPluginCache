---
name: ensemble-arranging
description: Arrange a melody or progression for a group in Music Block — jazz combo or big band horns, rock, pop or funk band, string quartet, choir, folk ensemble. Use whenever an example has three or more parts, or the user asks for an arrangement, a head, a chart, a section, a band or a choir.
---

Use this skill when a Music Block example has three or more parts, or when the
user asks for an arrangement of any kind. Six parts written one after another
against a chord symbol are not an arrangement: each part picks its own
alterations and passing tones, nothing rests, and the result clashes. An
arrangement is built in a fixed order, and the order is what this skill
enforces. Open the matching file in `references/` for the ensemble before
writing a note.

The tool checks every part against the chord symbol in effect on each beat
and rejects two spellings of one chord degree sounding together (natural 9
against b9, natural 5 against b13, major 3rd against minor 3rd, b7 against
major 7th). It warns about non-chord tones parked on strong beats, semitone
collisions, crossed or gapped section voices, a piano left hand doubling the
bass, and wind parts that never rest. Treat every one of those as a bug.

## Workflow

1. **Lead sheet first.** Write the melody and the chord symbols before any
   other part. Put the chord on every bar's `chord` field; when the harmony
   changes inside a bar, put the second chord on the `chord` field of the
   beat where it starts. Compose the melody with human-melodic-phrasing.
2. **Assign roles.** Every part gets exactly one role: lead, harmony
   (section voices under the lead), bass, comping or pad, time (drums).
   The reference file for the ensemble lists which instrument takes which
   role. Two parts never share the comping role in the same register.
3. **Decide one spelling per chord.** Before writing harmony parts, list the
   chord tones and the tensions you will use for each bar and stick to them
   in every part. If the symbol says alt, b9 or b13, no part plays the
   natural 9, 5 or 13 anywhere in that bar. If you want a natural 9, change
   the symbol.
4. **Derive the harmony parts from the lead, beat by beat.** Section voices
   share the lead's rhythm (block writing) or hold long notes under it
   (backgrounds). Each voice is within an octave of the voice above and
   never crosses it. Use only chord tones and agreed tensions on the lead's
   attacks; passing tones only where the lead has one too. Voicing recipes
   are in the reference file.
5. **Write the bass.** Roots on strong beats, approach notes into the next
   chord, one register, contrary motion against the melody where possible.
   With a bass part, the piano left hand stays above C3 and never plays
   roots in half notes.
6. **Add comping in the gaps.** Piano or guitar hits fall where the melody
   rests or holds, on offbeats, three or four notes per voicing, roots
   omitted when there is a bass.
7. **Add time.** Drums follow the style pattern in the reference, vary the
   kick every two to four bars, one fill at the phrase end.
8. **Plan the space.** Horns and voices phrase for two bars and rest for at
   least a beat. Backgrounds enter after the lead has started a phrase.
   Not every part plays in every bar; a part dropping out for a bar is an
   arranging tool. Keep the bar count equal by writing rests.
9. **Check the verticals.** For each beat, list what every part sounds.
   Confirm: one chord spelling, no semitone between parts unless both notes
   are chord tones or tensions of the symbol, upper voices within an octave
   of their neighbours, bass alone below C3, everything inside the
   instrument ranges from instrument-ranges-and-idioms.
10. Call the tool. If it returns harmony errors or warnings, fix the beat it
    names rather than defending it.

## Universal rules

- **Register map.** Bass instruments own E1 to G3. Comping and inner voices
  live between C3 and C5. The lead sits between C4 and C6. Pads hold the
  middle. Two parts in the same register playing the same rhythm is mud.
- **Guide tones carry the harmony.** In any voicing the 3rd and 7th must be
  present; the root belongs to the bass; the 5th is the first note to drop.
  Guide tones move by step from chord to chord.
- **Doubling.** Double the root or the 5th, never the 3rd or the 7th, and
  never the tension.
- **Motion.** Not every part changes notes on every beat. Hold at least one
  part through each bar. Melody and bass prefer contrary motion.
- **Low interval limits.** No thirds below C3, no seconds below G3, no
  minor 9ths against the bass anywhere.
- **Repetition is structure.** Bars 5 to 8 of an eight-bar arrangement
  reuse the rhythm and texture of bars 1 to 4 with a different ending. A new
  texture every bar sounds generated.
- **Music Block limits.** Up to eight parts; every part the same bar count;
  set `feel` for swing rather than writing triplets; keep every part
  engraved in an arrangement; write concert pitch, the tool transposes.

## Self-check before calling the tool

- The melody and chords were written first, and the chords are on every bar.
- Every part has one role and one register; no two parts comp together.
- One spelling per chord, obeyed by every part, alterations included.
- Section voices follow the lead's rhythm or hold, within an octave, never
  crossing.
- Bass has the roots; piano left hand stays above C3.
- Horns and voices rest at least every two bars; at least one part is silent
  in at least one bar.
- Bars 5 to 8 echo bars 1 to 4.
