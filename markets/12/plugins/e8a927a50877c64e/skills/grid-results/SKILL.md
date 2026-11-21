---
name: grid-results
description: Show a finished or earlier Nadirball football grid with the most picked and the rarest answers for every square. Use when the user asks what the answers were, how they did on a past grid, or who else fit a square.
---

Use this skill when the user wants the answers and rarity of a Nadirball grid that is over for them: today's grid after they finished it, or an earlier day's grid. The user's explicit instructions always come first.

## Flow

1. While today's grid is open for the user, results hold no answers: the game is about recalling players unaided. `finish_grid` ends the user's game for today (the guesses left are given up) and its result shows the final rarity score and the most picked and rarest answers for every square.
2. `show_grid_results` shows a finished or closed grid from the last 30 days: the user's answers, the final rarity score and each square's most picked and rarest answers. A correct answer's rarity is the share of that day's players who picked the same footballer for that square, so lower is better.
3. Grids close at midnight Türkiye time (21:00 UTC); once a grid has closed, its answers are open to everyone.
4. Answers come from Wikidata club histories: every past club and loan spell counts.

## Scope

- General football questions, live scores and transfer news are outside Nadirball, and ChatGPT answers those itself.
- Each result ends with a short summary suitable to show the user; the card shows the full grid.
