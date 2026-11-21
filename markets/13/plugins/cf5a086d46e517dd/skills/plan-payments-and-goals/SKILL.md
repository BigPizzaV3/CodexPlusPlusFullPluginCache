---
name: plan-payments-and-goals
description: Plan upcoming card payments, cash needs, a purchase or a savings goal using Fina's saved financial context. Use when the user asks what is due, whether a purchase fits, or how to plan toward a goal. This plans and records preferences; it never pays bills or moves money.
---

# Plan payments and goals

Read [Fina's shared workflow](references/fina-core.md) and [financial facts](references/financial-facts.md). Check setup and guide missing prerequisites before the dependent plan; use partial evidence only when the user deliberately proceeds with its limitations.

1. For an overall decision first read `get_financial_context(detail=summary)` for the relevant horizon, even if the proposed purchase price is missing. Reuse saved goals and constraints. A simple card-due question can use `get_upcoming_card_payments` directly after setup.
2. For this calendar month use `period=current_month` on `get_projection` / `get_upcoming_card_payments`. For a specific horizon use paired `from`/exclusive `to` within their 91-day maximum; do not combine selectors. `get_financial_context` uses paired dates, not the `period` argument.
3. Separate current recorded cash, expected receipts, dated cash obligations, total card debt, loan obligations and assets. Use the backend's `financial_decision` and coverage fields. Recorded cash already includes earlier purchases and payments: never subtract them again.
4. Show upcoming obligations with their actual dates and the correct amount meaning. Unknown card schedule amounts stay unknown, even when an estimated component exists. A transfer association or a passed due date does not prove a statement was paid.
5. For a purchase, obtain missing price, currency, payment method and timing together. If `spending_approval_supported=false` or `safe_to_spend=null`, do not turn a known subtotal into permission to spend. Explain the material gap and still compare supported options or next steps. Never invent current product prices.
6. For a goal, reuse its saved amount, currency, target date and reserve preference. Ask only missing decision inputs. Explain where the proposed plan depends on future income or incomplete obligations. Do not sell guaranteed returns or infer risk tolerance from the user's wealth.

When asked to save a goal or preference, read current context/version and use `update_financial_preferences` with only the user-declared changed fields. A hypothetical discussion alone does not authorize saving. Re-read to confirm the saved result. Use wealth-and-debt for supported debt/fixed-income scenarios; do not implement a second amortization engine.

Deliver a dated, understandable plan with concrete options and assumptions. A suggested repayment is a plan; it never authorizes executing it or recording a payment that has not happened.
