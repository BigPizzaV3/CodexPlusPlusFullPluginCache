---
name: shared-checklist
description: Publish a checklist page a group ticks off together with create_shared_checklist, read progress, overdue items and who did what with show_checklist_results, and add, change, remove, tick or close with update_shared_checklist.
---

# Zovo Shared Checklist

Use this when a group works through one list together (moving, wedding prep, event setup, onboarding) and everyone should tick items on a shared page.

1. `create_shared_checklist`: pass `time_zone` (IANA name such as Europe/London; ask if you cannot tell) and `items` (1 to 150). Items can be plain text or objects with `section`, `assignee` (first name) and `due` (YYYY-MM-DD).
2. Reply with both links from the result. Say plainly: share the public link with the group; keep the organizer link private.
3. Progress questions ("what is left", "what is overdue", "who did what") need the organizer link: call `show_checklist_results` with it. Overdue and "today" use the checklist's time zone.
4. Changes go to `update_shared_checklist` with the organizer link: `add_items`, `edit_items` (by item number), `remove_items`, `mark_done` / `mark_not_done` (item numbers, with `done_by` for the name shown), `title`, `note`, or `status` closed / open.

Do not use this for a private note, a reminder at a time, or tasks in another tool (Jira, Asana). Names only: do not ask for emails or phone numbers.
