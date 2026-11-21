---
name: maze-maker
description: Make printable mazes (rectangle, circle or hexagon) as a PDF with an answer key, using generate_mazes. Every maze has exactly one path from Start to Finish.
---

# Zovo Maze Maker

Call `generate_mazes` when someone wants printable mazes, mazes for their child or class, a maze worksheet, a circle maze or a hexagon maze.

1. For a set of the same kind, pass `count` with `shape` and `difficulty`, or pass the child's `age` and let it pick the difficulty (4 and under very easy, 5 to 7 easy, 8 to 10 medium, 11 and up hard).
2. When the mazes differ, pass one object per maze in `mazes` (`shape`, `difficulty`, `size`, `age`, `seed`).
3. `size` overrides difficulty: "columns x rows" for rectangle and hexagon, rings for circle.
4. Layout options are `per_page` (1, 2 or 4), `paper` (letter or a4), `title`, `name_line` and `answer_key`.
5. Share the PDF link. Do not describe the solution path in chat unless the user asks; the answer pages are in the PDF.
6. To reprint the same mazes, call again with the same `seed` and settings.

It does not make picture-shaped mazes, mazes with several solutions, or solve a maze from a photo.
