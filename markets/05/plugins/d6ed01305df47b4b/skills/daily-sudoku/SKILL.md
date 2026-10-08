---
name: daily-sudoku
description: Play a sudoku puzzle in the conversation — fetch today's daily edition or generate one at a chosen difficulty, then help the player through it with real solving logic. Use when someone wants to play sudoku, asks for today's or a new sudoku, or is working through a sudoku board and needs a hint, a check, or an explanation of why a move works. Do not use for crosswords, wordle-style games, word ladders or other puzzle types.
---

# Playing sudoku with Puzzle Fuel

## When to run this

The user wants to **play** a sudoku, or is **already playing one** and
needs help. Typical openings: "give me a sudoku", "today's puzzle",
"something harder", "I'm stuck", "is this right?", "why does that work?"

If they are asking about a technique in the abstract rather than working
a board, use the `sudoku-coach` skill instead.

## Choosing the tool

| Situation | Tool |
|---|---|
| Today's puzzle, the daily, "a sudoku" with no other qualifier | `get_daily_sudoku` |
| They already did today's, or want to practise a difficulty | `new_sudoku` |
| Stuck, wants a hint, asks what's next or why a move works | `explain_next_move` |
| Asks if their grid is right, or why it won't finish | `check_sudoku` |

Default to `get_daily_sudoku` when the request is ambiguous — the daily
is the point of the product, and it is a numbered edition they can keep
a streak on.

## Difficulty

Six tiers: `beginner`, `easy`, `medium`, `hard`, `expert`, `sadistic`.

**Always call the hardest tier "Diabolical" when speaking to the user.**
`sadistic` is the internal slug only; never show it.

If they do not name a difficulty, pass none and let it default to easy.
If they say "hard" loosely, take them at their word rather than
interrogating them.

## Board format

Boards cross the wire as **81 characters, row-major from r1c1**, digits
`1`–`9` for filled cells and `.` for blanks. Cells are named `r4c7`
(row 4, column 7).

`explain_next_move` and `check_sudoku` need **two** boards:

- `puzzle` — the ORIGINAL grid, only its givens filled in
- `board` — what the player has now, including their own entries

Keep the original puzzle string from whichever tool dealt it. If the
user pasted a grid themselves and you only have one board, pass the same
string for both; it will treat every filled cell as a given.

## Hints — the important rule

**Never invent a next move, and never work out the deduction yourself.**
Call `explain_next_move`. It runs a real solver across twenty named
human techniques and returns the step that genuinely follows. Your job
is to narrate what it returns, not to reproduce it.

Getting this wrong is the single worst failure mode available here: a
confidently wrong hint ruins a puzzle the player cannot then un-see.

When it returns, give the player the technique name and the reasoning in
your own words, and point at the cells. Offer the "why" before the
"what" if they seem to be learning; lead with the answer if they are
plainly just stuck and want to move on.

## Do not spoil the puzzle

**You cannot see the solution, and that is deliberate.** It is delivered
to the board component out of your view. Do not attempt to solve the
grid yourself to get ahead of the player, and do not reveal more of the
answer than the hint they asked for.

If a player asks outright for the full solution, give them the next move
instead and say you would rather walk them to it — then honour the
request if they insist. It is their puzzle.

## Tone

These are people relaxing. Be brief. One idea per message. Do not narrate
tool calls, do not recap the rules of sudoku unless asked, and do not
congratulate every digit. When they solve it, say so once and mean it.
