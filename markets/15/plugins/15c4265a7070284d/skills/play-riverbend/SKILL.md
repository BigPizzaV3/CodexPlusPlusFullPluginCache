---
name: play-riverbend
description: Play today's PuzzlePal RiverBend word puzzle with the user. Use when the user wants to play RiverBend, a daily word puzzle or a brain teaser, or asks about a RiverBend clue.
---

# Playing RiverBend

RiverBend is a daily word puzzle. The board is a grid of letters with a few clues; each answer is a path of
neighbouring letters, and together the paths fill the grid. The user plays on the interactive board by swiping.

1. Call `riverbend_today` to show today's board. Mention the clues if it helps, but never give an answer.
2. When the user asks for a hint, call `riverbend_hint` for that clue. Ask for one more letter each time they want
   another hint on the same clue.
3. When the user types a guess in the chat, call `riverbend_check`. Say only whether it is right; a right answer still
   has to be traced on the board.
4. Call `riverbend_reveal` only when the user asks for the answer or gives up on a clue.
5. The board tells you which clues are solved. When the user finishes, congratulate them briefly and offer to explain
   how the answers fit their clues.

Pass the `date` from `riverbend_today` to the other tools when the user is still on an earlier day's board.
