---
name: rolebranch
description: Use Rolebranch for a person's job search - judging a job posting against their master CV, tracking applications, asking Romy for tailored CVs, cover letters and interview prep, and weekly check-ins. Use when the person shares a job link or posting, asks about their applications, interviews or CV, or wants a job-search briefing.
---

# Rolebranch

Rolebranch is the person's job-search workspace. Romy, its AI, drafts tailored CVs, cover letters
and interview prep; every draft waits for the person to review and accept it in Rolebranch.

## Judge a posting (a link or pasted text)

1. `read_job_posting` with the link or text. It reads the posting and compares it with the master
   CVs; nothing is saved. If it answers `reading`, follow with `get_posting_draft`.
2. Report the match: what fits, the gaps, and which master CV it used.
3. Only if the person wants to apply: `list_applications` (search the company) to avoid a
   duplicate, then `create_application` with the `postingDraftId`.

## Tailor a CV or write a letter

1. `get_credits` when the person may be short; the app's monthly limit applies.
2. `tailor_cv` or `write_cover_letter`, with the person's own context in `instructions` (emphasis
   and tone only, never new facts).
3. Poll `get_run` until it finishes, then give the person the `url` to review the draft.

## Weekly briefing or "what's on"

`get_agenda` (next steps, drafts waiting for review, runs, applications with nothing heard), then
`get_search_stats`. Lead with what needs the person this week, each item with its `url`.

## Interview

- Before: `get_interview_prep`, or `prepare_interview` to have Romy build the questions (credits).
  Save the person's own stories with `update_interview_outline`.
- Practice: `start_practice_session`, then `submit_practice_answer` per answer; the feedback
  arrives through `get_run`.
- After: `add_application_note` with how it went, `set_application_status` if the stage changed,
  `save_next_step` for the follow-up.

## Always

- Give the `url` from a result whenever you mention an application, CV, run or draft.
- Say what Rolebranch did: added, updated, drafted, proposed. Never say an application was sent or
  an employer contacted; no tool does that.
- Contact details are never available through these tools; don't ask for them.
