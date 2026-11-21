---
name: apply-to-jobs
description: Help the user apply to a remote job on Himalayas, from checking fit to a tailored resume and cover letter, saved application answers, the employer's apply link and interview practice. Use when the user wants to apply to a job, tailor a resume or cover letter to one, answer application questions, or prepare for an interview.
---

# Apply to jobs

Follow [himalayas-basics](../himalayas-basics/SKILL.md) for the shared rules.
Applying needs a Himalayas account. The user submits every application
themselves on the employer's site.

## 1. Check fit

Read the job with `get_job_details` and the user's profile with
`get_my_profile`. Before going further, point out anything that rules the job
out: the countries it is open to, required work permits, time zone, seniority
or salary. If the user decides not to apply, offer `skip_job` with the reason.

## 2. Tailor the documents (optional)

`generate_application_documents` writes a resume and a cover letter tailored
to the job from the user's profile and saves them to their account, where they
can edit them and download a PDF. Check the plan in `get_my_profile` first:

- **Plus plan:** offer to tailor them for this job.
- **Free, not used yet:** a free account gets one tailored resume and one cover
  letter, ever. Say so, and use them only if the user wants them for this job.
- **Free, already used:** skip this step and apply with the user's own resume.
  If the tool reply says the free documents are used, say once that more
  tailored documents need a Himalayas Plus plan, and carry on.

Pass `documents` to make only one of the two. A second call for the same job
returns the documents already made, without using anything up.
`list_documents` and `get_document` read them back. `update_document` renames
a document or replaces a cover letter's text; resume content is edited in the
website's resume editor.

A thin profile makes thin documents. If the profile is missing experience,
offer [build-candidate-profile](../build-candidate-profile/SKILL.md) first.

## 3. Application questions

`list_saved_answers` shows answers the user saved to common questions, such as
work authorisation or notice period. Use them to draft answers for this
application, and show the drafts to the user. `update_saved_answer` changes
one after the user confirms.

## 4. Apply

When the user has decided to apply, call `get_apply_link`, on any plan.
No plan limit ever holds this step back. It returns the
employer's application link and marks the job as applied in the tracker. The
user opens the link and submits the application. Never fill in the employer's
form for them. The limit is 50 links per account per day.

If the user ends up not applying to a job you got the link for (they compared
it and passed, the form was blocked, or the posting is gone), record that
before you finish: `update_job_status` with the tracker ID from the reply,
outcome `didnt_apply` and a reason (`job_closed` if the posting is gone).
Otherwise it stays as applied and the user is asked whether they heard back.

## 5. Prepare for interviews

- `get_interview_practice_link` returns the Himalayas page where the user
  practises interviewing for this job, or for a job elsewhere with
  `application_link`. Free accounts include one text mock interview; spoken
  mock interviews need a Himalayas Plus plan (30 minutes a month).
- Without the link, you can still help: draft likely questions from the job
  description and the user's profile, and give feedback on their answers in
  the conversation.
- `list_interviews` shows past practice and the minutes and credits left.
- `get_interview_results` returns scores and feedback for one job. Summarise
  the two or three things to work on.

## 6. Afterwards

Record progress with `update_job_status` (see
[track-applications](../track-applications/SKILL.md)).
