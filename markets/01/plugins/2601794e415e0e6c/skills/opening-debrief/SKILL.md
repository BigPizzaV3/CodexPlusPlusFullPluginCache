---
name: opening-debrief
description: Identify the likely opening family from the current Chess app move history and explain its practical plans. Use when the user asks what opening was played, how the opening developed, where play left familiar theory, or what plans to remember next time. Treat names and ECO codes as heuristic because the app exposes no opening database.
---

# Opening Debrief

## Inputs

Use the early portion of the current widget's model-visible SAN and coordinate `moves`, plus the current `fen` when it helps explain the resulting pawn structure. Use the user's experience level to choose vocabulary and depth.

If no moves have been played, explain that there is no opening sequence to classify. If only a few half-moves are available, identify broad opening principles or a family rather than forcing a precise name.

## Workflow

1. Quote the relevant opening sequence in SAN.
2. Identify the most likely opening family or named variation.
   - State confidence when the move order is short, unusual, or compatible with transpositions.
   - Mention at most one plausible alternative name when ambiguity materially helps.
3. Explain the defining pawn structure, development pattern, and king-safety choices.
4. Give the typical practical plans for White and Black in the resulting structure.
5. Identify the first instructive decision for White. Call it a departure from theory only when sufficiently confident; otherwise describe it as a practical choice.
6. Finish with two or three priorities the user can remember in a future game.

## Output

Use this structure:

- **Opening sequence**
- **Likely opening**
- **Position character**
- **Plans for both sides**
- **Remember next game**

## Boundaries

- Do not imply access to an opening database, live theory, or Stockfish analysis.
- Omit an ECO code unless the user requests one and the classification is highly confident; label any supplied code as tentative.
- Do not invent missing moves or claim that a move is the first theoretical error without reliable evidence.
- Do not call `start-game` or alter the current game.
