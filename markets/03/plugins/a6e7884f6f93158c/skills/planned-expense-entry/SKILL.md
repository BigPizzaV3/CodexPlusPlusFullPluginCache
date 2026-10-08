---
name: planned-expense-entry
description: Use when the user wants to add planned or forecasted costs to an awarded grant's budget — a single planned expense, or a recurring cost spread across the remaining grant period.
---

# Planned expense entry

Add **planned** (not-yet-incurred) expenses to a grant budget.

## The rule that governs this entire skill

**Only ever create planned expenses.** The create call treats an expense as an **actual** unless you explicitly mark it planned — the planned flag defaults to off, so omitting it silently records real spend. **Always set it explicitly on every row, every time.**

If the user asks to log what was **actually** spent, decline and explain that actuals belong in their accounting system, which is the source of truth, and that Instrumentl reads actuals from there.

## Ground rules

- **Confirm before any write.** Restate exactly what will change and wait for a yes.
- **No internal identifiers in output.** Never show an ID, cursor, or API field name.
- **Never invent grant data.** Never guess an amount, a date, or a category the user didn't state.
- **Out of scope** — say so plainly and point to the Instrumentl app: creating or configuring projects, writing or storing proposal narrative, building or restructuring budget categories, recording actual expenses.

## Money formats — three different representations, do not mix them

1. **Budget figures** come back as **integer cents** — divide by 100 to present. `2500000` is $25,000.00.
2. **When creating an expense**, the amount must be **sent** as integer cents — $1,500.00 is `150000`.
3. **When reading an expense back**, the amount comes back as a **decimal dollar string** — the expense you just created as `150000` reads back as `"1500.00"`. **Do not divide it.**

The dry-run preview reports in cents; the expense list reports in dollars. Always restate dollars to the user, never a cents value.

## Workflow

1. **Find the budget and category.** Call `list_budgets` first — it accepts a grant name or project title and returns the grant name and project title, so you can confirm the target in plain language. Match the expense to a category by name.
   - Categories are a **tree** and a parent's totals already include its children. Place the expense on the most specific matching category.
   - Prefer a category whose remaining balance can cover the amount. If none can, say so rather than picking arbitrarily.
   - If no category clearly matches, **ask** — do not fall back to an uncategorized bucket, and do not create a category (that's done in the app).

2. **Always dry run first.** Preview the impact before creating anything. The preview reports, per category, the projected remaining balance, whether it would be overspent, and any expenses that already exist in that category.

3. **Show the user the preview**: projected remaining, whether it would overspend, and any existing expense that looks like a possible duplicate — they may want to update that one instead of adding another.

4. **For recurring costs** ("$1,500 a month for the rest of the grant year"), lay out the individual dated expenses in full before creating them. Get one confirmation for the set, then create in a single batch.

5. **Only create after explicit confirmation.**

6. **Report what actually happened.** Rows are created independently, so the result may be partially successful. Report any failures in plain language: the grant or category wasn't found or belongs to another account, the caller lacks permission, or the row failed validation.

## Guardrails

- Only planned expenses. Never record actual spend.
- Don't restructure a budget or create categories.
- Never place an expense in a category the user didn't approve.

## Removing or ignoring existing expenses

These are separate operations from creating, and both are available. Treat them as higher-risk than a create:

- **Ignoring** an expense excludes it from budget totals but keeps the record. It is reversible. Use it when the user wants a charge to stop counting against a category.
- **Deleting** an expense removes it permanently. There is no undo. Expenses linked to a connected external system (QuickBooks, Sage Intacct, Financial Edge NXT, or any other integration) cannot be deleted here and will be refused — those must be removed in the source system first.

Rules for both:

1. Never delete or ignore anything unless the user explicitly asked for it. Do not infer it from a duplicate you noticed.
2. **List every affected expense by description, amount, and date, and get a yes before acting.** Never act on a filter or a description alone — resolve to specific records and show them first.
3. Prefer ignoring over deleting when either would satisfy the request, and say why: ignoring is reversible.
4. Report exactly what changed, including any rows that were refused.
