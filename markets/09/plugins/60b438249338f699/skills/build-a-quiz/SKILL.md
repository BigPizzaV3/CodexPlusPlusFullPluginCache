---
name: build-a-quiz
description: Build or edit a live RedMo quiz from a topic, notes, or a lesson plan, using the RedMo app. Use when someone asks for a quiz, a class review game, trivia for an event, or changes to a RedMo quiz.
---

# Build a RedMo quiz

RedMo quizzes are played live: the host shows each slide on a big screen and
the room answers on their phones against a timer. Write for that room.

## Before writing

1. Ask only what changes the quiz: who plays (age, level), how many
   questions, and the language. Assume sensible defaults for the rest.
2. Call `list_question_types` and trust it over anything you remember.

## Writing the questions

- Show the questions in the chat first, so they can be corrected while that
  is cheap. Then save.
- Mix types where the content suits them: a slider for a number, put in order
  for a sequence, pin on an image for a place on a map, a word cloud to open
  a lesson. Do not force variety where multiple choice is the honest fit.
- Keep question text short enough to read from the back of a room. Answers
  are a few words, not sentences.
- Exactly one clearly correct answer unless the type says otherwise, and do
  not always put it first.

## Saving

1. `create_quiz`, then `add_slides`. A new quiz is published by that step
   and can be hosted right away.
2. For pictures: `search_images`, show the results, let the person choose,
   then `add_image` and use the URL it returns.
3. Give the link the tool returned and say the quiz is in RedMo under
   My quizzes.

## Editing an existing quiz

- `get_quiz` first. Change one slide at a time with `update_slide`,
  `insert_slide`, `move_slide` or `remove_slide`, by id.
- Every write carries the version from your last read. If it is refused as
  stale, the person changed the quiz meanwhile: read it again and apply your
  change to what is there now. Never resend an old list.
- Edits to a published quiz go to a draft. Call `publish_quiz` only when the
  person asks.

## Out of scope

Say so plainly and point to redmo.xyz when asked to start or run a live game,
show players or scores, or delete a whole quiz. These are not available here.
