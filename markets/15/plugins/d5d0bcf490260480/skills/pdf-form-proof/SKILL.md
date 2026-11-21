---
name: pdf-form-proof
description: Fill a fillable (AcroForm) PDF form the user attaches and prove the result shows on the page. Use when asked to fill out, complete, inspect, or check a PDF form (grant, intake, consent, or any agency form), when a filled field "looks blank", or when a form must be verified before it is sent. Inspect exact field names, fill by name with unknown names refused, then read the rendered page back to confirm each value shows.
---

# pdf-form-proof

Every tool takes the PDF the user ATTACHED as its `file` input. Never ask the
user for a file path, and never paste file contents into a tool call.

## 1. Inspect

Call `pdf_form_inspect` with the attached file. Copy field names exactly as
returned. For checkboxes, note `on_states` (for example "/Yes").

- `kind` is `none`: the PDF has no fillable fields (a flat or scanned page).
  Say it cannot be filled by this tool. Do not call `pdf_form_fill`.
- `kind` is `xfa`: an XFA-only form; this tool does not fill it.

## 2. Fill and prove (one call)

Call `pdf_form_fill` with the attached file and a `values` map of exact names.
A checkbox takes `true` or its on-state. The call fills the form in memory,
reads every value back, renders the page and OCRs it, and returns a proof
receipt: `input_sha256`, `output_sha256`, `fields_written`,
`read_back_mismatches`, and `rendered_page_check` (verdict PASS when every
text value is VISIBLE).

- Leave `strict` on. If the result is `refused` with `unknown_fields`, tell
  the user which names do not exist and offer the real ones from step 1.
  Never retry with `strict=false` to make an error go away.
- Report the receipt to the user: status, both hashes, the fields written,
  and the page-check verdict. Repeat the limit: this proves the values show,
  not that they are correct.
- No PDF file comes back in chat. `include_base64` stays false unless the
  caller is a program that can save a file.
- Ask the user for any value you do not have. Never invent a value, and never
  decide what an official form should say on the user's behalf.
- Do not put government identifiers (such as Social Security numbers),
  payment card numbers, or health information into a fill.

## 3. Verify an already filled PDF

Call `pdf_form_verify` with the attached file and the values the user expects
to see. Each value gets VISIBLE, INVISIBLE, RENDER-ONLY, or MISSING. On a
blank form an expected value is MISSING, which is the correct answer.
`REFUSE` with `kind: tool_failure` means the check did not run; make no
claim about the document.

## Fingerprint

`pdf_sha256` returns the SHA-256 and byte size of the attached file.

## Limits

AcroForm only. No signatures. OCR can misread small or stylized fonts. This
tool fills forms; it does not give legal, tax, or benefits advice.
