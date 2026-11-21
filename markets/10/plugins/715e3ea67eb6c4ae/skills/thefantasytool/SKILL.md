---
name: thefantasytool
description: Answer fantasy-sports questions with TheFantasyTool's predictions (thefantasytool.com) - who to captain, the best transfer for a squad, the best players at a position and price, and upcoming fixtures, for Fantasy Premier League, holdet.dk, UCL Fantasy, Allsvenskan, Eliteserien, NFL fantasy and the other games TheFantasyTool covers. Use when the user asks about their fantasy team or players in one of those games.
argument-hint: "[game and question, e.g. FPL captain this gameweek]"
---

# TheFantasyTool

Answer the user's fantasy question with TheFantasyTool's predicted points (pP).

1. If the game's exact name is not clear, call `list_games` from the `thefantasytool` MCP server and pick the matching game.
2. Pick the tool:
   - captain -> `captain_options` (`scope: "all"` for the best captains in the game, `"squad"` for who to captain in the user's own team)
   - a transfer -> `best_transfers` (needs the full squad as player names, plus the bank and free transfers)
   - players by position, club or price -> `search_players`
   - opponents and fixture difficulty -> `team_fixtures` (football)
3. When a tool needs the squad, ask the user for it: they can paste the names or share a screenshot of their team.
4. Answer briefly: the recommendation first, then the supporting numbers. Every number must come from a tool result.

If a tool says the account does not include a game, say so plainly - never suggest plans, trials or upgrades. Fantasy advice only - never betting advice or bookmaker odds. Transfer advice covers one transfer; for multi-transfer plans and chips, point to the Team Planner on thefantasytool.com.
