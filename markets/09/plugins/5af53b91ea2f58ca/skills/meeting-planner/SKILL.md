---
name: meeting-planner
description: Convert times between cities and time zones with exact daylight saving time handling (convert_time), and find meeting times for 2-8 places with working hours and .ics calendar files (find_meeting_time).
---

# Zovo Meeting Planner

Use `convert_time` for "what time is X in Y" questions (time zone converter, PST to EST, EST to IST, New York to London).
Use `find_meeting_time` to plan a meeting across time zones or to see a team's working-hour overlap.

1. Always pass explicit dates as YYYY-MM-DD (resolve "next Tuesday" yourself). Offsets depend on the date.
2. Places can be cities ("Bangalore", "Portland, Maine"), IANA zones ("Europe/Berlin"), US states, countries, UTC offsets ("UTC+5:30"), or abbreviations ("PST", "CET"). Prefer the city the user named over an abbreviation.
3. For `find_meeting_time`, list the organizer first (their dates define the range), keep ranges to 14 days or less, and pass `work_start`/`work_end` or per-person `work_days` when the user mentions them.
4. Report the result's `status_note`, `difference_note`, `dst_note`, and `notes` to the user: they explain skipped or repeated times, clock changes within 7 days, and ambiguous abbreviations (IST, CST, AST, BST).
5. For meetings, lead with slot 1 and each person's local time. Mention `start_window` (every start in it works for everyone) and `also_on` (other dates with the same local times). If `has_full_overlap` is false and `next_full_overlap` is present, tell the user that closest time that works for everyone, just after their dates.
6. Share the `.ics` link for the slot the user picks. To get a calendar file for a different start, call `find_meeting_time` again with `selected_start_utc`.

Do not use these tools for questions about the history or politics of time zones, writing emails, booking travel, or unit conversion. They do not read calendars, check availability, send invitations, or account for public holidays.
