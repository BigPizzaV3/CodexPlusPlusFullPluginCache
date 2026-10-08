---
name: june-create-case-document
description: Create a case document in JUNE from an approved template, supplied text, or an uploaded local file. Use when a user asks to draft, render, file, or upload a document for a specific JUNE case, including DOCX and PDF output.
---

# Create a JUNE case document

Identify the exact case first. Document creation writes data and can create duplicates, so do not guess identifiers or retry automatically.

## Choose the path

### JUNE template

1. Resolve the case with `get_case_by_reference` or `get_case_context`.
2. Call `list_document_templates` for that case before creation.
3. Select only a returned `template_id`, supported output format, and returned addressee `participant_id`. A contact ID is not a participant ID.
4. If the template is blocked or the intended addressee is absent, explain the missing participant role. Use `create_contact` and `add_case_participant` only when the user asks to add that participant.
5. Confirm the case, template, addressee, format, and any claims-account options when they are not already explicit.
6. Call `create_case_document` once.

For PDF, report the filed document ID. For DOCX, surface the short-lived download URL immediately and explain that the file is not yet filed in the case. If the template is designed for interactive editing, retain that warning.

### Text document

Use `create_document_from_text` only after confirming the target case, safe filename, direction, document type, and final text. Preserve user-supplied wording unless asked to edit it.

### Local file upload

Use `request_document_upload` and `finalize_document_upload` only when both tools are available and the client can upload the file bytes to the returned URL with every required header. Resolve `document_type` with `get_value_list` first. Use only letters, digits, spaces, dot, hyphen, and underscore in filenames.

If the client cannot perform the binary upload, tell the user to download or edit the file and file it through JUNE instead of pretending the upload completed.

## Safety and result

Every `create_case_document` call creates a new document. After an error or timeout, check the case before retrying. Do not expose a short-lived download URL beyond the user who requested it. Report the case reference, filename, output format, whether it was filed, document ID when present, and the required next step.
