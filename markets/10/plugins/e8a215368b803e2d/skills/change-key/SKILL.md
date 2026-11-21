---
name: change-key
description: Transpose a PlayableNotes score to another key, for example to suit a student's reading level or a singer's range.
---

# Changing the key

1. Call `get_score`. Read the `KEY:` header (fifths) and any `M<n> KEY:` changes. Work out the current key from the signature and the harmony (major or relative minor).
2. Choose the interval. Prefer the key the teacher named. If they asked for "easier", pick the nearest key with fewer accidentals, and say which key you chose and why.
3. Transpose every note by the same interval, spelling notes in the new key: a diatonic step moves to the matching scale step. Keep chromatic notes chromatic, with the same function. For example, a raised fourth stays a raised fourth.
4. Rewrite the accidentals as they would be printed in the new key. KM accidentals are printed accidentals: write one only where a printed score would show it. Use `n` where the new key signature has to be cancelled, and remember that accidentals carry through the measure on the same staff and line.
5. Change the `KEY:` header (and every `M<n> KEY:` line) to the new fifths. Minor keys share their relative major's signature.
6. Keep the register sensible. If the new key pushes the music far above or below the original, move it by an octave the other way. Move whole sections at once, and check that the left hand stays below the right.
7. Check the clefs: if the left hand now sits high, keep the bass clef unless the original changed clef there. Don't add clef changes the original didn't have.
8. Send the whole KM to `edit_score` with a summary such as "Transposed from E♭ major down a minor third to C major".

Check before sending: the number of measures and the rhythms are identical, only pitches, accidentals and key lines changed, and spot-checked chords still spell the right harmony (a V7 is still a V7).
