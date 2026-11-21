---
name: football-dynasty
description: Coach a fictional high school American football program in Kickhollow. Use when the user wants a football coaching or dynasty game, to play today's game day, or to recruit.
---

Use this skill when the user wants to play Kickhollow: a text high school American football (gridiron, not soccer) coaching and dynasty game where they coach a fictional small-town program, alone or in an online dynasty league with friends. The user's explicit instructions always come first.

## Flow

1. `create_program` starts the user's program: one per ChatGPT user, a 36-player roster and a seat in an 8-school conference. A made-up town, a mascot and a friend's 6-letter conference code are optional. A user who already has a program gets it back unchanged.
2. `get_program` shows the program in the card: home (the record, the next game and the opponent's scouting report), roster, recruiting, standings, schedule, or a game's box score.
3. Recruiting runs on 10 recruiting hours a day. `scout_recruit` (2 hours) narrows the user's range for a prospect's rating, `call_recruit` (1 hour) raises his interest and tells what he cares about, `host_official_visit` (5 hours) raises it a lot, and `offer_scholarship` commits a scholarship that stays committed until Signing Day. Star ratings are a guess; a prospect's true rating stays hidden from the user and from the results until he signs.
4. `set_depth_chart` picks the starters (auto starts the best-rated player at every position), and `set_game_plan` sets the offense (run_heavy, balanced or pass_heavy), the defense and how aggressive to be for the next game.
5. `play_game_day` has the engine play today's game from both teams' lineups and game plans. Its result gives the final score, the key moments in order and when the next game day opens; the narration comes from those moments. One game day per real day per conference, opening at midnight in the conference's time zone; with friends, a game day kicks off once every coach has locked in, or at 7 PM. After 9 game days (7 conference games, semifinals or consolation games, placement finals), the next call holds Signing Day and the next season starts.

## Friends and scope

- Friends share a conference with its 6-letter code: a new coach starts with `create_program` and the code, and a coach who already has a program moves with `join_conference`.
- Every town, school, player and recruit is fictional. Real high school football, real recruits and practice plans for a real team are outside the game, and ChatGPT answers those itself.
- Each result ends with a short summary suitable to show the user; the card shows the full program.
- `delete_program` deletes the program and its data when the user asks for it.
