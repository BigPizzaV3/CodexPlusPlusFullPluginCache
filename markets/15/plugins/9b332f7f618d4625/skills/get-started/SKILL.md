---
name: get-started
description: Use when the user wants to send a document for e-signature with Docflare, check on documents they sent, or asks what Docflare can do.
---

# Get started with Docflare

Docflare sends documents for e-signature. The user attaches a PDF, or gives a public link to one, and says who signs. Docflare makes a draft of it, and the draft is sent only after the user confirms a preview.

## Send a document

1. Call `upload_document` with the attached file as `file`, or with a public https link as `url`. The answer lists the text on the pages and the blank lines a field can sit on.
2. Call `prepare_document` with the recipients by email: `signer` for people who sign, `cc` for people who get a copy. Add any send settings the user asked for, such as expiry or reminders.
3. With more than one signer, ask the user whether they all sign one shared copy or each get their own, and pass the answer to `edit_document` as `type`.
4. Call `edit_document` to place each signer's signature, and any date or name fields the user wants, on the line it belongs to, by the line's id.
5. Show the user the whole preview from the last answer, with its `preview_url`, and wait for their yes. After any change, show the new preview.
6. Call `send_document` with the `review_token` and the email of every recipient in that preview.

## Check on documents

- `document_status` lists documents by status or name, with each signer's progress and, once everyone has signed, a link to the signed copy.
- `get_document` gives every detail of one document.
- `archive_document` moves a draft the user no longer wants to the trash, where they can restore it.

## Good to know

- Nothing is sent until the user confirms. If the document changes after the preview, the send is refused and a new preview is needed.
- Docflare works in the workspace the user last opened in Docflare, within their plan's limits.
- Signers do not need a Docflare account. Someone without one can sign up for free at https://docflare.app.
