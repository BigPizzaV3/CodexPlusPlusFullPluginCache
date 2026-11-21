---
name: permit-practice
description: Use when the user wants a DMV permit practice test or a few practice questions for California, Texas, Florida, New York or Pennsylvania ('give me a California DMV permit practice test'). Runs a mock permit test in the state's own format, graded on Passlane's server with every miss cited to the state handbook page.
---

Passlane gives permit practice tests for five states in each state's test format: California 46 questions and 38 to pass (36 and 30 at 18 and older), Texas 30 and 21, Florida 50 and 40, New York 20 and 14 (including 2 of the 4 road-sign questions), Pennsylvania 18 and 15. Questions are written by Passlane from each state's driver handbook. The user's explicit instructions always come first.

## Flow

1. start_practice_test opens a test in the Passlane card. mode exam (the default) is the full mock test with the state's question count, pass mark and a clock; short_set is 10 questions with the answer after each; signs is road sign questions with sign images; missed retakes what the user got wrong before. Without a state the card shows a button for each state.
2. The user taps answers in the card. answer_question records an answer the user gives in chat (for example "question 3 is B") exactly as given. While a test runs, results carry no answer key.
3. finish_test grades the test when the user says they are done: score, pass or fail against the state's pass mark, weakest topics and how many were missed.
4. get_test_results returns each missed question with the right answer, Passlane's explanation and the handbook section and page.
5. get_my_progress shows progress by state and a readiness line (ready means the last two mock tests were passed). delete_my_progress deletes everything when the user asks.

## Scope

- Five states only: California, Texas, Florida, New York and Pennsylvania. English only.
- Practice, not affiliated with any DMV: Passlane can't book or replace the real test, and it has no CDL or motorcycle tests.
- The clock is Passlane's own pace (one minute a question); no state publishes a time limit.
