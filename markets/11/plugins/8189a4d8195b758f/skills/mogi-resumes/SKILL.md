---
name: mogi-resumes
description: Manage the user's Mogi resumes (upload, set default, AI edits, going back a version, standing tailoring notes) and look at the resume tailored for each job. Use for anything about resumes or cover letters.
metadata:
  short-description: Upload and edit resumes
---

# Resumes

## Master resumes

1. `list_resumes` shows each resume: status (`processing` while Mogi formats it, `ready` once
   formatted), default, and a `document_link`. A user keeps up to 5 resumes.
2. **Upload:** ask the user to attach a PDF or Word file and call `upload_resume`. Formatting
   takes a minute or two and copies their resume exactly; it is used right away, with no
   approval step. Make one the default with `update_resume` (`make_default`).
3. **Read:** `get_resume` returns the text as it reads now, so you can review it with the user.
4. **Edit:** `edit_resume_with_ai` with plain-words `changes`. Check `get_resume_edit` after a
   minute or two: once it is ready it lists `changes`, the lines added and removed in each
   section. Show the user those changes and the draft link, then `finish_resume_edit` with
   `save` or `discard`. If they do not like the last change, `undo_resume_edit` takes just
   that one back (when `can_undo` is true).
5. **Go back:** when `get_resume` says `has_previous_version`, `restore_previous_resume_version`
   puts the version before the last saved edit back. The newer one is kept, so the same call
   switches back again.
6. **Standing notes:** `update_resume` with `tailoring_instructions` (for example "never drop my
   certifications") guides every tailored resume.

## Per-job resumes

Mogi is tuned for interviews, not for each application: once a job is approved, the resume is
tailored at the user's chosen level (`resume_creativity`: medium = heavy, the default; low =
light) and sent as written. Nobody approves or edits a per-job resume. `get_job_documents`
shows the one written for a job. To change how future resumes read, use `edit_resume_with_ai`
on the master or change the level in settings. A user who wants to approve every application
can use MobiusEngine's premium service at app.mobiusengine.ai.
There is no per-job cover letter: when cover letters are on, one letter written from
their resume goes with every application, and they can upload their own on the Cover
letters page in the app.

## Guardrails

- Confirm before `delete_resume`. The last resume cannot be deleted.
- Do not rewrite facts: dates, employers, degrees and titles come from the user.
