# Workflow: standings digest

Produce a short standings / playoff-picture digest for one league.

## Inputs

- League slug (`nba`, `mlb`, `nfl`, `nhl`, …)
- Optional: conference / division focus

## Steps

1. `get_standings` with the league (or REST standings)
2. Note the resolved `season_year` / edition so offseason reads are clear
3. Highlight top seeds, bubble teams, and biggest recent movers only if
   game results are in evidence — do not invent streaks
4. Write the digest

## Artifact shape

```markdown
# {League} standings digest

Season: {season_year}

## Leaders
- …

## Bubble / notes
- …

## Rerun inputs
league: …
as_of: …
```
