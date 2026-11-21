---
name: tennis-scouting
description: Answer tennis tactics and scouting questions with the RallyIQ tools - a game plan for one player against another, one player's strengths, weaknesses and serving habits, why a charted match went the way it did, and tactical leaderboards - and report the numbers honestly (what per 100 means, 90% margins, sample bias, the licence's attribution). Use whenever the user asks how a professional player should play an opponent, where a player serves, a player's weaknesses, who would win a matchup, why a match was won or lost, or which players lead on a tactical measure.
---

# Tennis scouting with RallyIQ

The `rallyiq` MCP server gives read-only access to RallyIQ's models of professional tennis, built from the Match Charting Project: volunteer charts that record every shot of more than 11,000 ATP and WTA matches. Each shot is valued by how much it moved its hitter's chance of winning the point, compared with an average tour player in the same position. This skill is about choosing the right tool and reporting what it says honestly.

## Pick the tool

- **A matchup** ("how should Sinner play Alcaraz?", "who wins Swiatek v Sabalenka on clay?"): `get_game_plan` with `player` (the side the plan is for), `opponent` and, when the user names one, `surface` (`hard`, `clay`, `grass`). It returns the forecast, a serve plan for each court, the opponent's serve plan, a return plan, rally shots to favour and avoid, career shot ratings side by side and the charted head-to-heads. For the other player's view, call it again with the names swapped.
- **One player** ("what are Gauff's weaknesses?", "where does Medvedev serve on break points?"): `get_player`. Names can be surnames or misspelt; pass `tour` (`atp` or `wta`) when a surname is shared. If the result lists `other_matches`, say which player you used and offer the others.
- **One match** ("why did Djokovic lose the 2023 Wimbledon final?"): `explain_match` with `player` and whatever the user gave of `opponent`, `tournament` and `year`. It picks the most recent charted match that fits and lists the others.
- **A ranking** ("who chooses shot direction best on the WTA?", "whose serve is most exploitable?"): `get_leaders` with a `board`, `tour` and `scope` (`active` or `all_eras`).

## Read the numbers correctly

- **per_100 is points per 100 shots** (or per 100 serves or returns, as the field says) against an average tour player in the same position. +1.0 per 100 is one extra point every hundred shots. Career shot ratings rarely pass ±1; the edge of one shot type in a plan can run several points.
- **margin is a 90% interval.** When an edge is smaller than its margin, or a field such as `clear` or `optimal_mix_clear` is false, say the data cannot tell it from zero rather than recommending it.
- **Use `compared` for ratings** ("better than 82% of rated WTA players") rather than inventing your own reading of a percentile. For points left on the table, lower is better, and `compared` already says so.
- **Serve plans:** `won_when_in_pct` is the share of points the server wins when a first serve to that direction lands, adjusted for this returner. The optimal mix allows for the returner reading a habit and stays within the range real servers vary; quote its gain as points per 100 first serves.
- **Return plans** compare returns with each other, not with zero. **Rally edges** add the hitter's skill with a shot to what this opponent usually gives up against it.
- **Weaknesses:** `most_exposed_to` lists opponents' shots, and `costs_per_100` is what each one costs the player.
- **Match breakdowns** split each player's points against expectation into direction choice, shot selection and execution. One player's gain is the other's loss. Shot selection partly reflects the ball a player was given, since the charts record no pace, spin or court position.
- **Forecasts are scouting estimates, not betting lines.** Charted matches lean toward finals, stars and charters' favourites, and the 90% range covers only the players' strength estimates.

## Attribution

The data is licensed CC BY-NC-SA 4.0, which requires crediting the Match Charting Project wherever the numbers appear. Every result carries the credit in its notes; keep a short credit in the answer ("Data: Match Charting Project, via RallyIQ").

## Good answers look like this

Placeholders in angle brackets stand for values from the tool results.

- "On the deuce court, <player>'s first serve wins <won_when_in_pct>% of points when it lands <direction> against <opponent>, the best of the three. RallyIQ's optimal mix moves <direction> from <current_share_pct>% to <optimal_share_pct>%, worth about <gain> points per 100 first serves (90% margin <margin>), so it is a lean, not a certainty."
- "<player>'s direction choice is <per_100> per 100 shots, <compared>. Their execution is <per_100>, which is inside its margin of <margin>, so the charts cannot separate it from an average player."
- Link the `url` for the full page on RallyIQ when the user wants the tables.
