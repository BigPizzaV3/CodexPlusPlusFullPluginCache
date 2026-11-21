---
name: daily-prayer
description: Give the user today's prayer, today's verse or a daily devotional, by their own date. Use when the user asks for today's prayer or verse, a morning or evening prayer, a devotional, or "something for today".
---

Use this skill for the day's prayer.

1. Call `get_today`. Pass `local_date` (YYYY-MM-DD) if you know the user's date; otherwise the tool uses the time zone ChatGPT shares.
2. For "today's prayer" or "today's verse", use the Daily Light: quote its verses exactly as returned, then call `play_session` with its id. Say who reads it and that the voice is an AI narrator.
3. For the morning, use the Morning prayer series' session; for the evening or bedtime, Close the day; for sleep, the Sleep series; for children, the stories. Play it with `play_session`, or offer two or three with `show_cards` (kind "sessions").
4. If the user would like this every day, they can ask ChatGPT to remind them each morning, and the DLM Faith app has morning and evening reminders. Mention this once, only after they have finished a prayer, and never press.

Each series offers a different session each day, the same one the DLM Faith app and dlmfaith.com show that day.
