---
name: junqi
description: Use when the user wants to play Junqi / Luzhanqi (军棋, 陆战棋), open the fullscreen 12 × 5 field, make a move, use a railway, inspect a game, undo, or ask the model to play blue.
---

# iPlugin Junqi

Use this skill when the user asks to play Junqi, Luzhanqi, 军棋, 陆战棋, or a two-player military chess game with 25 pieces per side. Call `junqi_home` **once** to open the fullscreen field. It is the only tool that renders UI; keep every game action and model reply inside that same field. Never call `junqi_home` again after the field is open, not even to start a new game: call `junqi_start_game` in the existing view. Extra home calls create extra app tabs.

This is **face-up Junqi (明棋)**. Both armies are visible. There is no secret deployment, no hidden piece, and no referee. The human always plays the 25 **red** pieces at the bottom; the model always plays the 25 **blue** pieces at the top. `firstPlayer` only decides who moves first; it does not change sides.

## Board and coordinates

The field has 12 rows and 5 columns. Rows are `A`–`L` from the top to the bottom; columns are `1`–`5` from left to right. Examples: `A2`, `F3`, `L4`. Blue starts in rows A–F, red in rows G–L.

- **Camps (行营)** are C2, C4, D3, E2, E4, H2, H4, I3, J2 and J4. A piece in a camp cannot be attacked. A camp can hold only one piece, so you cannot enter an occupied camp.
- **Headquarters (大本营)** are A2, A4 for blue and L2, L4 for red. The flag must start in one of its side's headquarters. A piece that enters a headquarters can never move again. Pieces cannot pass through a headquarters.
- **Railways (铁路)** run along rows B, F, G and K and along columns 1 and 5. The front crossings at F1–G1, F3–G3 and F5–G5 are connected; F2–G2 and F4–G4 are blocked by the mountain (山界).
- **Roads (公路)** connect adjacent squares and the diagonals through camps.

## Pieces and rank

Each side has exactly 25 pieces:

| Piece | Count | Rank / special |
| --- | --- | --- |
| 司令 Field Marshal | 1 | 9 |
| 军长 General | 1 | 8 |
| 师长 Major General | 2 | 7 |
| 旅长 Brigadier General | 2 | 6 |
| 团长 Colonel | 2 | 5 |
| 营长 Major | 2 | 4 |
| 连长 Captain | 3 | 3 |
| 排长 Lieutenant | 3 | 2 |
| 工兵 Engineer | 3 | 1 |
| 地雷 Landmine | 3 | immobile; only an engineer defuses it |
| 炸弹 Bomb | 2 | trades with any enemy piece |
| 军旗 Flag | 1 | immobile; its capture loses the game |

A higher rank destroys a lower rank. Equal ranks destroy each other. A bomb and its target both die. An engineer attacking a landmine destroys the mine and survives; every other piece attacking a landmine dies with it. Capturing the flag wins immediately, even with a bomb (the bomb also dies).

Deployment is always legal: every non-camp square in a half is occupied, the flag is in one headquarters, a mine guards the other, the other two mines are in the back two rows, bombs are not on the front row, and three engineers start on railway squares. `junqi_start_game` creates a fresh random legal deployment unless a `seed` is supplied.

## How a move works

On a turn, move exactly one piece:

- **Road:** one step to an adjacent empty square, or one step onto an enemy square to attack. Diagonal steps are allowed only along the diagonals through camps.
- **Railway:** a piece standing on a railway may travel any distance in a straight line along the railway, stopping at the first occupied square. It may capture an enemy there; it may not jump over any piece.
- **Engineer railway:** an engineer may travel any distance along connected railways and **turn corners**, still stopping at the first occupied square. It may capture an enemy there.
- Landmines and flags never move. A piece in a headquarters never moves. A piece in a camp may move out and attack normally.
- A piece may not move onto its own piece, onto an occupied camp, or through a piece.

Win by capturing the enemy flag, or by leaving the opponent with no legal move. If the move limit is reached, the game is a draw.

## Tools

- `junqi_home` — open the fullscreen field. No arguments. Call once only.
- `junqi_start_game` — start a new game with `firstPlayer` (`human` or `ai`), `difficulty` (`easy`, `normal`, `hard`), and an optional `seed`.
- `junqi_get_state` — read the authoritative board, both armies, legal moves, history, battle results and next turn for a `gameId`.
- `junqi_play_move` — apply one legal red move using `gameId`, `from`, and `to`.
- `junqi_ai_move` — apply the model's chosen blue move using `gameId`, `from`, and `to`. The server rejects any move that is not in the current `legalMoves`.
- `junqi_undo` — permanently remove the latest complete turn (blue reply plus red move, a pending red move, or the blue opening). Fallen pieces are restored. Removed moves cannot be restored.
- `junqi_resign` — end the active game after the human explicitly confirms resignation.

## Playing as blue

The model is the blue player. There is no engine, opening book, learning system, hidden information, or hidden move selector. After every red move, or after starting with `firstPlayer: "ai"`, inspect the returned `legalMoves` and immediately call `junqi_ai_move` with one of them. Do not reply with text only and do not leave the blue turn waiting. The field's follow-up prompt may include a compact board and the legal move list; use the latest tool state as authoritative.

Prefer moves that:
- capture the enemy flag when the route is open;
- win exchanges or trade a low piece for a high piece;
- use railways and engineer corner turns to reach the enemy back rows;
- keep your own flag headquarters covered and your engineers available for mines;
- avoid feeding the field marshal to a bomb or a mine.

Honour the selected difficulty:
- `easy`: favour simple road moves and avoid deep combinations.
- `normal`: balance development, exchanges, and railway pressure.
- `hard`: calculate exchanges, hunt the flag, and use engineers to clear mines and turn corners.

The state reports `armies.human` and `armies.ai` with `alive`, `movable`, `flagAlive`, `flagAt`, `fieldMarshalAlive` and per-type counts. If the state is `finished` or `draw`, do not attempt another move; explain the result briefly and offer a new game. Before resignation, ask the user to confirm.
