---
name: game-day
description: Set the lineup and game plan and play today's Kickhollow game day. Use when the user wants to call plays, set a run or pass game plan, or play and hear today's high school football game.
---

Use this skill when a Kickhollow coach wants to get ready for and play today's game: read the opponent, pick the starters, set the game plan and play the game day. The user's explicit instructions always come first.

## Flow

1. `get_program` (home view) shows the record, the next opponent and the opponent's scouting report: four letter grades for its run game, pass game, run defense and pass defense.
2. `set_depth_chart` picks the starters. With auto it starts the best-rated player at every position; a move names the player to start and, optionally, the player he replaces.
3. `set_game_plan` sets the plan for the next game: offense run_heavy, balanced or pass_heavy; defense stack_the_box (against the run), balanced or coverage (against the pass); aggression conservative, normal or aggressive; and optionally a feature player who gets more touches.
4. `play_game_day` has the engine play today's game from both teams' lineups and game plans. Its result holds the final score, the quarter scores, the key moments in order (quarter, clock, score) and the leaders, and says when the next game day opens. The narration of the game comes from those key moments; the score and the plays are the engine's.
5. A conference plays one game day per real day, opening at midnight in the conference's time zone. With friends in the conference, the game day kicks off once every coach has locked in, or at 7 PM. A second game on the same day is not possible; the result says when the next one opens.
6. After the 9th game day the next `play_game_day` call holds Signing Day: recruits pick their schools, seniors graduate and the next season begins.

## Scope

- The game is fictional: real teams, real games and practice plans for a real team are outside it, and ChatGPT answers those itself.
- Each result ends with a short summary suitable to show the user; the card shows the scoreboard, the key moments and the box score.
