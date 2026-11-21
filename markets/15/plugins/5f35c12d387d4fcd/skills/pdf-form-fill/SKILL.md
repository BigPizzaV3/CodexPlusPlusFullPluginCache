---
name: pdf-form-fill
description: List the fields of a fillable PDF form with list_form_fields and fill them with fill_pdf_form, then return the filled PDF with a read-back check.
---

# Zovo PDF Form Fill

Use this skill when the user attaches a fillable PDF form and wants to see its fields or have it filled in.

1. Call `list_form_fields` with the attached `file`. It returns each field's full `name`, `type`, `label` (the printed text next to the field), options, `required`, `max_length` and page, 40 fields at a time. For a long form, call it again with `start` set to `next_start`, or with `page`.
2. Map the user's answers to fields by the `label`. Ask the user for values that are missing or unclear. Do not guess values for required fields.
3. Call `fill_pdf_form` with the same `file` and `values` as a list of `{field, value}`. Use the `name` as listed. Use text for text fields, `true` or `false` for checkboxes, one listed option for radio groups and dropdowns, and a list of options for multi-select list boxes. An empty string clears a field. Set `flatten: true` only when the user wants the answers locked into the page.
4. If the call is refused, nothing was filled. Read the message: it names unknown fields with the 3 closest names, options that are not listed, and text that is over the field's maximum length. Fix those values and call again.
5. Report the filled count, the read-back check (how many values were read back from the new PDF and match), required fields still empty, skipped fields, and the download link. Say that the link expires in about 1 hour.

Limits: standard fillable (AcroForm) PDFs up to 20 MB and 2,000 fields. XFA-only forms and password-protected PDFs are refused with a reason. Signature fields are not signed; tell the user to sign the downloaded PDF with a signing tool. Field text can use Latin, Greek, Cyrillic and Vietnamese letters; CJK, Arabic, Hebrew and emoji are refused.

Do not use this skill for flat PDFs without form fields, for scanned paper forms, or to sign a document.
