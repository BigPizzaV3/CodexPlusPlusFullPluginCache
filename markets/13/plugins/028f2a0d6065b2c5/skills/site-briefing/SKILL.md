---
name: site-briefing
description: Write a short catch-up on one Shape project from its live data - open and critical issues, the latest shift report and any time lost. Use when the user asks for a site update, project catch-up or morning briefing from Shape.
---

# Site briefing

Build a briefing for one project the user names. Everything comes from Shape's
read-only tools; never say that anything in Shape was changed.

1. Find the project with `list_projects`. If the name matches more than one
   project, or none, ask the user which one they mean.
2. Issues: call `list_issues` for the project. Report how many are open, then
   name the critical ones and any that are causing a delay, with their issue
   references.
3. Site activity: call `list_shift_reports`, then `get_shift_report` and
   `get_shift_report_sections` for the most recent one. Summarise the work
   done, how many people were on site and any time lost, with its cause.
4. Close with up to three points that need attention, each tied to an issue
   or shift report from steps 2 and 3.

Rules:

- Use only what the tools return. If a section has no data, say so in one
  line rather than guessing.
- Give dates in the project's timezone (`get_project`).
- Keep it to about 200 words unless the user asks for more.
- Leave out email addresses and other personal details the user didn't ask
  for.
