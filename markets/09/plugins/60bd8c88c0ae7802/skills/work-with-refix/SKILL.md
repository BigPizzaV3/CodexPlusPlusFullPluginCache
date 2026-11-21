---
name: work-with-refix
description: Use Refix to answer questions about company data, run ongoing watchers, and catch up on what Refix found.
---
# Work with Refix

Call `refix_get_context` before new work. If something is missing, send the user to the
returned link. Never ask for passwords or other secrets in chat.
Use only the sources that `refix_get_context` lists as usable.
Refix only reads data. Source writes are not available through this connection.

## Ask a question

- Call `refix_investigate` with a new `idempotency_key`. Keep the `investigation_id`.
  Give the user the `report_url` at once. It opens the conversation in Refix.
- Call `refix_get_investigation` until the run finishes. Each call waits up to 25 seconds
  for news, so call again right away. Do not start another investigation to check progress.
- A run can take several minutes, and the user sees nothing unless you send it. When a
  result has `latest_step`, send it to the user as a one-line message before the next call.
- When the answer has a table of numbers over time or across categories, show it as a chart
  if you can draw one. Use Refix's numbers exactly.
- If the state is `needs_input`, ask the user the pending question. Send the answer with
  `refix_investigate` and `response_to_input_id`.
- For a follow-up in a finished conversation, use `session_id`. To dig into a finding,
  use `finding_id`. Send only one of these.
- Investigations count toward the workspace's Refix usage. They send no Slack messages or emails.

## Set up a watcher

A watcher carries a goal. Refix keeps working on it and tells the user what it finds. Offer
one when the user wants an ongoing outcome, not a single answer.

- Call `refix_list_watchers` first. Do not create a duplicate watcher.
- Tell the user that watchers count toward the workspace's Refix usage and that everyone in
  the workspace can see the watcher.
- Ask where alerts go. Read `alert_channel` from `refix_get_context`:
  - Offer this option only if you can run scheduled tasks:
    **Here.** I'll check Refix on a schedule and tell you here. Alerts arrive when I next check, not instantly.
  - `slack`: also offer **Slack DM.** Refix messages you in Slack as soon as it finds something.
  - `email`: also offer **Email.** Refix emails you as soon as it finds something.
  - `none`: say alerts stay here, and give the `connect_slack` link for instant Slack alerts.
- Create the watcher with `refix_create_watcher`. Use `alerts: "mcp_assistant"` for "here".
- After creation, say: Done. Refix will [keep alerts here / DM you on Slack / email you].
  Everyone in your workspace can see this watcher in Refix. To change where alerts go, open
  the watcher in Refix: <watcher_url>
- If the user picked "here" and you can schedule tasks, set up a scheduled task that calls
  `refix_list_findings` with the watcher's `watcher_id`, passing `since` as the time of the
  previous check. If you cannot schedule tasks, say that alerts appear when the user asks
  what is new. Never promise a check you cannot run.
- To change a watcher, use `refix_update_watcher`. The objective cannot change: stop the watcher
  and create a new one.

## Catch up

- Call `refix_list_findings` without `watcher_id` to get watcher alerts and other Refix updates.
- Call it with no `since` for "what's new" in a new chat. It returns the last 7 days, newest first.
- For a scheduled check, pass `since` as the time of the previous check.
- Say "nothing new" only when the call succeeds with no items. Report errors as errors.
- Reading findings changes nothing in Refix.

## Rules

- Let Refix do the analysis. Do not rebuild it with other tools.
- Reuse an `idempotency_key` only to retry the identical request.
- Follow the `next_action` in an error.
