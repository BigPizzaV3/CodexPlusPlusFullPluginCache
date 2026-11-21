# Champion SQL (ClickHouse) Reference

Use this when the task is champion-level analysis across many players.
For "best player on champion" or "top one tricks", load `references/leaderboard-sql.md`.

## Command scope

- `run_sql({ sql })`: global ClickHouse champion analysis (use this file).

## Setup (fast)

Templates below use these defaults:

- `champion_id = 51`
- `position = 'BOTTOM'`
- `region = 'NA1'`
- `queue_id = 420`
- `patch = 1606`
- `tier >= 3` (Gold+)

Swap defaults to the user's scope. Use known `champion_id`; lookup only if unsure.
Champion IDs are the standard Riot API/Data Dragon champion IDs.

```sql
-- Find recent patches with enough games
SELECT patch, count() AS games
FROM summoner_match
WHERE queue_id = 420
GROUP BY patch
ORDER BY patch DESC
LIMIT 6;
```

## Query templates (tested)

### 1) Matchup floor (blind-pick safety across all champions)

Use when users ask which champions are safest into bad matchups.

```sql
WITH matchup AS (
  SELECT
    champion_id,
    other_champion_id,
    sum(games) AS games,
    sum(wins) AS wins
  FROM champion_pairwise_stats
  WHERE position = 'BOTTOM'
    AND other_position = 'BOTTOM'
    AND is_ally = 0
    AND patch = 1606
    AND tier >= 3
  GROUP BY champion_id, other_champion_id
  HAVING games >= 500
),
per_champ AS (
  SELECT
    champion_id,
    sum(games) AS total_games,
    sum(wins) / sum(games) AS overall_wr,
    quantileExactWeighted(0.10)(wins / games, games) AS wr_p10,
    min(wins / games) AS worst_wr
  FROM matchup
  GROUP BY champion_id
  HAVING total_games >= 15000
),
name_map AS (
  SELECT champion_id, any(champion_name) AS champion_name
  FROM summoner_match
  WHERE patch = 1606
  GROUP BY champion_id
)
SELECT
  p.champion_id,
  n.champion_name,
  p.total_games,
  round(p.overall_wr * 100, 2) AS overall_win_rate,
  round(p.wr_p10 * 100, 2) AS matchup_win_rate_p10,
  round(p.worst_wr * 100, 2) AS worst_matchup_win_rate
FROM per_champ p
LEFT JOIN name_map n ON n.champion_id = p.champion_id
ORDER BY matchup_win_rate_p10 DESC, p.total_games DESC
LIMIT 12;
```

### 2) Counter matchups for one champion (Bayesian edge)

Use when users ask "what beats this champion?" without overreacting to low sample.

```sql
WITH pair_agg AS (
  SELECT
    other_champion_id,
    sum(games) AS games,
    sum(wins) AS wins
  FROM champion_pairwise_stats
  WHERE champion_id = 51
    AND position = 'BOTTOM'
    AND is_ally = 0
    AND other_position = 'BOTTOM'
    AND patch = 1606
    AND tier >= 3
  GROUP BY other_champion_id
  HAVING games >= 1200
),
baseline AS (
  SELECT sum(wins) / sum(games) AS base_wr
  FROM pair_agg
),
name_map AS (
  SELECT champion_id, any(champion_name) AS champion_name
  FROM summoner_match
  WHERE patch = 1606
  GROUP BY champion_id
)
SELECT
  p.other_champion_id,
  n.champion_name AS opponent,
  p.games,
  round((p.wins / p.games) * 100, 2) AS raw_win_rate,
  round((((p.wins + 300 * b.base_wr) / (p.games + 300)) - b.base_wr) * 100, 2) AS bayes_edge_pp
FROM pair_agg p
CROSS JOIN baseline b
LEFT JOIN name_map n ON n.champion_id = p.other_champion_id
ORDER BY bayes_edge_pp ASC, p.games DESC
LIMIT 12;
```

### 3) Best support pairings for one ADC (Bayesian edge)

Use when users ask for high-confidence synergies.

```sql
WITH pair_agg AS (
  SELECT
    other_champion_id,
    sum(games) AS games,
    sum(wins) AS wins
  FROM champion_pairwise_stats
  WHERE champion_id = 51
    AND position = 'BOTTOM'
    AND is_ally = 1
    AND other_position = 'SUPPORT'
    AND patch = 1606
    AND tier >= 3
  GROUP BY other_champion_id
  HAVING games >= 800
),
baseline AS (
  SELECT sum(wins) / sum(games) AS base_wr
  FROM pair_agg
),
name_map AS (
  SELECT champion_id, any(champion_name) AS champion_name
  FROM summoner_match
  WHERE patch = 1606
  GROUP BY champion_id
)
SELECT
  p.other_champion_id,
  n.champion_name AS support,
  p.games,
  round((p.wins / p.games) * 100, 2) AS raw_win_rate,
  round((((p.wins + 200 * b.base_wr) / (p.games + 200)) - b.base_wr) * 100, 2) AS bayes_edge_pp
FROM pair_agg p
CROSS JOIN baseline b
LEFT JOIN name_map n ON n.champion_id = p.other_champion_id
ORDER BY bayes_edge_pp DESC, p.games DESC
LIMIT 12;
```

### 4) Lane-state dependency at 10 minutes

Use when users ask whether a champion must win lane to win game.

```sql
SELECT
  multiIf(
    gold_diff_at_10 >= 1000, 'Ahead 1k+',
    gold_diff_at_10 <= -1000, 'Behind 1k+',
    'Even'
  ) AS lane_state,
  count() AS games,
  round(avg(won) * 100, 2) AS win_rate,
  round(avg(gold_diff_at_10), 1) AS avg_gold_diff_10,
  round(avg(cs_diff_at_10), 1) AS avg_cs_diff_10
FROM summoner_match_timeline
WHERE champion_id = 51
  AND position = 'BOTTOM'
  AND region = 'NA1'
  AND queue_id = 420
  AND patch = 1606
  AND tier >= 3
GROUP BY lane_state
ORDER BY games DESC;
```

### 5) Snowball vs comeback edge (champion vs role baseline)

Use when users ask if the champion converts leads better than peers.

```sql
WITH champ AS (
  SELECT
    avgIf(won, gold_diff_at_10 <= -1000) AS champ_behind_wr,
    avgIf(won, gold_diff_at_10 >= 1000) AS champ_ahead_wr
  FROM summoner_match_timeline
  WHERE champion_id = 51
    AND position = 'BOTTOM'
    AND region = 'NA1'
    AND queue_id = 420
    AND patch = 1606
    AND tier >= 3
),
role_field AS (
  SELECT
    avgIf(won, gold_diff_at_10 <= -1000) AS role_behind_wr,
    avgIf(won, gold_diff_at_10 >= 1000) AS role_ahead_wr
  FROM summoner_match_timeline
  WHERE position = 'BOTTOM'
    AND region = 'NA1'
    AND queue_id = 420
    AND patch = 1606
    AND tier >= 3
)
SELECT
  round(champ.champ_behind_wr * 100, 2) AS champ_win_behind_1k,
  round(role_field.role_behind_wr * 100, 2) AS role_win_behind_1k,
  round((champ.champ_behind_wr - role_field.role_behind_wr) * 100, 2) AS behind_edge_pp,
  round(champ.champ_ahead_wr * 100, 2) AS champ_win_ahead_1k,
  round(role_field.role_ahead_wr * 100, 2) AS role_win_ahead_1k,
  round((champ.champ_ahead_wr - role_field.role_ahead_wr) * 100, 2) AS ahead_edge_pp
FROM champ
CROSS JOIN role_field;
```

### 6) Duration profile vs role field

Use when users ask "when is this champ strongest?"

```sql
WITH champ AS (
  SELECT
    multiIf(
      game_duration < 1200, '<20m',
      game_duration < 1500, '20-25m',
      game_duration < 1800, '25-30m',
      game_duration < 2100, '30-35m',
      '35m+'
    ) AS duration_bucket,
    count() AS champ_games,
    avg(win) AS champ_wr
  FROM summoner_match
  WHERE champion_id = 51
    AND position = 'BOTTOM'
    AND region = 'NA1'
    AND queue_id = 420
    AND patch = 1606
    AND tier >= 3
  GROUP BY duration_bucket
),
field AS (
  SELECT
    multiIf(
      game_duration < 1200, '<20m',
      game_duration < 1500, '20-25m',
      game_duration < 1800, '25-30m',
      game_duration < 2100, '30-35m',
      '35m+'
    ) AS duration_bucket,
    count() AS field_games,
    avg(win) AS field_wr
  FROM summoner_match
  WHERE position = 'BOTTOM'
    AND region = 'NA1'
    AND queue_id = 420
    AND patch = 1606
    AND tier >= 3
  GROUP BY duration_bucket
)
SELECT
  c.duration_bucket,
  c.champ_games,
  round(c.champ_wr * 100, 2) AS champ_win_rate,
  f.field_games,
  round(f.field_wr * 100, 2) AS role_field_win_rate,
  round((c.champ_wr - f.field_wr) * 100, 2) AS edge_pp
FROM champ c
INNER JOIN field f USING (duration_bucket)
ORDER BY c.champ_games DESC;
```

### 7) First component path outcomes (tempo + lane context)

Use when users ask which first component paths look best.

```sql
SELECT
  first_component_item,
  count() AS games,
  round(avg(won) * 100, 2) AS win_rate,
  round(avg(gold_diff_at_10), 1) AS avg_gold_diff_10,
  round(avg(cs_diff_at_10), 1) AS avg_cs_diff_10,
  round(avg(first_component_timestamp) / 60000, 1) AS avg_first_component_min
FROM summoner_match_timeline
WHERE champion_id = 51
  AND position = 'BOTTOM'
  AND region = 'NA1'
  AND queue_id = 420
  AND patch = 1606
  AND tier >= 3
  AND first_component_item IS NOT NULL
GROUP BY first_component_item
HAVING games >= 600
ORDER BY games DESC
LIMIT 10;
```

### 8) Damage-share buckets (carry threshold)

Use when users ask what performance level is needed to win on this champion.

```sql
SELECT
  multiIf(
    team_damage_percentage < 0.2, '<20%',
    team_damage_percentage < 0.25, '20-25%',
    team_damage_percentage < 0.3, '25-30%',
    team_damage_percentage < 0.35, '30-35%',
    '35%+'
  ) AS dmg_share_bucket,
  count() AS games,
  round(avg(win) * 100, 2) AS win_rate,
  round(avg(damage_per_minute), 1) AS avg_dpm
FROM summoner_match
WHERE champion_id = 51
  AND position = 'BOTTOM'
  AND region = 'NA1'
  AND queue_id = 420
  AND patch = 1606
  AND tier >= 3
GROUP BY dmg_share_bucket
HAVING games >= 500
ORDER BY games DESC;
```

### 9) Improvement deltas (wins vs losses on this champion)

Use when users ask "how should I improve?" at champion level.

```sql
SELECT
  round(avgIf(kills, win = 1) - avgIf(kills, win = 0), 2) AS delta_kills,
  round(avgIf(deaths, win = 1) - avgIf(deaths, win = 0), 2) AS delta_deaths,
  round(avgIf(assists, win = 1) - avgIf(assists, win = 0), 2) AS delta_assists,
  round(avgIf(total_cs, win = 1) - avgIf(total_cs, win = 0), 2) AS delta_cs,
  round(avgIf(vision_score, win = 1) - avgIf(vision_score, win = 0), 2) AS delta_vision,
  round(avgIf(damage_per_minute, win = 1) - avgIf(damage_per_minute, win = 0), 2) AS delta_dpm,
  round(avgIf(gold_per_minute, win = 1) - avgIf(gold_per_minute, win = 0), 2) AS delta_gpm
FROM summoner_match
WHERE champion_id = 51
  AND position = 'BOTTOM'
  AND region = 'NA1'
  AND queue_id = 420
  AND patch = 1606
  AND tier >= 3;
```

### 10) Win rate by day (daily trend)

Use when users ask how a champion is performing day-to-day or trending recently.

```sql
SELECT
  toDate(fromUnixTimestamp64Milli(match_timestamp)) AS day,
  count() AS games,
  round(avg(win) * 100, 2) AS win_rate
FROM summoner_match
WHERE champion_id = 51
  AND position = 'BOTTOM'
  AND queue_id = 420
  AND patch = 1606
  AND tier >= 3
GROUP BY day
ORDER BY day ASC;
```

Good candidate for `show_results` with `view: "line"`.
