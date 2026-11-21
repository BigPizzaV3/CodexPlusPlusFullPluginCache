# Pro Player SQL (ClickHouse) Reference

## Command

- `run_sql({ sql })`

## Tables

- `pro_summoner_match`: one row per pro player-game.
- `pro_match`: one row per team-side game (usually 2 rows per match).
- Full schema reference: `get_guide("sql-schema-reference")`. Live tables and columns: `get_schema`.

## Live Dataset Snapshot (ClickHouse)

- Snapshot date: 2026-10-05
- Years: 2014 to 2026 (`year` is the calendar year the game was played)
- Distinct matches: 102,635
- Distinct players: 11,076
- Distinct teams: 2,096
- Total player-game rows: 1,018,263
- Canonical role rows (TOP/JUNGLE/MIDDLE/BOTTOM/SUPPORT): 1,018,263 / 1,018,263
- Every `team_id` and `player_id` has one name (the latest), so `any(team_name)` is safe.
- Production note: `region` is not a column on `pro_summoner_match`; filter by `league` for regional asks.

## Categorical Filter Values (Live DB)

### `playoffs`

- `0` = regular season (842,033 rows)
- `1` = playoffs (176,230 rows)

### `side`

- `Blue` (509,173)
- `Red` (509,090)

### `split`

Season buckets: Oracle's Elixir's Winter/Spring/Summer names are kept; any other split name (Cup, Split 1, Rounds 1-2…) takes the season of its median month (to February: Winter, March to May: Spring, then Summer). International events, and qualifiers or cups played before or after their season's year, have no split.

- `Summer` (402,157)
- `Spring` (344,072)
- `NULL / missing` (195,545)
- `Winter` (76,489)

### `position`

- `JUNGLE` (203,757)
- `TOP` (203,756)
- `MIDDLE` (203,729)
- `BOTTOM` (203,641)
- `SUPPORT` (203,380)

### `data_completeness`

- `complete` (910,615)
- `partial` (107,648)

### `year`

- `2026` (92,871)
- `2025` (98,854)
- `2024` (101,540)
- `2023` (110,675)
- `2022` (124,283)
- `2021` (122,369)
- `2020` (96,792)
- `2019` (80,919)
- `2018` (66,540)
- `2017` (54,774)
- `2016` (41,710)
- `2015` (17,987)
- `2014` (9,149)

### `league` (all values in live DB, ordered by volume)

```text
LPL	71,720
LDL	69,854
LCK	54,760
LCKC	26,640
TCL	26,363
VCS	25,177
LEC	22,890
CBLOL	21,780
LJL	21,295
PRM	19,929
LAS	19,771
LCS	19,190
NACL	19,010
LFL	18,816
PCS	17,773
NA LCS	17,360
NLC	16,356
LCSA	16,040
EM	15,750
EU LCS	15,529
CK	13,904
WLDs	13,530
LMS	13,290
LPLOL	13,003
UL	12,670
EBL	12,667
HM	12,581
LVP SL	12,250
OPL	11,684
LLA	11,530
LMF	10,920
GLL	10,859
HC	10,516
LSPL	10,210
UPL	10,086
LHE	9,790
AL	9,613
CBLOLA	9,610
EUM	9,480
PGN	9,397
NEXO	9,352
LFL2	9,214
LCL	8,941
DDH	8,219
ESLOL	8,041
TAL	7,881
MSI	7,650
LCO	6,880
SLO	6,360
DCup	6,246
CLS	5,800
LCP	5,739
CD	5,553
PGC	5,528
RCL	5,414
LRS	5,400
LIT	5,342
LRN	5,295
EU CS	4,992
ROL	4,643
HLL	4,533
NA CS	4,520
RL	4,498
LLN	4,391
UKLC	4,297
PCL	4,285
BRCC	4,179
OGN	3,940
KeSPA Cup	3,800
OCS	3,641
HW	3,368
BIG	3,327
OTBLX	3,323
PRMP	3,138
EWC	2,840
SL (LATAM)	2,731
GL	2,668
VL	2,624
BM	2,430
IC	2,400
AM	2,398
EPL	2,370
CT	2,275
LTA S	2,220
CDF	2,159
LTA N	2,140
NLC Aurora Open	2,134
CU	2,090
LES	2,073
DL	1,980
BL	1,960
EL	1,747
LJLA	1,680
NASG	1,560
NL	1,430
ASCI	1,421
IEM	1,390
GPL	1,380
UGP	1,320
TPL	1,282
USP	1,060
LJLCS	1,045
TSC	1,018
TCS	970
CISC	915
EGL	909
WSCI	850
FST	800
GLLPA	790
IGNIS	550
GSG	530
NEST	500
EBLPA	431
ASI	420
NERD	420
IWCI	400
LTA	400
CCWS	390
AOL	370
AmCh	350
KeSPA	340
MSC	250
Riot	200
AC	190
LGL	80
WLRQ	60
```

## Frontend League -> Region Mapping

Source: `packages/shared/src/pro.ts` (`PRO_LEAGUE_REGIONS`).

- `CHINA` (3 mapped leagues): `LDL`, `LPL`, `LPLOL`
- `KOREA` (3 mapped leagues): `CK`, `LCK`, `LCKC`
- `EMEA` (11 mapped leagues): `HM`, `LEC`, `LFL`, `LFL2`, `LVP SL`, `NLC`, `NLC Aurora Open`, `PRM`, `PRMP`, `TCL`, `UL`
- `PACIFIC` (6 mapped leagues): `LCO`, `LJL`, `LJLA`, `LJLCS`, `PCS`, `VCS`
- `LTA` (10 mapped leagues): `CBLOL`, `CBLOLA`, `LCS`, `LCSA`, `LLA`, `LTA`, `LTA N`, `LTA S`, `NACL`, `SL (LATAM)`
- `INTERNATIONAL` (2 mapped leagues): `EWC`, `MSI`
- `OTHER` (87 mapped leagues): `AC`, `AL`, `AOL`, `ASCI`, `ASI`, `Asia Master`, `BIG`, `BL`, `BM`, `BRCC`, `CCWS`, `CD`, `CDF`, `CISC`, `CLS`, `CT`, `CU`, `DCup`, `DDH`, `DL`, `EBL`, `EBLPA`, `EGL`, `EL`, `EM`, `EPL`, `ESLOL`, `EU CS`, `EU LCS`, `EUM`, `FST`, `GL`, `GLL`, `GLLPA`, `GPL`, `GSG`, `HC`, `HLL`, `HS`, `HW`, `IC`, `IEM`, `IGNIS`, `IWCI`, `KeSPA`, `LAS`, `LCL`, `LCP`, `LES`, `LGL`, `LHE`, `LIT`, `LLN`, `LMF`, `LMS`, `LRN`, `LRS`, `LSPL`, `MSC`, `NA CS`, `NA LCS`, `NASG`, `NERD`, `NEST`, `NEXO`, `OCS`, `OGN`, `OPL`, `OTBLX`, `PCL`, `PGC`, `PGN`, `RCL`, `Riot`, `RL`, `ROL`, `SLO`, `TAL`, `TCS`, `TPL`, `TSC`, `UGP`, `UKLC`, `UPL`, `USP`, `VL`, `WLDs`

### Live DB leagues by frontend region bucket

- `CHINA`: `LPL` (71,720), `LDL` (69,854), `LPLOL` (13,003)
- `KOREA`: `LCK` (54,760), `LCKC` (26,640), `CK` (13,904)
- `EMEA`: `TCL` (26,363), `LEC` (22,890), `PRM` (19,929), `LFL` (18,816), `NLC` (16,356), `UL` (12,670), `HM` (12,581), `LVP SL` (12,250), `LFL2` (9,214), `PRMP` (3,138), `NLC Aurora Open` (2,134)
- `PACIFIC`: `VCS` (25,177), `LJL` (21,295), `PCS` (17,773), `LCO` (6,880), `LJLA` (1,680), `LJLCS` (1,045)
- `LTA`: `CBLOL` (21,780), `LCS` (19,190), `NACL` (19,010), `LCSA` (16,040), `LLA` (11,530), `CBLOLA` (9,610), `SL (LATAM)` (2,731), `LTA S` (2,220), `LTA N` (2,140), `LTA` (400)
- `INTERNATIONAL`: `MSI` (7,650), `EWC` (2,840)
- `OTHER`: `LAS` (19,771), `NA LCS` (17,360), `EM` (15,750), `EU LCS` (15,529), `WLDs` (13,530), `LMS` (13,290), `EBL` (12,667), `OPL` (11,684), `LMF` (10,920), `GLL` (10,859), `HC` (10,516), `LSPL` (10,210), `UPL` (10,086), `LHE` (9,790), `AL` (9,613), `EUM` (9,480), `PGN` (9,397), `NEXO` (9,352), `LCL` (8,941), `DDH` (8,219), `ESLOL` (8,041), `TAL` (7,881), `SLO` (6,360), `DCup` (6,246), `CLS` (5,800), `LCP` (5,739), `CD` (5,553), `PGC` (5,528), `RCL` (5,414), `LRS` (5,400), `LIT` (5,342), `LRN` (5,295), `EU CS` (4,992), `ROL` (4,643), `HLL` (4,533), `NA CS` (4,520), `RL` (4,498), `LLN` (4,391), `UKLC` (4,297), `PCL` (4,285), `BRCC` (4,179), `OGN` (3,940), `OCS` (3,641), `HW` (3,368), `BIG` (3,327), `OTBLX` (3,323), `GL` (2,668), `VL` (2,624), `BM` (2,430), `IC` (2,400), `EPL` (2,370), `CT` (2,275), `CDF` (2,159), `CU` (2,090), `LES` (2,073), `DL` (1,980), `BL` (1,960), `EL` (1,747), `NASG` (1,560), `ASCI` (1,421), `IEM` (1,390), `GPL` (1,380), `UGP` (1,320), `TPL` (1,282), `USP` (1,060), `TSC` (1,018), `TCS` (970), `CISC` (915), `EGL` (909), `FST` (800), `GLLPA` (790), `IGNIS` (550), `GSG` (530), `NEST` (500), `EBLPA` (431), `ASI` (420), `NERD` (420), `IWCI` (400), `CCWS` (390), `AOL` (370), `KeSPA` (340), `MSC` (250), `Riot` (200), `AC` (190), `LGL` (80)

## Region Presets For Natural-Language Prompts

Use these when prompts say things like "NA", "Korea", "EMEA", "China", "Pacific", "International", or "LATAM".

- `NA` -> `league IN ('LCS', 'LCSA', 'NACL', 'LTA N', 'NA LCS', 'NA CS')`
- `LATAM` -> `league IN ('CBLOL', 'CBLOLA', 'LLA', 'LLN', 'LTA S', 'SL (LATAM)', 'BRCC')`
- `EMEA / EU` -> `league IN ('LEC', 'LFL', 'LFL2', 'LVP SL', 'PRM', 'PRMP', 'NLC', 'NLC Aurora Open', 'TCL', 'UL', 'HM', 'EU LCS', 'EUM')`
- `KOREA / KR` -> `league IN ('LCK', 'LCKC', 'CK', 'LAS')` (LAS is the LCK Academy Series)
- `CHINA / CN` -> `league IN ('LPL', 'LDL', 'LPLOL')`
- `PACIFIC` -> `league IN ('PCS', 'VCS', 'LJL', 'LJLA', 'LJLCS', 'LCO')`
- `INTERNATIONAL` -> `league IN ('WLDs', 'MSI', 'FST', 'EWC')`

## Query Library (More Interesting)

### 1) Pro players with the most games (all-time)

```sql
SELECT
  player_id,
  any(player_name) AS player_name,
  COUNT(*) AS games,
  uniq(match_id) AS matches,
  min(year) AS first_year,
  max(year) AS last_year
FROM pro_summoner_match
GROUP BY player_id
ORDER BY games DESC
LIMIT 50;
```

### 2) Playoff clutch leaders (playoffs minus regular season win rate)

```sql
WITH stage_stats AS (
  SELECT
    player_id,
    any(player_name) AS player_name,
    countIf(playoffs = 0) AS regular_games,
    countIf(playoffs = 1) AS playoff_games,
    avgIf(win, playoffs = 0) AS regular_win_rate,
    avgIf(win, playoffs = 1) AS playoff_win_rate
  FROM pro_summoner_match
  GROUP BY player_id
)
SELECT
  player_id,
  player_name,
  regular_games,
  playoff_games,
  round(regular_win_rate * 100, 1) AS regular_win_pct,
  round(playoff_win_rate * 100, 1) AS playoff_win_pct,
  round((playoff_win_rate - regular_win_rate) * 100, 1) AS delta_pp
FROM stage_stats
WHERE regular_games >= 60
  AND playoff_games >= 20
ORDER BY delta_pp DESC, playoff_games DESC
LIMIT 50;
```

### 3) Side bias by player (Blue vs Red)

```sql
SELECT
  player_id,
  any(player_name) AS player_name,
  countIf(side = 'Blue') AS blue_games,
  countIf(side = 'Red') AS red_games,
  round(avgIf(win, side = 'Blue') * 100, 1) AS blue_win_pct,
  round(avgIf(win, side = 'Red') * 100, 1) AS red_win_pct,
  round((avgIf(win, side = 'Blue') - avgIf(win, side = 'Red')) * 100, 1) AS blue_minus_red_pp
FROM pro_summoner_match
GROUP BY player_id
HAVING blue_games >= 40 AND red_games >= 40
ORDER BY abs(blue_minus_red_pp) DESC, blue_games + red_games DESC
LIMIT 100;
```

### 4) Lane kingdom leaderboard at 15 minutes (pick a role)

```sql
SELECT
  player_id,
  any(player_name) AS player_name,
  count() AS games,
  round(avg(ifNull(gold_diff_at_15, 0)), 1) AS avg_gold_diff_15,
  round(avg(ifNull(xp_diff_at_15, 0)), 1) AS avg_xp_diff_15,
  round(avg(ifNull(cs_diff_at_15, 0)), 1) AS avg_cs_diff_15,
  round(avg(win) * 100, 1) AS win_rate
FROM pro_summoner_match
WHERE position = 'MIDDLE'
GROUP BY player_id
HAVING games >= 40
ORDER BY avg_gold_diff_15 DESC, win_rate DESC
LIMIT 50;
```

### 5) First-blood involvement demons

```sql
SELECT
  player_id,
  any(player_name) AS player_name,
  count() AS games,
  round(avg(ifNull(first_blood_kill, 0)) * 100, 1) AS fb_kill_pct,
  round(avg(ifNull(first_blood_assist, 0)) * 100, 1) AS fb_assist_pct,
  round(avg(ifNull(first_blood_kill, 0) + ifNull(first_blood_assist, 0)) * 100, 1) AS fb_involvement_pct
FROM pro_summoner_match
GROUP BY player_id
HAVING games >= 80
ORDER BY fb_involvement_pct DESC, games DESC
LIMIT 50;
```

### 6) Pocket picks with meaningful sample

```sql
WITH totals AS (
  SELECT player_id, count() AS total_games
  FROM pro_summoner_match
  GROUP BY player_id
)
SELECT
  p.player_id,
  any(p.player_name) AS player_name,
  p.champion_name,
  count() AS games,
  round(count() * 100.0 / t.total_games, 1) AS champ_share_pct,
  round(avg(p.win) * 100, 1) AS win_rate
FROM pro_summoner_match p
ANY INNER JOIN totals t USING (player_id)
GROUP BY p.player_id, p.champion_name, t.total_games
HAVING games >= 20
  AND (count() * 100.0 / t.total_games) >= 20
ORDER BY champ_share_pct DESC, win_rate DESC, games DESC
LIMIT 100;
```

### 7) Draft tax: first-pick win-rate delta by champion

```sql
SELECT
  champion_name,
  countIf(first_pick = 1) AS first_pick_games,
  countIf(first_pick = 0) AS non_first_pick_games,
  round(avgIf(win, first_pick = 1) * 100, 1) AS first_pick_win_pct,
  round(avgIf(win, first_pick = 0) * 100, 1) AS non_first_pick_win_pct,
  round((avgIf(win, first_pick = 1) - avgIf(win, first_pick = 0)) * 100, 1) AS first_pick_delta_pp
FROM pro_summoner_match
GROUP BY champion_name
HAVING first_pick_games >= 30 AND non_first_pick_games >= 30
ORDER BY first_pick_delta_pp ASC, first_pick_games DESC
LIMIT 75;
```

### 8) Team side bias (from `pro_match`)

```sql
SELECT
  team_id,
  any(team_name) AS team_name,
  countIf(side = 'Blue') AS blue_games,
  countIf(side = 'Red') AS red_games,
  round(avgIf(win, side = 'Blue') * 100, 1) AS blue_win_pct,
  round(avgIf(win, side = 'Red') * 100, 1) AS red_win_pct,
  round((avgIf(win, side = 'Blue') - avgIf(win, side = 'Red')) * 100, 1) AS blue_minus_red_pp
FROM pro_match
WHERE team_id IS NOT NULL AND team_id != ''
GROUP BY team_id
HAVING blue_games >= 20 AND red_games >= 20
ORDER BY abs(blue_minus_red_pp) DESC, blue_games + red_games DESC
LIMIT 100;
```

### 9) Duo synergy pairs (same team side, same match)

```sql
SELECT
  a.player_id AS player_a_id,
  any(a.player_name) AS player_a_name,
  b.player_id AS player_b_id,
  any(b.player_name) AS player_b_name,
  count() AS games,
  round(avg(a.win) * 100, 1) AS win_rate
FROM pro_summoner_match a
INNER JOIN pro_summoner_match b
  USING (match_id, side)
WHERE a.player_id < b.player_id
GROUP BY player_a_id, player_b_id
HAVING games >= 30
ORDER BY win_rate DESC, games DESC
LIMIT 100;
```

### 10) Champion pool evolution by year (single player)

```sql
SELECT
  year,
  count() AS games,
  uniq(champion_name) AS champ_pool,
  round(avg(win) * 100, 1) AS win_rate,
  round(avg(ifNull(kills, 0)), 2) AS avg_kills,
  round(avg(ifNull(deaths, 0)), 2) AS avg_deaths,
  round(avg(ifNull(assists, 0)), 2) AS avg_assists
FROM pro_summoner_match
WHERE player_id = 'oe:player:e1edfc5cea461399a63cb813cf795cc'
GROUP BY year
ORDER BY year DESC;
```

### 11) Game 5 closers (playoff deciders)

```sql
SELECT
  player_id,
  any(player_name) AS player_name,
  count() AS game5s,
  round(avg(win) * 100, 1) AS game5_win_pct,
  round(avg(ifNull(kills, 0)), 2) AS avg_kills,
  round(avg(ifNull(deaths, 0)), 2) AS avg_deaths,
  round(avg(ifNull(assists, 0)), 2) AS avg_assists
FROM pro_summoner_match
WHERE playoffs = 1
  AND game_number = 5
GROUP BY player_id
HAVING game5s >= 5
ORDER BY game5_win_pct DESC, game5s DESC
LIMIT 50;
```
