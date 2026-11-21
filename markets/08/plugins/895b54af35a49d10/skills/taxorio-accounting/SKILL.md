---
name: taxorio-accounting
description: Use when working with the Taxorio MCP connector for Czech invoices, expenses, receipts, payments, VAT, income-tax summaries, recurring invoices, or any taxorio_* tool call.
license: Proprietary. See https://www.taxorio.cz/obchodni-podminky.html
metadata:
  author: Taxorio
  homepage: https://www.taxorio.cz
---

# Taxorio accounting

Taxorio is an invoicing and evidence service for Czech sole traders. It is not full accounting and does not replace individualized tax advice. The MCP server's tool schemas, authorization checks, and live resources are authoritative.

## Start with the live guidance

Before non-trivial work, read `taxorio://docs/overview` and the resource for the workflow you will use. Follow returned warnings and supported-scope limits even when they differ from this packaged summary. Do not invent a tax treatment, silently substitute another year, or approximate an unsupported case.

User-specific tax behavior always depends on both `vatStatus` and `taxRegime`. Read both from Taxorio; never infer either axis from the other. In particular, a non-payer, identified person, VAT payer, standard taxpayer, and flat-tax taxpayer can require different answers.

## Execute the user's job

Act on the requested outcome when the connector supports it. Do not stop at generic instructions when the user asked to create, record, match, mark, pause, export, or inspect something. Explain briefly while doing the work, ask only for information that is genuinely missing, and end with the concrete result and any next action the user must take.

- Translate natural language into the workflow. Do not ask the user for an internal UUID when a name, invoice number, variable symbol, supplier, or visible document can be resolved with list/get tools.
- Resolve one unambiguous record and continue. If several records match, show the smallest useful disambiguation: human-readable name or number, date, amount, currency, and status.
- Read current state before changing it. For updates, preserve fields the user did not ask to change and describe the effective change, not the raw API payload.
- Use the user's explicit instruction as authorization for reversible, non-communicative actions. Still follow every preview or confirmation-token flow required below. Sending e-mail and issuing numbered documents need the specific safeguards in this skill.
- If a request has both read and write parts, finish the safe lookup and preparation first, then ask for confirmation only at the actual write boundary.
- Do not claim success from a planned call. Verify the returned object or re-read the record when the response leaves the final state uncertain.

## Money, dates, and document scope

- Send money as decimal strings, such as `"1210.00"`, never floating-point numbers. Send dates as ISO `YYYY-MM-DD` dates.
- CZK is Taxorio's tax and reporting currency. Invoice documents may also use EUR, USD, GBP, CHF, PLN; read the invoice workflow resource for the applicable ČNB date and payment rules.
- Issued invoices and recurring plans support the current `supplyRegime` values, including supported EU, export, third-country-service, and domestic reverse-charge cases. Read `taxorio://workflow/invoices` for the full matrix and repeat every returned regime warning.
- Issuing customer credit notes and other unsupported corrections are not exposed by this connector. Direct the user to the Taxorio app instead of approximating them.
- Omit optional fields unless the user supplied them or the live resource defines a safe default. Never erase an existing value merely because the user did not mention it.

## Invoices

Before `taxorio_create_invoice`, resolve the client, assemble the complete document, and show the user an exact preview: client, dates, currency, language, supply regime, every line, VAT, totals, payment details, and note. Call the tool only after the user confirms that preview. An issued number cannot be reused or silently removed.

Treat the tool response as part of the result. Repeat the assigned number, totals, `supplyRegime`, and all warnings. Never hide a warning in internal reasoning.

For real external communication, never retry `taxorio_send_invoice_email` after an ambiguous result. Inspect the invoice state or ask the user what to do, because a retry can send a duplicate. Apply the same caution to `taxorio_send_payment_reminder`; confirm the intended invoice and recipient context before sending and do not automatically retry an uncertain send.

## Expenses and Inbox documents

Run `taxorio_check_duplicate_expense` before `taxorio_create_expense` whenever the document has a number. A negative duplicate check is not a guarantee; for unnumbered receipts compare visible supplier, date, and amount with existing expenses.

After creating or updating an expense, report every returned `warnings` entry, `attachment.stored`, and `vatRateWarning`. Do not claim a scan was retained when `attachment.stored` is false. Do not silently fill optional tax fields that the user did not provide.

`taxorio_confirm_inbox_document` is a two-call operation. First call without a token, show the complete `willRecord` preview including the proposed payment date, and only then use the returned confirmation token after the user approves it.

For a group of receipts, upload or inspect the whole group first, then process documents in a stable order. Confirm each materially distinct preview. If one document is ambiguous or fails, stop the batch before later writes unless the user explicitly asked for independent best-effort processing; report completed, skipped, and failed items separately.

## Payments and outstanding invoices

- For “what is unpaid/overdue”, use invoice list/detail data and report invoice number, client, due date, currency, outstanding amount, and status. Do not treat a draft, cancelled invoice, or credit note as an ordinary receivable.
- For a manual payment, inspect the invoice first and call `taxorio_mark_invoice_paid` with the actual payment date and, for foreign-currency invoices, the amount and currency that really reached the account. Do not invent a ČNB rate or silently turn a partial payment into full payment.
- For bank imports, begin with `taxorio_list_payment_inbox`. Explain mismatches before `taxorio_confirm_payment_match`; use reassign, reject, or unmatch only for the user's intended item. A cross-currency proposal or amount mismatch must remain a human decision, not an automatic match.
- After a payment change, report which invoice was affected, the recorded amount/currency/date, and the resulting paid state. If a write response is ambiguous, inspect state before retrying.

## Tax summaries and exports

For questions about VAT, flat-rate tax, income tax, or insurance, read the profile and requested year/period before choosing the tool. Say clearly whether a result is an estimate, a filing input, or unsupported. Never present `isProjected: true` as a binding amount.

Before `taxorio_generate_vat_export`, verify `vatStatus`, `taxRegime`, filing period, and the requested date range. Surface every blocker and finding before describing an export as usable. Identified persons and VAT payers follow different paths; non-payers do not receive a Czech VAT return. Taxorio does not know whether a period was already filed, so remind the user to consider corrective or subsequent filings when older DUZP data changed.

## Confirmation tokens and irreversible actions

For any tool that returns a confirmation preview, use two calls exactly as described by the live tool:

1. Call without `confirmationToken`.
2. Show the complete preview and consequences to the user.
3. Call again with that exact token only after explicit confirmation.

Never execute a confirmation token the user has not seen. Never reuse a token for another tool or target. This applies to cancellation, deletion, Inbox confirmation/deletion, terminal recurring-plan actions, and any sensitive settings update that requests a token.

## Recurring invoices

Before `taxorio_create_recurring_invoice`, show the same exact content preview required for a one-off invoice plus the cadence, start date, billed period, end condition, and automatic action. Create the plan only after the user confirms it, then call `taxorio_get_recurring_invoice` and show the resolved next invoice.

- `taxorio_pause_recurring_invoice` and `taxorio_resume_recurring_invoice` are reversible. Inspect `pausedReason` before resume and explain why the plan stopped; resume may require PRO and does not recreate every old missed period.
- `taxorio_finish_recurring_invoice` is terminal and uses two-step confirmation. Use it when the arrangement has ended but its plan history should remain.
- `taxorio_delete_recurring_invoice` permanently removes the plan and its lines and uses two-step confirmation. Previously issued invoices remain. Prefer finish when the user wants to stop future invoices while retaining the plan record.

## Completion and failures

Return a compact operational summary: what changed, identifiers a person recognizes, money/date/status, warnings, and the next unresolved step. For mixed outcomes, never collapse partial success into “hotovo”. Do not retry a mutation after a timeout or ambiguous result until you have checked whether it already took effect.

When the connector refuses a legal but unsupported case, explain the specific limit in Czech and direct the user to the relevant Taxorio screen or a qualified accountant/tax adviser. Do not replace an unsupported workflow with a nearby one that produces different tax or document consequences.

Do not maintain or assume a fixed tool count. Discover current capabilities from the connected server and its live resources.
