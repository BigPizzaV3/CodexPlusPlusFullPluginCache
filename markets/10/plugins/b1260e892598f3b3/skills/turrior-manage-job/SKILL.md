---
name: turrior-manage-job
description: Find and manage an existing Turrior job when the user asks to edit, publish, unpublish, inspect, or get the application link for a vacancy.
---

Use this skill for operations on an existing job post.

1. Resolve a named job with `list-short-job-posts`.
2. If several jobs could match, ask the user which one they mean.
3. Before modifying the job, always call `get-full-job-post`.
4. For edits, call `patch-job` with only the fields the user requested to change.
5. Resolve category, country, and city IDs with their dictionary tools; never guess IDs.
6. Use `publish-job` or `un-publish-job` only when the user's request calls for that action.
7. For an application link, verify that the job is active and has a slug, then return:
   `https://turrior.com/apply/{slug}`
