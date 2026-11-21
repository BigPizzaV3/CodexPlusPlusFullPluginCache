---
name: football-grid
description: Play today's Nadirball football grid. Use when the user wants a football or soccer trivia grid or quiz, futbol grid'i, or to name players who played for two clubs.
---

Use this skill when the user wants to play today's Nadirball grid: a daily 3x3 football (soccer) trivia grid, also called football tic-tac-toe (in Turkish futbol grid'i or futbol XOX), where each square needs a player who played for both its row club and its column club, or for a club and a nation. The user's explicit instructions always come first.

## Flow

1. `show_daily_grid` opens today's grid in a card: three row headers and three column headers (clubs from the Süper Lig, Premier League and Bundesliga, sometimes a nation), the user's answers so far, guesses left and the rarity score. Everyone gets the same grid, and a new one starts at midnight Türkiye time (21:00 UTC).
2. The game is about recalling players unaided, so results for an open grid contain no answers, only the headers and the user's own picks.
3. When the user names a player for a square, `submit_answer` takes the row and column (1-3) and the name as the user gave it, and checks it against Wikidata club histories, where every past club and loan spell counts. An answer counts once `submit_answer` has checked it. Accents and Turkish letters are optional.
4. A correct answer scores the share of today's players who picked the same name for that square, so lower is better; an empty square counts 100. There are 9 guesses a day.
5. When the user is done, `finish_grid` ends today's game; its result lists each square's possible answers, most picked answers and rarest pick. `show_grid_results` shows them for a finished or closed grid.
6. `get_my_stats` shows the streak and recent scores, and `create_share_link` makes a link to the user's board that names no players while the grid is open.

## Scope

- Nadirball is one shared daily grid. General football questions, live scores and custom quizzes are outside it, and ChatGPT answers those itself.
- Each result ends with a short summary suitable to show the user; the card shows the full grid.
- `delete_my_data` deletes the user's boards, streak and share links when they ask for it.
