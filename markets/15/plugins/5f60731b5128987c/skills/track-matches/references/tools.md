# Matchbook tool reference

## `list_venues`

Read-only. Returns unique `{ venueName, city, country }` rows from the current user's tournaments, sorted by venue name, city, then country. Dates are tournament dates, not import dates. Includes tournaments without matches; events without a venue name are excluded.

- `{}` (or omitted arguments): current calendar year in UTC, evaluated at request time.
- `{ "years": [2025] }`: one year.
- `{ "years": [2024, 2026] }`: selected years, not the intervening years.
- `{ "allTime": true }`: all history.

`years` must be a nonempty array of integer years from 1 to 9999. Do not combine it with `allTime: true`. Duplicate years are harmless. `allTime: false` keeps the default year unless `years` is supplied.

Venue name, city and country together identify a location; Unicode, case and whitespace variants are merged. The first recorded spelling in the selected period is used. Same-name venues in different cities or countries stay separate. Missing city/country are returned as empty strings. No matching tournaments returns `[]`.

## `import_tournament`

Creates a tournament, its deck if needed, and its match rows atomically.

Required: `name`, `date` (`YYYY-MM-DD`), `format`, `eventType`, `deckName`. `venueName` is required unless `cardMedium` is `digital`. `matches` is optional and defaults to `[]`.

Optional `cardMedium` is `digital`, `non_digital`, or null (unknown). It describes the cards, not whether the event was remote. Do not infer it from the game or venue.

Optional: `game` (`magic`, `riftbound`, `one_piece`, `lorcana`, or `null` when unknown), `city`, `country`, `deckNotes`, `notes`, `status` (`active` or `completed`, default `completed`). Game and format are separate. Deck identity includes the card game; changing an event's game can change its deck ID.

Optional tournament fields `wins`, `losses`, `draws` store the complete W/L/D record when match details are missing or incomplete. Supply all three nonnegative integers, e.g. `{"wins":3,"losses":1,"draws":0}`. These totals replace match-derived W/L/D, including when some matches are recorded, and do not add to them. `update_tournament` can edit these totals; setting all three to `null` restores match-derived totals. Omitted update fields retain their stored values.

## `add_match`

Adds one round to `eventId`, or to the current active tournament when `eventId` is omitted.

Optional `playoffRound`: `round_of_16` (top 16 / 1/8), `quarterfinal` (top 8 / 1/4), `semifinal` (top 4 / 1/2), or `final`. Omit or use `null` for Swiss rounds; `null` in `update_match` clears the stage. Keep `roundNumber` unique and sequential across the whole tournament, including playoffs. Only one match per playoff stage is allowed per tournament. Imports, additions and updates support this field.

Required match fields: `roundNumber`, `result` (`win`, `loss`, `draw`), `resultType` (`played`, `bye`, `concession`, `no_show`, `technical`).

Optional match fields: `opponentName`, `opponentArchetype`, `playerGamesWon`, `opponentGamesWon`, `notes`. Game scores are optional or nullable even for played matches. The stored `result` is authoritative and is never inferred from game scores.

Optional `games` contains individual games; `gamesComplete` is true only when all played games are listed, and defaults to false. Each game has a positive unique `number`, optional nullable `result` (`win`, `loss`, `draw`), `firstPlayer` (`player`, `opponent`), and `playerOpening` / `opponentOpening`. Each opening object may contain nullable nonnegative integers `mulliganCount`, `cardsReplaced`, and `keptHandSize`. Null means unknown and zero is known. They measure different things and should not be inferred from one another. `games` also works within `import_tournament` matches.

`scoreCheck` is `incomplete` when the game list is partial, `missing_results` when a complete list lacks outcomes, `score_unknown` when outcomes are complete but the aggregate is missing, `consistent`, or `mismatch`. The server never overwrites the match score or result based on game details.

## `get_game_profile`

Read-only. Supply `{ "eventId": 42 }` to use a saved tournament, or `{ "game": "riftbound", "format": "Standard" }` for a new event. Returns the appropriate opening-hand field and guidance. Limits describe ordinary rules, not hard validation; variants may differ. Unknown game returns a null opening profile.

## `upsert_game`

Requires `matchId` and positive game `number`. Creates the game or updates only supplied fields, including nested opening fields; explicit null clears a field. Returns the saved game and `scoreCheck`. Access is restricted to the authenticated owner. Example:

```json
{"matchId":117,"number":3,"firstPlayer":"player","playerOpening":{"cardsReplaced":2}}
```

## `update_match`

Requires `matchId`; accepts changed match fields, including `gamesComplete`, but not `games`. Use `upsert_game` for game details. Unspecified fields are preserved.

## `delete_match`

Requires `matchId`. Permanently removes that match row.

## `update_tournament`

Requires `eventId`. Accepts `name`, `date`, `game`, `cardMedium`, `format`, `venueName`, `city`, `country`, `eventType`, `deckName`, `deckNotes`, `notes`, and `status`. Omit `cardMedium` to preserve it or set it to null to clear it.

## `list_tournaments`

Takes `{}` and returns the user's tournaments with summary records.

## `get_tournament`

Requires `eventId` and returns the tournament, deck, and complete match list, including any recorded game details and score checks.

## `list_opponents`

Takes `{}` and returns all named opponents across the current user's tournaments, sorted by name. Returns `[]` when none are known. Read-only.

Each row contains `name`, `matches`, `wins`, `losses`, `draws`, `gamesPlayed`, `gamesWon`, and `gamesLost`. Wins and losses are from the user's perspective. Match results include all result types; game totals include only `resultType=played`. `gamesPlayed` is `gamesWon + gamesLost`; drawn games are excluded.

Names are grouped using Unicode normalization, ignoring case and extra whitespace. Missing and `Unknown` names are excluded. The first recorded spelling is used for display.

## Shared analytics filters and results

The five tools below are read-only and scoped to the authenticated user. They default to **all time**, unlike `list_venues`, which defaults to the current year. Unknown properties are rejected.

Event filters, combined with AND:

- `from`, `to`: inclusive tournament dates (`YYYY-MM-DD`), not creation/import dates. Either bound may be omitted; `from` must not exceed `to`.
- `format`: exact tournament format, except for `list_decks`, where it is the registered deck format.
- `game`: exact card game; excludes tournaments with an unknown game.
- `cardMedium`: `digital`, `non_digital`, or `unknown` to select tournaments with no recorded card medium.
- `deckId`: a positive integer from `list_decks` or a tournament response.
- `venueName`, `city`, `country`: exact text matches after trimming the input. Use location fields to distinguish same-name venues.

All except `list_decks` also support:

- `eventId`: positive tournament ID.
- `opponentName`: exact full name ignoring Unicode compatibility forms, case and extra whitespace (including zero-width separators). It is not substring/fuzzy search. Missing/unknown names never match.
- `opponentArchetype`: exact archetype ignoring case and extra whitespace; `Unknown` can be queried.
- `result`: `win`, `loss`, or `draw`.
- `resultTypes`: nonempty array of up to five entries from `played`, `bye`, `concession`, `no_show`, `technical`. Omit to include all types; use `["played"]` for played matches only.

Summaries contain `tournaments`, `matches`, `wins`, `losses`, `draws`, `gamesWon`, `gamesLost`, `gamesPlayed`, and these rates as **fractions**, not percentages:

| Field | Formula |
| --- | --- |
| `matchWinRate` | wins / (wins + losses) |
| `drawRate` | draws / (wins + losses + draws) |
| `gameWinRate` | gamesWon / (gamesWon + gamesLost) |

`get_stats` includes explicit tournament W/L/D totals in its summary and month/deck/venue groups unless match-level filters are supplied. Matchup/opponent statistics and match listings only use recorded matches, never synthetic matches from totals. Game totals always use recorded game scores.

A zero denominator returns `0`; always interpret rates with the sample size. Game totals include only `resultType=played`, even if another result type has recorded scores. `gamesPlayed = gamesWon + gamesLost`; drawn games are excluded. Counts of tournaments include empty tournaments unless any match-level filter (`opponentName`, `opponentArchetype`, `result`, `resultTypes`) is supplied, in which case only tournaments with qualifying matches count.

## `list_matches`

Accepts all analytics filters and optional `limit` (integer 1–100, default 50) and `offset` (nonnegative safe integer, default 0).

Returns `{ items, total, limit, offset, nextOffset }`. Each item contains `matchId`, `eventId`, `tournamentName`, `eventType`, `date`, `format`, `venueName`, `city`, `country`, `deckId`, `deckName`, `roundNumber`, `playoffRound`, `opponentName`, `opponentArchetype`, `result`, `resultType`, `playerGamesWon`, `opponentGamesWon`, and `notes`. Missing names, scores and notes can be `null`. `eventType` is the recorded tournament type, not a normalized competitive tier.

Sorted by tournament date descending, event ID descending, Swiss rounds first, playoff stages in elimination order, round number ascending, then match ID ascending. Follow `nextOffset` with the same filters until it is `null`. `total` counts all matching rows, not just the page; an offset beyond the end returns empty items and `nextOffset: null`. Offset pagination reflects current data; restart if concurrent edits change the selection.

Example: Modern losses against Burn in a period:

```json
{"from":"2026-01-01","to":"2026-03-31","format":"Modern","opponentArchetype":"Burn","result":"loss","resultTypes":["played"],"limit":50}
```

## `get_stats`

Accepts all analytics filters and optional `groupBy`: `month`, `deck`, or `venue`.

Returns `{ summary, groupBy, groups }`. Without grouping, `groupBy` is `null` and `groups` is `[]`. Each group contains the same summary fields plus its dimension:

- `month`: `month` as `YYYY-MM`.
- `deck`: `deckId`, `deckName`, `format` (tournament format). A reused deck ID in different tournament formats remains separate.
- `venue`: `venueName`, `city`, `country`. Same-name venues in different locations remain separate; Unicode, case and whitespace variations of the same location are grouped.

Groups appear in order of their most recent matching tournament (month groups are newest first). Empty tournaments can produce zero-match groups. An empty selection returns zero summary fields and empty groups.

```json
{"from":"2026-01-01","to":"2026-12-31","format":"Modern","groupBy":"month","resultTypes":["played"]}
```

## `get_matchup_stats`

Accepts all analytics filters. Use `deckId` and/or `format` to narrow the player's deck; otherwise results combine all selected decks and formats.

Returns `{ summary, matchups }`. Each matchup contains `opponentArchetype`, all summary fields, and `lastPlayed` (latest matching tournament date). Archetypes are grouped ignoring case and extra whitespace; display spelling comes from the most recent matching record. Includes `Unknown` as its own group. Sorted by match count descending, then archetype name. An empty selection returns `matchups: []`.

```json
{"deckId":12,"format":"Modern","resultTypes":["played"]}
```

Use a real deck ID returned by Matchbook; `12` is illustrative.

## `list_decks`

Accepts event filters only: `from`, `to`, `format`, `game`, `cardMedium`, `deckId`, `venueName`, `city`, `country`. Here `format` filters the registered **deck** format; usage counts include tournaments of any format within the remaining filters.

Returns an array of `{ deckId, name, format, notes, tournaments, lastPlayed }`, sorted by name and deck ID. Counts and dates reflect the selected period/location; an empty tournament still counts as deck use. Without date/location filters, unused decks are included with `tournaments: 0` and `lastPlayed: null`. With date/location filters, only decks used in matching tournaments are included. Notes may be `null`. Distinct IDs remain distinct, even for similarly named decks. Returns `[]` when nothing matches.

```json
{"format":"Modern","from":"2026-01-01","to":"2026-12-31"}
```

## `get_opponent_history`

Requires `opponentName`; use `list_opponents` to discover the exact name. Empty/unknown placeholder names are rejected. Accepts all other analytics filters and the same pagination as `list_matches`.

Returns `{ opponentName, summary, archetypes, items, total, limit, offset, nextOffset }`. `items` use the `list_matches` fields and sort order. `summary` and `archetypes` always describe **all matching history**, independent of pagination; archetype rows use the `get_matchup_stats` fields. Names that normalize to the same key are treated as the same opponent, as in `list_opponents`; no distinct-person identity is inferred from a shared name. A known-name query without any matching records returns zero totals and empty arrays.

```json
{"opponentName":"Alex Romero","format":"Modern","limit":20,"offset":0}
```
