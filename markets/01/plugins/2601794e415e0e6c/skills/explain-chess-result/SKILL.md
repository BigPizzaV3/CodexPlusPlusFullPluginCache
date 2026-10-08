---
name: explain-chess-result
description: Explain why the current Chess app game ended and turn the result into one practical lesson. Use when the user asks why the game was checkmate, stalemate, a draw, a resignation loss, or otherwise finished. Use the model-visible outcome reason and final position as authority; do not infer an ending when no outcome is present.
---

# Explain Chess Result

## Inputs

Read the current widget's model-visible `outcome`, `fen`, `moves`, `turn`, `inCheck`, and `phase`.

If `outcome` is null, state that the widget has not recorded a final result. Explain the difference between the current status and a completed game if helpful, but do not invent an ending.

## Workflow

1. State the result, winner when present, and recorded reason.
2. Explain the relevant rule in plain language:
   - **Checkmate:** the side to move is in check and has no legal escape.
   - **Stalemate:** the side to move is not in check but has no legal move.
   - **Threefold repetition:** the same position, including the same side to move, occurred three times.
   - **Fifty-move rule:** fifty moves by each side passed without a pawn move or capture.
   - **Insufficient material:** the remaining material cannot produce checkmate.
   - **Resignation:** White ended the game voluntarily, so Black received the win.
3. Connect the rule to the final position or the last relevant moves without fabricating unavailable details.
4. Give one recognition tip or practical lesson for future games.

## Output

Use this compact structure:

- **Result**
- **Why it ended**
- **How it appears here**
- **Takeaway**

## Boundaries

- Treat `outcome.reason` as authoritative.
- Do not substitute another draw rule or claim an unrecorded adjudication.
- Do not present a Stockfish evaluation or principal variation.
- Do not call `start-game`; explain the recorded game only.
