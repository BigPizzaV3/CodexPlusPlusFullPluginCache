---
name: developer-handoff
description: Use when the user wants a finished Sitewalk audit turned into tasks for a developer, a client's developer or an agency team, such as a ticket list, a to-do list or a brief.
---

Turn a finished audit into a task list. Do not start a new audit for this.

1. Use the `audit_id` of the audit already discussed in this chat. If there is none, ask which site, then run the audit as usual first.
2. Call `get_audit_report` with `top_n` set to 25.
3. Write one task per issue, in the report's order. Each task has: a short title, why it matters in one line, the number of pages affected, two or three example URLs, the fix as the report states it, and how to check it is done.
4. Group the tasks under "Fix first", "Next" and "Later", following the report's ranking.
5. End with the full report link and the CSV and PDF links from the report, so the developer has every affected URL.

Use only the issues, counts and URLs the report returns. Do not invent effort estimates or deadlines.
