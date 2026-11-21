---
name: job-alerts
description: Create, change, pause, or delete Emploive trackers, which email the user new jobs that match saved filters. Use when the user wants alerts, notifications, or to follow a search over time.
---

Use this skill when the user wants to be told about new jobs, or wants to manage the trackers they have.

1. For a new tracker, collect the filters as in the find-jobs skill. Use the current conversation's search when the user says "this search".
2. Name the tracker in a few words, such as "SF SWE internships".
3. Use one email a day unless the user asks for another cadence. Valid cadences in minutes: 5, 15, 30, 60, 180, 360, 720, 1440.
4. Call create_tracker. If the result has a `note`, tell the user in one sentence. It says when the user's plan slows the alerts down.
5. Confirm the tracker name, its filters in plain words, and the alert cadence. Show a few of `newest_matches` so the user sees the tracker works.
6. To change a tracker, call list_trackers to find its id, then update_tracker with only the fields that change. Pass `paused: true` to pause it.
7. Before delete_tracker, confirm with the user by name. Deleting stops its emails.

If a tool says a filter needs a different plan, tell the user that their plan does not include it, and continue without that filter if they agree. Do not describe prices or push an upgrade. Do not add links to pricing, trials, or checkout.
