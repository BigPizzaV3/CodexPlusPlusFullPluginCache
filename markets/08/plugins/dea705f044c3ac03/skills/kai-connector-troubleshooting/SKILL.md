---
name: kai-connector-troubleshooting
description: Diagnose and fix problems with the Kai connector inside ChatGPT, and answer questions about what it can access and how to disconnect. Covers tool calls that fail or return FORBIDDEN, Kai tools missing from a conversation, "user timezone is not configured" errors, empty calendar, email, task, or meeting results, expired authorization, subscription status, and revoking access. Use when a Kai tool call fails, the user says Kai isn't working, isn't connected, or can't see their data, or asks what Kai can read or change, whether it costs anything, or how to remove it.
---

# Kai connector troubleshooting

Kai is an AI executive assistant (hirekai.ai). The connector gives this assistant access to
the user's Kai data: calendar, email, tasks, and recorded meetings, across the accounts they
connected in Kai. The user approves it once on Kai's own screen at `web.hirekai.ai`. There's
no API key and nothing to install on their side.

Use this skill to work out why something failed and what to try next. Don't retry a failing
call more than once without changing something.

## Symptom to cause

| What you see | Likely cause | What to do |
|---|---|---|
| Every Kai tool call returns `FORBIDDEN`, or the connection is reported unavailable, although Kai shows as connected | The user added Kai by URL in Developer mode and the toggle has turned off. Nothing else in the flow reports it. | Settings → Security and login → Developer mode: turn it on, then rerun the same request. Not a plan issue; it works on Free. Doesn't apply to installs from the app directory. |
| The Kai tool you need isn't in this conversation (no email tools in a calendar chat, or the reverse) | ChatGPT loads a subset of an app's tools per conversation, chosen by topic. | Start a fresh conversation and open with the topic word: "calendar", "email", "meeting", "task". Mentioning Kai by name helps. |
| `User timezone is not configured` from `list_tasks`, `list_meeting_sessions`, `list_ai_notifications`, or `mutate_ai_notifications` | The user's time zone was never written to their Kai account. It happens on existing accounts too. | Retry with `ianaTimeZone` set (for example `Europe/Brussels`). For a permanent fix: in Kai, Settings → Preferences, change the time zone to something else and back. A displayed value isn't enough; the change is what saves it. |
| Authorization errors (401) after it used to work | The access token expired and couldn't refresh, or the grant was revoked. | Disconnect and reconnect Kai in ChatGPT. It runs Kai's approval screen again; the user signs in to Kai and clicks Approve. |
| Calendar or email results are empty or missing an account | Kai only sees accounts connected inside Kai, and declined invites are hidden by default. | Check `list_accounts`. If an account is missing, connect it in the Kai app (web.hirekai.ai), not in ChatGPT. Pass `includeDeclined: true` to `list_events` if declined invites matter. |
| No meetings, or a meeting the user expected isn't there | Kai only has meetings its notetaker joined and finished processing. | Say so. There's nothing to recover from ChatGPT; the meeting has to be captured in Kai. |
| A list looks short, or fields are missing | Responses are capped (50 tasks, 50 meetings) and drop optional fields under size pressure. `truncated: true` and `elidedFields` say so. | Narrow the date range, or request specific fields with `includeFields` on `list_events`, or fetch a few items in full with the `get_*` tool. |
| Tools fail with an account or entitlement message after authorization succeeded | Kai is a paid product after the trial. If the trial ended or the subscription lapsed, features stop. | Ask the user to check their plan in the Kai app under Settings, and to contact hello@hirekai.ai if it looks wrong. The connector itself is free with a Kai account. |

## What Kai can and can't do here

Can:

- Calendar: read events across every connected calendar; create, move, edit, and cancel
  events. Adding attendees sends real invitations.
- Email: search and read mail across Gmail and Outlook; save drafts and send them on the
  user's explicit word; forward.
- Tasks: read, create, update, complete, reopen, delete the user's own Kai tasks.
- Meetings: read recaps, action items, and (on request) transcripts of meetings Kai captured.
- Triage: read and act on the notifications Kai raised from email and meetings.

Can't:

- Archive, label, star, or delete email. On the mailbox Kai reads and drafts only.
- Reach tasks in other tools (Todoist, Notion, Linear). Kai tasks are native only.
- Read meetings Kai didn't attend.
- Scope access per request. The approval is account-wide, which is why one connection
  serves every use case.

## Posture for anything that leaves the account

Sending an email, forwarding one, moving or cancelling an event with attendees, and deleting
anything all reach other people or can't be undone. Show what you're about to do and wait
for the user's confirmation before calling those tools, whatever the conversation's
permission setting is.

## Disconnecting

- In ChatGPT, disconnecting the Kai app revokes the grant on Kai's side and stops access.
- Uninstalling or deleting a Developer-mode plugin doesn't revoke the grant by itself.
  Disconnect the connection first.
- Access tokens are short-lived; the long-lived credential is what disconnecting revokes.
  Reconnecting later runs the approval screen again.

## Where to send people

- Support: hello@hirekai.ai, or https://hirekai.ai/contact
- Setup guide and use cases: https://hirekai.ai/kai-mcp
- Privacy: https://hirekai.ai/privacy
