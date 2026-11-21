---
name: puzzel-activities
description: Create, find, edit, copy, share, embed, or run interactive Puzzel.org puzzles, quizzes, games, and classroom exercises. Use whenever the user wants a hosted learning activity or refers to an activity in their Puzzel.org account.
---

# Puzzel.org activities

Use the Puzzel MCP tools for hosted activities that the user can play, edit, print, embed, or run with a class.

## Choose an activity type

Choose the type that best matches the requested interaction. Make a sensible choice when the request is clear; ask only when different choices would materially change the result.

Available types include crosswords, word searches, acrostics, word scrambles, hangman, Wordle-style games, match-ups, jigsaws, typing practice, spinning wheels, memory, flash cards, sorting, ordering, quizzes, board games, cryptograms, calculation puzzles, sudoku, sliding puzzles, arrow crosswords, strands, fallen phrases, bingo, times tables, I Have Who Has, fill-in-the-gap exercises, sentence analysis, Name Them All, keypads, mazes, Jeopardy-style boards, logic puzzles, quartets, scavenger hunts, spatial reasoning, interactive videos, rebuses, A to Z quizzes, Guess Who boards, map quizzes, spelling tests, and advent calendars. The `type` parameter of `create_activity` is the complete, current list: every type it names is supported, so check it before telling the user a kind of activity is not available.

Before creating an activity, call `get_activity_type` for the chosen type unless its schema has already been returned in the current conversation. Follow the returned content shape exactly. Write polished, age-appropriate content in the language the user is using unless they request another language.

For image-based jigsaws or sliding puzzles, use an image the user supplied or explicitly asked to generate. Do not attach an image to other activity types.

## Create and deliver

Call `create_activity` with a useful dashboard title, the selected type, the complete content object, and a two-letter language code. The user's request to create the activity authorizes this action; do not add a redundant confirmation.

After creation, always give the user:

- the play link, for participants;
- the edit link, for the owner.

Give the embed link when the user asks to place the activity on a website or learning platform.

## Find and change existing activities

Use `list_activities` with a title query or type filter to find a referenced activity. Prefer a narrow search and a short page. If multiple plausible matches remain and choosing the wrong one would matter, present the concise choices before changing anything. Do not fetch every page unless the user asks for a complete inventory.

Before changing an activity, call `get_activity`. Preserve everything the user did not ask to change, then send the complete revised content to `update_activity`, because updates replace the stored content. If the activity cannot be changed through the tool, give the user its edit link.

Use `copy_activity` when the user wants a variant while preserving the original.

## Run with a class

Use `open_join_pin` when the user wants a classroom code. Return both the PIN and the join link, and state how long the PIN remains valid when that information is available. Use `close_join_pin` when the user is finished and explicitly wants the code disabled.

## Boundaries

Puzzel tools do not expose student responses or results. Say so plainly if asked, and do not imply that activity analytics were inspected.

Keep answer keys or hidden solutions out of participant-facing prose unless the user asks to review them. When sharing an existing activity, use its play link rather than exposing its editable builder state.
