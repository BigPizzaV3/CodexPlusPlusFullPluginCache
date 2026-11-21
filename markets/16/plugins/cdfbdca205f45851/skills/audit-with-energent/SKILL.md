---
name: audit-with-energent
description: Send a deliverable and its source files to Energent for an independent audit, follow the audit until it finishes, and show the findings and the report. Use when the user asks to audit, verify, fact-check or double-check numbers, claims or calculations against source data, or asks for a re-audit after fixes.
---

# Audit with Energent

Energent runs an independent audit of work in its own sandbox. The auditor checks each number and claim against the source files and writes a report.

## Start an audit

1. Collect the deliverable (the work to check) and the source files (the data it is based on). Use only files and text that the user gave in this conversation.
2. Call `energent_start_audit`. Put a short description of what to check in the request, and send the files inline. For files larger than 10 MB in total, call `energent_prepare_upload` first and upload each file to the URL it gives.
3. Call `energent_wait`. If the result has `timed_out: true`, call `energent_wait` again. Repeat until the audit stops running.

## Read the results

- When the status is `completed`, show the final answer: each claim with pass or fail, the correct value, and the reason.
- Call `energent_list_files` to find the report. Call `energent_get_file` to read it, or give the user its download link.
- Give the user the `web_url` so they can open the full audit in the Energent web app.

## Other statuses

- `needs_input`: the auditor has a question. Show it to the user. Send the user's answer with `energent_reply`, then call `energent_wait` again. The user can also answer in the Energent web app.
- `failed`: tell the user that the audit failed and show the error message.
- An error about credits or file uploads: show the link in the message, where the user can add credits.

## Re-audit

After the user fixes the errors, call `energent_reaudit` with the updated work. The auditor keeps the earlier findings and checks what changed. Then follow the steps in "Read the results".

## Stop

If the user asks to stop or cancel the audit, call `energent_stop`.

## Limits

- Energent does not open links. Ask the user to attach the files.
- Energent does not send email or messages, and it cannot see the user's other Energent conversations.
