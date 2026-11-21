---
name: compose
description: Write a new piano piece, exercise or study from a description, with no sheet music attached, at the right level for a student, and save it to PlayableNotes as a playable, editable score. Use for "write me…", "compose…", "make up a piece…" requests.
---

# Composing a piece

The goal is a short piece that sounds like music, sits well under the hands, and is exactly as hard as the student can manage. Write original material.

## Pin down the request

Choose sensible defaults instead of asking. Ask one short question only when the level is unknown and the request depends on it: "Who is it for: a first-year student, or someone further along?" Use the levels in `arrange-for-student` (1 · First year to 4 · Intermediate); the user's own description always wins.

Defaults when the user hasn't said:

- **Length:** 8 measures at level 1; 16 at levels 2 and 3; up to 32 at level 4.
- **Key:** one from the level's list (C, G or F major, or A minor, at level 1). Minor for sad, spooky or mysterious requests.
- **Meter:** 3/4 for a waltz or minuet, 2/4 or 4/4 for a march, 6/8 or 3/4 for a lullaby, 4/4 otherwise.
- **Title:** short and fitting ("Morning Waltz", "Rainy Day Blues"). Leave the composer out unless the user gives one.

## Plan before writing

1. **Form.** Build in 4-measure phrases. 8 measures: a question phrase ending on V (half cadence), then an answer that ends on I. 16 measures: A A′ B A′. End on the tonic, on a long note, after V–I.
2. **Harmony.** Write a chord plan first, one chord per measure at levels 1 and 2, for example I I V V | I IV V I. Use I, IV, V and vi; add ii and V7 from level 3.
3. **Melody (right hand).** Mostly steps, some skips of a third, leaps only to chord tones. Repeat and vary a motive: measure 3 echoes measure 1's rhythm. One high point, in the second half. Each phrase ends on a tone of its cadence chord.
4. **Accompaniment (left hand), by level:**
   - 1: single bass notes or open fifths (`[C3 G3]/1`), one per measure or per half.
   - 2: root-position triads or root and fifth on the beats; simple broken chords in quarters.
   - 3: Alberti bass or broken chords in eighths; inversions for smooth voice leading.
   - 4: freer patterns, bass lines and octaves.
5. **Rhythm and range** follow the level table in `arrange-for-student`. Keep the right hand around C4 to G5 (a five-finger position at level 1) and the left hand around C2 to C4, below the right hand, so the hands never collide.
6. **Style.** Waltz: bass on beat 1, chord on beats 2 and 3 (level 2 and up). March: dotted rhythms, strong beats. Lullaby: gentle, stepwise, soft. Blues: 12 measures of I-IV-V, written in straight eighths. Rock or pop feel: steady left-hand eighths on roots and fifths.
7. **Marks.** A dynamic at the start, a crescendo into the high point, slurs over phrases from level 2, and a final barline.

## Write the KM

Follow the KM rules (`arranging_guide playablenotes` covers them in depth):

- The first line is `KEY: <fifths>  TIME: <beats>/<beat-type>`, for example `KEY: -1  TIME: 3/4` for F major in 3/4.
- Then, for every measure, `M<n> RH:` and `M<n> LH:` lines. Put `{G}` and `{F}` clefs on measure 1.
- Every line must add up to exactly one measure. Count the beats in each line before saving.
- Write accidentals only where they would be printed: the key signature applies automatically.
- End the last right-hand line with `|]`.

Example, 8 measures at level 1 (a shape to follow, not to copy):

```km
KEY: 0  TIME: 4/4
M1 RH: {G} \mf <slur> C4/4 D4/4 E4/4 F4/4 </slur>
M1 LH: {F} [C3 G3]/1
M2 RH: G4/2 E4/2
M2 LH: [C3 G3]/1
M3 RH: <slur> F4/4 E4/4 D4/4 E4/4 </slur>
M3 LH: [G2 D3]/1
M4 RH: D4/1
M4 LH: [G2 D3]/1
M5 RH: <slur> C4/4 D4/4 E4/4 F4/4 </slur>
M5 LH: [C3 G3]/1
M6 RH: G4/2 A4/2
M6 LH: [F2 C3]/1
M7 RH: G4/4 F4/4 E4/4 D4/4
M7 LH: [G2 D3]/1
M8 RH: C4/1 |]
M8 LH: [C3 G3]/1
```

Call `create_score` with the title, the whole KM, a tempo that suits the style, and the request in a sentence. It checks the KM first: if anything is wrong (a measure with too many or too few beats, an unknown symbol), it saves nothing and lists each problem by line and measure. Fix those lines and call it again.

## After saving

Describe the piece in a sentence or two, for a musician: the key, the form, and what the student practises in it. Offer one follow-up: easier or harder, another key (`change-key`), or a practice link (`share_with_student`). Every later change is a new version through `edit_score`.

## Copyright

Write original music. Don't write out copyrighted songs (current pop songs, film or show tunes) from memory, not even approximately; offer an original piece in that style or mood instead. Traditional and public-domain tunes, such as folk songs, hymns, carols and classical themes like Ode to Joy, can be arranged.
