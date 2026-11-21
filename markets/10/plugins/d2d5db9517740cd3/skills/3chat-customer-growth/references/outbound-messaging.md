# Outbound Messaging

Sending changes external state. Do not call a send tool when the user only requests analysis, audience selection, drafting, or preview.

## Confirmation

Immediately before sending, show the exact customers, sender account or channel, final text, attachments, and single or batch scope. Send only after explicit confirmation. Reconfirm after any business parameter changes.

## Attachments

- Use an existing final directly downloadable HTTP/HTTPS URL when available.
- The URL must not require authentication, custom headers, an interactive page, or redirect-only short link.
- Otherwise call `upload_3chat_attachment`.
- Prefer passing the complete returned `data.attachment` into `attachments`; at minimum pass `data.attachment.url`.
- Never shorten, rewrite, escape, or Markdown-wrap the URL.
- Successful upload does not mean a message was sent.

## Single and Batch Sends

- Customer single send: use `send_3chat_customer_message` with one resolved `customer_id`.
- Generate a stable idempotency key for one logical send; reuse it only for an explicitly permitted same-request retry.
- Customer batches support at most 100 items; prefer 1 to 3.
- Every `items[]` entry has its own confirmation token and idempotency key.
- After receiving `job_id`, query the original task and never recreate the batch.
- `data.results[].success` determines whether each item was processed successfully.

`accepted`, `sent`, and `COMPLETED` are processing states, not proof of channel delivery or read status.
