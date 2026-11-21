---
name: attendance-reporting
description: Analyze Swoogo session check-ins, attendance rates, and no-show patterns for an event. Use for attendance comparisons and post-event reporting; not for recording check-ins, changing attendance, or assuming registration counts equal attendance.
---

# Report session attendance

Read [the shared workflow rules](../../references/workflow-rules.md).

1. Resolve the event and requested sessions. Read event dates/timezone and sessions with `swoogo_get_events` and `swoogo_get_sessions`, using `session_id` for detail or `event_id` for a paginated list.
2. Call `swoogo_session_attendance_stats` with `event_id` and optional `session_id`. It automatically reads at most 1000 attendance records. Report any `_warning`; a session filter may still hit the cap.
3. Map session IDs to names. Report total attendance records, checked-in records, and returned rates. The tool's `registered` value counts attendance records, and its rate is checked-in records divided by those records. It is not a denominator of all event registrations, session capacity, or unique attendees.
4. For a complete result beyond the cap, paginate `swoogo_get_session_attendance` with the event and optional session filter until complete, requesting only fields needed for the calculation. Recompute rates from complete records and show the denominator. If full data is unavailable, retain a clear partial label rather than extrapolating.
5. For session fill or registration-to-attendance comparisons, separately fetch session registration counts using `swoogo_get_sessions` with `expand: registrantCount`. For event registration totals use `swoogo_registrations_get`. Label each measure and do not mix their denominators. Deduplicate by returned registrant IDs only if the user requests unique attendees and the full relevant dataset is available.
6. A missing check-in is not evidence of a real no-show for a future or ongoing session. Use event timezone and session end times to distinguish pending check-ins from post-session unchecked records. Do not infer missing duration, checkout time, or reasons for absence.

Deliver a session comparison with checked-in counts, denominators, rates, and completeness. State the reporting time and event timezone. Offer operational observations supported by the data, without changing check-ins or emailing attendees. If the user separately requests attendance writes, use the appropriate live tools within that authorization rather than treating the report as permission.
