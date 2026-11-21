---
name: track-matches
description: "Record and correct trading-card-game tournaments and matches with Matchbook, including screenshot results, playoffs, deck versions, statistics, and Modern Performance reports. Use for logging events and rounds or reviewing a player's record."
---

# Track matches

Use the connected Matchbook tools as the source of truth. Inspect current tool schemas before calling them. Never invent an endpoint, saved record, deck version, or interactive widget. Match the user's language.

## Resolve the event

1. Use `list_tournaments` to find the event, then `get_tournament` to inspect matches, status, location, deck, and notes. Reuse a verified event ID from this conversation when unambiguous.
2. Resolve relative dates in the user's timezone; use the actual event date for historical imports.
3. Before `import_tournament`, check for an existing event with the same date, name, and venue if known. Set `status=active` for an ongoing event. Supply required name, date, format, eventType, and deckName from evidence; venueName is also required unless the cards are digital. Ask only for required information that remains unknown.
4. Pass `eventId` explicitly when logging matches. Ask which event if several could be intended. Never silently use an unrelated active event.
5. Preserve venue spellings and locations unless normalization is requested. Do not infer a city solely from a store name.
6. Read the tournament's `game` separately from `format`: `magic`, `riftbound`, `one_piece`, `lorcana`, or null. When creating an event, use an explicitly supplied or clearly established game; ask if necessary, but do not assign a game to historical records by guesswork. For a known event, use its saved game and `get_game_profile` when opening-hand details are requested. If the game is unknown and the meaning of a reported mulligan is unclear, ask which game; recording an ordinary match does not require game details.
7. Record `cardMedium` as `digital` or `non_digital` only when supported by the user's information. Null means unknown; do not infer it from the venue, game, or whether participants played remotely. Use the `cardMedium` filter when comparing digital and non-digital results.

## Record a match

1. Extract round, opponent, archetype, result, and optional game score from text or screenshots. Read scores from the user's perspective. Distinguish a round score from a cumulative event record.
2. Let the user's explicit result or correction control the result. Ask about uncertain player identity or conflicting score evidence. If only win/loss/draw is known, omit game scores or use null; never convert “won” to 2–0.
3. Omit unknown opponent names rather than writing placeholders. Preserve accents and confirmed spelling. Correct unambiguous archetype typos without inventing an archetype from a partial image.
4. Inspect existing matches to avoid duplicate rounds. Update an existing match when correcting it. After a timeout or uncertain write response, read the tournament before retrying.
5. Supply required `result`, `resultType`, and `roundNumber` to `add_match`. Use `played` for ordinary played matches. Use `bye`, `concession`, `no_show`, or `technical` only with supporting evidence. An ordinary in-game scoop does not automatically classify the whole match as a concession.
6. Number rounds sequentially across Swiss and playoffs. Assign `playoffRound=round_of_16`, `quarterfinal`, `semifinal`, or `final` only when known. Use null to clear a wrong playoff stage. Do not infer playoffs from position alone.
7. Record an intentional draw as `result=draw`, normally `resultType=played`, with an explicit intentional-draw note. The current schema has no separate intentional-draw flag. Omit unknown scores.
8. Write only when recording or correction is requested. Verify returned saved details, or read the tournament when needed. Report failures and pending writes accurately.
9. Game details are optional. Use `games` in `add_match` or `import_tournament`, or `upsert_game` to change one game of an existing match. `firstPlayer` is `player` for the account owner or `opponent`. Save only explicit facts; never infer game order, winners, starting player, or opponent mulligans from the match score. Ask about an ambiguous detail only when it is needed to fulfill the user's request. Null is unknown; zero is known.
10. Opening fields have distinct meanings: `mulliganCount` counts mulligans (Magic, One Piece), `cardsReplaced` counts individual cards (Riftbound, Lorcana), and `keptHandSize` is the explicitly known hand size. Do not convert between these fields without evidence. Ordinary profile limits are guidance; format rules can differ.
11. Set `gamesComplete` only when the user establishes that every played game is listed. If the returned `scoreCheck` is `mismatch`, explain the discrepancy and ask how to correct it; do not silently change the match score or result. `missing_results`, `score_unknown`, and `incomplete` do not imply a conflict. Match result remains independently authoritative.

## Correct or finish an event

- Resolve the intended match ID before `update_match`; send only changed fields. Do not delete and recreate a match merely to edit it.
- Delete a match or tournament only at the user's explicit request, after identifying the exact record. Use the current tool schema for the requested deletion.
- Merge note additions with existing notes. Put standings, attendance, and event-wide comments in tournament notes; put opponent or game details in match notes.
- Treat tournament `wins`, `losses`, and `draws` as complete overriding totals that already include known rounds. Supply all three only when an overall record is known. Never add these totals to match-derived results. Restore match-derived totals with all three set to null when requested.
- Mark the event completed when the user has finished, dropped, or played their final match. Do not close it after one round or after Swiss if playoffs are pending.

## Keep deck versions accurate

- Inspect `list_decks` for available IDs and names. Matching names or archetypes do not establish identical card lists across events.
- Reuse a deck identity for “same deck,” but never assert an old list was registered at a new event without evidence.
- When a build changed and the new list is pending, record that in the specific tournament's notes; do not present an old list as the new build.
- Current tools expose deck notes but no explicit immutable event-deck snapshot API. Do not promise version isolation or assume `deckNotes` changes only one event. Until backend semantics are verified, preserve an event-specific list or pending-list note in tournament notes rather than overwriting shared deck notes.

## Review statistics

- Use `get_stats` for summary rates and month/deck/venue groups, `get_matchup_stats` for archetypes, and `get_opponent_history` for a known opponent. Discover names through `list_opponents` and decks through `list_decks` as needed.
- Apply date, format, deck ID, location, and result-type filters consistently. Filters combine with AND. Use separate queries for comparisons when needed; do not invent unsupported filters.
- Follow `list_matches.nextOffset` until null for a complete match list. Label an incomplete listing.
- Report W–L–D and sample size beside rates. Match win rate is W/(W+L), excluding draws from that denominator; show draws separately. Game win rate is gamesWon/(gamesWon+gamesLost), using recorded played-match scores. Convert fractions to percentages.
- Default queries include all result types; label that scope. Use `resultTypes=["played"]` for played matches. Intentional draws can still be included under the present schema; do not claim the filter excludes every unplayed result.
- Explicit tournament totals can exceed known round details. Explain coverage differences between event aggregates and match-level filters or matchup breakdowns. Never fabricate missing opponents or rounds.
- Describe an empty denominator as no eligible results rather than meaningful 0% performance. Avoid strong conclusions from small samples.
- Route durable analytical reports and dashboards to the relevant analysis workflow when appropriate.
- For an on-demand Modern Performance report, follow [references/modern-performance.md](references/modern-performance.md). Build it from current Matchbook records in the conversation or the requested artifact.

## Confirm saves consistently

After a verified match save, use this compact text pattern in the user's language, omitting unknown fields:

**{Event name} · {format} · {date}**
Round {number}{known playoff stage} · {opponent} · {opponent archetype}
**{Win/Loss/Draw} {known game score}** · Event record: **{verified W–L–D}**
{Brief note only when useful.}

For a correction, state what changed and show the updated result. For multiple rounds, use a small table. Report only server-verified event totals. Use plain Markdown; do not output raw HTML or claim a live widget exists without a supported app view.
