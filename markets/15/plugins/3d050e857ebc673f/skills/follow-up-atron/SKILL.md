---
name: follow-up-atron
description: Follow-up-atron. Use when the user asks who they owe a reply to, who has not replied to them, what email follow-ups are pending, or wants nudges drafted.
---

# Follow-up-atron

Find the conversations that are stuck, and get them moving again. Nothing is sent.

## 1. Find them

- Call `delegent_find_follow_ups` (default the last 7 days).
  - **You owe**: emails expecting the user's reply with no reply yet.
  - **Owed to you**: emails the user sent with no answer.
- If `outlook` is not `connected` and this app has its own mail tool, use it to check sent mail for the "owed to you" side.
- Use `delegent_get_calendar` or a calendar tool for last week's meetings: promised follow-ups often live in meeting actions. Check open actions with `delegent_list_my_tasks`.

## 2. Triage

Rank by what matters: client over internal, days waiting, deadlines mentioned, meetings coming up with the same people. Show:

| Who | Subject | Waiting | Why it matters | Suggested move |

Suggested moves: reply now, nudge, turn into a task, or ignore.

## 3. Act on the user's picks

- **Reply or nudge**: draft the text in the chat. If the user wants it in their mailbox, `delegent_create_email_draft`, with `reply_to_email_ref` to keep the thread. Always say it was not sent.
- **Make it a task**: `delegent_capture_work` (kind action, due date), citing the email ref.
- **File it**: `delegent_file_email` to the right workstream.

Never send, and never draft to recipients the user did not approve.

When using `delegent_get_calendar` for a Google account, set `include_google: true`; `include_outlook` retains its Outlook-only meaning. Treat partial or unavailable coverage as unchecked, not an empty calendar.
