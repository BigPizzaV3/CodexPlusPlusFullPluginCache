---
name: puzzle-maker
description: Make crosswords from answers and clues, word searches from word lists, and sudoku with exactly one solution using GridSmith Puzzle Maker; each puzzle is playable in the chat and comes with a printable PDF and answer key.
---

# GridSmith Puzzle Maker

Pick the tool from the request and call it right away when the request already has what it needs:

- `generate_crossword`: crossword maker. Needs 4-40 `entries`, each `{answer, clue}`. If the user gives only vocabulary words, write one short, age-appropriate clue per word first, then call the tool. Do not draw the grid yourself.
- `generate_word_search`: 5-40 `words`. `difficulty` easy (right and down, good for young kids), medium (adds diagonals, default), hard (all directions, backwards). Leave `size` out unless the user asks for one (8-25).
- `generate_sudoku`: `difficulty` easy, medium or hard. Needs no other input. Every puzzle has exactly one solution; hard always needs a technique beyond singles.

After the tool returns:

1. Give a one-line summary (grid size, words placed, difficulty) and the PDF link. The widget is playable, so do not repeat the grid as text.
2. If answers or words are listed as not placed, say which and why, and offer a new layout (pass a different `seed`) or replacement words.
3. Keep the answer key hidden unless the user asks for it.
4. For "make another one" with the same words, call again with a different `seed`.

Do not use these tools to solve an existing puzzle, answer a single crossword clue, explain solving strategies, or play other games.
