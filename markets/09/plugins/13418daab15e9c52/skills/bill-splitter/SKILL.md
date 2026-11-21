---
name: bill-splitter
description: Split a restaurant bill item by item with tax and tip, settle group or trip expenses with the fewest payments (who owes who), or split rent by room size or income, using the split_bill, settle_group_expenses, and split_rent tools. Exact to the cent; calculation only.
---

# Zovo Bill Splitter

Use these tools for "split the bill", "split the check with tax and tip", "who owes who", "trip expense splitter", "settle up", "split rent by room size", and "split bills by income".

1. `split_bill` (one bill). Pass `items` with `price` (per unit), optional `quantity`, and `shared_by` names; omit `shared_by` for items everyone shared, and add `weights` for unequal portions. List everyone in `people`. For an even split without items, pass `bill_amount` plus `people` or `people_count`. Use `tax_percent` or `tax_amount` (the receipt's figure), `tip_percent` or `tip_amount`, `service_charge_*`, `discount_*`, `equal_fee_amount` (delivery fee), `round_up_to: 1` for whole units, and `paid_by` when one person paid. If the bill amount already includes tax, do not add tax again.
2. `settle_group_expenses` (several expenses, several payers). One entry per expense with `amount`, `paid_by` (one person), `split_among` (omit for everyone), and `split`: equal (default), exact, percent, or shares with `split_values` keyed by name. Pass `people` when someone never paid. A repayment already made is an expense paid_by the person who paid it back with `split_among` set to the receiver. All expenses must be in one currency; if they are not, ask the user for converted amounts or run one call per currency.
3. `split_rent`. `total_rent` and `rooms` with `size` (any one unit), optional `occupants`, `adjustment_percent`, or `income`. Use `shared_area` when the user gives the shared space size, otherwise `shared_percent`; the default is 50% shared. `extra_costs` (utilities) are split per occupant.

After a tool returns, state each person's amount and who pays whom using the tool's numbers; never recompute or round them yourself. The widget lets the user change the tip, round up, toggle who shared an item, mark a payment as done, or download a CSV.

Do not use these tools to send payment requests, move money, convert currencies, give tax or legal advice, or answer etiquette questions about who should pay.
