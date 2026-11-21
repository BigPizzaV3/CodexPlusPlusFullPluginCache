---
name: mogi-review-jobs
description: Review the jobs Mogi found for the user and approve or pass on them. Use for any request about new jobs, the approval queue, or which jobs Mogi should apply to.
metadata:
  short-description: Approve or pass on new jobs
---

# Review new jobs

## Workflow

1. Call `list_jobs` with `stage` `needs_approval`, `page_size` 10, `sort` `fit`.
2. Show each job on one or two lines: title, company, location and work mode, pay if listed,
   fit score (1 to 10), and its `client_job_id`. Say how many more are waiting.
3. Offer: details on any job (`get_job`), approve, or pass.
4. Act only on the jobs the user names, with `decide_jobs` (up to 50 ids per call).
   - approve: Mogi applies to it.
   - reject: pass on it. undo moves a job back to waiting.
5. For "approve all the good ones", explain `approve_high_fit_jobs` (every strong match) and
   confirm first. For "clear out the weak ones", `reject_low_fit_jobs` (fit 5 or lower).
6. If approval is refused because the resume is not approved yet, switch to mogi-resumes.
7. Page with `page` 2, 3... using the same filters.

## Guardrails

- Never approve or pass on a job the user did not choose. Bulk actions need a clear yes.
- If many passes share a reason (wrong seniority, wrong location), suggest fixing the search
  instead (mogi-job-searches).
- Show only jobs the tools returned. Never invent pay, dates or companies.
