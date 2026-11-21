---
name: anniversary-poster
description: Count the days, weeks, months, hours and full moons since a relationship began, find the dates of the next milestones (1,000th day, 100th day, 500 weeks, anniversaries) and make a printable "our story in numbers" poster PDF and a milestone calendar file with the generate_anniversary_poster tool.
---

# Zovo Love Story Poster

Use `generate_anniversary_poster` when someone asks how long they have been together, wants an "our story in numbers" or anniversary poster, or asks when a milestone falls ("when is our 1,000th day?").

1. Pass `start_date` exactly as the user gave it (first date, the day they met, wedding day). If it is missing, ask for it; never guess it. The start date must be in the past.
2. Add `start_time` and `time_zone` (IANA, e.g. `Europe/London`) when the user mentions a time or a city; they make the hours count clock changes and date full moons locally.
3. Set `occasion` (`together`, `married`, `engaged`, `friends`, `family`) and `names` when given. For "our 100th day" in the Korean style (the first day is day 1) set `count_first_day: true`.
4. Use `as_of` when the poster is a gift for a later date, e.g. the anniversary itself. Otherwise the count runs to today.
5. After the tool returns, give the day count, the years-months-days line, two or three other numbers, the next milestones with their dates, every "Assumed" note that changes the meaning (day counting, February 29), and the poster PDF and calendar links.

Do not use this skill for countdowns to a future event, a single person's age, or writing love letters.
