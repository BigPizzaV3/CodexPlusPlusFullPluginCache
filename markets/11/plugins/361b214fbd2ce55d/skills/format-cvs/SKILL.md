---
name: format-cvs
description: CV formatting and resume formatting for recruiters. Format a CV or resume into the recruitment firm's own branded template - one candidate or several at once - and return the finished Word, PowerPoint or Excel document (candidate profile, candidate summary, one-page bio, CV in house format, shortlist or tracker). Use when a recruiter or executive search consultant says "format this CV", "put these resumes into our template", "make a candidate profile", "reformat these CVs for the client" or attaches CVs to turn into the firm's format.
---

# Format CVs into the firm's template

Done when: every CV the user gave is in a finished document in the template they
chose, and the user has the download link(s) plus a list of anything that could
not be filled.

Explicit instructions from the user take priority over this skill.

## Ground rules

- Reply in the user's language. The document follows the template's language and
  extraction prompt; do not translate unless asked (translate-candidate-profile).
- Use only what is in the CV. Never invent employers, dates, titles, degrees,
  compensation, notice periods or achievements.
- 1 credit per candidate. If the user clearly asked to format the CVs, go ahead and
  state the total; otherwise say the cost first and wait. Short of credits: say so,
  credits are managed in Formatix; no talk of prices or plans.
- Pass a `request_id` on every fill and reuse it on a retry.
- Templates Formatix set up for the firm are read-only: follow their extraction
  prompt and schema exactly.

## Steps

1. **Collect the CVs.** Attached files (PDF, Word, text) or pasted text. If the user
   asks you to take CVs from their email or cloud storage and has that app connected
   in ChatGPT, use what it returns; Formatix itself needs only the CV text or file.
2. **Choose the template.** Use the one the user named, else `find_template` with
   their words ("one-page executive bio", "candidate profile"). Show at most three
   options (name, type, formats); if one clearly fits, say which you will use.
3. **Choose the route.**
   - `format_cv` - Formatix reads the CV. One attached CV: `cv_file`. Pasted text:
     `cv_text` exactly as given (never summarised or rewritten). Several pasted CVs:
     `cv_texts` (up to 10). Best for a straight "format this CV".
   - `fill_template` - you read the CVs. Call `get_template_schema`, follow the
     extraction prompt for the output format (`docx_`, `pptx_`, `xlsx_`), and send
     `candidates` keyed by the schema's field names. Use it for several attached
     CVs in one document, when the user wants wording choices (shorter summary,
     emphasis on board experience), or a Studio/own template.
   - A `cvtobios` template puts up to 10 candidates in one document; a `custom`
     template or a Word `user_template` holds one candidate (one call each).
4. **Output format.** `docx` unless the template lists `pptx`/`xlsx` and the user
   wants it. Pass `candidate_name` for the file name.
5. **Photos.** Only when the template has a photo slot and the user supplied the
   photo. Otherwise leave it out; it can be added later (fix-a-document).
6. **Wait and deliver.** Formatting takes 30 seconds to a few minutes. If you get a
   `record_id` without a link, say it is in progress and call `get_formatted_cv`
   (pass `template_type` `user_template` for Studio templates). Links work for an
   hour; `get_formatted_cv` gives a fresh one.
7. **Report.** Download link(s), one line per candidate, and any detail the CV did
   not give (for example no notice period). Ask the user to check before sending.

## If Formatix refuses a repeat

`looks_like_correction` means the same candidate went into the same template within
the hour. Do not resend. Explain that a correction is free (fix-a-document) and a
new document uses credits again. Resend with `confirm_new_document=true` only after
the user says yes.

## Afterwards (offer, do not do unasked)

- Save to the user's cloud storage, only if they ask and have that app connected.
- Attach it to the candidate in their ATS or CRM (below), only if they ask.
- Corrections: fix-a-document. Client email: client-submission-email.

## The firm's ATS or CRM (only if connected in Formatix)

`ats_connections` shows what is connected (JobAdder, HubSpot, Salesforce, Ezekia). With
it you can find the candidate or job (`ats_find_candidates`, `ats_find_jobs`,
`ats_get_job`). Attach a finished document (`ats_attach_document`) or add a note
(`ats_add_note`) only when the user asks and has confirmed the record, and show a note's
wording first. If a system cannot do something, Formatix says so: pass that on. Contact
details are never returned.
