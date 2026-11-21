---
name: client-submission-email
description: Write the candidate submission email (candidate summary, CV cover note, "why this candidate" note) to send a client or hiring manager with a formatted candidate profile - factual highlights against the role, availability and next step - as a draft the user checks and sends themselves. Use when a recruiter says "write the email to submit this candidate", "candidate summary for the client", "cover note for this CV" or "introduce this candidate to the hiring manager".
---

# Client submission email

Done when: the user has a ready-to-edit email draft (subject and body) for the
client, based only on the candidate's CV, the Formatix profile and the user's notes
- shown in the chat or saved as a draft in their mail app. Nothing is sent.

Explicit instructions from the user take priority over this skill.

## Ground rules

- Reply in the user's language. Write the email in the language the user asks for
  (default: the language they write in).
- Facts only from the CV, the formatted profile and the user's notes. Never invent
  achievements, motivations, compensation, notice periods or interview availability.
- This skill uses no credits on its own. If there is no formatted profile yet and the
  user wants one attached, follow format-cvs first (1 credit per candidate; say so).
- Never send the email. If asked to send it, say the user sends it after checking it
  and the attachment.

## Steps

1. **Source the facts.**
   - A profile Formatix made in this conversation: `get_cv_details` with its
     `record_id` (read-only, no credits) for the exact details in the document.
   - Otherwise the CV the user shared, plus their notes.
2. **Ask once** if missing: the role and client (or confidential descriptor), and the
   next step the user wants (call, interview slots, feedback by a date).
3. **Write** in the firm's voice:
   - Subject: role and candidate (no client name on a confidential search).
   - One opening line: who the candidate is now (title, company type, location).
   - 3-5 bullets of evidence against the role's must-haves, each traceable to the CV
     or the user's notes.
   - Availability, notice and compensation only if the user gave them.
   - The next step, and a line that the profile is attached.
4. **Deliver.** Show the draft. If the user asks and has Gmail or Outlook connected,
   save it as a draft there (with the recipient only if the user gives it).
   Formatix links expire after an hour: tell the user to download the profile and
   attach the file, not to paste the link.

Several candidates for one client: offer one email with a short section per
candidate, or client-shortlist-pack for the full pack.
