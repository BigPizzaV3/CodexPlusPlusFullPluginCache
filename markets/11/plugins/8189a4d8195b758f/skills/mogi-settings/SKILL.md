---
name: mogi-settings
description: Change how Mogi runs for the user (auto-approve, resume customization Heavy / Light / My own, the cover letter, email preferences), pause or resume all applications, and update the profile answers used on application forms.
metadata:
  short-description: Auto-approve, pausing, emails, profile
---

# Settings and profile

## Settings

1. Call `get_settings` and explain the current choices in plain words using `meaning`.
   `resume_customization` is what the user sees in the app: Heavy, Light or My own.
2. Change with `update_settings`:
   - `job_auto_approve`: high_fit (strong matches approved automatically, the rest wait for
     the user) or all (every job approved). Approving every job by hand can no longer be
     chosen. This is about jobs only: resumes are never held for review.
   - Resume customization: Heavy = `resume_creativity` medium (the default and most
     interviews, AI may add or change details), Light = `low` (small edits), My own =
     `custom_resume_opt_in` false (their file, unchanged). Use the words Heavy, Light and My
     own with the user.
   - `generate_cover_letter`: one cover letter, written once from their resume, goes with
     every application.
3. Report anything in `not_applied`.
4. Emails: `update_email_preferences` (categories, daily cap, digest cadence, or unsubscribe all).

## Pausing

- `pause_applications` stops every queued and in-progress application at once; jobs already
  sent stay. `resume_applications` puts the same jobs back.
- Confirm with the user before either.

## Profile answers

1. `get_profile` lists the answers Mogi puts on application forms and any missing.
2. `update_profile` with only the fields that change. Required answers can be changed, never
   removed.

## Guardrails

- Auto-approve means Mogi applies without asking. Explain and confirm before
  turning it on.
- Payments and account deletion are not available here. Point the user to the Mogi app.
- Never guess a profile answer (work authorization, sponsorship, date of birth).
