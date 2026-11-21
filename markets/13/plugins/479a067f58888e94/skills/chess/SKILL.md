---
name: chess
description: Use when the user wants to play chess, open a fullscreen board, make a move, inspect the position, promote a pawn, undo, or resign.
---

# iPlugin Chess

Use this skill when the user asks to play chess, start or resume a board, make a move, inspect the position, undo, resign, or open the fullscreen board. Call `chess_home` once to open the board. It is the only tool that renders UI; keep every game action and computer reply inside that same board.

The board is a standard 8×8 chess board. Squares use algebraic notation: `a1` is the bottom-left square from White's view, `h8` is the top-right. Files are `a`–`h`; ranks are `1`–`8`. The human and the computer play opposite colours. White always moves first, so `firstPlayer: "ai"` means the computer plays White and moves first; `firstPlayer: "human"` means the human plays White.

The model is the computer player. It does not call a chess engine, opening book, or hidden move selector. Choose one move from the `legalMoves` returned in the latest game state and apply it with `chess_ai_move`. After a human move, call `chess_ai_move` immediately with a legal reply; do not answer with text only. Before resigning, ask the human to confirm.

## Tools

- `chess_home` — open the fullscreen board. Accepts no arguments.
- `chess_start_game` — start a new standard game with `firstPlayer` (`human` or `ai`) and `difficulty` (`easy`, `normal`, or `hard`).
- `chess_get_state` — read the authoritative board, FEN, legal moves, move history, check status, material, and captures for a `gameId`.
- `chess_play_move` — apply one legal human move using `from`, `to`, and optionally `promotion` (`q`, `r`, `b`, or `n`).
- `chess_ai_move` — apply the computer's chosen legal move using the same arguments.
- `chess_undo` — remove the latest complete turn (the computer reply and the human move, or a pending human move).
- `chess_resign` — end the active game after the human confirms resignation.

## Rules handled by the server

The server validates every move, including castling rights and transit squares, en passant, pawn promotion, check, checkmate, stalemate, insufficient material, the fifty-move rule, and threefold repetition. A move that is illegal, out of turn, or targets an occupied square is rejected without changing the position. The server stores games in memory.

## Difficulty

- `easy`: prefer natural developing moves and simple captures; avoid deep calculation.
- `normal`: check captures, checks, and immediate threats before choosing a principled move.
- `hard`: calculate immediate tactics and king safety first, then choose the most testing move available.

Honour the difficulty stored in the game state. If the state says `check`, the side to move must answer the check; only legal moves are available. If the state is `finished` or `draw`, do not attempt more moves; explain the result briefly and offer a new game.
