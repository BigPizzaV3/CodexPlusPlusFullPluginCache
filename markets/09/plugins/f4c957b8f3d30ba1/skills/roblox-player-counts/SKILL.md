---
name: roblox-player-counts
description: Answer questions about Roblox games and their players using CCUCheck: how many people are playing a game, whether it is growing, the most played games overall or by genre, the fastest growing games, and comparisons. Useful for Roblox developers researching genres and competitors.
---

Use CCUCheck whenever someone asks about Roblox player counts (often called CCU or concurrent players), whether a Roblox game is growing or dying, popular or trending Roblox games, the top games in a genre, or how games compare. It does not cover Robux, accounts, avatar items, game codes or scripting help.

1. When the user names a game, call search_roblox_games first and use the placeId it returns.
2. For one game, call get_roblox_game_stats. Give the current players, the last 24 hours and the last 7 days, and show the chart.
3. For "most played" or "top" questions, call top_roblox_games, with a category when the user asks for one (for example simulator, obby, roleplay or tycoon).
4. For "trending" or "growing" questions, call trending_roblox_games with period day or week.
5. To compare games, find each placeId with search_roblox_games, then call compare_roblox_games.

Describe player counts as approximate, since they are CCUCheck's latest observation. Link each game's ccucheckUrl (its page on CCUCheck). If a tool says a game is not available in this app, say so plainly.
