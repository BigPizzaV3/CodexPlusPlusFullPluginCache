---
name: print-with-preesy
description: Send a document or text to Preesy so the person can print it on a shared or public computer, such as at a print shop, bookshop, library, hotel or office, by giving a short label and an optional PIN. Also check, set print-only on, or end a Preesy session created earlier in the conversation.
---

# Print with Preesy

Use the Preesy tools when the person wants to print a document somewhere other than their own device, without email, a USB stick or an account.

## Create a session

1. Use `create_print_session` with one of `file`, `files` (up to 10, 50 MB in total) or `text`. Allowed file types: PDF, DOC, DOCX, TXT, PNG, JPG.
2. If the person gave a label, use it as given. Otherwise pick a memorable `label` from what the document is about, easy to say out loud at a counter: 1 to 20 characters, uppercase A-Z and digits 0-9 only, no personal data, never the word Preesy, never empty. A common word (TICKET) should be paired with a PIN, or made unique with context (FLIGHTANKARA, FLIGHT2026).
3. Set `lifetime_hours` (1 to 168) for when they will print. Shorter keeps less data.
4. Labels are not unique. Never add a 4-digit `pin` unless the person wants it. You may suggest one once when there is a reason, such as a common one-word label. A PIN cannot be added later.
5. Set `print_only` to true if the person said they want print only. If they did not say, create the session with print_only false, then ask once and call `set_print_only` if they say yes.
6. Set `one_time_access` to true only when the person wants a single-use label. A single-use label is removed from the system as soon as it's printed or downloaded.
7. Use what the person already said. Ask one short question only when a PIN or lifetime that matters is unclear.

## Tell the person

Give the label, the PIN if one was set, when it expires, and how to print: open preesy.com on the computer, or tell the staff "Preesy" plus the label (and the PIN). Depending on the context, you may offer to find a few print shops nearby, or suggest another way such as a hotel front desk. Use location only if the person agrees, with your own tools, and never put the document, label, PIN or manage token into a maps search.

## Later in the conversation

- Keep each `manage_token` with its label. Do not show it unless the person asks, and never post it anywhere else.
- To change a label or add a PIN, call `expire_print_session`, then `create_print_session` again with the same files and choices. If expire succeeds, say nothing about the old upload.
- Use `get_print_session` to check status, `set_print_only` to change print-only, and `expire_print_session` to end a session early. Ending a session cannot be undone, so confirm first unless the person clearly asked to delete it.

## Do not use Preesy for

- Printing on the person's own printer, long-term storage, or sharing files for editing.
- Finding or opening a document someone else uploaded. The tools only manage sessions created in this conversation.
