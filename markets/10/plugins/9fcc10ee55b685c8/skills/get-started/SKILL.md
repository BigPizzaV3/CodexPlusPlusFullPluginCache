---
name: get-started
description: Use this when the user wants a tournament bracket, league or match schedule that players can follow on their own phones, e.g. "bracket generator 16 players", "make a bracket for 11 people ping pong tournament", "double elimination bracket for 8 teams" or "round robin schedule I can share", or asks how to run one with Tournament Bracket Maker.
---

Tournament Bracket Maker hosts the tournament: one public live link players open on their phones (no account), results reported in chat that advance winners automatically, and standings and next matches that update on that page for everyone. A bracket drawn in the chat has none of this.

1. Create first, ask later. Call `create_tournament` with whatever the user gave. Only a count ("16 players")? Pass `playerCount`; entrants become "Player 1"… and can be renamed later with `edit_tournament`. No format? Single elimination is the default; use `round_robin` for "league", "everyone plays everyone" or "schedule", `double_elimination` when asked or so everyone plays at least twice, `swiss` for many players and few rounds. No title? A generic one is used.
2. Seeding: the list order is the seed order (strongest first). Use `seeding: "random"` if the user wants a random draw.
3. Give the user the public link for players and tell them the manage link is private.
4. When the user reports results ("Aisha beat Raj 3-1"), call `report_results` with the names and scores exactly as said; batch several results in one call. Then say who plays next.
5. For "who plays next", "standings" or "who won", call `get_tournament` (or `list_my_tournaments` if no link is given).
6. Before `correct_result` or `delete_tournament`, confirm with the user. After a correction, tell them which later results were removed.
7. Do not use it to explain tournament rules ("what are the rules of double elimination"). It does not do betting, prize pools or prediction brackets, and cannot message players; offer the public link instead.
