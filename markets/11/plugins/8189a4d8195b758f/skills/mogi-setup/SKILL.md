---
name: mogi-setup
description: Walk a Mogi user through setup in chat once their account is active: upload a resume, create a job search, add the first jobs, fill the required application answers, then accept the Terms and go live. Use whenever setup is not complete.
metadata:
  short-description: Set up your search and go live
---

# Finish setup

## Workflow

1. Call `get_onboarding_status`. If `plan_active` is false, explain that setup continues once
   the account is active in the Mogi app (`app_url`), and stop. Otherwise follow `next_steps` in order and say how many are left.
2. **Resume.** Ask the user to attach their resume (PDF or Word), then call `upload_resume`.
   Formatting takes a minute or two; check with `list_resumes`. When the status is `ready`,
   share `document_link`, and call `approve_resume` only after the user says it looks right.
3. **Search.** Ask which roles and where (remote, hybrid or on-site; cities or states) and any
   pay floor. Call `preview_new_jobs` once to show a sample. Adjust with the user, then call
   `add_jobs_from_search` with the filters and the ids they liked.
4. **Answers.** For each item in `missing_answers`, ask the user and save with
   `update_profile`. `referral_source` is how they heard about Mogi. Never guess an answer
   (work authorization, sponsorship, phone).
5. **Three key terms.** Show the user each of the three `key_acknowledgments`, one per
   message, word for word, and ask for an explicit yes to each before showing the next: AI
   writes their resumes and cover letters and they take responsibility for them; about 20 to
   30% of applications are a looser fit, at no extra charge; they can pause or cancel any time
   themselves. If they will not agree to one, do not go live; answer their question instead.
6. **Go live.** Show the user `terms_text` and every other acknowledgment from
   `get_onboarding_status`, word for word, and ask:
   - whether Mogi approves strong matches (`job_auto_approve` `high_fit`) or every match
     (`all`); approving every job by hand is not offered;
   - how their resume is used: Heavy customization (default, recommended, `resume_creativity`
     medium), Light (`low`), or My own file (`custom_resume_opt_in` false). Tailored resumes
     are sent without per-resume approval; say so plainly.
   - whether they want one cover letter that goes with every application (default no).
   Then ask them to type their initials. Call `complete_onboarding` with
   `user_agreed_to_key_terms` and `user_agreed_to_terms` true only after they explicitly agree.
7. Confirm Mogi is live and offer to review the first jobs (mogi-review-jobs).

## Guardrails

- Going live signs the Terms. Never set `user_agreed_to_key_terms` or `user_agreed_to_terms`
  without the user's explicit yes in this conversation (one yes per key term), and never type
  their initials for them.
- One question at a time; keep each message short.
- Use only facts the user gave.
