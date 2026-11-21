---
name: log-repairs-and-expenses
description: Log a repair or maintenance job, act on an existing job, record a renewed certificate, or book an expense in PAM. Use when the landlord reports a problem at a property, says a certificate was renewed, mentions paying for something, or asks PAM to find and book a contractor.
---

Use the `pam` connector's tools; call `list_properties` first if you do not yet have the property id.

**Repairs**
- A problem the landlord noticed → `create_job` with a one- or two-sentence description a contractor would understand, a category and an urgency.
  - `let_pam_handle: false` just logs it.
  - `let_pam_handle: true` makes PAM ring contractors now. Ask first ("Shall I have PAM find and book a plumber for this?"), and only once the landlord says yes call again with `confirmed: true`.
- Existing jobs (`get_maintenance` gives the ids) → one tool per action: `start_job_sourcing` (PAM rings contractors) and `approve_job_quote` (book the quoted contractor) need an explicit yes then `confirmed: true`; `mark_job_self_managed`, `pause_job_sourcing`, `resume_job_sourcing`, `retry_next_contractor` and `cancel_job` do not, but say what you did.
- "Who could do this?" without booking → `find_contractors` (read-only).

**Certificates**
- "The gas safety was renewed on 3 March, expires 3 March next year" → `update_certificate` with `cert_type`, `issue_date` and `expiry_date` (YYYY-MM-DD). Confirm the property and dates back to the landlord in your reply.

**Expenses**
- "I paid the plumber £180" → `book_expense` with the amount in pounds, an SA105 category (repairs_maintenance, insurance, management_fees, professional_fees, travel, advertising, interest_finance, ground_rent, service_charge, other_allowable, other), a short description and the date (today if not given). Leave `property_id` out for a general cost.

**Secure-browser tasks** (last resort): when the request needs a website PAM has no tool for (a council licence, a deposit scheme, a utility account), use `start_browser_task` with a clear goal; PAM asks the landlord before submitting or paying anything. `list_agent_tasks` shows tasks waiting on them; `approve_browser_task_step` carries out the exact step PAM asked about (needs an explicit yes, then `confirmed: true`), `answer_browser_task` passes an answer such as a code, `deny_browser_task_step` refuses the step, and `cancel_browser_task` stops the task.

Report what PAM did in one or two sentences, including the job reference when one is returned.
