---
name: check-manuscript
description: Select or upload a DOCX/PDF manuscript and start Paperpal checks. Use for generic requests to check, review, assess readiness, or upload a manuscript when the user has not identified an existing Paperpal document.
---

# Check a manuscript

1. Confirm the Paperpal connector is available. If it is disconnected, ask the user to connect it before continuing.
2. If the current message has a DOCX or PDF attached and the host supplies both `file_id` and a real `download_url`, call `check_attached_document` with that attachment. Do not call `show_document_upload` afterward. If the host supplies only a private file id or sandbox path, call `show_document_upload` so the user can select the file; never invent a download URL.
3. Otherwise call `show_document_upload`, including for generic requests such as “check my paper” or “is the manuscript ready to submit?” Pass `document_name` only when the user supplied a save-as name. Do not search existing results for generic phrases such as “the manuscript”.
4. Let the Paperpal app handle file selection and upload. Never ask for a server-local path or request base64 content in chat.
5. Start the selected checks only after upload succeeds and the user confirms the action in the app.
6. Show the returned progress app. Do not repeatedly poll or hold the task open while checks run.
7. On a later refresh request, call `get_check_run_status` with the available run ID.

Use only real Paperpal results. Clearly identify pending, failed, unavailable, and quota-limited checks. Do not invent findings or completion estimates.
