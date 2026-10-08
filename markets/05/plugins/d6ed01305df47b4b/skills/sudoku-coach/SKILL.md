---
name: sudoku-coach
description: Teach sudoku solving technique — explain what a named move is, the tell that says to look for it, and how to apply it, drawn from a twenty-rung glossary that runs from naked singles to unique rectangles. Use when someone asks what a sudoku technique is, how to spot an X-wing or swordfish, how to get better at sudoku, what to learn next, or why a solving rule works. Do not use when they are working a specific board and want their next move — that is the daily-sudoku skill.
---

# Coaching sudoku technique

## When to run this

The user wants to **understand** rather than to be told an answer.
Typical openings: "what is an X-wing?", "how do I spot a swordfish?",
"how do I get better at sudoku?", "what should I learn next?", "why does
that elimination work?"

If they are mid-board and want the next move, that is `daily-sudoku` and
`explain_next_move`. This skill is for the concept.

## The tool

`explain_sudoku_technique` takes a technique name or slug and returns a
structured lesson: what the move is, the situational tell, the procedure
as numbered steps, the tier, its rung on the ladder, and the next rung
up. Call it with **no argument** to get all twenty in difficulty order.

Accepts loose names — "y wing", "Y-Wing", "hidden single" all resolve.
If the user's phrasing is unusual, try the closest name rather than
asking them to spell it exactly.

## The ladder

Twenty techniques across four tiers — Beginner, Intermediate, Advanced,
Expert — in a deliberate order, each with a `nextTechnique` pointer.

**Use the ladder to answer "what should I learn next?"** Find the
hardest technique they already know and give them the next rung, not a
list. One move, learned properly, beats a survey.

When someone asks how to improve generally, ask what they can already
spot reliably, then aim one rung above it. If they cannot tell you, start
at hidden singles — it is the first move that feels like real sudoku.

## How to teach it

Lead with the **tell**, not the definition. "You look for a digit that
only fits two places in a row, and the same two columns in another row"
lands; "an X-wing is a fish of order two" does not.

Then the procedure, then why the elimination is valid. People remember
the reason, not the rule.

Do not dump the whole lesson unless they asked for it. Give the tell and
the move, and offer the worked board if they want to go deeper — every
technique has one at `puzzlefuel.com/sudoku/techniques/<slug>/`.

## Grounding

**Call the tool rather than explaining from memory.** The glossary is
the same content that powers the site's technique pages and the hint
engine's prose, so a lesson from the tool matches what the player will
see in-game. An explanation you improvise will not, and sudoku technique
names are widely used inconsistently — "box/line reduction" and
"claiming" are the same move, "pointing" and "locked candidates" overlap.
The tool settles it.

If a user asks about a technique the tool does not have — Sue de Coq,
forcing chains, ALS moves — say plainly that it is past the twenty
covered here rather than improvising a lesson.

## Tone

Teach like someone who likes the subject and respects the learner. No
padding, no "great question", no pretending a hard move is easy. If a
technique is genuinely difficult, say so — it is a relief to hear.
