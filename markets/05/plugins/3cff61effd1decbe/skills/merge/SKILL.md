---
name: merge
description: Merge two or more parallel revisions of the same original into one Word document with attributed tracked changes. Use when reviewers edited separate copies of a shared base.
---

# Merge parallel revisions

1. Identify one original and at least two revisions of it. Ask which draft everyone
   started from when the shared base is unclear. If the drafts were written
   independently, use the combine workflow. If they form a chronological chain,
   use version history.
2. Confirm the author labels for the revisions. Do not guess authors. Revision order
   does not change the result, so do not ask the user to order parallel edits.
3. Call `get_instructions`, then `create_merge`, passing attached files in `base_file`
   and `next_version_files` (or accessible file paths), original file names, and the
   confirmed `next_version_authors`.
4. Follow the upload instructions if the result asks for uploads, then call
   `get_merged_document` until generation finishes.
5. Download and present the Word document in the conversation with its interactive
   link. The user resolves competing tracked changes in Word. Use `read_text` only
   when the user requests analysis.

Excel is unsupported for this workflow. Explain that limitation before starting.

Selected documents are uploaded to Version Story and stored in the user’s account.
Follow the user’s explicit instructions. Use only files they selected and that this
session can access. Complete OAuth through the host’s sign-in flow; never request
passwords or tokens in chat. If files are unavailable, ask the user to attach them.

When a transfer or tool call fails, report it with `report_issue`, omitting document
contents and credentials, then explain the failure and stop. If the account limit is
reached, tell the user, give them the upgrade link from the message, and stop.
