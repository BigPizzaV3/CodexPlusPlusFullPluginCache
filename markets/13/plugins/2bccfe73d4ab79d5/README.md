# Mizar — invoice PDFs from your notes

Mizar creates invoices as PDFs from your notes, hours, or timesheets inside ChatGPT — a business-admin productivity
tool for freelancers and small businesses. Published by Midchat · https://midchat.io/mizar/

## What it does

- Turns notes, hours, or a timesheet into invoice line items for you to confirm.
- Checks common invoice fields (seller and client details, invoice number, dates, tax rate, payment details) and asks
  for missing ones; checks the IBAN checksum.
- Calculates line amounts, VAT per rate, discounts, and the total with decimal arithmetic, rounded to the cent.
- Renders a one-page invoice in English or German as a PDF and printable HTML via a download link that expires after
  about an hour. Missing fields appear as visible placeholders on a document marked DRAFT.

Please review each invoice before sending it.

## Limitations

Mizar does not send invoices, take payments, create structured e-invoices (XRechnung/ZUGFeRD), store invoice data, or
give tax or legal advice, and it does not confirm that an invoice meets the legal requirements of your country.

## How it works

- MCP server: `https://mcp.midchat.io/mcp` (streamable HTTP, no sign-in) with three read-only tools:
  `validate_invoice_fields`, `compute_invoice_totals`, `render_invoice`.
- Skill: `skills/invoice-from-notes/` guides the conversation (gap check → confirm → totals → render) and keeps
  code / chat-only fallbacks.

Privacy: https://midchat.io/mizar/privacy/ · Terms: https://midchat.io/mizar/terms/ · Support: https://midchat.io/mizar/support/
