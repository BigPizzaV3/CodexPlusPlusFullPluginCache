---
name: work-my-practice-queue
description: Show a sales rep what Quotain practice is assigned or recommended and help them start the most important one. Use when the user asks what practice is due, what they were assigned, or what they should practice today.
---

Use this skill when the user wants to know what to practice in Quotain.

1. Call `listPracticeAssignments` with scope `mine`.
2. If no assignments are open, call `listPracticeRecommendations`.
3. List open items in this order: overdue, then due soonest, then items with no
   due date. For each item, show the sim or drill name, the due date, and the
   status. Show at most five items.
4. Suggest the first item and ask whether to start it.
5. When the user picks an item that is a sim, call `startPracticeCall` with its
   `buyerId` and give them the link. For a drill, explain that drills start
   from Quotain and point them to the assignment there.

Rules:

- Managers who ask about their team's assignments can use scope `team`. Report
  only what the tool returns.
- Format due dates in the user's language and locale.
- Do not invent assignments, due dates, or scores.
- Explicit instructions from the user take priority over these steps.
