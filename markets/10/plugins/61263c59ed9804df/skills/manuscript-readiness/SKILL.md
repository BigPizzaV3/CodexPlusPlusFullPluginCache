---
name: manuscript-readiness
description: Start or assess a Paperpal manuscript-readiness check. Use when the user asks whether a manuscript is ready to submit, what needs attention, or which Paperpal findings should be fixed first.
---

# Assess manuscript readiness

1. Resolve the document source before assessing readiness:
   - Current message has a DOCX/PDF attachment: call `check_attached_document`.
   - A `check_run_id` for this manuscript already exists in the conversation (from an earlier `check_attached_document`/`get_check_run_status` call or its rendered card): call `get_check_run_status` or `get_check_run_findings` with that ID.
   - No attachment and no `check_run_id` already in the conversation: call `show_document_upload`. Generic phrases such as “my paper”, “the manuscript”, and “this document” are not identifiers, and there is no tool to look a document up by filename, title, or library listing — never search or ask for one.
2. Let the upload/check-selection app run before attempting an assessment.
3. Base the assessment only on completed Paperpal checks and their returned details.
4. State the coverage first: completed checks versus pending, failed, or unavailable checks.
5. Group attention into `Resolve before submission`, `Review`, and `No reported issue` only when supported by results.
6. Keep the recommendation concise and direct the user to Paperpal for editing.
7. In case of a check/API failure, direct the user to https://edit.paperpal.com/ to retry.

Never convert an incomplete check set into an overall approval. Treat plagiarism output as a signal requiring human review, not proof of misconduct.
