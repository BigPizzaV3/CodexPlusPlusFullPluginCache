---
name: plan-my-day-and-week
description: Plan my day or week. Use when the user asks what their day or week looks like, what to focus on, or wants a morning brief or week-ahead view from Delegent right now.
---

# Plan my day / week

This is the on-demand version of the morning brief. To get it automatically, see `set-up-delegent`.

## Today

1. **Meetings**: calendar tool or `delegent_get_calendar` for today. For each client meeting, a short `prep-me`: objective, what changed, open actions, sources.
2. **Tasks**: `delegent_list_my_tasks` with `due_before` today. Overdue first, then due today, then assigned to the user.
3. **Follow-ups**: `delegent_find_follow_ups` for the last 7 days (see `follow-up-atron`).
4. **Delegent Inbox**: `delegent_list_inbox_items` for new assignments and questions.
5. **Focus**: the three things that matter most today, and why.

## This week (or on Mondays)

Add:
- The week's meetings, grouped by client, flagging which need prep.
- Deadlines this week (`delegent_list_my_tasks` with `due_before` Friday).
- Collisions: deadlines on heavy meeting days, and prep that needs to start today.

Keep it scannable: one block per meeting, then lists. Save nothing unless the user asks.

When using `delegent_get_calendar` for a Google account, set `include_google: true`; `include_outlook` retains its Outlook-only meaning. Treat partial or unavailable coverage as unchecked, not an empty calendar.
