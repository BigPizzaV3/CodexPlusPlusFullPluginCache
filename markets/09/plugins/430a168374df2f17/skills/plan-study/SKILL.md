---
name: plan-study
description: Plan the reader's study days in Laya, apply a plan when the reader agrees, add, move, time, tick or remove plan entries, and review how the days and weeks went with Laya's own figures. Use when the reader asks what to study, to plan a day or a week, to change a planned item, for their planning preferences, or for a weekly recap, a table of their plan or a chart of their progress.
---

# Plan study days and review them

For a today or home overview, call `get_my_laya` without an id and report the existing plan for today and tomorrow, due revision, the three suggested questions with Laya's reasons, this week beside last week, the streak, grading availability, booklet availability and the returned next steps. Keep the sections concise. State when a section is empty or unavailable rather than omitting it or inventing figures. Do not call `propose_plan` for this overview.

1. Read the plan with `get_my_laya`. Without an id it gives today and tomorrow. The id `plan:<date>` gives one day, and `plan:<date>:<days>` gives up to 14 days from that date. The id `plan_preferences` gives the planning preferences. Use the dates Laya gives, whose day starts at midnight in India.
2. Only when the reader explicitly asks to create or replace a schedule, call `propose_plan` once. A question about what to do today is an overview request, not permission to propose a replacement. Show the dates, the minutes, each item with Laya's own reason and anything left out. When the reader wants a different preference, show the change and set it with `set_plan_prefs` after a yes.
3. On a plain yes, call `apply_plan` with the proposal's digest and range and a fresh `idempotency_key`. `undo_plan` reverses an apply within 24 hours, after a yes.
4. To place things yourself, call `add_to_plan` once with up to 30 entries. Each entry names an answer, a set, a deck, a Zubani check of an answer or a chapter of one of the reader's books by its id, with a day, or with a Monday to pin it for that week. Give minutes only when the reader gives them. Show the entries with their days first and wait for a yes.
5. To move an entry, change its minutes or tick it, call `update_plan_entry` after a yes, with any of the three together. A tick marks the entry done and records no revision. `remove_plan_entry` takes an entry off the plan and keeps what it pointed to.
6. End with the plan's link from the result.

For a weekly recap, call `get_my_laya` with `week:last`, or `week:<Monday>` for another week. For study over time use `series:7`, `series:30`, `series:90` or `series:365`, for a summary `summary:30` or `record:30`, for one day `day:<date>`, and for coverage `coverage:gs`, `map` or `weak:gs`. Read the next page when a report gives one. Give every figure with its unit as Laya returns it. Draw a chart or a table only from the rows Laya returns, and read again when the reader asks for fresh figures.

Reading from the reader's own books follows the books skill. Prelims practice stays in its own exercises, apart from the plan. Use Laya's own schedules, reasons and numbers, and quote its reasons as given. The reader's own explicit instructions always outrank these steps.

Buniyaad is a PDF booklet collection. Plan its copied book chapters through add_to_plan. Do not recommend legacy Buniyaad lectures or enable include_buniyaad. Historical lecture entries may be omitted from the connector view without changing saved records. Use the returned entries and totals.
