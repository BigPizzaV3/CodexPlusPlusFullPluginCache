---
name: chord-charts
description: Make printable chord diagram PDFs for guitar (standard tuning), ukulele (G C E A) and piano from a list of chords or a pasted chord sheet, with transpose, capo, left-handed diagrams and note-checked shapes, using generate_chord_chart and find_chord_fingerings.
---

# Zovo Chord Chart Maker

Use `generate_chord_chart` for a printable chord chart or chord diagrams for a song. Use `find_chord_fingerings` when the user asks how to play one or a few chords (it returns up to 4 positions per chord).

1. Put chord names in `chords` as a list, e.g. `["G", "Em", "C", "D"]`. If the user pastes a song or uploads a photo of a chord sheet, read the chord names from it yourself and send the list. Pass raw pasted text in `chord_sheet` only when you cannot list the chords.
2. `instrument`: `guitar` (default), `ukulele` or `piano`. For several, send them together, e.g. `"guitar and ukulele"`; each instrument gets its own pages in the same PDF.
3. Transpose with `transpose_semitones` (e.g. 2 or -3) or `to_key` (e.g. "A"; add `from_key` when the song's key is known). Use `capo` for a capo fret. By default the chord names are the shapes fingered with the capo, as chord sheets that say "Capo 2" write them. If the user gives the chords that should sound and asks which shapes to play with a capo, add `capo_mode: "sounding"`. Use `capo: "auto"` when the user wants easy open shapes.
4. Optional: `left_handed: true`, `per_page` 6, 12 or 24, `paper` letter or a4, `title`.
5. After the tool returns, give the PDF link, list any chords it could not draw with the reason, and repeat any transposition or capo note.

Do not use it for bass, mandolin, banjo or alternate tunings, for tabs or sheet music, or for audio.
