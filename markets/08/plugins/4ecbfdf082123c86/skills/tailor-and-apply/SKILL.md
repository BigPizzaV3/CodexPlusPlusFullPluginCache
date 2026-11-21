---
name: tailor-and-apply
description: Adapt a user's saved JobSprout resume to a specific job and draft a matching cover letter. Use when the user wants to tailor a resume to a posting or write a cover letter for a job.
---

# Tailoring to a job

These tools work on the user's **saved** JobSprout resumes and require a linked account. If the user is not linked, the tools return a prompt to connect their account; relay that and continue once they have linked.

## Workflow

1. Call `list_my_cvs` to find the resume's `cv_id`. It shows the user nothing. If the user named the resume, use that one; if they have several and did not say which, ask. If they have none, suggest building one first (see **build-a-resume**).
2. Get the job description. Ask the user to paste the full posting.
3. Call `tailor_cv_to_job` once with the `cv_id` and the job description. By default it tailors the resume **in place**, exactly like tailoring inside the JobSprout editor. Only pass `mode: "new_copy"` if the user explicitly wants to keep the original untouched.
4. If the user asked for a cover letter, call `generate_cover_letter` once with the same `cv_id` and job description, only after the tailoring has returned. Otherwise offer one.
5. Each result is shown in its own card with open and download buttons. Do not repeat the cards, the change list, the letter text or the links; confirm in a sentence or two.

## Boundaries

- These are paid operations that use the account's JobSprout credits. If the account has no credits, the tool says so with a link to the plan options; relay that plainly and do not push an upgrade.
- Tailoring reframes the user's own experience; it never fabricates. In-place tailoring rewrites the summary, skills, and experience bullets of the chosen resume (the user can undo in the editor); use `mode: "new_copy"` when they want the original preserved.
- Never invent experience to match the job. Tailoring reframes what the user already has.
- Never search for jobs or claim to submit applications.

## Do not trigger on

- Requests to find or apply to jobs.
- Anonymous users with no saved resumes and no intent to link (offer **build-a-resume** instead).
