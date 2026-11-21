---
name: golf-game-review
description: Review a golfer's game from their Matrix Golf data. Use when the golfer asks how they are playing, what to practice, why a round went the way it did, or how they compare with earlier rounds.
---

# Reviewing a golfer's game

The Matrix Golf tools read the signed-in golfer's own rounds. A good review
answers one question the golfer cares about, with their own numbers.

## What to read

- A question about one round ("how did Saturday go?"): `list_rounds` to find it,
  then `get_round` for the hole-by-hole card.
- A question about the game in general ("what should I practice?"): `get_playing_stats`.
  It already applies the definitions the Matrix apps use, so prefer it to adding
  up scorecards.
- Level matters for advice. `get_my_profile` gives the handicap index; read it
  before saying what is good or bad for this golfer.

## How to read it

- Compare like with like. `to_par` covers only the holes played, so a nine-hole
  round and an eighteen-hole round are not the same scale.
- A null statistic means the golfer did not track it. Say so, and suggest
  tracking it, instead of treating it as zero.
- Look for where the shots go: three-putts, missed greens that were not saved,
  penalty holes, a par type (3s, 4s or 5s) that scores worse than the others.
- One round is noise. For a trend, use the `trend` series or several rounds.

## How to answer

Lead with the single biggest finding and the number behind it. Give at most
two or three points, each tied to a figure the golfer can check on the card.
When a card is shown, the golfer already sees the table, so do not repeat it.
Keep practice advice concrete and proportionate to what the data shows.
