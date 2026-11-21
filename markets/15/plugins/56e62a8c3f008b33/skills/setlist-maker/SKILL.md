---
name: setlist-maker
description: Make a printable band setlist (stage pages in large type plus a band copy table) with set and show totals and a CSV, using generate_setlist. Reads pasted song lists, set breaks, segues, keys, tempos, capo and transposition.
---

# Zovo Setlist Maker

Call `generate_setlist` when someone wants a setlist for a gig, a printable set list, a stage setlist, a setlist template filled with their songs, or wants to know how long their set runs.

1. When you can read the songs, pass `songs[]` in play order: `title`, and only the fields the user gave: `key`, `bpm`, `capo`, `duration` ("3:45"), `notes`, `segue` (runs into the next song), `transpose` (+2, -1 or "to A"). Put a plain string "SET 2" or "Encore" between songs to start a new set.
2. If the sets are already decided, pass `sets[]` with `name` and `songs`. If the list is messy or very long, pass it unchanged as `text`.
3. Do not invent keys, tempos or durations. Songs without a duration are left out of the totals and listed in the result.
4. To split one list, use `split_sets` (sets of similar length, order kept) or `break_after_minutes`. Add `changeover_seconds` if the user wants time between songs counted.
5. For a new singer or tuning, use `transpose_all` (semitones or a key) or `transpose` per song. The result gives the key to play in and capo shapes.
6. Options: `band`, `venue`, `date` (printed as given), `layout` (both, stage, band) and `paper` (letter, a4).
7. Share the set totals, the show total and the PDF and CSV links.

It does not look up song keys, tempos or lengths, and does not write chord charts or lyrics.
