---
name: get-started
description: Use OxbridgeAI to practise TMUA and ESAT questions, get answers marked with worked solutions, and diagnose timing problems.
---

# OxbridgeAI TMUA and ESAT practice

Use this plugin when a student wants TMUA or ESAT practice, wants an answer marked, or describes a timed paper that went badly.

## Tools

- `get_tmua_question`: one original TMUA question by paper, topic words or difficulty band.
- `get_esat_question`: one original ESAT question by part (Maths 1, Maths 2, Physics, Chemistry, Biology), topic words or difficulty band.
- `check_answer`: marks the answer letter the student chose and returns the correct letter and the worked solution.
- `get_hint`: a hint for a TMUA question, or a general way in for ESAT.
- `diagnose_timing`: finds the main bottleneck in a timed paper and gives a skip rule and a 7-day plan.

## How to use them

1. Show the question exactly as returned, with its options and suggested time. Never reveal the answer when you show a question.
2. Wait for the student to choose a letter before calling `check_answer`. If they ask for the answer without trying, offer a hint first.
3. Only call `check_answer` or `get_hint` for a question this plugin has shown in the conversation.
4. For `diagnose_timing`, ask for the number of questions, how many were attempted, how many were right, how many were guesses and the minutes used before calling it. Do not guess these numbers.
5. This plugin does not cover personal statements, interviews or other exams. Say so instead of calling a tool.

The plugin has no sign-in and does not receive the student's name, email or ChatGPT account.
