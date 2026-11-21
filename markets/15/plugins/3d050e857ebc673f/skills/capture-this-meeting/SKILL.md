---
name: capture-this-meeting
description: Capture this meeting. Use when the user has finished a meeting or call and wants its transcript, decisions and action items kept in Delegent.
---

# Capture this meeting

## 1. Get the transcript

Prefer a source you already have:

- A transcript the user pasted or attached.
- The user's Outlook, Teams or Google Meet tools in this app, if connected.
- Otherwise `delegent_find_teams_meetings`, then the meeting's `teams_meeting_ref`. This works when the user connected Outlook to Delegent.

If no transcript is available, ask the user to paste it or upload it in Delegent.

## 2. Choose the workstream

Match by client or project name. If more than one fits, or none, ask. Offer `delegent_create_workstream` only if the user confirms it is new work.

## 3. Show what you will save, then save it

Show briefly: meeting title, date and workstream; **Decisions**, one line each; **Actions**, one line each with owner and due date when stated; **New people** worth adding as contacts.

Wait for a yes and apply edits. Then:

1. `delegent_import_meeting` with the transcript (or `teams_meeting_ref`), title, start and attendees. If the transcript came from Teams or Google Meet, pass `provider_meeting` so it is never imported twice.
2. `delegent_capture_work` with the decisions and actions, citing the returned `meeting_ref`.
3. If decisions change the project picture, `delegent_propose_overview_update` for decisions, risks or next steps.
4. `delegent_save_contact` for new stakeholders the user approved.
5. Assigning someone follows `hand-it-off`.

Report exactly what was saved, with the `open_in_delegent` link. Never describe decisions the transcript does not support.

## 4. Offer a routine, once

"Want me to do this every evening for all of today's meetings?" If yes, follow `routine-daily-wash-up`.

For an existing Google Meet conference record already identified by the host, `delegent_import_meeting` can fetch transcript entries with `provider_meeting: {provider: "google_meet", external_id: "<conference record ID>"}` and no transcript. This requires separate Meet permission; if unavailable, ask for manual transcript text. It does not read Drive.
