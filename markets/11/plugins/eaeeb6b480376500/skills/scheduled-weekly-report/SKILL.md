---
name: scheduled-weekly-report
description: Use when the user wants a recurring report ("email me a sales summary every Monday", "send a daily digest to our Slack channel", "pause/change my weekly report"). Creates, updates, pauses, resumes or deletes a 1stPage schedule that delivers by email and/or Slack.
---

# Scheduled report

1. Delivery: use only email addresses and/or Slack channel IDs the user stated in this conversation. If the user has not said where to deliver, ask (email address, Slack channel, or both). Never invent an address or reuse one the user did not give for this report.
2. Timing: confirm the time of day, the frequency (daily, weekly with days, or monthly with a day of the month) and the IANA timezone. If no timezone was given and none is on the user's profile, ask for it.
3. Write the saved prompt as the question to answer on each run, phrased so it stays correct every time, for example "Summarize the most recent complete week of sales versus the week before, with the top five products and any alerts." Prefer "the most recent complete day/week" over a literal "yesterday", because settled Amazon reports lag two to three days.
4. Call `create_schedule` with a short `name`, the `prompt`, `frequency`, `time`, `days_of_week` or `day_of_month`, `timezone`, and `emails` and/or `slack_channel_ids`.
5. Read the result back to the user: name, schedule, timezone, next run time and recipients.
6. To change, pause, resume or delete a schedule, call `list_schedules` first to get its `schedule_id`, then `update_schedule`, `pause_schedule`, `resume_schedule` or `delete_schedule`. Confirm with the user before deleting; deletion cannot be undone.
