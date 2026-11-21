---
name: jobsite-status
description: Produce a jobsite status report for a BOLDR project — per-job progress, out-of-tolerance measurements, and recent activity — ready to paste into a standup or email.
---

# Jobsite status report

Use this when the user asks how a project or job is going, what's left, or
what's out of spec.

1. If the user didn't name a project, call `list_projects` and ask which one
   (or pick the obvious match from their words).
2. Call `get_project_progress` for the roll-up, then `list_jobs` for per-job
   completion fractions.
3. For each active job the user cares about (or the 2–3 least complete),
   call `find_out_of_tolerance` and `get_job_progress`.
4. Report, in this order: overall project completion, per-job completion,
   then out-of-tolerance items as "group → column: measured X vs target Y
   (band min–max)" using the values exactly as the tools format them —
   never convert units yourself; pass the user's preferred `unit` to the
   tools instead.
5. If the user wants the full table, call `export_job_csv` and provide the
   CSV rather than re-typing values.

Keep the report short: lead with the one number they asked for, then the
exceptions. Offer the CSV export instead of pasting large tables.
