# Platform submission draft

## Type
Skills only.

## Name
Personal Control Plane

## Category
Productivity

## Short description
One conversational entry point for tasks, knowledge, events, monitoring, mail, files, and team work.

## Long description
Personal Control Plane routes natural-language intentions to the appropriate connected system of record. It distinguishes durable knowledge, personal actions, fixed-time events, future-condition monitoring, shared team work, email operations, and files. It avoids duplicate state, performs compound workflows in semantic order, and retrieves prior state without requiring users to remember which app contains it.

## Starter prompts
1. "Remind me Monday to deal with this."
2. "Save the decision we just made and the reasons behind it."
3. "Schedule this appointment and add a preparation task if needed."
4. "What did we decide about this before?"
5. "Research this now, then turn the result into the next action."

## Positive test cases

### 1 — Personal task
Prompt: "I need to call the garage next Monday about my MOT."
Expected behavior: classify as DO; use an available task tool; do not create a Calendar event merely because a date exists.
Expected result: one actionable task with Monday due/reminder in the user's timezone.

### 2 — Fixed-time event
Prompt: "Dentist appointment Tuesday at 16:00. Put it on my calendar."
Expected behavior: classify as EVENT; create one calendar event.
Expected result: calendar event at the resolved local date/time; no duplicate task unless preparation is separately requested.

### 3 — Durable decision
Prompt: "Save that we decided to keep the WebView approach for MVP because it reduces implementation scope."
Expected behavior: classify as KNOW; write a concise decision record to an available knowledge system.
Expected result: durable record containing decision and rationale.

### 4 — Conditional monitoring
Prompt: "Let me know when the price drops below €2,000."
Expected behavior: classify as WATCH; create a supported condition watch rather than a static task.
Expected result: one future-condition monitoring workflow.

### 5 — Compound workflow
Prompt: "Research MOT options near me and remind me Monday to book the best one."
Expected behavior: perform current research, summarize useful choices, create a Monday action, avoid persisting unnecessary research noise.
Expected result: ranked current options plus one task/reminder; optional knowledge capture only if durable value is clear.

## Negative test cases

### 1 — Pure Q&A
Prompt: "Why do cars need MOT inspections?"
Expected behavior: answer normally; do not create persistent state.
Why: no execution or persistence intent.

### 2 — Vague aspiration
Prompt: "Maybe I should learn Spanish someday."
Expected behavior: discuss if useful; do not create task/habit automatically.
Why: no concrete commitment or next action.

### 3 — Backend unavailable
Prompt: "Save this decision" when no knowledge-writing tool is available.
Expected behavior: do not claim success and do not silently substitute an unrelated backend; explain that persistence could not be completed.
Why: prevents fake writes and source-of-truth drift.

## Release notes
Initial 0.1.0 submission. Adds semantic routing for persistent personal/work intentions, source-of-truth rules, de-duplication, compound workflows, retrieval routing, and quality gates.
