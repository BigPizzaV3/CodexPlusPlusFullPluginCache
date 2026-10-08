# Workflow: MLB matchup memo

Produce a pregame MLB matchup memo (pitching + lineup context).

## Inputs

- Date (default: today)
- Optional: specific teams or game

## Steps

1. `get_mlb_matchups` for the date (or REST matchup endpoints)
2. If a game is selected, pull `get_play_by_play` / recent form only when
   it sharpens the memo — don't dump raw PBP
3. Resolve key batters via `search_player` when citing individuals
4. Write the memo

## Artifact shape

```markdown
# MLB matchups — {date}

## {Away} @ {Home}
- **Pitching:** …
- **Lineup / keys:** …
- **Edge:** one paragraph

## Rerun inputs
date: …
games: …
```

## Parallelism

One sub-agent (or parallel tool batch) per game when covering a full slate.
