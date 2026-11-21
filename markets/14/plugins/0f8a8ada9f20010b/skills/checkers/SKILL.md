---
name: checkers
description: Use when the user wants to play Chinese checkers (Sternhalma), open the fullscreen star board, make a move, jump, inspect a game, undo, or resign.
---

# iPlugin Checkers

Use this skill when the user asks to play Chinese checkers, 跳棋, marbles, the star board, or wants a 1v1 board game of stepping and jumping. Call `checkers_home` **once** to open the fullscreen board. It is the only tool that renders UI; keep every game action and model reply inside that same board. Never call `checkers_home` again after the board is open, not even to start a new game: call `checkers_start_game` in the existing view. Extra home calls create extra app tabs.

The game is a 1v1 Chinese checkers race on a 121-hole star board. The human always plays the ten **porcelain** pegs from the bottom camp. The model always plays the ten **cinnabar** pegs from the top camp. `firstPlayer` only decides who takes the first turn; it does not change camps.

## Goal and turn rules

- The goal is to move all ten of your pegs into the ten holes of the **opposite camp**. The porcelain side wins by filling the top camp; cinnabar wins by filling the bottom camp.
- A turn is exactly one of:
  - one **step** to an adjacent empty hole, or
  - one or more **jumps**: leap over one adjacent peg (either colour) into the empty hole immediately beyond, then optionally continue jumping from the landing hole in any direction.
- A jump chain is applied as one move. The server chooses and validates the complete path from the `from` and `to` holes.
- Pegs are never captured. A jumping peg merely passes over another peg.
- A peg may not land on an occupied hole, and may not combine a step with a jump in the same turn.

## Coordinates

Rows are lettered `A` through `Q` from the top point to the bottom point. Within each row, holes are numbered left to right. Because the star rows have different widths, valid numbers depend on the row (`E1`–`E13` on the wide row E, for example). Always prefer coordinates from the latest `legalMoves` list instead of guessing a coordinate.

## Tools

- `checkers_home` — open the fullscreen board. Accepts no arguments.
- `checkers_start_game` — start a 1v1 game with `firstPlayer` (`human` or `ai`) and `difficulty` (`easy`, `normal`, or `hard`).
- `checkers_get_state` — read the authoritative board, pieces, legal moves, progress, history, and next turn for a `gameId`.
- `checkers_play_move` — apply one legal human move using `gameId`, `from`, and `to`.
- `checkers_ai_move` — apply the model's chosen cinnabar move using `gameId`, `from`, and `to`. The server rejects any coordinate that is not in the current legal move list.
- `checkers_undo` — permanently remove the latest complete turn (the cinnabar reply plus the human move, a pending human move, or a cinnabar opening). Removed moves cannot be restored.
- `checkers_resign` — end the active game after the human explicitly confirms resignation.

## Playing as the model

The model is the cinnabar player. There is no engine, opening book, learning system, or hidden move selector. After every human move, or after starting with `firstPlayer: "ai"`, inspect the returned `legalMoves` and immediately call `checkers_ai_move` with one of them. Do not reply with text only and do not leave the cinnabar turn waiting.

Prefer moves that:
- advance pegs out of the crowded home camp,
- use jumps and multi-jump chains to cover distance,
- open lanes for the pegs still at home,
- block the human's shortest route when the position calls for it.

Honour the selected difficulty:
- `easy`: favour short, simple moves and avoid long forcing jump chains.
- `normal`: balance jump distance, lane development, and home-camp clearance.
- `hard`: look for the longest useful jump chains, efficient camp evacuation, and blocking moves.

The state reports `progress.human` and `progress.ai` as the number of pegs already in the far camp (0–10). The game ends at 10. If the state is `finished` or `draw`, do not attempt another move; explain the result briefly and offer a new game. Before resignation, ask the user to confirm.
