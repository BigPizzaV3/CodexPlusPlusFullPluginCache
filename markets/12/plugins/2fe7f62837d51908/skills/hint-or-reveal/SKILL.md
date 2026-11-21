---
name: hint-or-reveal
description: "Give a Sonarlex hint, or reveal the word when the user gives up. Use when the user is stuck on today's Sonarlex word puzzle, asks for a hint or a nudge without spoiling the answer, or wants to see the secret word."
---

Use this skill when the user is stuck on a Sonarlex puzzle. The user's explicit instructions always come first.

## Flow

1. `show_puzzle` returns the puzzle in progress: the user's words so far, turns used and hints left.
2. `get_hint` shows one word closer than the user's best so far, about halfway to the secret word and no closer than #10. It uses one turn, and each puzzle has 3 hints. It takes the puzzle number and language from the board.
3. A word suggested by the assistant is another kind of nudge: when the user plays it, `guess_words` takes it with `proposed_by: assistant`, and the share squares mark that turn.
4. `reveal_word` ends the puzzle when the user explicitly gives up, and shows the secret word and its closest words. It counts as given up in the user's stats.

## Scope

- Hints come from Sonarlex's own ranking for this puzzle; the secret word stays on Sonarlex's server until the puzzle ends.
- Word definitions, crossword clues and other word games are outside Sonarlex, and ChatGPT handles those itself.
