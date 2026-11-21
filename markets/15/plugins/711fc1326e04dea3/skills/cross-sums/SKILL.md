---
name: cross-sums
description: Make printable cross-sum puzzles (6x6 to 12x12 grids where each run of white squares adds up to its clue with no repeated digit) as a PDF with an answer key, using generate_cross_sums. Each puzzle is checked by a solver to have one solution, and the card lets the user solve it on screen.
---

# Zovo Cross Sum Puzzles

Call `generate_cross_sums` when someone wants printable cross sum puzzles, number crossword puzzles with sums, addition logic puzzles, or a cross sum worksheet with answers.

1. For a set of the same kind, pass `count` with `size` (6 to 12, counting the clue row and column) and `difficulty` (easy, medium, hard).
2. When the puzzles differ, pass one object per puzzle in `puzzles` (`size`, `difficulty`, `seed`).
3. Layout options are `per_page` (1, 2 or 4), `paper` (letter or a4), `title`, `name_line` and `answer_key`.
4. Share the PDF link. Tell the user they can also fill in digits and press Check in the card.
5. Do not write the answers in chat unless the user asks; they are on the answer pages.
6. To reprint the same puzzles, call again with the same `seed` and settings.

If the reply notes that a hard puzzle was made at medium for a seed, pass that on and offer another seed. It does not solve a puzzle from a photo and does not make grids larger than 12 x 12.
