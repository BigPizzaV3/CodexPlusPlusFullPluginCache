# Common SQL (ClickHouse) Reference

Use this file first for common analytics asks:

- recent win rate
- games played volume
- region and tier breakdowns
- simple time trends

If the user asks for advanced matchup/synergy modeling or leaderboard rankings, switch to the specialized reference.

## Command scope

- `run_sql({ sql })`: global ClickHouse queries.

## Core columns (`summoner_match`)

Use these first for most analysis:

- `match_id`: unique match id
- `puuid`: player id
- `match_timestamp`: game start time (unix ms)
- `game_duration`: game length (seconds)
- `patch`: patch as 4-digit int
- `region`: shard/region
- `queue_id`: queue (for ranked solo use `420`)
- `tier`: rank tier bucket (0=Iron to 9=Challenger, NULL = unranked)
- `rank`: division in tier
- `lp`: league points
- `champion_id`: Riot champion id
- `champion_name`: champion name
- `position`: role (`TOP`, `JUNGLE`, `MIDDLE`, `BOTTOM`, `SUPPORT`)
- `team_id`: 100 blue / 200 red
- `win`: 1/0 outcome
- `kills`: kills
- `deaths`: deaths
- `assists`: assists
- `gold_earned`: total gold
- `total_cs`: lane + jungle CS
- `vision_score`: vision score

Full schema reference (all tables + full column lists): `get_guide("sql-schema-reference")`. Live tables and columns: `get_schema`.

## Fast defaults

Start with:

- `queue_id = 420` (ranked solo)
- recent patches (for example `patch IN (1604, 1605, 1606)`) or recent time window
- optional region/tier filters only when the user asks for them

## Query templates

### 1) Recent games by region and tier

```sql
SELECT
  region,
  tier,
  count() AS total_games
FROM summoner_match
WHERE queue_id = 420
  AND toDateTime(match_timestamp / 1000) >= now() - INTERVAL 30 DAY
GROUP BY region, tier
ORDER BY total_games DESC
LIMIT 200;
```

### 2) Global win rate over the last 180 days

```sql
SELECT
  round(avg(win) * 100, 2) AS win_rate,
  count() AS games
FROM summoner_match
WHERE queue_id = 420
  AND toDateTime(match_timestamp / 1000) >= now() - INTERVAL 180 DAY;
```

### 3) Region game share over the last 30 days

```sql
SELECT
  region,
  count() AS games,
  round(count() * 100.0 / sum(count()) OVER (), 2) AS pct_games
FROM summoner_match
WHERE queue_id = 420
  AND toDateTime(match_timestamp / 1000) >= now() - INTERVAL 30 DAY
GROUP BY region
ORDER BY games DESC;
```

### 4) DATE group-by pattern (daily trend)

```sql
SELECT
  toDate(toDateTime(match_timestamp / 1000)) AS day,
  count() AS games,
  round(avg(win) * 100, 2) AS win_rate
FROM summoner_match
WHERE queue_id = 420
  AND toDateTime(match_timestamp / 1000) >= now() - INTERVAL 30 DAY
GROUP BY day
ORDER BY day;
```

### 5) Patch comparison (recent patches)

```sql
SELECT
  patch,
  count() AS games,
  round(avg(win) * 100, 2) AS win_rate
FROM summoner_match
WHERE queue_id = 420
  AND patch IN (1604, 1605, 1606)
GROUP BY patch
ORDER BY patch DESC;
```
