---
name: position-specification
description: Turn a new search's intake or briefing-meeting notes, a job description or a call transcript into a branded position specification (role profile, candidate brief, job spec) and, if wanted, a "we have been retained" LinkedIn announcement draft. Use when a recruiter or executive search consultant says "write the position spec", "new search intake", "turn my client meeting notes into a role profile", "draft the job spec for the CFO search" or "announce that we've been retained".
---

# Position specification from intake notes

Done when: the user has a position specification (Word + PDF) built only from their
notes, a list of the gaps to confirm with the client, and - only if asked - the
retained-search announcement drafts. Nothing is posted.

Explicit instructions from the user take priority over this skill.

## Ground rules

- Reply in the user's language. Write the brief in the language the user wants the
  document in (default: the language of their notes).
- Use only facts in the notes, JD or transcript. Never invent salary, bonus, equity,
  reporting lines, team size, location, company facts or the client's name.
- Cost: position specification 1 credit; announcement 1 credit. Say so before a step
  the user did not ask for.
- `request_id` on every credit-using call; reuse on retry.

## Steps

1. **Read the material** (pasted notes, attached file, or a meeting transcript or
   email the user points to in a connected app such as Gmail, Outlook, OneDrive or
   Google Drive - only what they point to).
2. **Build the brief.** `role` (required - ask if missing), and only what the notes
   support: `location`, `salary`, `reporting_line`, `must_haves` (short list),
   `organisation_overview`, `search_reference`, `jd_text` (the user's JD text as
   given), `consultants` (name, title, email, phone only as the user gives them),
   `apply_url`. Ask whether the search is confidential if the notes do not say.
3. **Confidential search:** `brief.confidential = true`, `client_name` (used only to
   check the output) and `client_descriptor` (for example "a PE-backed UK healthcare
   group"). Never write the client's name in your reply or any draft.
4. **Show the brief** in two to six lines and the gaps you left out ("no salary
   given"). If the user already asked for the document, go straight on.
5. **Render.** `render_search_document` with `template_key`
   `position-specification` and the brief; `kit_id` only if the user wants a client's
   brand (`list_brand_kits`). Takes up to a few minutes.
6. **Announcement (only if asked).** `create_launch_announcement` with the same brief:
   two post drafts and graphics. Formatix does not post; the user posts after the
   client agrees. Never post or publish for them.
7. **Report.** Download links, the gaps to confirm with the client, and the offer to
   draft the announcement or a candidate outreach teaser later
   (formatix-recruitment-documents: appointment brief, role teaser).

## Optional connected apps

If the user asks and has a CRM or ATS connected (HubSpot, Salesforce, Recruit CRM,
Manatal), you may read the job record to fill gaps the user confirms, or attach a
note that the specification was drafted. Do not create or change records unasked.
