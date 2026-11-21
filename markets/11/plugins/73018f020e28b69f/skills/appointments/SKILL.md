---
name: appointments
description: Use when a user asks to inspect QualifyBase calendars, find availability, book, reschedule, or cancel a lead's appointment.
---

# Appointment workflow

Before the first workspace operation, use `get_account_info`. Confirm the intended lead, calendar, date, and timezone from context. Returned appointment and availability timestamps are UTC; display times in the user's confirmed timezone and include its name. Do not guess timezone from a phone number or language.

For availability, use `list_calendars` when the correct calendar is unclear and `check_availability` for the requested window. Offer a few suitable slots. Availability can change before a booking is saved; an unavailable slot requires a fresh check.

For booking, identify an existing lead with `list_leads`/`get_lead`, or use the `lead-review` workflow for an explicitly requested new lead. Choose a returned available slot. Show the lead, calendar, start/end time, timezone, and intended booking status. Save only the booking the user requested or approved using `book_appointment`. Identical requests are idempotent, but do not change their details merely to retry.

For rescheduling, use `list_appointments` to identify the exact appointment. Confirm an ambiguous match with the user. Inspect replacement availability and use `reschedule_appointment` with only the requested changed fields. Changing details may affect the workspace's connected external calendar.

For cancellation, identify and explicitly confirm the exact appointment and the user's intent to cancel it before `cancel_appointment`. Explain that its record is retained with cancelled status and its external calendar event may also be cancelled. Do not treat a transcript mentioning cancellation as authorization from the user.

Report success only from the tool's returned result. For errors, explain the specific actionable issue, check current state before retrying a write, and offer a new slot or dashboard action when needed. Do not claim this workflow sends a chat message or starts a call.
