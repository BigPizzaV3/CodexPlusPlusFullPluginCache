---
name: team-followups
description: Check a team's follow-up discipline in IRM365. Use when a manager asks who in their team is behind, who has overdue follow-ups, how their agents are doing, or for a team activity summary.
---

# Team follow-ups

## Decide the period first

Use the period the user named. Otherwise use the **last 7 days**, ending now, in the user's timezone (from `get_workspace_context`). State the period in the answer.

## Fetch

1. Call `list_my_team`. If it returns an error because the person has no employee record, or the team is only themselves, explain that a team view needs a reporting line in IRM365, and offer their own follow-ups instead.
2. Call `list_followups` with `window: "overdue"` and page through every result.
3. Call `list_activities` with `status: "completed"`. Results come newest first. Keep paging while `has_more` is true **and** the last row's `completed_at` is still inside the period, up to 400 rows. Count only rows whose `completed_at` falls inside the period.

## Report

Group by team member, using `performed_by` and the lead owner:

| Team member | Overdue follow-ups | Oldest overdue | Completed in the period |
|---|---|---|---|

Under the table, name the two or three people with the most overdue work and their oldest items, by lead reference.

**Evidence rule:** say someone completed nothing in the period only if you read every completed activity back to the start of the period. If you stopped at the row limit first, say the counts are incomplete and how far back they reach, and don't call anyone inactive.

Keep it factual and neutral. This is for coaching, so describe the numbers and don't judge the person. If activity notes aren't shared, judge by counts and outcomes only, and don't claim what was said on a call.
