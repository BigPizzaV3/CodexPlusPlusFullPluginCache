---
name: bracket-maker
description: Build tournament brackets and schedules with Zovo Tournament Maker - single or double elimination with standard seeding and byes, round robin (circle method), Swiss pairings, timetables over several courts, printable PDF and CSV - and update them with results and standings.
---

# Zovo Tournament Maker

Use for "make a bracket", "tournament bracket for 6 teams", "double elimination bracket", "round robin schedule", "Swiss pairings", "who plays next", "update the bracket, Ann beat Bob 21-15".

1. `generate_tournament_bracket`: pass every name in `participants` (2-128; use `participant_count` only if the user gives just a number). Pick `format`: single_elimination, double_elimination, round_robin or swiss.
   - Seeding: the list order is the ranking with the default `standard` seeding (seed 1 first). Use `random` when the user asks for a random draw, `as_listed` when they want 1st vs 2nd, 3rd vs 4th.
   - Byes go to the top seeds automatically; never add "BYE" entries yourself.
   - Optional: `third_place_match` (single), `grand_final_reset` (double, default true), `swiss_rounds`, `meetings: 2` for home and away, `courts` + `match_minutes` (+ `break_minutes`, `start_time`) for a timetable.
2. `calculate_bracket_standings`: same arguments as before (reuse the returned `request`) plus all `results` so far, each `{p1, p2, winner}` or `{p1, p2, score1, score2}` or `{match: "M5", winner}`. Use `"draw"` only in round robin and Swiss. For Swiss give results round by round; the next round is paired from them.

After a tool returns: summarise in 2-4 lines (format, byes, number of matches, first matches or next matches, champion when finished) and give the PDF and CSV links. The widget shows the bracket and lets the user click winners, so do not redraw the bracket as text art.

Do not use these tools to predict winners, fill in picks for famous tournaments, or plan league fixtures with venue constraints; do not invent results the user did not give.
