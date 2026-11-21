---
name: math-cages
description: Make printable math cage puzzles (4x4 to 9x9 grids with cages, a target and a sign) as a PDF with an answer key, using generate_math_cages. Each puzzle is checked by a solver to have one solution.
---

# Zovo Math Cages

Call `generate_math_cages` when someone wants printable math cage puzzles, arithmetic cage puzzles, math logic puzzles for a class, or a cage puzzle worksheet with answers.

1. For a set of the same kind, pass `count` with `size` (4 to 9), `operations` and `difficulty` (easy, medium, hard).
2. When the puzzles differ, pass one object per puzzle in `puzzles` (`size`, `operations`, `difficulty`, `seed`).
3. Pass the operations the user names as signs or words: "+ -", "add only", "multiplication and division", "all four", "no division". Default is all four.
4. Layout options are `per_page` (1, 2 or 4), `paper` (letter or a4), `title`, `name_line` and `answer_key`.
5. Share the PDF link. Do not write the answers in chat unless the user asks; they are on the answer pages.
6. To reprint the same puzzles, call again with the same `seed` and settings.

Subtraction and division cages have 2 cells, so puzzles with only those signs have many single-number cells; say so if the user asks for them. It does not solve a puzzle from a photo and does not make classic sudoku or grids larger than 9 x 9.
