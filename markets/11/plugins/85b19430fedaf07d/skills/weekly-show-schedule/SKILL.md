---
name: weekly-show-schedule
description: Use when the user wants shows at set times, for example a show every Friday at 8 pm, instead of one playlist on a loop.
---

# Weekly Show Schedule

1. Confirm the time zone the user plans in.
2. Find a calendar stream with playout_list, or create one with playout_create_scheduled.
3. Call calendar_get before any change, and again whenever its result is no longer in front of you. Never write entries from memory.
4. Add each show with calendar_add_entry: the videos (ids and lengths from media_list), the start and end as instants in the calendar's time zone, and daysOfWeek for a repeating show.
5. Read the schedule back in the user's words ("every Friday 20:00 to 21:00, Madrid time").
6. Starting and stopping the stream around the shows by itself (lifecycle AUTO) needs the scheduling feature, which comes with the Channel plan and up; without it the user starts the stream by hand.

Change one show with calendar_update_entry, remove one with calendar_delete_entry. Shows that already aired are a read-only record.

Rules for every playout.video workflow:
- Read ids from the list tools (playout_list, playlist_list, media_list, channel_list). Never invent an id or reuse one from memory.
- Anything that starts, stops or changes a stream is visible to its audience. Say what will happen and let the user confirm before calling the tool.
- If a tool refuses, relay its reason in plain words. When a step needs a different plan, say which plan includes it and that plans are listed on playout.video. Do not quote prices and do not offer to upgrade or buy anything.
- The user's explicit instructions come before this skill's steps.
