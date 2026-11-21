---
name: semana-organizada
description: Give the user a clear view of their upcoming work and help organize it. Use when the user asks what they have today, tomorrow or this week, wants to plan their week, or asks for tasks pending in their appointments.
---

1. Call `get_schedule` with the period (default: today plus 6 days) and always pass `today` (the user's local date).
2. Present the appointments grouped by day, in time order: time, client, place and what is planned. Mark recurring ones that are only projected ("previsto") — the app creates them closer to the date.
3. If the user wants to prepare a visit, call `list_open_tasks` or add a checklist with `add_job_tasks`.
4. To move an appointment, call `reschedule_job` WITHOUT `confirmation_id` first, show the preview (including other appointments that day) and only call it again with `confirmation_id` after the user explicitly agrees. Remind the user that the client is not notified automatically and offer to draft a message.
5. Never present projected occurrences as confirmed by the client.
