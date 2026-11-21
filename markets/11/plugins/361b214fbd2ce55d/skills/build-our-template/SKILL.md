---
name: build-our-template
description: Turn the firm's own Word, PowerPoint or Excel document (a candidate profile, CV layout, shortlist deck or candidate tracker) into a reusable Formatix template that keeps its fonts, colours, logos and layout, check it with a preview, and change it later in plain language. Use when a recruiter or executive search firm says "make this our template", "use our CV format", "set up our house style", "turn this profile into a template" or "change our template".
---

# Build the firm's template from its own document

Done when: Formatix has saved the template without problems, the user has seen the
preview pages (an invented example candidate) and knows the template's name - or
the user knows exactly what to fix in their file.

Explicit instructions from the user take priority over this skill.

## Ground rules

- Reply in the user's language. The template stays in its document's language.
- Use only the file the user attached in this conversation and asked to turn into a
  template. Keep its design; never promise styling it does not have.
- Templates Formatix set up for the firm are read-only: when the user wants something
  different, build a NEW template; the original is never touched.
- Never put the firm's or a client's template, logo or candidate data in anything
  public. Ask the user to remove real candidate details from the file if it holds
  any; the preview uses an invented candidate.

## Main path - you design it (no credits)

1. Ask for the file if it is not attached (.docx, .pptx or .xlsx) and a title.
2. Read `get_template_design_guide` and follow it.
3. In your code tool, work on a COPY of the user's file:
   - replace only the candidate's details with fields; keep fonts, colours, logos,
     spacing and layout;
   - Word: the candidate inside `{%p for c in parsed_resume %}` ... `{%p endfor %}`
     (each on its own line), fields `{{ c.Field_Name }}`; never the dash forms
     `{%-` / `-%}`; lists in one paragraph with line breaks keep bullets tight;
   - PowerPoint and Excel: as the design guide says (A_/B_ prefixes for several
     candidates per slide).
4. Write the extraction prompt (one line per field; dates, letter case, tone,
   pronouns and bullet length follow the user's document and what the user says -
   ask when unclear; never invent) and a JSON schema listing every field.
5. `push_designed_template` with the file, `title`, `template_format`, prompt,
   schema and a `request_id`. If it returns `problems`, nothing was saved: fix them
   and push again.
6. Show the preview pages and compare them with the user's document. Offer to format
   a CV with it (format-cvs, `template_type` `cvtobios`).

## Quick path - Formatix builds it (1 credit)

Offer when the user wants it fast or the document is complex:
`create_template_from_file` with the attached file and a title, then
`check_template_status` until `ready`. It is then a `user_template`.

## Change the firm's own template later

`refine_template` with the template's id, one clear instruction ("add a languages
section after education", "make the headings navy") and a `request_id`
(`template_type` `cvtobios` for one saved with `push_designed_template`).
Formatix changes it in place and keeps every earlier version; `get_refine_status`
if it is still working. If it asks a question, pass it on and wait.

## Filling it here

The user's OWN templates can be filled in the conversation: `get_my_template_file`
(24-hour link) plus `get_template_schema`. Templates Formatix set up for the firm
are filled only with `format_cv` or `fill_template`; never offer another way round
credits.
