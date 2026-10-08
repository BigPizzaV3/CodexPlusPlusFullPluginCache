---
name: playable-fretted-parts
description: Write guitar, electric guitar, bass and ukulele parts (string/fret "bars" for Music Block) that a human can actually finger at the stated tempo. Use before composing any fretted lick, riff, exercise, bass line or chord voicing, and when fixing a playability warning.
---

Use this skill whenever a Music Block example contains a part written as `bars`
(string + fret per note) for guitar, electric-guitar, bass or ukulele. The
tool only rejects impossible input (two notes on one string, a string that does
not exist) and warns about chords wider than five frets. Everything below is
what the validator cannot judge and what separates real TAB from random
string/fret pairs.

## Workflow

1. Pick the position first. A position is the fret under the index finger.
   The hand covers that fret plus the next three (one finger per fret) and
   any open string. Write the whole phrase inside that window before
   considering a shift.
2. Choose strings for the line, not just pitches. Every pitch exists in
   several places; put a fast run on two or three adjacent strings inside the
   position rather than walking up one string.
3. Place shifts deliberately: on a slide, on an open string, on a long note,
   or at a rest. Never shift in the middle of a run of eighths or sixteenths.
4. Add technique markings where a player would use them (below). They are
   the main way to make a line sound human, because the format has no
   dynamics or articulation.
5. Before calling the tool, run the self-check at the end of this file.

## Left hand: positions and stretches

- One finger per fret. Inside a beat, fretted notes span at most 4 frets
  (open strings do not count). Across a phrase without a shift, at most 5.
- Above fret 12 the frets are closer; a span of 5 to 6 is fine there. Below
  fret 5 the frets are wide; keep spans to 4.
- A stretch of one extra fret with the pinky is fine for a single note, not
  for a repeated figure.
- Consecutive beats that jump more than 5 frets need a slide, a rest, or an
  open string between them. If none fits, refinger the second note on
  another string in the current position.
- Do not mirror keyboard thinking: a guitar run that changes string on every
  note is awkward. Group two to four notes per string.

## Tempo limits

| Tempo | Sixteenths | Eighths | Position shifts |
| --- | --- | --- | --- |
| up to 90 BPM | anywhere inside the position | free | on any beat boundary |
| 90 to 140 BPM | adjacent frets and adjacent strings only | free inside the position | at most one per bar, on a slide or long note |
| above 140 BPM | short bursts of 4 or fewer, on one string with hammer or pull | inside the position, at most two string changes per beat | none mid-phrase |

Triplet eighths count as eighths; sextuplets count as sixteenths.

## Technique markings

- `hammer` and `pull` connect this beat to the next beat on the SAME string,
  1 to 3 frets apart. Hammer goes up in pitch, pull goes down. Never mark a
  hammer or pull into a note on a different string or the last beat of the
  example.
- `slide` connects to the next beat on the same string. Keep slides to 5
  frets or less in fast passages; long slides only into a held note.
- `bend-half` and `bend-full` belong on strings 1 to 3 at fret 5 or higher.
  Bending a wound string (4 to 6) or a low fret is possible but rare; avoid it
  unless the user asks. A full bend needs the note below the target: write the
  fret of the starting pitch, the bend supplies the rest.
- `vibrato` on notes of a quarter or longer, especially phrase endings and
  bend peaks.
- `palm-mute` on low-string riff notes, typically eighths on strings 5 and 6.
- `let-ring` on arpeggiated chord tones on different strings.
- A single lick usually carries two to four markings, not one per note.

## Chord voicings

- At most 4 fretted notes in a shape unless one fret is a barre (two or more
  notes on the same fret with nothing lower). A barre covers all higher
  strings at that fret, so an open string cannot sit between barred strings.
- Fretted notes in a shape span at most 4 frets below fret 5, 5 frets higher
  up. The tool warns above 5.
- Every note in a chord is on a distinct string. Prefer common shapes: open
  chords, E and A shape barres, drop-2 and drop-3 voicings on strings 1 to 4
  or 2 to 5, shell voicings (root, 3rd, 7th) for jazz comping.
- Comping under a lick: 3 or 4 note voicings on the middle strings, not
  6-string barres on every beat.
- Chord notes played together must be reachable at the same time; do not
  combine a note at fret 2 on string 6 with fret 8 on string 1.

## Bass

- Same one-finger-per-fret rule over 4 frets; many players use a 3-fret
  span below fret 5. Open strings are the usual shift point.
- Walking bass: quarter notes, roots or fifths on beats 1 and 3, chord tones
  or chromatic approach notes on beats 2 and 4, at most one leap per bar.
- Sixteenth-note bass lines stay on one or two strings and repeat a pattern.
- Bass lines rarely go above fret 12 or use chords; keep the register in
  frets 0 to 9 unless the user wants a solo.

## Ukulele

- Standard tuning is re-entrant: string 4 (G4) is higher than string 3 (C4).
  Melodies live on strings 1 and 2, sometimes 3. Do not write a "low" bass
  note on string 4.
- Position window is 4 frets; chords use all four strings; no bends.

## Self-check before calling the tool

- Each phrase sits inside one 4-fret window (plus open strings) or shifts at
  a slide, open string, long note or rest.
- No beat-to-beat jump larger than 5 frets without one of those.
- Sixteenths obey the tempo table.
- Every hammer, pull and slide has a following note on the same string.
- Bends are on strings 1 to 3 at fret 5 or above.
- Chord shapes have at most 4 fretted notes or a barre, span 4 to 5 frets,
  and contain no open string between barred strings.
- Bass and ukulele parts follow their sections.

If the tool returns a playability warning, treat it as a bug in the example
and re-voice the beat rather than explaining the warning to the user.
