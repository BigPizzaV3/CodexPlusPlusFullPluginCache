---
name: compare
description: Compare document versions and create a PDF redline or Word tracked-changes file. Use when the user requests a comparison, redline, blackline, or explanation of changes.
---

# Compare documents

1. Identify the original and revised documents. Ask which is the original if unclear.
2. Call `get_instructions` for the current connector workflow.
3. Use `create_comparison` for files: pass attached files in `base_file` and
   `comparison_files`, or accessible file paths. Use `create_comparison_from_links`
   for HTTPS document links. Follow the upload instructions only when the result
   asks for uploads.
4. Use `get_redlines` to obtain the finished documents. Leave `download_options` unset
   for the normal viewable redline. Request `word_redline` when the user asks for Word
   or tracked changes.
5. Download and present the actual result file in the conversation, with the interactive
   redline link. Use the file presentation supported by this OpenAI environment.
6. If the user requests an explanation of the changes, use `read_text` as the source
   for that analysis. A request for a redline alone does not request a summary.

Selected documents are uploaded to Version Story and stored in the user’s account.
Follow the user’s explicit instructions. Use only files they selected and that this
session can access. Complete OAuth through the host’s sign-in flow; never request
passwords or tokens in chat. If files are unavailable, ask the user to attach them.

When a transfer or tool call fails, report it with `report_issue`, omitting document
contents and credentials, then explain the failure and stop. If the account limit is
reached, tell the user, give them the upgrade link from the message, and stop.
