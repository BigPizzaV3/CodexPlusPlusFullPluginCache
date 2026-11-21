---
name: league-schedule
description: Make round robin league schedules (fixtures) for 3 to 24 teams on real dates with the generate_league_schedule tool - single or double (home and away) round robin, balanced home and away games, byes, play days, blackout dates, venues and time slots - with a printable PDF, Excel workbook and calendar files.
---

# Zovo League Fixtures

Use `generate_league_schedule` when someone wants a league schedule, round robin schedule, fixture list or home and away season for 3 to 24 teams.

1. Put the team names into `teams` as an array (convert a pasted list; objects `{"name","venue"}` when each team has a home ground). Use `teams_text` only if the list cannot be split.
2. `start_date` is required. If it is missing, ask one short question ("When is the first round?"). Pass `play_days` when the user names weekdays (e.g. ["Tuesday","Thursday"]); otherwise the weekday of the start date is used. Use `every_weeks: 2` for every other week.
3. `format`: "single" (each pair once, default) or "double" (each pair twice, home and away). Phrases such as "play each other twice" or "home and away" mean double.
4. Holidays and breaks go into `blackout_dates` (single dates or ranges). A season deadline goes into `end_date`.
5. Shared fields or courts go into `venues`, kickoff times into `time_slots` (or one `kickoff_time`). Add `timezone` only if the user gives one.
6. If the tool refuses (season does not fit before the end date, too few venue slots, duplicate names, fewer than 3 or more than 24 teams), pass on its message and ask the user which of the suggested changes to make.
7. After it returns, give the season span, rounds and games, the first rounds, the home/away balance in one line, skipped blackout dates, and the PDF, Excel, all-games ICS and per-team ZIP links.

Do not use it for knockout brackets, one-day tournaments, scores, standings or real professional league fixtures.
