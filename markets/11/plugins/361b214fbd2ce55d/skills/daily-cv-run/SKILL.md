---
name: daily-cv-run
description: Set up a recurring ChatGPT scheduled task that formats new CVs or resumes arriving in a mail label or folder into the firm's template every day, with a daily credit cap, no duplicates and a summary of what was done and skipped. Use when a recruiter or delivery team asks to "format new CVs automatically every morning", "process the CVs in my Candidates label each day", "set up a daily CV run" or "automate CV formatting".
---

# Daily CV run (ChatGPT scheduled task)

Done when: the user has approved a scheduled task with a clear source, template,
daily credit cap and schedule - or knows why it cannot be set up on their account
and how to run the same steps by hand.

Explicit instructions from the user take priority over this skill.

## What ChatGPT supports (tell the user plainly)

- Scheduled tasks run one-time or recurring work and can use connected apps such as
  Gmail. Active task limits depend on the plan; free accounts run at most once a
  day; hourly runs and exact times need a paid plan. Tasks are managed under
  **Scheduled**. A task created inside a project cannot read that project's files.
- Event-triggered tasks (for example "when a new email arrives with this label") run
  in Work on eligible Plus, Pro, Business, Enterprise and Edu accounts, not on Free
  or Go.
- Actions that need the user's approval may pause a task until the user reviews it.
  Formatting creates documents and uses credits, so a run may wait for approval.
- If you cannot create the task from this conversation, give the user the task text
  below to paste into **Scheduled > New task**.

## Set-up conversation (ask, then confirm)

1. **Source:** the mail label or folder (for example Gmail label "Candidates/To
   format") and that the user's mail app is connected in ChatGPT. Formatix itself
   only needs the CV text or file.
2. **Template:** `find_template` -> the user picks one; note its id, type and
   output format.
3. **Daily limit:** a number from the user (1 credit per candidate). Never assume
   one. Ask them to set it at https://platform.formatix.ai/assistant/activity/ too:
   Formatix then stops the run itself at that number, and shows what was done.
   `get_activity` reads the limit; an assistant cannot change it.
4. **Schedule:** time and time zone, weekdays or every day.
5. **Output:** where results go - the task's summary in ChatGPT (default), or a draft
   email to the user, or saved in their cloud storage if that app is connected.
6. Read the task text back and create it only after the user says yes.

## Task text (fill the brackets)

> Every [weekday at 08:00 Europe/London]: find emails in [label] received since the
> previous run with a CV or resume attached (PDF or Word). For each, up to
> [N] candidates in total this run: read the CV and format it into Formatix template
> [name] (id [id], type [type], [docx]) with `format_cv` (`cv_text` = the CV's full
> text as written) or `fill_template` following the template's extraction prompt,
> with a `request_id` of "[message id]", so Formatix never formats the same email
> twice. Never invent details. Skip, and list, any email without a CV, any candidate
> already formatted (Formatix answers already_done or looks_like_correction) - never
> resend with confirm_new_document - and stop at daily_limit_reached, listing what is
> left. Send nothing to candidates or clients. Finish with a summary:
> formatted (name, link), skipped (why), credits used, credits left if known.

## Rules for every run

- Formatix enforces the daily limit and answers `daily_limit_reached`; leftover CVs
  wait for the next run and are listed.
- The same `request_id` is never formatted or charged twice (30 days).
- If Formatix reports too few credits, stop and say so in the summary.
- Links last an hour: the summary tells the user to open them promptly, or
  `get_formatted_cv` gives fresh ones.
