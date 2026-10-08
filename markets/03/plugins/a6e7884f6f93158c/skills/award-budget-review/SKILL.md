---
name: award-budget-review
description: Use when the user asks about spending on an awarded grant — budget versus actuals, remaining balance by category, or whether spenddown is on track for the grant period.
---

# Award budget review

Report on how an awarded grant's budget is tracking. This skill is read-only.

## Ground rules

- **No internal identifiers in output.** Never show an ID, cursor, or API field name.
- **Never invent grant data.** If a fact isn't in the record, say the record doesn't cover it.
- **Out of scope** — say so plainly and point to the Instrumentl app: creating or configuring projects, writing or storing proposal narrative, building or restructuring budget categories, recording actual expenses.

## Money formats — read this before reporting any figure

The two sources use **different representations** and mixing them produces wrong numbers by a factor of 100:

- **Budget figures** (`amount_cents`, `actual_cents`, `planned_cents`, `remaining_cents`) are **integer cents**. Divide by 100. `2500000` is $25,000.00.
- **Expense amounts** are **decimal dollar strings** — `"700.00"` is $700.00. Use as-is. **Do not divide an expense amount by 100.**

## Category totals roll up — do not sum them

Expense categories are a **tree**. A parent category's actual, planned, and remaining figures already include everything in its children — summing every category in the list double-counts spending. Report the parent, or its children, never both added together. The **budgeted** amount is the exception: it is each category's own line and does not roll up children, so a parent's budgeted figure can be smaller than its children's combined. Nesting can run three levels deep.

## Workflow

1. **Identify the grant.** `list_budgets` accepts a grant name or project title and returns the grant name and project title on each budget, so no separate name resolution is needed here. If the grant is unclear, list the awarded grants that have budgets and ask. Only awarded grants with expense categories set up appear — a submitted or in-progress grant won't, and neither will an awarded grant with no categories yet.

2. **Report by category**: budgeted, actual, planned, and remaining. Present as dollars.

3. **Flag the exceptions:**
   - Any category where remaining is **negative** — over budget.
   - Any category nearly exhausted.
   - Any category **underspent relative to how far into the grant period they are**, using the budget phase's start and end dates. **Sanity-check the phase range first.** If it is implausible for the phase's name — a phase called "Year 1" spanning eight years, or a range ending before it starts — say so and skip the pace calculation rather than reporting a figure built on it. A wrong range makes everything look dramatically underspent, and the award period dates on the tracker record cannot be read back to cross-check it.
   - An **"Uncategorized"** category with spending against a zero budget means expenses landed without a category assignment. Report it as unassigned spending needing attention in the app, not as an overspent line item.
   - A **negative actual** is a refund or correction. Report it as recorded; don't treat it as an error.

4. **If the user asks for expense detail**, call `list_expenses` — it requires at least one filter, so scope it by saved grant, grant name, or project name. Expenses carry only a category ID, so map them back to category names using the budget you already pulled.

5. **Offer the follow-on action** — adding a planned expense — and hand off to the planned expense skill. Do not create anything here.

## Guardrails

- This skill does not write. Hand off rather than acting.
- If the user asks to log what was **actually** spent, decline and explain that actuals belong in their accounting system, which is the source of truth, and that Instrumentl reads actuals from there.
- Never delete or ignore an expense from this skill. Expenses can carry an ignored marker; report it, never set it here — if the user asks to remove or ignore one, hand off to the planned expense skill.
- Don't restructure a budget or create categories — that's done in the Instrumentl app.
