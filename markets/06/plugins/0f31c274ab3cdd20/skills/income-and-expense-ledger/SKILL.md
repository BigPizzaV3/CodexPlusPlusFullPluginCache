---
name: income-and-expense-ledger
description: Turn freelancer documents or notes into a reconciled, evidence-aware income and expense ledger.
---

# Income and Expense Ledger

Use when a user provides transaction notes, invoices, processor statements, receipts, or asks for a reusable freelance bookkeeping tracker.

## Process

1. Confirm jurisdiction, tax year, currency, accounting period, and whether the records describe cash received/paid or invoices incurred.
2. Extract only visible fields. Normalize dates and amounts while retaining original values and currencies. Mark missing or ambiguous values instead of guessing.
3. Deduplicate transactions using date, amount, vendor/client, and reference; preserve refunds, chargebacks, reimbursements, and transfers as distinct types.
4. Separate gross receipts from fees, refunds, sales tax/VAT collected, and transfers between the user's own accounts when the source permits. Flag uncertain distinctions.
5. For expenses, retain vendor, amount, business purpose, business-use percentage and basis, document type, and review status. Do not infer a business purpose from a merchant name alone.
6. Reconcile subtotals against statements when totals are provided; explain every mismatch and do not force-balance the ledger.

## Output

Provide a clean table or CSV-ready rows, totals by month and category only when supported, a duplicate/missing-data list, and reconciliation notes. Label every classification as user-stated, document-visible, or tentative.

## Safety and scope

Do not store or request credentials or full account identifiers. Encourage redaction. Keep original source descriptions available for audit traceability. This ledger is a working organizer, not a filed return or final tax classification.
