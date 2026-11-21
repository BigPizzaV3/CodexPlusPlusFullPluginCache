---
name: football-data
description: Retrieve Match Terminal fixtures, results, statistics and pre-match metrics.
---
Use team names as the normal query; never require the user to know a match ID. Use search_matches or the detail tools with team, optional opponent and UTC date. A team name on its own returns the teams with that name (senior, women's, youth and other clubs), each with its league and country; show that list and wait for the user to choose, then call search_matches with the chosen teamId to show the team's upcoming matches and latest results. With an opponent or date, the search returns matching fixtures. Show the returned numbered selection list, including full team names, competition, country and kickoff. Wait for the user to choose via number or Show all data button; never automatically pick the first or only result. Use the selected internal ID to retrieve all available match data. If results are truncated, offer to narrow by fuller name, opponent or date.
Use get_match_statistics for results and match statistics; its card also includes available pre-match context.
Use get_team_ratings for the pre-match metric breakdown: 30 rolling prior-match metrics and five group ratings.
Preserve returned units, match windows, zero values, missing values, source and calculation timestamps. Pre-match context describes prior matches, not performance in the selected fixture. Do not invent missing values or guarantee outcomes.
Player ratings are removed for now. Do not offer or infer them.

Example commands:
- Show yesterday’s Arsenal results.
- Show match statistics for [team] vs [opponent] on [YYYY-MM-DD].
- Show the pre-match metric breakdown for [team] vs [opponent].
- Compare strength, scoring, control, passing and defence for [team] vs [opponent].
- Show statistics and pre-match metrics for [team] vs [opponent].
