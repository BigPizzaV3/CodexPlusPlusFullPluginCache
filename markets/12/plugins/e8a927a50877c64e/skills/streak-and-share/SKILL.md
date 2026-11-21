---
name: streak-and-share
description: Show the user's Nadirball streak and scores, and make a share link of today's football grid that spoils nothing. Use when the user asks about their streak or record, or wants to share their grid with friends.
---

Use this skill when the user wants to see how they are doing over time or to challenge friends with their result. The user's explicit instructions always come first.

## Flow

1. `get_my_stats` returns days played, the current and best streak, perfect grids, the best and average rarity score and the last 7 grids.
2. `create_share_link` creates, or returns the existing, public link to a page with the user's grid as coloured squares and the rarity score. While the grid is open the page names no players, so it spoils nothing; once the grid closes, names show.
3. Friends who open the link can play the same grid in ChatGPT the same day and compare rarity scores: lower is better.

## Scope

- A link holds only the board: no name, email or chat of the user's.
- `delete_my_data` deletes the user's boards, streak and share links when they ask for it.
- Each result ends with a short summary suitable to show the user.
