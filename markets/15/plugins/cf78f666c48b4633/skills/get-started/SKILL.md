---
name: get-started
description: First steps with Scorekin after installing it. Use when the user sets up Scorekin or asks how to start tracking their board games.
---

# Get started with Scorekin

Help the user put their games into Scorekin. Keep it short and let them pick one path.

1. Ask whether they already track their games on BoardGameGeek.
   - If yes, ask for their BGG username and call `import_from_bgg`. Tell them how many games and plays were imported, then call `show_collection`.
   - If no, ask them to name a few games they own and add each with `add_to_collection` (status `own`). Then call `show_collection`.
2. Offer to log their most recent game night: "Tell me what you played and the scores, for example: We played Azul, I scored 72, Anna 65." Use `log_play` for each play they describe.
3. Mention what they can ask next, in one sentence: stats ("show my stats this year"), a game's history ("how do I do at Azul?") and suggestions ("what should four of us play in an hour?").

Do not ask for anything except game names, play details and, if they choose the import, their BGG username.
