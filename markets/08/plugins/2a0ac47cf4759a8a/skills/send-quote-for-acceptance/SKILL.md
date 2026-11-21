---
name: send-quote-for-acceptance
description: Make a quote in the user's own brand with DocsAutomator and send it to them for acceptance, so they can accept it and see the accepted PDF in DocsAutomator. Use when the user wants to send a quote or proposal for acceptance, or asks how to start with DocsAutomator.
---

# Send a quote for acceptance

You make a quote in the user's brand and send it to the user for acceptance. The user accepts it from the email and sees the accepted PDF and its record in DocsAutomator under Documents.

## First check

If no DocsAutomator tools are available, tell the user plainly that DocsAutomator is not signed in. To fix it, they open Settings, then MCPs, choose docsautomator and choose Authenticate, then start a new chat. Do not try to do the task another way.

## Before you start

Ask for two things in one message: the user's email address (the quote goes to them) and, optionally, their website (for the brand colors and logo).

## Steps

1. Call `list_automations`. If a quote automation exists, ask the user whether to reuse it; to reuse it, go to step 6. Otherwise call `create_automation` with `title: "Quotes"` and `dataSourceName: "API"`.
2. Call `generate_word_template` on the new automation:
   - `title: "Quote"` and `signingMode: "none"`, because acceptance needs no signature block.
   - `brandWebsite` set to the user's website, when they gave one. It reads their brand colors and logo.
   - A prompt for a one-page quote: logo, quote number, date, valid-until date, sender and client details, a line items table (description, quantity, rate, amount), subtotal, tax, total and terms.
3. If generation fails, call `search` with `in: "templates"` and the query "quote", then `set_template` with the `galleryTemplateId` of a result that has a Word version.
4. Call `configure_placeholders` with a description for every placeholder and a format for every amount and date. Set the user's `locale` with `configure_automation`.
5. Call `configure_esignature` with `closeType: "acceptance"`, `deliveryMethod: "email"` and one signer `{ role: "Client", emailSource: "request" }`.
6. Call `get_automation` for the placeholders. Fill every placeholder with realistic sample data for the user's business. Send numbers as numbers and dates as ISO dates.
7. Call `create_document` with `mode: "test"` and `recipients: [{ signer: 1, email: <user's email>, name: <user's name> }]`.
8. Tell the user to open the email from DocsAutomator, type their name and click Accept.

Test mode sends the real email and adds a preview watermark.

## Done

The quote is accepted when `list_esign_sessions` with the `sessionId` returns `status: "completed"`. Then give the user the accepted PDF (`signedPdfUrl`) and the record at https://app.docsautomator.co/documents.

## Next steps

Suggest one of these:
- Send it to a real client: call `create_document` again with `mode: "live"` and the client's email in `recipients`. Ask the user before you send.
- Make the quote from Airtable: the user connects Airtable in the DocsAutomator app under Settings, Integrations. Then call `set_data_source` with the table and the field `mappings`.
- Use the user's own Word template: call `set_template` with their .docx file as `fileBase64`.

## Wording

- Say "accept" and "acceptance". Do not say "sign" for this flow.
- Do not describe an acceptance as legally binding.
- Never accept a document for a recipient. Only the recipient can accept, through the link in their email.
