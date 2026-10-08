---
name: mercury-personal-finance
description: Review personal and household Mercury cash flow, spending against a user-provided budget, recurring charges, savings goals, and emergency-fund coverage. Use for personal finance questions when the authorized connection exposes the required accounts. Do not use for business operating runway or customer invoice aging.
---

# Mercury Personal Finance

Provide read-only analysis of the selected personal or household accounts. Apply `../mercury-mcp-shared/SKILL.md` before retrieval. Reuse instructions already read in this session.

## Select the smallest useful workflow

- Current balances: use `../mercury-cash-runway/SKILL.md`; retrieve no history.
- Spending, recurring charges, or possible duplicates: use `../mercury-spend-review/SKILL.md`.
- Who was paid or a recipient identity check: use `../mercury-vendor-review/SKILL.md`.
- Budgets, cash flow, savings goals, and expense coverage: use the definitions below with the required balance and transaction tools.
- Customer invoices from a freelance business: use `../mercury-invoice-review/SKILL.md` only for that explicitly selected business account.

The personal definitions and thresholds below replace business-specific defaults for personal requests. Shared privacy, currency, completeness, and read-only controls always apply.

## Scope and dates

Use the user's period and selected accounts. For a monthly spending or budget question without a period, use the last complete calendar month. For an average monthly cash-flow, cash-buffer, or savings baseline, use the last three complete calendar months. For a recurring-charge review without a period, use the last three complete calendar months. Never expand an explicit period to find a pattern; label insufficient history instead. Do not retrieve comparison history unless requested. Label an explicitly requested current month partial and compare only the elapsed period or a user-approved prorated budget; never treat it as a complete month.

Separate personal, joint, and business accounts. Do not retrieve another connection merely because it is installed. State missing external bank, investment, debt, or card coverage when it limits the requested result. Do not claim full net worth or total household spending from a partial account view.

## Prepare the cash-flow view

Use complete, settled transactions and exact arithmetic. Exclude confirmed transfers within the selected scope. Keep transfers to owned accounts outside the scope separately identified; do not call them household consumption or earned income. If ownership is uncertain, retain them in observed cash flow and mark the uncertainty.

Show salary or other income only when source evidence or the user supports the classification. Deposits can be loans, refunds, reimbursements, gifts, asset sales, or transfers. Do not label all inflows income. Classify essential expenses only with the user's categories or explicit confirmation; merchant names alone do not establish necessity.

Cash-flow and purchase-spend views can differ. For cash flow, count each actual scoped cash movement once. For purchase spending, avoid counting card purchases and their repayment twice. If card detail is absent, show the repayment separately and state that category-level purchase spending is incomplete. Reconcile refunds separately; net them only with evidence and a stated method.

## Calculations

Keep currencies separate. Use complete calendar months and state account coverage, period, and the denominator for every measure.

- Observed net cash flow = scoped external inflows minus scoped external outflows. This is not automatically income minus consumption or a savings rate.
- Budget variance = observed category spend minus the user's same-period category budget. A positive amount means over budget. With no supplied budget, provide a spending baseline; do not invent a target or say the user overspent.
- Monthly surplus = evidenced monthly income minus the selected monthly expense base. Label uncovered expenses and uncertain classifications. Treat observed surplus as a historical measure, not a promise of future saving.
- Expense coverage without income = selected available cash divided by average monthly expenses. State that this assumes no future income. For essential-expense coverage, require an essential-expense base supplied or confirmed by the user; otherwise offer total observed expense coverage with a clear label.
- Cash depletion with income = selected available cash divided by (average monthly expenses minus evidenced average monthly income), only when that denominator is positive. If it is zero, report balanced cash flow; if negative, report a surplus. Do not report infinite coverage.
- Savings goal gap = max(user's goal amount minus the amount the user has allocated to that goal, 0). Do not allocate all cash automatically or double-allocate cash across goals.
- Months to goal = gap divided by a positive monthly contribution supplied by the user. If the user requests an estimate from observed surplus, label that contribution as an assumption and show the account-coverage limits. If gap is zero, the goal is funded. If contribution is zero or negative, the goal has no finite completion time under the scenario.

Do not divide by zero. Zero observed expenses do not prove unlimited expense coverage. Label baselines with fewer than three complete months low confidence. A no-income expense-coverage scenario differs from a cash-depletion scenario with income; if the user's intended scenario is ambiguous and changes the answer, ask or show both labeled scenarios when supported.

## Personal review thresholds

Use a user-supplied threshold when available. Otherwise rank personal review candidates by absolute same-currency amount, change, and recurrence, with no fixed business currency floor. Present up to ten ranked items and state the selection rule. This cap limits the displayed queue, not the complete calculation population. For possible duplicates, calculate exposure over all qualifying groups and state how many are shown. Do not hide small recurring charges from an explicit recurring-charge request.

For merchant increases, require a requested equal-length comparison, at least 25% growth, and a positive absolute increase; rank by absolute increase without the business 500-unit floor. With zero prior spend, label the merchant new in period and omit a growth percentage. Retain the shared duplicate evidence rules and historical outlier requirements. These are review signals, not proof of error or unnecessary spending.

## Deliver the answer

Lead with the requested balance, spending result, budget variance, cash buffer, or goal scenario. Cite abbreviated source IDs and tools, show calculation inputs, and state material coverage limits. Keep observed facts distinct from user-supplied assumptions. Do not infer sensitive personal traits, judge lifestyle choices, recommend financial products, move money, cancel subscriptions, modify budgets in external apps, or contact payees under this skill.

## Requests to make changes

This review workflow remains read-only. When the user explicitly requests a supported payment, transfer, category, or transaction metadata change, route that part to `../mercury-actions/SKILL.md`. Keep any requested analysis separate from the authorized change.
