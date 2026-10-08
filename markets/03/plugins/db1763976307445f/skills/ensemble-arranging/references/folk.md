# Folk and traditional ensembles

## Roles

| Role | Instruments |
| --- | --- |
| melody | violin (fiddle), flute, recorder, pan-flute, voice, accordion written as organ, mandolin written as guitar |
| drone or chords | guitar (open chords or DADGAD), ukulele, organ held fifths, strings pad |
| bass | bass or contrabass on roots and fifths, or the guitar's low strings |
| rhythm | guitar strum patterns; drums only for revival or country bands |

One instrument carries the melody at a time. A second melody instrument
doubles it in unison with small differences (heterophony), not in harmony.

## Modal harmony

- Find the mode of the tune before choosing chords: Ionian (major),
  Mixolydian (major with b7), Dorian (minor with natural 6), Aeolian
  (natural minor).
- Mixolydian tunes: I and bVII, sometimes IV. No V7.
- Dorian tunes: i, IV (major) and bVII. No V7 to i.
- Aeolian tunes: i, bVII, bVI, and a minor v.
- Ionian tunes: I, IV, V and vi; V7 is fine here.
- Triads only, no 7ths or extensions except a sus4 or an added 2nd on a
  drone chord. One or two chords per bar; put the second chord on the beat
  `chord` field.
- A drone (root and fifth held, or an open-string pedal) under a modal
  melody is often better than chord changes.

## Rhythm patterns

| Tune type | Meter | Guitar | Bass |
| --- | --- | --- | --- |
| reel, hornpipe | 4/4 | boom-chuck: bass note on 1 and 3, chord on 2 and 4 | roots on 1 and 3 |
| jig | 6/8 | bass note on 1, chord on 2 and 3 (twice per bar) | root on 1, fifth on 4 |
| waltz | 3/4 | bass note on 1, chord on 2 and 3 | root on 1 |
| polka, march | 2/4 | bass note on 1, chord on 2 | roots on 1 |
| ballad | 4/4 or 3/4 | arpeggiated open chords with let-ring | half notes or none |

Set `feel: straight`. Jigs and reels are not swung.

## Form and texture

- Tunes are AABB with eight-bar parts. Arrange by changing the texture per
  repeat, not the melody: A alone with guitar, A again with the bass
  entering, B with a second instrument in unison, B again with a drone
  under it.
- Ornaments (rolls, cuts) are not available; use a quick sixteenth-note
  neighbour before the main note, sparingly.
- Melodies stay inside an octave and a fifth, mostly stepwise with
  arpeggiated leaps on chord tones.
- Guitar in DADGAD: set `tuning: "dadgad"`, use open strings as drones,
  chords as two or three fretted notes plus open strings.
- Endings: the last melody note held for a full bar with the chord under it;
  no drum fill, no big final chord in every part.
- Harmony singing, when used: a second voice a third above or a sixth below
  the melody on the chorus only, same rhythm, same words.
