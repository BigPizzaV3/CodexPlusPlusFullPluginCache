---
name: version-history
description: Trace changes through successive versions of a document and create one Word document attributing surviving changes to their source versions. Use for requests about how a document evolved or who introduced a change.
---

# Trace a document’s history

1. Establish the versions in chronological order, oldest first. If the user has not
   specified the order, propose it from the names or dates and obtain confirmation.
   Incorrect ordering changes attribution.
2. Confirm each version’s author label with the user. Use supplied names and do not
   invent authors.
3. Call `get_instructions`, then `create_version_history` with the attached files in
   `version_files` (or accessible paths) in the confirmed order, original file names,
   and the confirmed `version_authors`.
4. Follow the upload instructions if the result asks for uploads, then call
   `get_version_history_document` until ready.
5. Download and present the Word document in the conversation. Use `read_text` when
   the user requests an explanation or asks about a particular change.

Excel is unsupported for this workflow. Explain that limitation before starting.

Selected documents are uploaded to Version Story and stored in the user’s account.
Follow the user’s explicit instructions. Use only files they selected and that this
session can access. Complete OAuth through the host’s sign-in flow; never request
passwords or tokens in chat. If files are unavailable, ask the user to attach them.

When a transfer or tool call fails, report it with `report_issue`, omitting document
contents and credentials, then explain the failure and stop. If the account limit is
reached, tell the user, give them the upgrade link from the message, and stop.
