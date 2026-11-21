---
name: game2048
description: Use when the user wants to play 2048, open the 2048 board, get a hint on a 2048 position, or ask ChatGPT to take a 2048 move.
---

# 2048

Use 2048 when the user asks to play the sliding-tile game, open the board, continue a game, undo a slide, get advice on the current position, or hand a move to ChatGPT. Call `game2048_home` once to open the fullscreen board. It resumes the active board or starts one if needed, and it is the only tool that renders UI; every other result is data for the same board. After it opens, wait for the player and do not call `game2048_move` on your own.

The player owns the board. They slide with the arrow keys, W A S D, or a swipe, and each slide calls `game2048_move` with one direction. Do not move after the player's own move, do not recap every tile, and never claim the computer replied. The player may ask for a hint at any time.

## Reading the board

`game2048_get_state` returns `board` as four rows of four integers from the top row to the bottom row; `0` is empty. `legalMoves` lists the directions that would change the board, `score` is the current score, `maxTile` is the highest tile, and `moveLog` records each completed direction. Use the same `gameId` returned by `game2048_home`; omitting `gameId` reads the most recent board.

A move slides every tile as far as it can go. Equal tiles that meet merge once and add their new value to the score. After a successful move one new 2 or 4 appears in a free cell. A move that changes nothing is rejected.

## Coaching

When asked for the best move, call `game2048_get_state`, compare the legal directions, then call `game2048_hint` with one legal direction and a one-sentence reason. The board's coach panel shows the hint immediately. Then repeat the direction and reason briefly in chat. Prefer moves that create a merge, keep the largest tile in a corner, and preserve free cells. A hint must never call `game2048_move` or change the board, and never offer a direction the board rejects.

## Taking a move

Call `game2048_move` only when the user asks you to play, take over, or confirms a move you suggested. Apply exactly one move per request unless the user asks for several; describing a move without calling the tool does nothing, so make the call.

## Autoplay

The board can request an autoplay batch such as “play up to 8 moves”. In that one turn, make consecutive `game2048_move` calls—one direction per call—without asking the user between moves, until the batch size is reached, the game ends, or 2048 appears. Then stop and summarize the batch in one line. The board stops autoplay when the user presses Stop, takes over, starts a new game, or the game ends. Then briefly explain the direction and stop; the player can ask for the next move. The human's own keypresses already use this tool, so do not call it in reaction to their move.

If the board reports `status: "won"`, the 2048 tile has been reached. Ask whether to keep going; only call `game2048_keep_playing` after the user says yes. If `status: "over"`, the board has no legal moves and only `game2048_start_game` can continue.

`game2048_undo` removes the latest move, its merges, and the tile it spawned. Use it only when the user explicitly asks. `game2048_start_game` replaces the current board with a fresh one and resets the score; use it only on a restart request.

Keep explanations short and concrete. Trust the returned board over earlier messages, and never invent a score or tile.
