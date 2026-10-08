---
name: export-chess-game
description: Export the current Chess app game as copy-ready PGN movetext with conservative metadata. Use when the user asks to export, copy, save, share, or convert the current game to PGN. Build from the model-visible SAN history and result, preserve unfinished games with an asterisk, and never treat the current final FEN as a starting-position FEN.
---

# Export Chess Game

## Inputs

Use the current widget's model-visible `moves`, `phase`, and `outcome`. Use each move's stored SAN exactly. Accept optional header values such as event, site, date, round, or White's name from the user.

If no widget state is available, ask for the move list. An empty but valid game exports as `*`.

## Workflow

1. Set the result token to `outcome.result` only when the game is finished and an outcome exists. Otherwise use `*`.
2. Build PGN movetext by pairing SAN entries in order:
   - Prefix White's move with `1.`, `2.`, and so on.
   - Place Black's following move after White's move.
   - Preserve the stored SAN notation for captures, checks, mates, castling, and promotions.
3. Append the result token exactly once at the end of the movetext.
4. Include only known or user-supplied tag values. It is safe to identify Black as `Stockfish 18`; use `?` for an unknown White name rather than inventing one.
5. When the user requests the strict PGN Seven Tag Roster, include unknown values as `?` and an unknown date as `????.??.??`.
6. Return the PGN in a fenced `pgn` code block. Keep commentary outside the block minimal.

## Boundaries

- Do not invent dates, player names, ratings, event names, move comments, or variations.
- Do not add `SetUp` or `FEN` tags. Games start from the standard position, while the widget's `fen` is the current or final position.
- Do not recalculate or normalize SAN when the authoritative move history already supplies it.
- Do not call `start-game` or write the export to an external service.
