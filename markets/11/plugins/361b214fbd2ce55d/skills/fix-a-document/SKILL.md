---
name: fix-a-document
description: Change a candidate profile or formatted CV that Formatix already made - rewrite or shorten the summary, correct a date or job title, add a qualification, reorder roles, or give the candidate a new photo - and get the same document back in the same template at no credit cost. Use when the user says "fix", "correct", "change", "update", "shorten" or "add" something in a CV, profile or shortlist Formatix produced.
---

# Fix a document Formatix made

Done when: the user has the corrected document's new download link and a one-line
summary of what changed - or a clear explanation of why the change needs a new
document and what that costs.

Explicit instructions from the user take priority over this skill.

## Ground rules

- Reply in the user's language; keep the document's language unless asked.
- Changes use only facts the user gave or that are in the candidate's CV.
- A correction is ALWAYS `edit_formatted_cv` - never `fill_template` or `format_cv`
  again (that is a new document and charges credits again).
- Edits are free, up to 3 per document (a photo counts as one). At most about a fifth
  of the text may change. The candidate's name cannot change.
- Studio documents (`template_type` `user_template`) cannot be edited this way.

## Steps

1. **Find the document.** Use the `record_id` from this conversation. If you do not
   have it, ask the user which document (Formatix needs the record from the result
   that made it).
2. **Read it:** `get_cv_details` with the `record_id`: the details per candidate
   (`candidate_index`), whether the photo can change, how many changes are left.
3. **Write the change** yourself in the same shape as the details: send only the
   fields that change (a list field is sent whole), for example
   `[{"candidate_index": 0, "details": {"Summary": "..."}}]`.
4. **Apply:** `edit_formatted_cv` with `record_id` and `changes`. Each call rebuilds
   the document once and uses one of its 3 changes, so put all the corrections the
   user asked for into one call.
5. **Photo:** `set_candidate_photo` with the photo the user attached (`photo_file`)
   or a public `photo_url`, and `candidate_index`. Only if `get_cv_details` says the
   template has a photo slot; otherwise say the template has no place for a photo.
6. **Report:** the new link (works for an hour) and what changed; ask the user to
   check it. Earlier versions are kept in Formatix.

## Ask first - never decide alone

- **Rename / different candidate / big rewrite / another template / another
  language:** this cannot be an edit. Say so, say it is a new document costing 1
  credit per candidate, and wait for a yes. Then use format-cvs (or
  translate-candidate-profile / blind-candidate-profile).
- If that new fill is refused with `looks_like_correction` (same candidate, same
  template, within the hour), re-send with `confirm_new_document=true` only after the
  user confirms the new charge.
- **No changes left:** say so and offer a new document (credits) or editing the
  downloaded file by hand.
- Never change the template itself here; template changes are build-our-template.
