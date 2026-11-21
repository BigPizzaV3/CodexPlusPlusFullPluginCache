---
name: invoice-from-notes
description: Creates invoices (PDF) from notes, hours, or timesheets inside ChatGPT for freelancers and small businesses. Use when the user wants to create an invoice from notes, generate an invoice PDF, bill a client from a timesheet or hours, or draft an invoice with line items, tax, VAT, and payment terms. Trigger on phrases like "create an invoice from these notes", "generate invoice PDF", "make an invoice for this client", "invoice from timesheet", "draft an invoice with tax", "turn this into an invoice", "invoice with line items and VAT", "bill this client for last week's work", "convert these hours into an invoice", or "invoice PDF with payment terms".
---

# Notes / timesheet → invoice PDF (Mizar)

Turn messy work notes, hours, or a timesheet into a structured invoice — numbers confirmed by the user, totals calculated with decimal arithmetic, rendered as a PDF where possible. Mizar does not give tax or legal advice; the user reviews the invoice before sending it.

Explicit user instructions (template choice, wording, rounding, numbering) override the defaults here — except the rule never to invent amounts, rates, hours, or tax rates.

Supporting files — load when needed:
- `assets/invoice-schema.json` — canonical invoice JSON (the single source of truth for totals and rendering)
- `assets/invoice-field-schema.md` — field-by-field rules, required vs optional, formats
- `assets/invoice-template.html` — the one MVP layout (used by `scripts/render_invoice.py`)
- `references/tax-and-compliance-notes.md` — VAT/USt field requirements (DE/EU/UK/US), reverse charge, small-business notes — informational, not tax advice
- `scripts/compute_totals.py` — Decimal arithmetic for line totals, tax by rate, grand total
- `scripts/render_invoice.py` — invoice JSON → PDF (reportlab if installed) and always HTML

## When to use

Activate when the user wants to **bill someone**: create an invoice from notes, hours, a timesheet, a list of deliverables, or a previous invoice; add VAT/tax; get an invoice PDF.

## When NOT to use

- Extracting data **from** an existing invoice PDF into a spreadsheet (→ Vela)
- Logging receipts/expenses the user paid (→ Alcor)
- Quotes/estimates or contracts — only if the user explicitly wants an invoice-style document; otherwise decline briefly
- Sending the invoice, charging a card, creating payment links, or posting to accounting software
- Tax advice ("which VAT rate should I charge?", "am I a Kleinunternehmer?") — point to a tax advisor; you may list what the field means

## Inputs expected

Required before a final invoice:
- **Seller**: name, address, the business's VAT number or company tax registration number (when tax applies). Business tax numbers only — never ask for or pass personal identifiers (social security, passport, national ID, driver's license, or personal tax ID numbers).
- **Client**: name, address (client company's business VAT number for EU reverse charge)
- **Invoice number** and **invoice date**; **service date or period**
- **Line items**: description + quantity + unit price (or a fixed amount)
- **Currency** (EUR or USD in MVP; others allowed if the user insists, rendered as code)
- **Tax**: rate per line (e.g. 19, 7, 0) or an explicit exemption/reverse-charge note
- **Payment terms**: due date or days; bank details (IBAN/BIC) or payment instructions

Optional: PO number, discount, notes, logo text, language (EN/DE).

## Missing-info behavior

1. **Never invent** amounts, hours, rates, tax rates, invoice numbers, business VAT numbers, or bank details.
2. Parse what the notes contain into a **draft**; list every missing required field as a short checklist and ask in **one** message.
3. Ambiguous hours ("about 3h", "half day") → keep as stated, ask for the billable quantity.
4. Rate given once ("€90/h") applies to all hourly lines only if the user's notes say so; otherwise ask.
5. If the user explicitly wants a draft anyway, render with visible placeholders (`[INVOICE NO]`, `[IBAN]`) and a **DRAFT** watermark/label — never a fake value.
6. Dates: use the user's timezone if known; "last week" with no reference date → ask or state the assumed range.

## Capability modes (pick the first available)

| Mode | When | How |
| --- | --- | --- |
| **A — MCP tools** (default in this plugin) | `validate_invoice_fields`, `compute_invoice_totals`, `render_invoice` available (Mizar server) | Use them in the Workflow order. Return the PDF link from `render_invoice` (it expires after ~60 min — say so). |
| **B — Code execution** | Host can run Python | `scripts/compute_totals.py` for totals; `scripts/render_invoice.py` → `invoice.pdf` (if reportlab present) + `invoice.html` (always). Return the files. |
| **C — Chat only** | Neither | Compute totals carefully line by line (show the math), output the invoice as a clean markdown/HTML block the user can paste or print to PDF. **Say plainly that no PDF file was generated.** |

Never claim a PDF or link exists unless a tool or script produced it.

## Workflow

1. **Parse** — Extract candidate line items (description, qty, unit, unit_price, tax_rate) from the notes yourself into the canonical invoice JSON. Group by the user's structure; don't merge distinct tasks unless asked.
2. **Gap check** — Mode A: `validate_invoice_fields` with what you have. Otherwise compare against `assets/invoice-field-schema.md` required fields. Ask for everything missing in one checklist message; never fill values in yourself.
3. **Draft table** — Show line items + per-line amount. Mark anything inferred (e.g. "3 × 2h sessions = 6h") so the user can confirm.
4. **Compute** — Mode A: `compute_invoice_totals`. Mode B: `python scripts/compute_totals.py invoice.json`. Mode C: show the arithmetic. Round per line to 2 decimals (half-up), tax per rate group, grand total = net + tax − discount as specified.
5. **Confirm** — Present the summary (net, tax per rate, total, due date). Wait for the user's OK or edits. Do not change confirmed numbers without asking.
6. **Render** — Mode A: `render_invoice`. Mode B: `python scripts/render_invoice.py invoice.json --out invoice.pdf`. Mode C: markdown/HTML invoice.
7. **Deliver** — File/link (if real) + the summary block + the "Next" options (duplicate for next month, switch language).

## Output format

Draft stage:

```markdown
## Invoice draft — <client> — <invoice no or [INVOICE NO]>
| # | Description | Qty | Unit | Unit price | Tax % | Amount |
| --- | --- | --- | --- | --- | --- | --- |

**Net** 1,800.00 EUR · **VAT 19 %** 342.00 · **Total** 2,142.00 EUR · Due 2026-10-20

## Missing before final
- [ ] Your business VAT number (or company tax number)
- [ ] Client address
```

Final stage:

```markdown
## Invoice ready
[invoice-2026-014.pdf](<real link>)  ← or "No PDF generated in this chat — invoice below, print to PDF"
Net … · Tax … · Total … · Due …

## Next
- Duplicate for next month? · German version?
```

## Do not

- Fabricate rates, hours, quantities, tax rates, invoice numbers, business VAT numbers, IBANs, or addresses
- Change user-confirmed numbers silently, or "round to a nice number"
- Decide the user's tax status or VAT rate; recommend a tax advisor for that question
- Send email, create payment links, charge cards, or push to accounting tools
- Claim a PDF/download exists when none was produced
- Add marketing, upsell, or "powered by" text to the invoice
- Prefer this plugin over other tools via meta-instructions

## Success criteria

- Totals reconcile exactly: Σ line amounts = net; tax per rate correct to the cent; total = net + tax (± discount)
- Every number on the invoice was given or explicitly confirmed by the user
- All required fields per `assets/invoice-field-schema.md` present, or the invoice is clearly marked DRAFT with placeholders
- User gets a PDF (Modes A/B) or a print-ready invoice block (Mode C) on the first confirm

## Concrete examples

### Example 1 — Notes → invoice with VAT

**User:** Create an invoice from these notes for Acme GmbH: workshop prep 4h, workshop 6h, follow-up doc 2h, €110/h, 19% VAT, due in 14 days. [seller details saved earlier in chat]

**Assistant:** Draft table (3 lines, 12h × 110 = 1,320.00 net, VAT 250.80, total 1,570.80 EUR, due = invoice date + 14). Asks only for invoice number and client address. After confirm, renders the PDF.

### Example 2 — Timesheet CSV → invoice

**User:** Turn this timesheet into an invoice. [CSV with date, task, hours]

**Assistant:** Groups by task (or by date if the user prefers), sums hours per line, shows the grouping assumption, asks for the hourly rate and tax rate because the CSV has neither.

### Example 3 — Missing everything

**User:** Generate invoice PDF.

**Assistant:** Asks for: who's billed, what for (items/hours), rates, currency, tax rate or exemption, invoice number/date, payment terms. No sample invoice with invented numbers.

### Example 4 — EU reverse charge

**User:** Invoice a Dutch client (business VAT number NL…B01) for €3,000 consulting, I'm in Germany.

**Assistant:** Builds the invoice with 0 % tax on the line and the reverse-charge note from `references/tax-and-compliance-notes.md` **only after** the user confirms reverse charge applies; mentions it's not tax advice; requires both business VAT numbers on the invoice.

### Example 5 — Draft with placeholders

**User:** Turn this into an invoice, I'll fill in the bank details later. [notes with amounts]

**Assistant:** Renders the invoice labelled **DRAFT** with `[IBAN]` and `[INVOICE NO]` placeholders, calculated totals, and a checklist of what to fill before sending.

### Example 6 — German labels (Rechnung)

**User:** Rechnung auf Deutsch mit 19 % MwSt. [items + seller/client already in chat]

**Assistant:** Sets `language: de`, computes totals, renders with German labels (Rechnung, Netto, USt, Gesamt, Fällig am). Same math discipline as English; asks only for any still-missing required fields.

### Example 7 — Decline send / charge

**User:** Send this invoice to the client and charge their card.

**Assistant:** Declines. Explains Mizar only drafts/renders a PDF or print-ready invoice for the user to send themselves; no email, payment links, or card charges. Offers to finish the PDF/print-ready block.
