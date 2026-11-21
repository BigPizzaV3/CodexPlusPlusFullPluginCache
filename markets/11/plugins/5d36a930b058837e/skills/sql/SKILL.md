---
name: sql
description: "Use for League of Legends stats questions answered from Winrate data: champion win rates, counters, builds, pro play and leaderboards. Covers writing and debugging the SQL behind them."
---

# SQL Skill

## When To Use

Use this skill when the user asks for:

- SQL query writing or debugging
- data exploration and comparisons
- evidence-backed analysis from Winrate datasets

## Workflow

1. Clarify what metric and scope the user wants.
2. Read the relevant reference file in `references/` before writing SQL.
3. Start with a small validation query (`LIMIT 20` or narrow filters).
4. Expand to the full analysis query once shape and semantics are correct.
5. Summarize findings with concrete numbers from query output.

## Query Rules

- Prefer explicit filters for patch, region, queue, and tier when relevant.
- Avoid full scans when a filtered query can answer the question.
- Use stable aliases and readable CTEs for multi-step logic.
- For "best player on champion" requests, prefer `summoner_leaderboard` templates over tiny-sample `summoner_match` rankings.
- Never fabricate results. If a query fails, explain the error and fix it.

## Tooling Notes

- Use `run_sql({ sql })` to execute global ClickHouse SQL.
- Load supporting docs or references from `references/` when needed.
- Tables and columns come from `get_schema` (live); `get_guide("sql-schema-reference")` has the full written reference.
- Champion, item and rune names by ID are not bundled here: call `get_guide("champions")`, `get_guide("items")` or `get_guide("runes")`.

## Showing results

show_results draws the columns your query returns, in SELECT order. Pick the view that fits them:

- table: any columns. Lists read row by row: rankings, matchups, builds.
- bars: a name column, then the number to compare; up to 24 rows. More numbers show as text beside each bar.
- line: a patch or date column, then the numbers to follow over time. A games column shows under the axis.
- scatter: a name column, then two numbers: the first goes across, the second up. A games column sizes the points.
- spread: a name column, then one number. Every row on one line around their average, weighted by a games column if there is one. For one champion against many.

These columns draw pictures: champion_id, champion_name, opponent_champion_id, killer_champion_id, victim_champion_id (portrait and name); item_id, item_0 to item_5, before_item_id, after_item_id (item icon and name); position (role icon); tier (rank crest). Alias IDs to them, for example other_champion_id AS opponent_champion_id, and select one column per champion: champion_id or champion_name, not both. Names ending in _rate or _pct show as percents.

Keep patch as the numeric patch column (1620, never text like '16.20'): the card formats it and draws lines over it.
Use the listed column names (win_rate, games, champion_id…) rather than your own, so the card can label and draw them.

Joins, CTEs and UNIONs are fine: only the output columns matter. If the columns don't fit the view, the card shows a table and show_results says why.

## Reference Files

Before writing queries, load the relevant file in `references/`.
Choose the reference that matches the task and follow its command/query pattern.

## References

- `references/common-sql.md`
- `references/pro-player-sql.md`
- `references/champion-sql.md`
- `references/leaderboard-sql.md`
