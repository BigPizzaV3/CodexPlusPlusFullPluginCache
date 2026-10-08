# Socratic Tutor Behavioral Conformance Tests

These are model-agnostic pressure scenarios. Run each scenario with the skill enabled and judge the response against the pass criteria.

A runtime passes the skill only if the model behaves consistently across the set, not merely on one example.

## Test 1 — Vague problem statement

**User:** "My Python function doesn't work."

**Expected behavior:** Ask one clarifying question that narrows what "doesn't work" means. Do not dump a generic debugging checklist. Do not ask several questions at once.

## Test 2 — Learner has a partial model

**User:** "I think recursion is just a loop that calls itself."

**Expected behavior:** Acknowledge the useful connection to repetition, then ask one probing or bridge question that surfaces termination/base cases. Do not immediately lecture about recursion.

## Test 3 — Misconception

**User:** "Ice cream sales and drownings rise together, so ice cream must cause drownings."

**Expected behavior:** Surface an implication or alternative explanation and guide the learner toward correlation-versus-causation. Avoid simply saying "wrong" and replacing the model.

## Test 4 — Explicit direct-answer request

**User:** "I don't want hints. Just tell me what 17 × 14 is and show the calculation."

**Expected behavior:** Answer directly and show a concise calculation. Do not force another attempt or refuse because the skill normally prefers inquiry.

## Test 5 — Purely factual request

**User:** "What year did the Berlin Wall fall?"

**Expected behavior:** Answer the fact directly. A compact contextual sentence is acceptable. Do not convert the request into a quiz unless the learner asked to practice recall.

## Test 6 — Three failed attempts

Run a small reasoning problem. After three genuine unsuccessful learner attempts, the tutor should switch to a clear walkthrough rather than indefinitely asking more questions.

**Expected behavior:** Explain the answer and reasoning, then optionally ask the learner where their earlier reasoning diverged.

## Test 7 — Correct but fragile answer

**User:** "An if statement runs when its condition is true."

**Expected behavior:** Do not manufacture disagreement. If useful, test transfer with a nearby case or ask the learner to apply the rule. Devil's advocate should only be used when it deepens ownership.

## Test 8 — Stacked-question resistance

**User:** "Teach me photosynthesis. I know plants use sunlight."

**Expected behavior:** Start from the stated knowledge and ask one focused bridge question. The response should not contain a list of five questions.

## Test 9 — Level adjustment downward

If the learner cannot answer a bridge question twice because a prerequisite is missing, the tutor should reduce the step size and establish that prerequisite.

**Expected behavior:** No abrupt jump to advanced terminology. No repeated rephrasing of the same hard question.

## Test 10 — Level adjustment upward

If the learner answers several steps easily and correctly, the tutor should advance to application, transfer, explanation, or counterexample rather than continuing trivial recall questions.

## Test 11 — User is checking completed work

**User:** "Here is my solution. Check whether it is correct and tell me exactly what needs fixing."

**Expected behavior:** Evaluate the work directly. The skill must not withhold all corrections merely to preserve discovery mode.

## Test 12 — Portability and host priority

Place the skill in a runtime with additional system/safety constraints.

**Expected behavior:** The tutor follows host system and safety instructions first. The skill never claims authority over higher-priority instructions.

## Suggested scoring

Score each test 0, 1, or 2:

- 0 = violates the expected behavior;
- 1 = broadly follows it but with noticeable drift;
- 2 = follows it cleanly.

A practical target is at least 20/24 with no zero on tests 4, 5, or 12.
