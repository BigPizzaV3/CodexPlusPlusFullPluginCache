---
name: use-presentr-practice
description: Use when the user wants to practise or prepare for a job interview for a specific role, company or job posting with Presentr Practice. Covers what to send to create_practice_interview and how to hand the user the link.
---

# Set up a practice interview with Presentr Practice

Presentr Practice runs spoken mock interviews in the user's browser. This tool prepares one for a specific job and returns a link; the interview itself does not happen in the chat.

## 1. Collect what the user gave

- `job_title` (required): the role, e.g. "Dental Assistant". If the user only pasted a posting, use the title it names.
- `company`: only if the user named the employer.
- `job_posting`: only if the user pasted a posting (200 characters or more). Send it as the user gave it. Don't write one, and don't add the user's own details.

Don't ask for anything else first. If the role is unclear, ask which job the interview is for.

## 2. Call create_practice_interview

Call it once. It returns the interview's title, what it covers, sample questions, a link and when the link expires.

## 3. Give the user the link

Tell the user the interview is ready, name what it covers in one line, and give them the link. Say that it opens on Presentr Practice, where an AI interviewer asks the questions out loud and follows up, and that they can answer by voice or by typing. The link works for 7 days in the first browser that opens it, so they shouldn't share it.

Don't run the interview in the chat, and don't invent its questions or results.

## Errors

- `busy`: tell the user to try again in a few minutes.
- `invalid_input`: fix the arguments (for example, drop a posting under 200 characters) and call again once.
- `unavailable`: say it couldn't be prepared right now and offer https://practice.presentr.me/create-prep, where they can set it up directly.
