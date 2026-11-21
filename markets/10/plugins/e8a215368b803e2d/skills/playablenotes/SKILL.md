---
name: playablenotes
description: Use PlayableNotes to read piano sheet music into playable scores, open the user's scores or library pieces, change them with KM edits, and make practice links for students.
---

# PlayableNotes

PlayableNotes is for piano teachers. Every score lives in the teacher's PlayableNotes account (the same one as the website), and every change is a new version. When connecting, the teacher confirms that they own the music they send or may use it for teaching.

## Tools

| Need | Tool |
| --- | --- |
| Sheet music attached (page photos, screenshots, PDFs or MusicXML) | `read_sheet_music`: pages in order; pass the title and composer if you can read them |
| A well-known piece | `find_library_piece`, then `open_library_piece` |
| The teacher's own scores | `my_scores`, then `open_score` |
| The notes of a score | `get_score` (KM, version number, things to check). Use `measures: "5-12"` for part of a long score |
| A change | `edit_score` with the version you read, a one-sentence summary, and the changed measures (or the whole KM) |
| Title, composer, tempo | `set_score_details` |
| A link for a student | `share_with_student`, named after the student |
| Another arrangement, keeping the original | `copy_score`, then change the copy |
| A new piece or exercise from a description (nothing attached) | `arranging_guide` `compose`, then `create_score` with the whole KM |
| Guidance for a task | `arranging_guide` (`arrange-for-student`, `change-key`, `check-score`) |

Reading attached music uses the account's credits, 1 per line of music (pages without music are skipped, and none are used if reading fails); nothing else does. `my_scores` gives the balance if the teacher asks. If the account has too few, nothing is read: say how many are needed and how many they have. Nothing is sold in ChatGPT: don't say what credits cost, offer more, or link to a page for paying. If asked how to get more, say credits are managed in their account on the PlayableNotes website.

Reading takes a minute or two. The card shows progress, so don't keep calling `get_score` in a loop; one check after the teacher replies is enough. When the score is ready, mention any "things to check" and offer to review them, but don't start unless asked.

## Changing a score

1. Read the right guide first (`arranging_guide`).
2. Call `get_score` and work from that exact KM and version.
3. Make the change. Keep everything you weren't asked to change exactly as it is: dynamics, slurs, articulations, ornaments, repeats and endings, fingering-free layout, measure numbers.
4. Call `edit_score`. Send only the changed measures, each with all its lines (RH, LH, RH2/LH2, and any `M<n> KEY:` or `M<n> TIME:` line for it). For a change everywhere (a new key, a whole simplification), send the whole KM.
5. If `edit_score` lists errors, fix exactly those measures and send them again.
6. Tell the teacher what you changed in a sentence or two, the way one musician tells another ("the left hand is now block chords on beat one; the run in m. 12 is two octaves shorter").

If the card says the teacher selected a measure, "this measure" means that one.

## KM essentials

- Header: `KEY: <fifths>  TIME: <beats>/<beat-type>`. Sharps are positive and flats negative: `KEY: -3` is E♭ major or C minor.
- One line per staff per measure: `M7 RH: {G} E5/8 D#5/8 E5/4 r/4`, `M7 LH: {F} A2/8 E3/8 A3/4 r/4`. Each line starts with its clef.
- Durations: 1 2 4 8 16 32 (whole to thirty-second), with `.` for a dot and `t3` for triplets (`8t3`). Chords are `[C4 E4 G4]/2`, a rest is `r/4`, a spacer is `s/4`, and a whole-measure rest is `R`.
- Every voice must fill its measure exactly, except a pickup measure.
- Accidentals are written as printed: the key signature and earlier accidentals in the measure apply automatically. In D major `F4` sounds F♯ and `Fn4` is F natural.
- Ties are `~` after the duration, and dynamics come before a note (`\p C4/4`). Slurs, hairpins and ottavas use tags: `<slur> … </slur>`, `<cresc> … </cresc>`, `<8va> … </8va>`.
- Ornaments and fermatas follow the duration: `D5/4\trill`, `\prall` (upper mordent), `\mordent` (lower mordent), `\turn`, `\fermata` (also `r/4\fermata`, `R\fermata`).
- Repeats are written once, in printed order, on the measure's RH line: `|:` starts it for a start-repeat, `:|` ends it for an end-repeat, `||` is a double barline and `|]` a final one. Every measure under an ending bracket starts with `[1` or `[2`: `M8 RH: [1 {G} G4/2 :|`. Playback follows the repeats.

## Practice links

`share_with_student` makes a fixed copy of the current version at an unlisted link. Students can play it at any tempo, loop a passage, play hands separately and print it, without an account. Links are only for the teacher's own students. A later edit doesn't change an existing link; the teacher can update or revoke links in the PlayableNotes studio.
