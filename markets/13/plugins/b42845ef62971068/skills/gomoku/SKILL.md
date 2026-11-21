---
name: gomoku
description: Use when the user wants to play five-in-a-row, start or resume a board, make a move, inspect the current game, or open the fullscreen Gomoku app.
---

# Gomoku

Use Gomoku when the user asks to play five-in-a-row, start a board, make a move, inspect the current game, undo, resign, or open the board. Call `gomoku_home` to open the fullscreen board. It is the only tool that renders UI; keep all game actions and computer moves inside that same board. The UI follows the ChatGPT host language across its 55 supported locales, so continue in the user's conversation language. Respect the user's selected first player and difficulty. After a human move, or after starting with the computer first, call `gomoku_ai_move` yourself with the coordinate you choose from the returned board state. The model is the AI player: choose legal moves from the state and explain the move briefly. Never refer to training, learning, opening books, or a hidden engine.

The board is 15×15. Coordinates use `A1` through `O15`, where A is the leftmost column and 1 is the top row. Human is black and the computer is white. The game ends when a player makes five contiguous stones, the board is full, or the human resigns.

## Difficulty

- `easy`: prefer simple local moves and avoid deliberate long-range fork planning.
- `normal`: use balanced tactical and positional play, including immediate wins and blocks.
- `hard`: inspect immediate wins and losses first, then choose moves that create multiple threats and control the center.

Use the difficulty stored in the game state and honor it consistently. `gomoku_undo` removes the latest complete turn. `gomoku_resign` ends the game with the human resigning.
