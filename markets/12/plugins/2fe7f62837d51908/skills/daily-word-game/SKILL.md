---
name: daily-word-game
description: Play today's Sonarlex word puzzle. Use when the user wants a daily word game, a guess-the-secret-word puzzle or a hot-and-cold word game, in English or Turkish.
---

Use this skill when the user wants to play today's Sonarlex puzzle: a daily word game (kelime tahmin oyunu in Turkish) where the user guesses a secret word and each guess gets a number for how close its meaning is, hot-and-cold style. The user's explicit instructions always come first.

## Flow

1. `show_puzzle` opens today's puzzle in a card, in the user's ChatGPT language: English or Turkish, or the one `language` names. `practice: true` opens the practice puzzle, whose word is the same every day. Everyone playing a language gets the same word each day.
2. The secret word stays on Sonarlex's server and is in no result while the puzzle is open, so a word's rank is known once `guess_words` has ranked it.
3. When the user offers words, `guess_words` takes up to 5 single words with the puzzle number and language from the board. #1 is the secret word, and a lower number is closer. A call with at least one new word uses one turn; words already tried, unknown words and very common words cost nothing. `proposed_by: assistant` marks words the assistant suggested when the user plays them.
4. `get_hint` shows a word about halfway between the user's best word and the secret word, no closer than #10, for one turn. There are 3 hints a puzzle.
5. `reveal_word` ends the puzzle when the user gives up and shows the word and its closest words.
6. `get_my_stats` shows the user's streak and record, and `reset_my_stats` deletes their Sonarlex data when they ask for it.

## Scope

- One shared daily puzzle per language, plus the practice puzzle. Other word games, word definitions and crossword clues are outside Sonarlex, and ChatGPT handles those itself.
- Each result ends with a short summary suitable to show the user; the card shows the full board.
