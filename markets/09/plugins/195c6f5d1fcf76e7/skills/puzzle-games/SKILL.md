---
name: puzzle-games
description: Ten puzzle games on one board - Riddle Challenge, Word Link, Theme Connect, Memory Match, Tic Tac Toe, Join 4, Sudoku, Marble Solitaire, Math Dash and Math Chain - with stars and ranks.
---

`puzzle_lobby` shows the board with the ten games, the player's stars and rank. `puzzle_start`
starts a game: Tic Tac Toe, Join 4, Math Dash and Sudoku take a difficulty; Theme Connect takes
animals, food or celebrities; Memory Match takes food, colours or animals; Riddle, Word Link and
Sudoku take a puzzle number.

Riddle Challenge, Word Link, Theme Connect and Memory Match take typed answers through
`puzzle_answer`, which also has hint, skip, reveal and give_up. Tic Tac Toe and Join 4 take moves
through `puzzle_move`: squares 1 to 9 from the top left, or columns 1 to 7 from the left. Sudoku,
Marble Solitaire, Math Dash and Math Chain are played by tapping the board. The board can be
ahead of the latest result after taps; `puzzle_status` reports its current state without
showing a new board.

Results describe the board in plain text. Riddle, clue and link answers appear once they are
solved, skipped or revealed, and the Memory Match list appears when the game ends, so the games
play fairly in the chat.

Players earn stars for wins, solved riddles and links, sudokus and high scores, and climb twenty
ranks.
