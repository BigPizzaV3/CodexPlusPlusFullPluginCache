---
name: adaptive-chess-rematch
description: Recommend an appropriate Stockfish difficulty for a rematch and start a fresh Chess app game after the user authorizes it. Use when the user wants to play again, make the next game easier or harder, or adjust the level based on how the previous game felt. Use only the registered start-game tool and integer levels from 0 through 20.
---

# Adaptive Chess Rematch

## Inputs

Use the current widget's model-visible `difficulty`, `moves`, `phase`, and `outcome` when available. Give the user's explicit assessment of the previous game's difficulty more weight than the result alone.

## Choose the Level

1. Honor an explicit requested level from 0 through 20.
2. For a relative request, start from the current difficulty and use a conservative adjustment:
   - Move by 1 level for a slightly easier or harder game.
   - Move by 2 levels when the user says the game was clearly overwhelming or far too easy.
   - Keep the same level when the game felt competitive.
3. Clamp the recommendation to the inclusive 0–20 range.
4. Do not infer a large adjustment from one win, loss, draw, or resignation. If the user has not described how the game felt, ask one concise calibration question or recommend staying close to the current level.

## Start the Rematch

1. State the proposed level and one short reason.
2. Treat a direct request such as “make it harder and play again” as authorization. Otherwise, ask for confirmation before starting.
3. Call `start-game` with:
   - `difficulty`: the chosen integer from 0 through 20
   - `reason`: an optional concise explanation of the user's rematch request
4. After the call, briefly confirm the level. Let the returned widget provide the fresh game.

## Boundaries

- Use the tool name `start-game` exactly. Do not invent tool arguments.
- Expect the tool's structured content to contain only `difficulty`.
- Do not claim to modify, resume, or unfreeze the previous widget; every call creates a new game.
- Remember that the user is always White and moves first.
- Do not promise that a level maps to a formal player rating.
