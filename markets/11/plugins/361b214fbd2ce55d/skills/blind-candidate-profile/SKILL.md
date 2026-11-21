---
name: blind-candidate-profile
description: Make a blind CV or anonymised candidate profile for a client - the candidate's name, contact details and photo removed, in the firm's template, ready for a first submission or fair, bias-free screening. Use when a recruiter asks to "anonymise this CV", "make a blind CV", "remove the candidate's name" or "send an anonymous profile".
---

# Blind candidate profile

Done when: the user has a document in the firm's template with nothing that names or
contacts the candidate, and a list of what was removed.

Explicit instructions from the user take priority over this skill.

## Ground rules

- Reply in the user's language; the document follows the template's language.
- Use only facts in the CV. Never invent or replace employers, dates or achievements.
- 1 credit per candidate. Say so if the user did not clearly ask for the document.
- Pass a `request_id` and reuse it on a retry.
- This is a new document, not a correction: `edit_formatted_cv` cannot change a name.

## Steps

1. **Choose the template:** `find_template` with "blind profile" or the template the
   user named. A template with a photo slot stays empty: send no photo.
2. **Ask once what to hide** beyond the defaults, if the user has not said: current
   employer names, education institutions, age or nationality.
3. **Read the CV yourself** and follow `get_template_schema`. Always remove the name,
   email, phone, home address, personal links (LinkedIn included), photo, date of
   birth and referees. Use `Candidate A` as the name unless the user gives another
   label. Also remove these details where they appear inside the summary or
   achievements, and anything else that identifies the person.
4. **Fill:** `fill_template` with the candidates and `candidate_name` `Candidate A`.
   If Formatix answers `looks_like_correction`, explain that this is a new document
   using credits, and re-send with `confirm_new_document=true` only after a yes.
5. **Report:** the link, what was removed, and what could still identify the person
   (a rare job title, a small employer). Ask the user to check it before it goes out.
