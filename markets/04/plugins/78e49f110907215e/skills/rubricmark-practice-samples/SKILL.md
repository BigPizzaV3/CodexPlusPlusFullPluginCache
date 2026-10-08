---
name: rubricmark-practice-samples
description: Give sample questions, school guides, score-estimator links, writing comments, or flashcards when the learner asks for practice, schools, scores, essays, or study cards. Do not collect payment or run the full timed paper in chat.
---

# RubricMark practice samples

Use this skill when the learner asks for a practice test, mock, past paper, named exam sit, school/university profile, admission score check, writing comment, or flashcards.

## Practice test

1. Call `search_practice_tests` with `query` as their original words. Also set `exam`, `skill`, `focus`, `level`, and `difficulty` from that wording.
2. Present the three `freeQuestions`. Do not invent items or reveal answers.
3. Wait for A, B, C, or D. Call `check_free_sample` with the same fields and `answers`.
4. Show each verdict. Send `signupUrl` and `sitUrl`. Do not ask a fourth question.

## Which exams

If they ask which papers exist (without a specific sit), call `list_supported_exams` and list named exams with sit URLs. Do not invent papers.

## School Guide

Call `search_schools` with `query` (and `type` / `country` / `state` when clear). Summarise from `entries` only. Send `guideUrl` / `browseUrl`. Do not invent cutoffs or ranks.

## Score estimator

Call `open_score_estimator` with `testType` and `score`. Send `estimatorUrl`. Do not invent Likely / Target / Reach buckets in chat.

## Writing

Call `preview_writing_feedback` with the draft. Show the sample comment. Do not invent a band score. Send `signupUrl`.

## Flashcards

Write 8–12 retrieve-first cards in this turn. Call `generate_flashcards` with `topic`, `title`, and `cards`. Do not list answers in chat. Send `signupUrl`.

## Do not

- Collect payment or open checkout in chat.
- Run the full timed paper or paid marking pipeline.
- Invent exam items, cutoffs, score buckets, or a fourth sample question.
