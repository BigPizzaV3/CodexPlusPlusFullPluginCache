---
name: streak-and-stats
description: "Show the user's Sonarlex streak, record and stats, or delete their Sonarlex data. Use when the user asks about their Sonarlex streak, best streak, puzzles solved or turns, or asks to reset their stats."
---

Use this skill when the user asks how they are doing at Sonarlex, or wants their Sonarlex data deleted. The user's explicit instructions always come first.

## Flow

1. `get_my_stats` returns puzzles played, solved and given up, the current and best streak, and average and best turns, for each language played. `language` narrows it to English or Turkish.
2. `reset_my_stats` permanently deletes all the user's puzzles, words, streaks and stats when the user asks for it.

## Scope

- Sonarlex has no account: puzzles are kept under the anonymous ID ChatGPT shares.
- To compare with friends, a finished puzzle has share squares, one row per turn, that keep the word secret.
