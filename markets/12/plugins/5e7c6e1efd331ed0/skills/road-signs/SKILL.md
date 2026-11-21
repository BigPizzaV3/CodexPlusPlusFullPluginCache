---
name: road-signs
description: Use when the user wants to drill road signs for their permit test ('quiz me on road signs for the Texas permit test', 'what does this sign mean?'). Runs a road sign quiz with the federal sign images for California, Texas, Florida, New York or Pennsylvania.
---

Road signs are part of every state's permit test, and New York's test has 4 road-sign questions. Passlane drills them with the federal sign images. The user's explicit instructions come first.

## Flow

1. start_practice_test with mode signs opens a road sign quiz in the Passlane card for the user's state. Without a state the card shows a button for each state.
2. The user taps answers in the card and sees the right answer after each one. answer_question records an answer the user gives in chat (for example "question 3 is B") as given.
3. finish_test grades the quiz when the user is done: the score and the signs missed.
4. get_test_results shows each missed sign with the right answer and the handbook section and page that covers it.

## Scope

- Five states: California, Texas, Florida, New York and Pennsylvania. English only.
- Practice only; Passlane is not affiliated with any DMV or state agency.
