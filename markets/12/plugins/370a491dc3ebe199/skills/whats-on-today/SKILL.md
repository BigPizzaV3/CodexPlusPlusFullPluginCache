---
name: whats-on-today
description: Tell the user what's on for their family today or this week, from their FamilyWell tasks, shopping, calendar, birthdays and cars.
---

When the user asks what's on, what's due, or what they have today, call the FamilyWell `get_today` tool. For a specific day or range ("this weekend", "next week"), call `calendar_list_entries` with that date range instead.

Answer in a short list grouped as due now and later this week, using each item's title and due date. Mention overdue items first. If the client shows the Today widget, keep the text to one or two sentences and let the widget carry the list.

If a module the user asks about is missing, it is either turned off for the family or this connection was not allowed to read it: say so and suggest reconnecting FamilyWell to add it. Do not show ids or JSON.
