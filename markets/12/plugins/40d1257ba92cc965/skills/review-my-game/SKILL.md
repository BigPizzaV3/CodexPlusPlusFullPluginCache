---
name: review-my-game
description: Answer a golfer's questions about their own game from their AVA Golf data - where they lose strokes, club distances and gaps, recent rounds, trends, handicap history and what to practice next.
---

Use the AVA Golf tools to answer questions about the signed-in golfer's own game. Every tool only reads, and only that golfer's account.

1. For a broad question ("how's my game?", "what should I work on?"), start with `get_player_summary` for the handicap, recent activity, strongest and weakest trend, and top priorities.
2. Then use the tool that matches the question:
   - Where strokes are lost: `get_performance_map` (last 5, 10 or 20 rounds).
   - Club distances and gaps: `get_bag`; the club list itself: `list_clubs`.
   - A specific round or practice session: `list_activities`, then `get_round` or `get_practice_session`.
   - Shot statistics no chart covers (e.g. wedges from a distance band): `query_shots`.
   - Better or worse lately: `get_trends`, and `get_trend_chart` for one chart.
   - What to practice: `get_top_priorities`, then `get_issue` for the evidence behind one priority.
   - Handicap Index® over time: `get_handicap_history`. Swing tendencies: `get_swing_profile`.
3. Quote the numbers the tools return, with the window or sample size they cover. Strokes gained is measured against the baseline the tool reports; negative means strokes lost.
4. Don't invent data. If a tool returns little or nothing, say so and suggest recording more rounds or practice in AVA Golf.
5. The connection can't change anything in AVA Golf and can't read another golfer's data. If asked to edit, book or delete something, say it isn't possible through AVA Golf.
6. If a tool says a permission is missing, the membership isn't active, or the rate limit was reached, pass that message on plainly.
