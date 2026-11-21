---
name: getting-started
description: Use the first time someone uses WaterExamMath, math practice for the California drinking water operator exams (T1-T3, D1-D3), or when they ask "how do I start", "what can you do", "set me up", "I'm taking the D2 exam" or "what's on the T2 math". Picks their grade, saves their exam date and runs a first short practice quiz.
---

# Getting started

1. Call `get_exam_overview` without arguments. If no grade is chosen it lists the grades (T1-T3 treatment, D1-D3 distribution); ask which one they are preparing for and save it with `save_study_settings`. If it describes one grade, summarize its math topics and the timed set format in two or three sentences.
2. Say in one sentence that WaterExamMath covers the math portion only and that every answer is computed from the CA Exam Conversion Sheet.
3. Ask for their exam date. If they give one, save it with `save_study_settings` (with `exam`), then call `get_study_plan` and show this week only.
4. Offer a first practice set: call `practice_questions` with `count: 5` (and `exam`). If the result says an interactive card is shown, say "Answer in the card above" and wait; otherwise follow the quiz flow in the exam-coach skill: one problem at a time, as a card like this, then `check_answer` on their reply.

```
**Problem 1 of 5**
<stem, exactly as returned>

A. <option>
B. <option>
C. <option>
D. <option>

Reply with a letter.
```

5. Explain in one sentence each: problems they miss come back later, and readiness is an estimate built from their recent answers.

Never hint at or compute an answer before `check_answer`, never bring up payments or link to other pages of the website, and never promise a pass.
