# Leaderboard SQL (ClickHouse) Reference

Use this when users ask:

- "Who is the best on <champion>?"
- top one tricks / champion specialists
- leaderboard-style player ranking

## Command scope

- `run_sql({ sql })`: global ClickHouse query execution.

## Data source

- Use `summoner_leaderboard` first for ranking players.
- This view is refreshed from `summoner_match` and includes games from `patch >= 1600`.
- For patch-specific-only ranking, use the patch template at the end.

## Setup defaults

- `champion_id = 34` (Anivia example)
- `min_champion_games = 50`
- `min_champion_share = 0.60`

## Query templates (tested)

### 1) Best champion specialists by ladder strength (LP/tier first)

Use this as the default answer for "best <champion> player".

```sql
SELECT
  region,
  summoner_name,
  puuid,
  tier,
  rank,
  lp,
  games,
  wins,
  main_champion_games,
  main_champion_wins,
  round(main_champion_games / games * 100, 1) AS champion_share_pct,
  round(main_champion_wins / nullIf(main_champion_games, 0) * 100, 1) AS champion_win_rate,
  round((sum_kills + sum_assists) / greatest(sum_deaths, 1), 2) AS kda
FROM summoner_leaderboard
WHERE main_champion_id = 34
  AND main_champion_games >= 50
  AND main_champion_games / games >= 0.60
ORDER BY
  ifNull(tier, -1) DESC,
  ifNull(lp, -1) DESC,
  main_champion_games DESC
LIMIT 20;
```

### 2) Best champion specialists by performance (Bayesian, sample-aware)

Use this when users care about performance quality, not just ladder rank. The pool is Diamond+.

```sql
WITH pool AS (
  SELECT
    region,
    summoner_name,
    puuid,
    tier,
    rank,
    lp,
    games,
    wins,
    main_champion_games,
    main_champion_wins,
    main_champion_games / games AS champion_share,
    main_champion_wins / nullIf(main_champion_games, 0) AS champion_wr,
    (sum_kills + sum_assists) / greatest(sum_deaths, 1) AS kda
  FROM summoner_leaderboard
  WHERE main_champion_id = 34
    AND main_champion_games >= 30
    AND main_champion_games / games >= 0.50
    AND ifNull(tier, 0) >= 6
),
base AS (
  SELECT sum(main_champion_wins) / sum(main_champion_games) AS base_wr
  FROM pool
)
SELECT
  p.region,
  p.summoner_name,
  p.puuid,
  p.tier,
  p.rank,
  p.lp,
  p.main_champion_games,
  round(p.champion_share * 100, 1) AS champion_share_pct,
  round(p.champion_wr * 100, 1) AS champion_win_rate,
  round((((p.main_champion_wins + 150 * b.base_wr) / (p.main_champion_games + 150)) - b.base_wr) * 100, 2) AS bayes_edge_pp,
  round(p.kda, 2) AS kda
FROM pool p
CROSS JOIN base b
ORDER BY bayes_edge_pp DESC, p.main_champion_games DESC
LIMIT 20;
```

### 3) Patch-specific champion ranking (only when explicitly requested)

Use this if the user asks for one patch only. Keep a stronger min-games threshold.

```sql
WITH player_champ AS (
  SELECT
    puuid,
    argMax(summoner_name, match_timestamp) AS summoner_name,
    argMax(region, match_timestamp) AS region,
    argMax(tier, match_timestamp) AS tier_current,
    argMax(lp, match_timestamp) AS lp_current,
    count() AS games,
    sum(win) AS wins,
    avg(kda) AS avg_kda
  FROM summoner_match
  WHERE champion_id = 34
    AND queue_id = 420
    AND patch = 1606
    AND tier >= 3
  GROUP BY puuid
  HAVING games >= 20
),
base AS (
  SELECT sum(wins) / sum(games) AS base_wr FROM player_champ
)
SELECT
  p.region,
  p.summoner_name,
  p.puuid,
  p.tier_current,
  p.lp_current,
  p.games,
  round(p.wins / p.games * 100, 1) AS win_rate,
  round(p.avg_kda, 2) AS avg_kda,
  round((((p.wins + 80 * b.base_wr) / (p.games + 80)) - b.base_wr) * 100, 2) AS bayes_edge_pp
FROM player_champ p
CROSS JOIN base b
ORDER BY bayes_edge_pp DESC, p.games DESC
LIMIT 20;
```
