---
name: describe-the-word
description: Play today's Unsaid word. Use when the user wants a word game where they describe a word without saying it and ChatGPT guesses, in Turkish or English.
---

Use this skill when the user wants to play Unsaid: a daily describe-the-word game (anlatma oyunu in Turkish) where the user sees a secret word and its five forbidden words in the Unsaid card, gives clues, and ChatGPT guesses. The user's explicit instructions always come first.

## Flow

1. `start_game` opens today's word in the user's language (`tr` or `en`), the same word for every player that day, or a practice word with `mode: practice`. Calling it again returns the game in progress.
2. The secret word and its forbidden words appear to the user in the card and are in no tool result until the game is over, so ChatGPT's guesses are real guesses.
3. Each clue the user gives, typed in the chat or posted from the card as "Unsaid clue N: …", goes to `guess_word` as the user wrote it, with one guess at the word. A clue with a forbidden word in any form is void and still uses up one of the 5 clues; a clue that contains the secret word ends the game.
4. `get_game` shows where the game stands, and `give_up` ends it and reveals the word when the user gives up.
5. `get_stats` shows the user's streak and record, and `delete_my_data` deletes their Unsaid data when they ask for it.

## Scope

- One shared daily word per language, plus practice words. Other word games, word definitions and rhymes are outside Unsaid, and ChatGPT handles those itself.
- Each result ends with a short summary suitable to show the user; the card shows the full game.
