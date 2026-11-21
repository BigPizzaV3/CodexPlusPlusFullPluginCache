---
name: weiqi
description: Play fullscreen 19×19 Weiqi (Go) against the current ChatGPT model, with server-enforced captures, suicide, ko, passes, area scoring, undo and resignation.
---

# iPlugin Weiqi

Use this skill when the user wants to open, start, continue, or finish a game of Weiqi (Go). The plugin is a 19×19 MCP App. You and the human play opposite colours; Black always moves first.

## Opening the board

Call `weiqi_home` **once per conversation** to open the fullscreen board. It is the only UI-rendering tool and takes no arguments. After the board is open, use `weiqi_start_game` in the existing view. Never call `weiqi_home` again for a new game.

## Starting a game

Call `weiqi_start_game` with:

- `firstPlayer`: `"human"` or `"ai"`. The first player takes Black; the other side takes White.
- `difficulty`: `"easy"`, `"normal"`, or `"hard"`. This is guidance for your own move selection.

The response includes the authoritative `game`, `legalMoves`, and `nextAction`.

## Coordinates

Columns are **A–T without I** (`A B C D E F G H J K L M N O P Q R S T`). Rows are **1–19 from the bottom**. Examples: `D4` is lower-left, `Q16` is upper-right. Use uppercase coordinates.

## A turn

1. When `nextAction` is `"human_move"`, ask the human for their point unless their move is already clear.
2. Call `weiqi_play_move` with `gameId` and `coordinate`. The server rejects occupied points, suicide, and ko.
3. When the result says `"ai_move"`, choose exactly one point from `legalMoves` (or `"pass"`) and call `weiqi_ai_move`.
4. Continue until the human resigns or both sides pass.

Do not call `weiqi_ai_move` for the human, and do not call `weiqi_play_move` for the model. Always follow the returned `nextAction`.

## Rules enforced by the server

- A stone is captured when its connected group has no liberties after a move.
- Suicide is illegal.
- Positional superko is enforced: a move may not recreate an earlier board position with the same side to move.
- `coordinate: "pass"` passes. Two consecutive passes end the game.
- Scoring is **Chinese area scoring**: stones on the board plus empty regions bordered by only one colour, with **6.5 komi** for White. Dead stones are not removed automatically, so capture dead stones before both sides pass.
- The result shows Black and White totals, territory, komi, and the winner.

## Undo and resignation

- `weiqi_undo` removes the latest complete turn: the model reply plus the human move, a pending human move, or the model’s opening. Removed stones cannot be restored.
- `weiqi_resign` ends the game for the other colour. Call it **only after the human explicitly confirms resignation**. One unconfirmed request must not end the game.

## Model move policy

The plugin has **no Go engine, opening book, or hidden move selector**. You choose every computer move from the authoritative board and `legalMoves`. Use the difficulty guidance:

- easy: take simple captures and obvious points without long reading.
- normal: look for captures, keep groups connected, and claim useful territory.
- hard: read atari and captures, protect weak groups, and contest the largest open areas.

Prefer legal points with a clear purpose. Do not search files, open another game, or reply with text only when `nextAction` is `"ai_move"`.

## Errors

Invalid coordinates, occupied points, suicide, ko, out-of-turn calls, and ended games return JSON-RPC errors. Read the message, correct the call, and do not retry the same illegal move. If the board is no longer open, ask the user to reopen it rather than calling `weiqi_home` repeatedly.
