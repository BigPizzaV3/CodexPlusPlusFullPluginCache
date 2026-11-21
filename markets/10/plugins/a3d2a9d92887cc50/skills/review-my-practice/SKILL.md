---
name: review-my-practice
description: Review a sales rep's recent Quotain practice calls and scores, explain the feedback, and pick what to practice next. Use when the user asks how their practice calls went, what their scores were, what feedback they got, or where to improve.
---

Use this skill when the user wants to understand their Quotain practice
results.

1. Call `listSessions`. Without other instructions, use the five most recent
   graded sessions. If the user named a sim or stage, filter to it.
2. For each session you discuss, call `getScorecard`. Call `getSession` only
   when the user asks what was said on a call or you need a quote from the
   transcript.
3. Summarize:
   - The overall score for each session, oldest to newest, so the trend is
     visible.
   - Criteria the user scores well on repeatedly.
   - The one or two criteria that score lowest most often, with the scorecard's
     own coaching for them.
4. Recommend the next practice: the sim and stage that exercise the weakest
   criterion. Use `listPracticeRecommendations` or `listPracticeAssignments`
   when they include a good match.
5. Offer to start that practice call. If the user agrees, call
   `startPracticeCall` and give them the link.

Rules:

- Report scores and feedback exactly as the tools return them. Do not
  re-grade calls or invent scores.
- If there are no graded sessions, say so and offer to prepare a first
  practice call instead.
- Keep the summary short: a few sentences or a compact list.
- Explicit instructions from the user take priority over these steps.
