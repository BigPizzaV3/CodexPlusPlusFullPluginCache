# Workflow: prop slate brief

Produce a concise prop slate brief for one league and slate date.

## Inputs

- League (`nba`, `mlb`, …)
- Slate date (default: today in US/Eastern if unspecified)
- Optional: player list and lines; if missing, pick a short notable set
  from tonight's games

## Steps

1. `search_games` (or REST `GET /competitions/{comp}/editions/{year}/contests?date=`) for the league + date
2. For each focus player: `search_player` → `person_id`
3. Paid: `get_player_props` / `GET /analysis/player-prop` with line
4. Free fallback: `get_box_score` / game log windows; compute hit rate
   client-side only if the user asks — label it as approximate
5. Write the brief

## Artifact shape

```markdown
# {League} prop slate — {date}

## Picks
- **Player — market @ line** — one-sentence rationale · person_id=…

## Pass / fade
- …

## Notes
- Data freshness / injuries caveats

## Rerun inputs
league: …
date: …
players: …
lines: …
```

## Parallelism

Fan out prop cards per player. Do not serialize independent lookups.
