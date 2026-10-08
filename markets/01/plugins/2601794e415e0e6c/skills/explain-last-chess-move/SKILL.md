---
name: explain-last-chess-move
description: Explain the purpose and consequences of the latest move in the current Chess app game. Use when the user asks why Stockfish or White played that move, what changed, what the move threatens, or how to respond. Ground the answer in the latest model-visible SAN and coordinate move plus the current position, without claiming access to Stockfish's reasoning.
---

# Explain Last Chess Move

## Inputs

Use the current widget's model-visible `moves`, `fen`, `turn`, `inCheck`, and `phase`. Treat the final entry in `moves` as the latest move and use both its SAN and coordinate fields.

If the history is empty, explain that no move has been played yet. If the state is missing, ask for the move or current position.

## Workflow

1. Name the latest move and identify which side played it. If the user's wording names the wrong side, clarify gently.
2. Explain its immediate board effects:
   - movement, capture, check, promotion, or castling
   - newly attacked, defended, opened, or blocked lines
   - material or king-safety changes visible from the position
3. Describe one or two likely tactical or strategic purposes. Use language such as “likely,” “appears to,” or “one point is” when explaining Stockfish's move.
4. Identify the most important threat or consequence for the side to move.
5. When it is White's turn, offer a practical response idea. Give a concrete move only when confident it is legal; otherwise describe the plan or candidate set.

## Output

Use four short parts:

- **Move**
- **What changed**
- **Likely idea**
- **What to watch now**

Adapt the depth to the user's level and question.

## Boundaries

- Do not claim access to Stockfish evaluation scores, search lines, or internal intent.
- Do not call a move best, forced, winning, or a blunder without evidence available in the position.
- Do not invent prior moves or hidden analysis.
- Do not control the board or call `start-game`.
