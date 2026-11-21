---
name: translate-candidate-profile
description: Translate a candidate profile or CV into another language in the firm's template, keeping the layout - for example a German Lebenslauf from an English CV, or a French candidate profile for a client in Paris. Use when a recruiter asks to "translate this CV", "make this profile in German" or "send the client a French version".
---

# Translate a candidate profile

Done when: the user has a new document in the requested language, in the firm's
template, with names, employers, dates and figures unchanged.

Explicit instructions from the user take priority over this skill.

## Ground rules

- Reply in the user's language.
- Translate, never improve: add no facts. Keep names, employers, product names, dates
  and figures as they are. Keep qualifications in their original form when there is no
  exact equivalent, and say which ones.
- 1 credit per candidate: this is a new document. Say so if the user did not clearly
  ask for it. Pass a `request_id` and reuse it on a retry.
- The template's own headings stay in the template's language. If they should change
  too, say so first and look for a template in that language with `find_template`.

## Steps

1. **Get the source:** the CV the user shared, or the details of a document Formatix
   made (`get_cv_details` with its `record_id`; no credits).
2. **Choose the template:** the one the user named, else `find_template`, preferring
   one in the target language. Read `get_template_schema`.
3. **Translate** each field into the target language, using the terms a recruiter in
   that country would use. Follow the template's extraction prompt for everything else.
4. **Fill:** `fill_template`. If Formatix answers `looks_like_correction`, explain that
   this is a new document using credits, and re-send with `confirm_new_document=true`
   only after a yes.
5. **Report:** the link, one line on what was left untranslated and why, and a reminder
   to have a fluent speaker check it before it goes to a client.
