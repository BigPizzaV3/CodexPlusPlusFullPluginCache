---
name: chess-hint-ladder
description: Give progressive, Socratic hints for the current Chess app position without revealing the move too early. Use when the user asks for a chess hint, clue, nudge, or guided help and wants to think through the live position themselves. Do not use for direct best-move requests or completed-game reviews.
---

# Chess Hint Ladder

## Inputs

Use only the current game widget's model-visible `modelContent`:

- `fen` and `moves` for the position and its context
- `phase`, `turn`, and `inCheck` for timing and urgency

Use the conversation to track which hint level the user has already received.

## Workflow

1. Confirm that the state describes an active game and that it is White's turn.
   - If Black is thinking, ask the user to wait for Black's move.
   - If the engine is loading or unavailable, explain that a live move hint is premature.
   - If the game is finished or restarting, offer to discuss the position or review the game instead.
   - If the state is missing, ask for the current FEN or move sequence.
2. Check immediate forcing concerns first: whether White is in check, direct threats, loose pieces, checks, captures, and tactical motifs.
3. Start at the first unrevealed level unless the user requests a stronger hint:
   1. State the position's main problem or objective without naming a move.
   2. Identify the relevant board area, piece, or tactical motif without giving the full move.
   3. Narrow the search to one or two candidate ideas.
   4. Reveal a concrete candidate move and explain its purpose.
4. Give only one new level per response. Pause so the user can calculate before offering the next level.

## Output

Label the response `Hint 1`, `Hint 2`, `Hint 3`, or `Reveal`. Keep it brief, explain what the user should inspect, and end by inviting the next hint level when appropriate.

## Boundaries

- Do not claim access to Stockfish analysis, evaluation scores, principal variations, or its internal reasoning.
- Present a revealed move as a reasoned candidate, not a guaranteed best move.
- Do not make a move, control the widget, or call `start-game`.
- Do not reveal later hint levels unless the user requests them.
