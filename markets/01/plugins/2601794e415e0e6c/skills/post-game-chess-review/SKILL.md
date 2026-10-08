---
name: post-game-chess-review
description: Review a Chess app game and turn its move history into focused, practical lessons. Use when the user asks for a post-game review, recap, mistake analysis, turning points, or advice after finishing or abandoning a game. Ground the review in model-visible game state and do not present model judgments as Stockfish analysis.
---

# Post-Game Chess Review

## Inputs

Read the current widget's model-visible `difficulty`, `fen`, `moves`, `phase`, `turn`, `inCheck`, and `outcome`. Use any user-supplied goal, such as opening play, tactics, or time-independent decision making, to focus the review.

If no usable move history is available, ask the user to provide the game or reopen its widget. If the game is still active, clearly label the response as a review so far.

## Workflow

1. Establish the game context: difficulty, completion status, result, ending reason, and move count.
2. Reconstruct the game's story from the SAN and coordinate move history. Divide it into opening, middlegame, and endgame only when the moves support those phases.
3. Select two to four instructive decision points. Anchor each point to an exact move number and SAN move.
4. For each decision point:
   - Describe what changed.
   - Explain the practical danger or opportunity.
   - Offer a better plan or a concrete alternative only when confident it is legal.
   - Tie the moment to a reusable chess concept.
5. Identify at least one thing the user handled well. Avoid making the report a list of faults.
6. Finish with two or three prioritized lessons and one specific practice suggestion.

## Output

Use this compact structure:

1. **Game at a glance** — result, difficulty, and one-sentence story.
2. **Key moments** — move-anchored explanations.
3. **What worked** — one or more strengths.
4. **Next-game priorities** — two or three actionable lessons.
5. **Practice** — one focused exercise or theme.

## Boundaries

- Do not invent moves, positions, clock information, player ratings, or causes not present in the state.
- Do not use numeric evaluations, engine labels such as forced best move, or claims that Stockfish judged a move a blunder.
- Prefer positional plans over a concrete variation when legality is uncertain.
- Do not call `start-game`; keep this skill focused on reviewing the available game.
