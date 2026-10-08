---
name: combine
description: Combine two or more independently written documents into one Word draft with attributed tracked changes. Use when the documents have no shared original.
---

# Combine independent drafts

1. Confirm that the documents were written independently. If they are edits of one
   original, use merge. Ask when that distinction is unclear.
2. Confirm the author label for each document. Do not guess authors or ask the user
   to order independent documents.
3. Call `get_instructions`, then `create_combine` with the attached files in
   `document_files` (or accessible file paths), original names, and the confirmed
   `document_authors`.
4. Follow the upload instructions if the result asks for uploads, then call
   `get_combined_document` until generation finishes.
5. Download and present the Word document in the conversation with its interactive
   link. Use `read_text` only when the user requests analysis.

Excel is unsupported for this workflow. Explain that limitation before starting.

Selected documents are uploaded to Version Story and stored in the user’s account.
Follow the user’s explicit instructions. Use only files they selected and that this
session can access. Complete OAuth through the host’s sign-in flow; never request
passwords or tokens in chat. If files are unavailable, ask the user to attach them.

When a transfer or tool call fails, report it with `report_issue`, omitting document
contents and credentials, then explain the failure and stop. If the account limit is
reached, tell the user, give them the upgrade link from the message, and stop.
