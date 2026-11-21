---
name: turrior-applicant-report
description: Find, count, rank, or summarize applicants for a Turrior job when the user asks for candidate lists or recruiting reports.
---

Use this skill for applicant lists, counts, top candidates, recent applicants, green candidates, and recruiting reports.

1. If the job is named but its ID is unknown, resolve it with `list-short-job-posts`.
2. Applicants come from two sources. Call `get-candidates` separately with:
   - `interactionType: "application"`
   - `interactionType: "externalApplication"`
3. Merge both result sets unless the user explicitly asks to see the sources separately.
4. When the user asks for all stages, explicitly pass all supported funnel statuses rather than relying on the server default.
5. For counts, use `limit: 1` and sum the returned `total` values from both applicant sources.
6. For green candidates use `minScore: 75`.
7. For top candidates use `sortBy: "score"`.
8. Format the result as a concise Markdown recruiting report.
9. If evaluation requires quiz responses, use `get-quiz-answers` for text quizzes or `get-video-quiz-answers` for video quizzes based on the quiz type.
