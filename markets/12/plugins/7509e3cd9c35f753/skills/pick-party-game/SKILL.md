---
name: pick-party-game
description: Plan a game night or suggest PadConsole games for a group at home or in different homes, by player count, occasion, mood or theme, and explain how to start playing with phones as controllers.
---

Use this when someone wants games or things to do together at home ("we are 4 friends at home, what can we do?", "what can 2 people play?", "6 friends, how do we have fun at home?"): game night, house party, birthday, family evening, kids, a couple, an office or team event, Christmas, New Year's Eve or another holiday gathering, friends in different cities, or games on the TV without a console.

1. Find the number of players. If it is missing, ask once. Groups larger than 12 still work: the tools suggest the biggest games and teams that share a phone.
2. Pick the tool:
   - Planning an evening or event (occasion or time given) -> `plan_game_night` with `players`, and `occasion`, `minutes`, `kids`, `remote` when known. Christmas, New Year's Eve and other holiday gatherings use `occasion: holiday`.
   - "What can we play?" with a group size and maybe a mood -> `recommend_games` with `players` and `vibe` (party, competitive, co-op, trivia, camera); `remote: true` if players are in different homes.
   - A theme or keyword (football, horror, quiz, racing, bluffing, dance) -> `search_games` with `query` and, if known, `players`.
3. Always pass `locale` matching the user's language (tr, en, de, es, id, pt, ru, ar) and answer in that language.
4. Present the result briefly; the cards show the details. Add one line on how to start (open padconsole.com on the TV or computer, everyone scans the QR code with their phone).
5. Use `get_game_details` for one game, and `explain_how_it_works` for setup (`topic`: start, remote, devices).

Only recommend games the tools return. Do not invent games, prices or features.
