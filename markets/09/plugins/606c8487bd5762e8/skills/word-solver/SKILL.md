---
name: word-solver
description: Unscramble letters (with blank tiles and tile points), find words that fit a crossword-style pattern like C?T or _A_E_, and narrow down a 5-letter color-feedback guessing game with solve_anagram, solve_word_pattern and solve_word_guess.
---

# LetterLab Word Solver

All three tools look words up in the ENABLE English word list. Report words exactly as returned and never add words that are not in the results; models are unreliable at letter-level tasks, so do not "improve" the lists.

- `solve_anagram`: the user has a set of letters ("unscramble", "what words can I make from", "anagram of"). Pass `letters`; use `?` for each blank tile. Use `use_all_letters` for full anagrams, `length` for an exact length, `starts_with` / `ends_with` / `contains` for filters.
- `solve_word_pattern`: the user knows some letter positions ("crossword", "5 letters, second letter A", "words ending in ING"). Build `pattern` with `?` for each unknown letter and `*` for any run of letters (for example `?A?E?`, `S*ING`). Add `include_letters` / `exclude_letters` when given.
- `solve_word_guess`: the user plays a 5-letter guessing game with green/yellow/gray feedback. Convert each guess to `{word, feedback}` with one mark per letter: `G` green, `Y` yellow, `-` gray (colored squares also work). Keep repeated letters exactly as reported. Pass `hard_mode` if mentioned. With no guesses it suggests an opening word.

After a result, give the counts, the key words (full anagrams, top tile points, common matches, or the suggested next guess with its bits and words left), and say how many more there are. Tile points are face values without board bonuses.

Do not use these tools for word definitions, solving clues by meaning, today's answer of any game, or making a puzzle for others to play.
