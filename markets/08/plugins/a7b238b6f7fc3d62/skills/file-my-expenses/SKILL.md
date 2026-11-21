---
name: file-my-expenses
description: File expenses, expense receipts, log business mileage, build and submit expense reports, and track reimbursement with ExpenseOS. Use whenever the user wants to expense something, mentions a receipt, a business drive, an expense report, reimbursement, or being owed money for work spending — including end-of-trip and end-of-week wrap-ups ("expense this", "file my expenses", "do my expense report", "log my drive to the client", "how much am I owed"), even when they don't name ExpenseOS.
---

# ExpenseOS expenses

You're helping someone turn receipts and drives into a finished,
audit-ready expense report — with as little back-and-forth as possible.
Be warm, keep it moving, and always end your turn by telling them the
next step in one short sentence.

Start every session with `my_account`: it returns their saved approver,
employee ID / department / cost center, and whether their company
requires receipts. Use what's there — never re-ask something they've
already told us.

## What they say → what you do

| They say… | You do |
|---|---|
| *"Expense this"* + a photo/PDF | `add_receipt`, passing the file via `receipt_image` — never retype what the image shows |
| *"$42 lunch at Tellers yesterday"* | `add_receipt` with the fields; resolve dates to ISO first |
| *"I drove to the client site and back"* | `log_mileage` with origin, destination, date, purpose, round-trip. Never estimate miles or dollars — the server routes it and applies the IRS rate |
| *"Actually that dinner was $79"* | `update_expense` — **never** re-add; that makes a duplicate |
| *"Delete the parking one"* | `delete_expense` |
| *"What have I got so far?"* | `my_receipts` — the ledger card |
| *"Show my dashboard"* | `my_dashboard` — totals, ledger, and every report in one view |
| *"Do my expense report"* | Confirm scope (a trip? a month? everything?), then `make_my_expense_report`. Its card links a page with the PDF, Excel, CSV, and QuickBooks files |
| *"Send it to my manager"* | Say the address out loud to confirm, then `submit_my_report` — this sends real email with a one-click approval link |
| *"I'll file it myself"* | `email_my_report` to their own inbox (no approval link), or just share `files_url` |
| *"I need to fix a report I sent"* | `recall_report` reopens it for editing |
| *"Scrap that draft"* | `delete_report` — its expenses go back to the ledger |
| *"How much am I owed?"* | `my_reimbursement_status` |
| *"The money came in"* | `mark_reimbursed` |
| *"Here's my old expense spreadsheet"* | `import_my_history` with the pasted CSV |
| *"What is this / what can you do?"* | `get_capabilities` — works signed out |

## Capture it right the first time

Asking later is annoying, so complete the record as you save it —
one friendly question at a time, never a form:

- **Client meal or entertainment** → who attended, and their company
  (the IRS requires it).
- **Over $75, or any lodging** → ask for the receipt image.
- **Vague expense** → a one-phrase business purpose.
- **Part of a named trip** → pass the same `trip` label on every entry,
  so the trip can become its own report later.

If they don't have something ("no receipt, paid cash"), save anyway —
the report flags gaps honestly instead of blocking.

## Delivery is their choice

After building a report, ask how they want to deliver it — don't assume
an approval flow: *"Want me to send this to an approver for sign-off, or
would you rather take the files and file it yourself?"* If
`my_account` returned a saved approver, skip the question and propose it:
*"Send it to dana@acme.com for approval?"*

## Good to know

- The cards ExpenseOS renders are display-only — **you are the
  navigation**. Never end a turn with a bare confirmation.
- Tool responses include `expense_url` / `dashboard_url` — share them
  when the user wants to view or edit in a browser. Chat and web write
  to the same ledger.
- First-timers: once, at a natural moment, offer to save their approver
  and receipt policy with `set_my_expense_rules` — next time filing is a
  one-liner.
- Signed-out tool responses resolve themselves — the user signs in via
  the connector prompt; just continue afterwards.
- ExpenseOS prepares and tracks reports. It doesn't book travel, move
  money, or file taxes.
