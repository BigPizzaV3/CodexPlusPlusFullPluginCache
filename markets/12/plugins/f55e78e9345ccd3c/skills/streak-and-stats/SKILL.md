---
name: streak-and-stats
description: "Show the user's Unsaid streak and record, or delete their Unsaid data. Use when the user asks about their Unsaid streak, wins, best streak or stats, or asks to delete what Unsaid keeps about them."
---

Use this skill when the user asks how they are doing at Unsaid, or wants their Unsaid data deleted. The user's explicit instructions always come first.

## Flow

1. `get_stats` returns games played and won, the current and best streak, and wins by number of clues, for Turkish and English.
2. The streak counts daily words solved on consecutive days; practice words leave it as it is.
3. `delete_my_data` deletes all the user's Unsaid games, clues and stats in both languages when the user asks for it; streaks start again from zero.

## Scope

- Unsaid has no account: games are kept under the anonymous ID ChatGPT shares.
- To compare with friends, the card gives a share text at the end of each game with a square per clue and the score, and without the word.
