# Writing ABC for create_score

ScoreStarling reads ABC 2.1 with abc2xml, which handles several voices, piano staves, chord
symbols and lyrics. These patterns read correctly; keep to them.

## Header

```
X:1
T:Title as printed
C:Composer
M:3/4
L:1/8
Q:1/4=96
K:F
```

`K:` comes last. Write the printed key signature (`K:Bb`, `K:Gm`, `K:D dor`); for music without
one use `K:C` and write every accidental. `L:` is the unit length: with `L:1/8`, `c` is an eighth,
`c2` a quarter, `c3` a dotted quarter, `c/` a sixteenth, and `c>d` a dotted eighth and a
sixteenth (`c<d` the reverse). Leave `Q:` out when the page marks no tempo (it then plays at 100)
or pass the user's tempo as `bpm`.

Name the instrument and its clef even for a single line, before `K:`, so the part is labelled and
plays with the right sound: `V:1 clef=treble nm="Flute"` then `%%MIDI program 73`. Without a
`clef=`, a staff gets the treble clef, or the bass clef when its notes lie mostly below middle C.

## Notes

- Pitch: `C D E F G A B` from middle C (C4) up; `c d e ... b` the octave above (C5); `c'` C6;
  `C,` C3, `C,,` C2.
- Accidentals before the note: `^F` sharp, `_B` flat, `=B` natural, `^^F` / `__B` double. An
  accidental lasts to the end of the bar, as on the page. A note tied over the bar line passes
  its accidental to no later note: in `_E4- | _E2 E2 |` the last E reads as E natural, so write
  the accidental again (`_E2 _E2`).
- Rests: `z` (with length, `z2`), a whole-bar rest `Z`.
- Ties `c2-c`, slurs `(cde)`, triplets `(3cde`, grace notes `{g}a`, chords `[CEG]2`.
- Bar lines `|`, repeats `|:` and `:|`, endings `[1` and `[2`, final `|]`.
- A short first bar is the pickup; the last bar may complete it.

## Chord symbols and lyrics

```
"Am7"c2 e2 | "D7"d4 |
w:Twin-kle twin-kle lit-tle star
```

Chord symbols go in double quotes before the note they sit on; `"N.C."` (no chord) is drawn as
text. `w:` lines follow the line of music they belong to; `-` splits syllables, `_` holds a
syllable, `*` skips a note.

## Piano and other grand staves

Name only the first voice of a braced pair: then both staves form one piano part.

```
X:1
T:Two hands
M:4/4
L:1/8
%%score {RH | LH}
V:RH clef=treble nm="Piano"
V:LH clef=bass
K:G
V:RH
% bars 1-2
d2 g2 b2 a2 | g4- g2 z2 |
V:LH
% bars 1-2
G,,2 [D,G,B,]2 [D,G,B,]2 [D,F,A,]2 | G,,4- G,,2 z2 |
```

Two melodic lines on one staff (soprano and alto, a melody over held notes) use an overlay: `&`
inside the bar starts the second line, which must last the whole bar. Several instruments are
several voices, each with its own `nm=` and, for playback, `%%MIDI program n` (0-based General
MIDI) after its `V:` line.

## Jianpu

Write the tune in the key the `1=` names, so the digits keep their meaning:

| Jianpu | ABC with `K:D` (1=D) |
| --- | --- |
| `1 2 3 4 5 6 7` | `D E F G A B c` (1=D sits on D4) |
| a dot above the digit, a dot below it | the octave above (`d`), the octave below (`D,`) |
| one underline, two underlines | eighth, sixteenth (with `L:1/8`: `D` and `D/`) |
| a dash after a quarter (`5 -`), a dot beside it | a half note (`A4`), a dotted quarter (`A3`) |
| `0` | rest (`z`) |
| `#4`, `b7` (raised 4th, lowered 7th) | `^G`, `=c` (the key already sharpens C) |

Pick the octave so the melody's middle sits around middle C to the C two octaves up, as the
original staff notation or the singer would have it.

Minor tunes are written two ways. If the digits keep `1` as the home note and flatten 3 (often 6
and 7 too) throughout, the tune is in the minor of `1=`: `1=A` becomes `K:Am`, and its digits'
flats become plain notes. If `6` is the home note (la-based minor, as ScoreStarling's own jianpu
export writes), the key is the relative minor of `1=`: `1=C` with 6 as home is `K:Am`. A
dotted eighth and sixteenth (`1· 2` under one underline) is `A>B` with `L:1/8`.

## Checking before you call create_score

- Count the beats in every bar: each must add up to the time signature, except a pickup and the
  bar that completes it.
- Every voice has the same number of bars.
- Bars in ABC match the printed bars, one comment per system (`% bars 9-12`).
