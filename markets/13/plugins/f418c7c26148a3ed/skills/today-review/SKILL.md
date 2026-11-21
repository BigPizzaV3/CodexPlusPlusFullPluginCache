---
name: today-review
description: Review a member's Today queue - what needs them now, grouped by kind and urgency - then draft, rewrite, grade, snooze or skip the touches they flag, clear rows they are done with, and hand every approval back to them.
---

# Today review

Today in Kenso is one member's queue for the day: touches waiting for approval or failed, tasks due, meetings, replies waiting, signals, new leads, paused account plans and setup steps. The member sees it at `https://app.ken.so/<workspace id>/today`.

Trigger on "what needs me today?", "clear my queue", "go through my Today", or the start of a member's day.

Today, touches, approvals and the questions Kenso asks have no tool in this app: you cannot read the queue, or draft, approve, snooze, skip or clear a row here. What you can do: read the parts of the day the tools here reach (replies waiting, today's calendar and meetings, notifications), write, rewrite and grade a touch the member pastes, and send them to Today for every action on a row.

## The rule: the member approves every send

You draft, rewrite and grade. The member approves, edits, snoozes, skips and clears, in Today. Never say a touch was sent or approved because you wrote it.

- A touch with a body waits as `awaiting_approval` until the person clicks Approve in Today. Say it waits for their approval, and when it is due.
- Retrying a failed send is the member's Retry in Today too.
- Every write in this skill happens only on the member's request, one row at a time unless they ask for a batch.

Every tool here takes `workspace_id`. Send it on every call when the user can see more than one workspace (`list_workspaces()` lists them).

## Step 0 - Check what is on

Today and touches are in beta, on per workspace. The tools here reach these parts of the day:

| Part | Tools |
|---|---|
| Replies waiting | `get_inbox_counts()`, `list_inbox_threads()` |
| Today's calendar | `list_calendar_events()` |
| Recorded meetings and their notes | `list_meetings()` |
| Notifications | `list_my_notifications()` |
| Grading a touch the member pastes | `grade_email_copy()`, `check_email_copy()` |

- If https://app.ken.so/<workspace id>/today shows no queue for the member, Today is not on for this workspace: say so in one sentence, and work only the parts above.
- A part whose tool is missing or refuses: skip it, say which, and carry on.

## Step 1 - Read Today

Ask the member's time zone first, or say the day is UTC. Never guess a zone from a name or a company. Then read:

- `get_inbox_counts(tab="to_reply")`: replies waiting, with the unread and to-reply badges.
- `list_inbox_threads(tab="to_reply", sort="oldest_waiting", limit=10)`: the replies that waited longest, each with `waitingSince` and its `interest`.
- `list_calendar_events(from_time="2026-10-31T00:00:00Z", to_time="2026-11-01T00:00:00Z")`: today's calendar, from the member's midnight to the next.
- `list_meetings(from_time="2026-10-30T00:00:00Z", to_time="2026-11-01T00:00:00Z")`: meetings recorded since yesterday, to spot one that ended with no notes.
- `list_my_notifications()`: the member's unread notifications.

The rest of Today (touches waiting for approval or failed, tasks, calls, opportunities, new leads, account plans, signals, setup steps and questions) is only in the app. When the member wants help with it, ask them to open https://app.ken.so/<workspace id>/today and tell you or paste what is there.

## Step 2 - Group and present

Open with one line: how many replies wait, the next meeting, and how many notifications are unread. Then the groups that have rows, most urgent first:

| Group | From | What the member does |
|---|---|---|
| Replies waiting | `to_reply` threads | answer them (the `reply-handling` skill) |
| Meetings | today's calendar and recent recorded meetings | prep (the `meeting-prep-and-followup` skill), or add notes |
| Notifications | unread notifications | open each in Kenso |
| The rest of Today | what the member tells you from https://app.ken.so/<workspace id>/today | approve, edit, snooze or skip touches, do tasks and calls, resume or end plans, finish setup steps, all in Today |

- Give each group a count and its top 3 rows with title, person or account, and due time. Ask which ones to work; do not walk the whole list unasked.
- A reply thread whose `interest` is `out_of_office` is not a reply and nobody is waiting on it: list it apart, and never count it in "replies waiting". Count replies by distinct person.
- Never report opens.

## Step 3 - Work the touches the member flags

The member pastes the touch from Today: its channel (email, LinkedIn connect or message, call), the person and account, why it is planned, and its text, or says it has no text yet.

| The member wants | Do |
|---|---|
| it written | write a draft from what the member tells you about the person, the account and the reason for the touch. Ask for any fact you lack |
| it shorter, warmer, more specific, or in their voice | rewrite it and show the result |
| a grade | `grade_email_copy(subject_key="touch-9001", copy="...", channel="email")`: a score and what to improve. Use `channel="linkedin_connection"` or `"linkedin_message"` for LinkedIn. For an email, `check_email_copy(subject="...", body="...")` also checks it against the copy rules in code |
| their edit saved | they open the row in Today, click Edit, replace the text with the version they accepted and save it. The touch then waits for their approval |

- Show the full text, and let the member choose what goes into Today.
- Never invent a price, a meeting time, a discount or an offer. When the touch needs one the member has not given, leave it out and ask.
- Name only an event (funding, a hire, a launch) that the account's signals or research state, as the member reports them: Today will not save a touch that names one with no source.
- Funding is not a buying event by itself. Do not make a round the reason for the message unless the account's research ties it to a need the member's offer meets.
- A structural change to the message (new angle, new offer, new call to action) is a new draft the member reviews from scratch, not a small edit.
- A grade answers 429 `quota_exceeded` past 20 a minute or 500 a day: wait and grade again later.

## Step 4 - Snooze, skip and clear

Snoozing, skipping and clearing happen in Today: a touch waiting for approval has Approve, Edit and Skip, a failed send has Retry and Skip, and other rows have Snooze and Done.

- A snooze that breaks a Contact limits rule is refused.
- Some rows change more than the queue. Say so before the member clears them:
  - `done` on a reply row archives the thread, marks it read and clears its reminder: it leaves To Reply.
  - `done` on a `merge_suggestion` row means "not a duplicate" for the whole workspace, and needs Accounts edit.
  - `done` on an opportunity, new lead, merge suggestion, meeting notes or signal row dismisses it for good.
- Undoing a snooze, a skip or an approval is the member's own button in Today.

## Step 5 - Questions waiting for an answer

The questions Kenso asks the member have no tool here. They answer them in the app or in Slack, with a button or a reply. Do not pick an option for them.

## Step 6 - Hand the approvals back

Link Today: https://app.ken.so/<workspace id>/today. Everything that waits on the member (touches, replies, calendar changes, LinkedIn notes, agent proposals and campaign batches) is approved there, by their own click.

Report back: what waits for the member (by group, with counts), each draft or rewrite you gave them, and what still needs them in Today.

## What this skill cannot do yet

- Read Today, or draft, approve, retry, snooze, skip or clear a row: Today and touches have no tool here.
- Answer a question Kenso asked: that stays with the person, on purpose.
- Act on a reply, a meeting or an account plan from here: use the `reply-handling`, `meeting-prep-and-followup` and `accounts` skills.

