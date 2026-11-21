---
name: mogi-get-started
description: Introduce Mogi when it is first connected, or when the user asks what it can do or how their job search is going. Checks the account and routes new users into setup.
metadata:
  short-description: What Mogi can do and where you stand
---

# Get started with Mogi

Mogi finds jobs that match the user's searches and applies to them in the user's name,
automatically. These tools manage the user's own Mogi account.

## Workflow

1. Call `get_account`.
2. If `plan_active` is false, say their Mogi account is not active yet and is managed in the
   Mogi app (`app_url`), and stop. No other tool works until then. Never talk about what Mogi costs.
3. If `onboarding_completed` is false, say setup takes a few minutes in this chat and continue
   with the mogi-setup skill.
4. Otherwise tell the user, in four short lines at most:
   - how many jobs wait for their approval (`jobs_by_stage.needs_approval`);
   - applications submitted (`jobs_by_stage.applied`) and interviews (`interviews`);
   - anything blocking them (`blocked_reason`, `account_paused`, `applications_paused`);
5. Offer the next step that matters most: answer Mogi's questions on a job, review new jobs,
   review tailored resumes, or tune searches.

## What people use it for

- Reviewing and approving new jobs (mogi-review-jobs)
- Tuning saved searches (mogi-job-searches)
- Resumes and tailored documents (mogi-resumes)
- Settings, pausing applying, profile answers (mogi-settings)
- Following applications, interviews, messages and job emails (mogi-progress)
- Finishing setup (mogi-setup)

## Guardrails

- Quote only numbers the tools returned.
- Payments and anything else about the account itself happen in the Mogi app, never here.
  Never talk about what Mogi costs or about deals.
- If the tools are unavailable, ask the user to connect Mogi and sign in with the Google account
  they use for Mogi.
- If a tool says a daily limit is reached, say when it resets and stop calling it.
