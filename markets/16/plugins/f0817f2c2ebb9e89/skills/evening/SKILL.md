---
name: evening
description: Help the user wind down, pray before sleep, or fall asleep to scripture, and find Bible and Book of Mormon bedtime stories for children. Use when the user can't sleep, wants something calm for the night, an evening prayer, or a bedtime story for their kids.
---

Use this skill in the evening.

1. Can't sleep or wants something calm: call `search_sessions` with category "sleep" (readings to fall asleep to, and Close the day prayers). Play the best fit with `play_session`; one or two minutes is usually right.
2. Evening prayer: `get_today` gives today's Close the day prayer.
3. Children or a family: call `search_sessions` with category "stories" (Stories of Jesus, Old Testament stories, Book of Mormon stories). Offer two or three with `show_cards` (kind "sessions") so a child can choose.
4. Keep the reply short and quiet. Say who reads it and that the voice is an AI narrator. The user can lower the screen and listen.

If the user can't sleep because of something heavy, use the comfort skill instead.
