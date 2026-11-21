---
name: test-readiness
description: Use when the user asks whether they are ready for their permit test, how they are doing, or wants to retake the questions they missed ('how am I doing?', 'am I ready for the Florida permit test?', 'retake my missed questions'). Shows progress by state and drills the misses.
---

Passlane keeps each user's practice tests under ChatGPT's anonymous user ID, by state. The user's explicit instructions come first.

## Flow

1. get_my_progress shows progress by state: scores, the weakest topics and a readiness line. Ready means the last two mock tests were passed.
2. get_test_results returns the missed questions of a finished test, each with the right answer, Passlane's explanation and the handbook section and page.
3. start_practice_test with mode missed retakes only the questions the user got wrong before, until they stick; finish_test grades the retake.
4. delete_my_progress deletes the user's tests and progress when they ask.

## Scope

- Readiness is about Passlane's practice tests; it says nothing about passing the real test, which only the state agency gives.
- Five states: California, Texas, Florida, New York and Pennsylvania.
