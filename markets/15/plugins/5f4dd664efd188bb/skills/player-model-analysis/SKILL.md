---
name: player-model-analysis
description: Use when an FPL user asks for player profiles, comparisons, fixture probability analysis, market filtering, model feature importance or historical training-data inspection.
---

# Player and model analysis

Use only values returned by the connected Offside tools. All tools are read-only and forecasts are estimates rather than assured outcomes.

## Player discovery and comparison

- Use `get_player_profile` with a player name query or an established positive numeric `playerId`. If multiple matches appear, disambiguate before recommending.
- For a comparison of two to five players, resolve distinct positive FPL player IDs first and call `compare_players` with `playerIds`. Report unavailable IDs instead of inventing players.
- Use `get_player_fixtures` with a player's FPL player ID to investigate played-match stats and scheduled fixtures; future match statistics are unknown.
- Use `search_player_market` for filtered market searches. `position` is one of GKP, DEF, MID or FWD; `limit` must be 1–30. The optional `minProbGt5` is a 0–1 threshold and requires a `gameweek`. Make sure prices use the units reported by the server.

## Fixture analysis

- Use `get_fixture_difficulty` with `gameweek` and/or a **Premier League club team ID**, not a manager's FPL entry ID. With neither filter it returns the latest season's fixtures, which may be large.
- Interpret team-relative home/away win probabilities and clean-sheet probabilities in the correct direction. Do not treat forecasts as settled results.

## Model inspection

- Use `get_feature_importance` to inspect raw rows of feature importance when the user asks why the predictive model weights inputs as it does; pass `limit` and `offset` for pagination. Feature importance is not causal proof.
- Use `get_training_data` to inspect training records with `playerId`, `gameweek`, `season`, `isFuture`, `limit` and `offset` filters. `isFuture=true` means future fixture rows, not known outcomes. This is read-only access to returned model data.
- Do not claim that a training dataset field, feature, or model version exists unless present in returned data. Avoid mixing player IDs with Premier League team IDs or manager entry IDs.
