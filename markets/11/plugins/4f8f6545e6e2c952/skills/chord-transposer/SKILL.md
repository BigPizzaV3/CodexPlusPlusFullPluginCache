---
name: chord-transposer
description: Transpose chord sheets, find capo shapes and show an interactive monospaced sheet with a printable monospaced PDF.
---

# Keyshift Chord Transposer

Call `transpose_chords` with `sheet` and one choice: `semitones` (-11 to +11), `from_key` with `to_key` (same major/minor mode), or `capo_fret` (0 to 9). A capo-fret input returns shapes below the sounding key; shapes plus fret reproduce that key. Use `spelling: auto` for target-key spelling, or `sharps`/`flats` for consistent spelling across round trips.

Call `find_capo_options` with a sounding `key` or a `chords` list (1 to 100 names). Share the ten fret options and easy open chord counts. For a key input it uses the seven diatonic triads; ease counts only the listed open chord names and their 7 forms.

Call `show_chord_sheet` with `sheet` and optionally `from_key` to show the unshifted sheet. Its -1/+1 controls call `transpose_chords` on the current sheet.

Chord sheets support chord-only lines above lyrics and ChordPro brackets such as `[Am]Lantern [F]garden`. Sheets have a 12,000-character limit. Root and slash bass move; quality text stays the same. Tabs use 8-column stops, and collisions move later chords right with one separating space.

Read the summary, chord mapping, estimate note and PDF link to the user. Lyrics are in widget-only metadata and a sealed stateless file link, not the model-visible summary. The key estimate considers the first and last chord and can be wrong for songs that change key.

PDFs print Latin, Greek, Cyrillic, Vietnamese, Chinese, Japanese and Korean lyrics; CJK characters take two columns. Right-to-left scripts and emoji get a note instead of a PDF; do not silently transliterate the user's lyrics. No audio, tablature or staff notation is supported.

Conventional qualities combine minor/major aliases, extensions, suspensions, additions and alterations (for example min7, mmaj7 and maj7#11). Enharmonic names normalize to the chosen spelling; a reverse shift can restore pitches without restoring the original names. Keep the original sheet when its spelling must be restored.
