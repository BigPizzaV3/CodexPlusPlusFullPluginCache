---
name: nonogram-maker
description: Make printable nonogram puzzles (griddlers, hanjie, paint-by-number logic puzzles) from a built-in picture, a word, the user's own pixel grid or a random grid, as a PDF with an answer key, using generate_nonograms. Each puzzle has one solution, checked by a line solver.
---

# Zovo Nonogram Maker

Call `generate_nonograms` when someone wants a nonogram, a griddler, a hanjie, a paint-by-number logic puzzle, or wants to turn pixel art into a puzzle.

1. Put one object per puzzle in `puzzles` when they differ: `shape` (heart, star, house, cat, dog, fish, tree, smiley, apple, rocket, umbrella, note, anchor, duck, flower, crown, key, bell, moon, ghost), `text` (a word, A-Z and 0-9, up to 8 letters), `grid` (the user's rows, `#` filled and `.` empty, up to 25 x 25), or `difficulty` / `size` for a random grid.
2. For a set of random puzzles, pass `count` with `difficulty` (easy 10 x 10, medium 15 x 15, hard 20 x 20, expert 25 x 25) or `size`.
3. Pasted pixel art: send the rows as they are in `grid`; `/`, `|` or new lines separate rows, and `1`/`0` or `X`/`.` also work.
4. When a picture's clues allow more than one solution, `fix` decides: `hints` (default) prints a few shaded starter cells, `change` flips a few cells, `refuse` returns an error that lists the unclear rows. Use `refuse` when the user wants the picture unchanged and no starter cells.
5. Layout: `per_page` (1, 2 or 4), `paper` (letter or a4), `title`, `name_line`, `answer_key`.
6. Share the PDF link. Do not reveal the picture in chat unless the user asks; the answer pages are in the PDF.
7. To reprint the same puzzles, call again with the same `seed` and settings.

It does not make colour nonograms, read a photo or image file, or solve a puzzle from a photo.
