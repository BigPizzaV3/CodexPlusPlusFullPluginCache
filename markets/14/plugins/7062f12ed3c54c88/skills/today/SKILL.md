---
name: today
description: A daily brief from Notii, covering today's calendar, tasks due today or overdue, reminders and the daily note, plus help planning the day. Use when the user asks what's on today, to plan their day, for a standup summary, or what they have to do.
---

# Today in Notii

1. **Work out the user's date and time zone** from the conversation or the system. Ask only if you can't tell. "Today" is their local date (YYYY-MM-DD).
2. **Gather** (these don't depend on each other):
   - `get_calendar` with `from` and `to` both today: events from their calendars, dated tasks, board cards due, reminders and the daily note.
   - `list_tasks` with `due_before` today: open tasks that are overdue or due today.
   - `get_daily_note` for today with the time zone: its Tasks and Notes. Notii makes it from the template if it doesn't exist yet.
3. **Brief, short and scannable:**
   - **Schedule:** events in time order, with reminders in place.
   - **Must do:** overdue tasks (oldest first), then today's, grouped by note. Show about ten, then "and N more".
   - **Daily note:** open items not already listed, and anything noted there.
   - Link the daily note and the notes the tasks are in.
4. **Offer next steps:** tick tasks off (`complete_task`), add tasks to today (`add_task`), set a reminder (`set_reminder`) or block out the day in the daily note (`update_note` with `append_markdown`).
