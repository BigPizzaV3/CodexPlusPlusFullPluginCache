# Reconcile budget lines

Run for the selected job's financial wrap. Review all in-scope lines, then propose actionable exceptions for human review. Do not create a task for every nonzero cost, force Actuals to equal Estimate, or infer savings from missing Actuals.

## Establish scope and evidence

1. Read existing tasks and lists, then confirm the current source budgets and versions. Inspect each source budget once; exclude alternative revisions and composite totals from addition. Record the check time, currency, budget IDs, selected baseline and completeness warnings.
2. Read the complete budget overview/line inventory. Use phase-specific rollups, including applicable fringes, rather than summing phases or treating a legacy variance field as a reconciliation balance. For every line record Estimate, Running, Actual, visible source counts and coverage. Include zero-value lines with source activity. Empty zero-value lines are dormant, not evidence of completed work.
3. Inspect connected details, expenses, timecards, commitments and lineage with `grid.get_budget_line_context` for active lines. Check source invoices/receipts, payroll, payment applications and inbox items in both directions: line to evidence and source to allocation. Follow pagination and report unavailable evidence. Amount matches are candidates until identity, date, currency and source agree.
4. Reuse existing actualization/lineage and allocation math. Do not add invoices, their imported costs and their payments as three expenses. Distinguish refunds, cancelled orders, superseded invoices, duplicate captures, and tips charged separately. A budgeted line with no Actual is a coverage question, not proof a cost was incurred or is owed.

## Reconcile receipts and transactions

Inventory every actively job-tagged transaction with `grid.list_transactions`; follow all cursors. Each needs a source-backed Actual disposition or a reviewed non-cost exception. Project tags, bank matches, paid AP and zero unapplied balances do not prove cost coding. Trace payments through AP to existing costs rather than importing payments as costs. Treat signed credits/refunds separately and verify the original purchase and net Actual reduction.

Also search transactions **without a project filter** around each receipt date. Otherwise unassigned charges disappear from the job-only inventory. Respect accessible account scope and reject company/account/currency conflicts or allocations to another job. Nearby unassigned charges are candidates, not automatically this job's expenses.

Use `grid.read_document_inbox_file` for retained PDFs/images even when no project Document exists. Extract source facts in the host; do not infer tips from arithmetic or rely on a `needs_ocr` label to decide whether retained text exists. Use `grid.get_receipt_reconciliation` with source amount/date/currency/merchant and an explicitly itemized included tip when present. Its result groups single charges and base-plus-tip candidates, identifies existing expense/coding evidence, and states coverage blockers. It is read-only: even unique candidates need review. Incomplete transaction or expense inventories must be resolved before declaring no existing match.

A receipt total including a tip is one cost, even if the bank posted separate base and tip charges. Do not add the tip again, create an AP solely for a card-paid receipt, or recreate an already imported expense/Actual. Existing expense suggestions are duplicate-review candidates, not proof of source identity or complete budget allocation. Reuse verified costs and use separately reviewed matching/import operations.

Reuse the existing inbox/final-Actual tasks. Their `Done when` must explicitly require every job-tagged transaction and in-scope receipt to have verified source, transaction treatment, source-budget Actual coding (including credits), or a reviewed exception with evidence IDs. Record unresolved/ambiguous matches, missing source bytes, partial coverage and coding gaps; keep the task open. A reusable procedure does not automatically run when tasks are generated.

## Exception categories

| Category | Evidence that warrants review | Completion condition |
| --- | --- | --- |
| Missing costs | Incurred work/purchase lacks final Actuals, or budgeted work has no documented disposition | Import or reuse verified costs, or record supported non-incurrence/inclusion elsewhere |
| Reconciliation | Source totals, currency, allocations, lineage or final commitments disagree | Source and allocated Actual totals foot at currency precision; unused commitments are released or explained |
| Refunds/credits | Return, deposit or credit has no verified disposition | Link the original purchase and credit/refund and verify correct net cost and payment treatment |
| Client overages | Variance or recoverable cost lacks a reviewed billing decision | Explain variance; record billable decision, approval and issuance separately, or an accepted exception |
| Final review | Coverage, fees/fringes or sign-off remains incomplete | Each line and source has a reviewed disposition; remaining exceptions have explicit acceptance, evidence and ownership |

Compare Actual against the selected approved baseline and, separately, Running. A difference triggers investigation; create a task only when an explanation, source, decision or action is still missing. Keep unknown amounts unknown. Use currency precision for arithmetic reconciliation; any materiality threshold for task grouping must be stated rather than silently dropping small unresolved costs.

## Build the review set

- Group related gaps by vendor or action across lines; split when owner, action or completion condition differs. Categories are review labels, not a requirement to create five new lists or unsupported nested tasks.
- Reuse matching existing tasks by template marker, scope, counterparty and intent. Preserve user notes, ownership and progress. Refresh evidence in a proposed update; do not silently reopen completed/dismissed work. A recurring gap on completed work needs an explicit reopening proposal.
- Give each proposed task a stable marker derived from `financial.budget-line-reconciliation`, category and stable scope IDs. Include affected bid/line IDs, evidence IDs/links, observed amounts and baseline, uncertainty, next action, and `Done when`. Never include signed download URLs or sensitive bank/payroll data.
- Suggest the responsible project role and a separate follow-up/chasing person only where known. Resolve a stored role/contact before assigning it. Producer is the fallback recommendation when no specialist is staffed; unknown assignments remain unset. Do not invent a chaser field if the task contract has none.
- Put the complete proposals in the supported review queue when available. Otherwise present MCP previews or a review artifact explicitly as unsaved proposals; do not call them persisted queue entries. Preview and confirmation follow the parent skill. A procedure run does not authorize financial writes or task completion.
- Bind completion only to an available capability that proves the entire narrow task criterion. `payable.settled` does not prove invoice revision review, Actual coding, client approval or whole-job wrap. Keep unsupported checks manual and evidence-backed.

## Report the run

Report budgets/versions, line inventory coverage, inspected active lines, unverified sources, reused tasks and proposed additions. Separate screening from completed reconciliation. Retain a per-line review matrix and the concrete proposals so the next run can refresh the same work. Completion means reconciled lines or explicitly reviewed exceptions, never zeroing every variance.
