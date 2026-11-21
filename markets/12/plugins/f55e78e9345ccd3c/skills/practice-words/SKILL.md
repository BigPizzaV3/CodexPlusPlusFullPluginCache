---
name: practice-words
description: "Play an Unsaid practice word in English or Turkish, any time. Use when the user wants another round after today's word, wants to try the describe-the-word game first, or asks for a practice word with forbidden words."
---

Use this skill when the user wants an Unsaid practice word: the same describe-the-word game as the daily word, outside the daily streak. The user's explicit instructions always come first.

## Flow

1. `start_game` with `mode: practice` opens a practice word in the user's language (`tr` or `en`). Everyone's first practice word in a language is the same one; after that each player gets new ones.
2. The secret word and its five forbidden words appear to the user in the Unsaid card and are in no tool result while the game runs, so ChatGPT's guesses are real guesses.
3. Each clue the user gives goes to `guess_word` as the user wrote it, with one guess at the word. A clue with a forbidden word in any form is void and still uses one of the 5 clues.
4. `get_game` shows the game so far, and `give_up` ends it and shows the word.

## Scope

- Practice words leave the daily streak and stats as they are.
- Word definitions, rhymes and other word games are outside Unsaid, and ChatGPT handles those itself.
