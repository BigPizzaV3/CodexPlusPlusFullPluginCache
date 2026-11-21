---
name: review-tracker-matches
description: Show the newest jobs that match the user's Emploive trackers and help decide which to open. Use when the user asks what is new, what matches their alerts, or to catch up on their trackers.
---

Use this skill when the user wants to catch up on jobs that match their trackers.

1. Call list_trackers. If the user has none, offer to create one with the job-alerts skill.
2. Pick the tracker the user names. If they name none, go through the active trackers, newest first, and skip paused ones.
3. Call get_tracker_jobs for each tracker you review, 10 jobs at a time.
4. Group the jobs by tracker. For each job show title, company, location, pay when present, and how long ago Emploive found it, linked to its `url`.
5. Point out jobs found in the last day first; they are the most likely to still be open.
6. When the user asks about one job, call get_job and summarize the description: what the team does, requirements, and pay.

To browse visually, call open_emploive. It opens the Emploive view with the trackers and their jobs.
