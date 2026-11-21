---
name: generate-document-from-data
description: Make a PDF or Word document from one of the user's DocsAutomator automations with data the user gives in the chat, and send it for signature or acceptance when the automation has that step. Use when the user asks to create, fill or send a document such as an invoice, contract or certificate with DocsAutomator.
---

# Generate a document from data

## First check

If no DocsAutomator tools are available, tell the user plainly that DocsAutomator is not signed in. To fix it, they open Settings, then MCPs, choose docsautomator and choose Authenticate, then start a new chat. Do not try to do the task another way.

## Steps

The main path: you are the data source. You read the placeholders and send the values with `create_document`.

1. Find the automation. Call `list_automations` with `search` set to the document type the user names, for example "Invoices". If several match, ask the user which one.
2. Call `get_automation`. It returns the data source, whether the automation has a closing step (`esignature.enabled` and `closeType`) and the placeholders. Follow the `descriptions` it returns for each placeholder. Ask the user for any value you do not have. Do not invent amounts, names, dates or addresses.
3. Send raw values: numbers as numbers and dates as ISO dates (2026-10-01). DocsAutomator formats them.
4. If the automation reads from a record source (Airtable, Notion, Google Sheets, SmartSuite, ClickUp or Google Forms), send from this automation with the record id (`recId`). The record fills the document, and the signer emails come from its mapped fields. These tools cannot search records, so get the record from the user. Never copy the automation and never change its data source to send.
5. Call `create_document`:
   - `mode: "preview"` when the user only wants to see the document. Nothing is sent or saved.
   - `mode: "test"` for the first send of a new setup. Test mode sends the real email and adds a preview watermark.
   - `mode: "live"` only when the user asks for a real, counted document.
   - `recipients` with the name and email of every signer or recipient when the automation has a closing step. With `recId`, pass `recipients` only when the user names a different person. Ask the user for missing email addresses. Never guess one.
6. Give the user the PDF link, and the Word link when the automation saves one.

## Follow the request

- `list_esign_sessions` with `status: "open"` shows who has not signed or accepted yet. `waitingOn` names each pending recipient.
- `manage_esign_session` with `action: "remind"` and the `signerIndex` from `waitingOn` reminds one recipient. Ask the user before you call it, because it sends an email.
- `list_esign_sessions` with `sessionId` shows the status and, when it is completed, the final PDF.

## Rules

- Ask before any call that sends email or creates a live document.
- Show the document with `mode: "preview"` and confirm with the user before you send it.
- Templates are Word templates with placeholders. Never create or edit a Google Doc.
- Build reusable templates: the case details become placeholders. Never fill in a one-off document.
- Do not describe an acceptance as legally binding.
