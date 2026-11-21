---
name: financial-statement-sankey
description: Draws Sankey diagrams of income statements, cash flow statements, balance sheets and budgets with SankeyArt. Use when the user wants to see, draw or visualize financial figures as a Sankey or flow diagram, e.g. where revenue goes, how cash moves or how a budget splits, or change such a diagram.
---

# Financial statement Sankey diagrams

SankeyArt draws a diagram from flows: each flow goes from a `source` to a `target` with a positive `amount`. Every node in the middle of the diagram must take in as much as it passes on.

## Choose the tool

1. The user gives figures, in the chat or in a file: call `draft_sankey` with the complete diagram. Use only the figures the user gave or that are in their files. If a figure the diagram needs is missing, ask for it instead of estimating it.
2. The user asks for a company's statement without giving figures: ask them for the figures or a file with them. Don't draw a company's figures from memory.
3. When `draft_sankey` says that the user's SankeyArt account keeps their diagrams, save the diagram with `create_sankey` and its `draft_id` right away, before replying. From then on, draw new diagrams with `create_sankey` and change saved ones with `update_sankey`.
4. To change a drawn diagram that isn't saved, call `draft_sankey` again with the complete updated diagram.
5. `list_my_sankeys` lists the diagrams saved in the user's account and `get_sankey` opens one of them. Don't add images to such a list: a picture found elsewhere would show another diagram.

Always give the user the editor link that the tools return.

## Lay out the flows

List the flows from top to bottom, because the nodes of a column are stacked in the order in which they first appear: profits before costs, and the flows out of a node after those out of the nodes above it.

**Income statement**

- Revenue sources or segments → Revenue (only when the user gives a breakdown)
- Revenue → Gross profit, Revenue → Cost of revenue
- Gross profit → Operating profit, Gross profit → each operating expense (R&D, SG&A, ...)
- Operating profit → Profit before tax, Operating profit → interest and other expenses
- Other income → Profit before tax
- Profit before tax → Net income, Profit before tax → Income tax

**Cash flow statement**

- Operating, investing and financing inflows → Cash in
- Cash in → each outflow
- If cash went up: Cash in → Net increase in cash, for what is left. If it went down: Net decrease in cash → Cash in, with the decrease as a positive amount. If it didn't change, leave this flow out.

**Balance sheet**

- Each asset → Total assets
- Total assets → Liabilities and Equity, then each of those → its items

**Budget**

- Income sources → Total budget
- Total budget → each spending category
- If the income is more than the spending: Total budget → Savings, for what is left. If it is less: Budget deficit → Total budget, for the shortfall.

A loss can't be a negative amount. If there is an operating loss, it flows into Gross profit to cover the operating expenses, and the diagram ends there, without the items below the operating result.

## Fill in the details

- `company_name`, `fiscal_year`, `reporting_period` (`full_year`, `Q1`–`Q4`, `H1`, `H2` or a month) and `statement_type` (`income`, `cashflow`, `balance`, `budget` or `other`).
- Units: `settings.unit_prefix` (e.g. `$` or `€`) and `settings.unit_suffix` (e.g. `M` or `B`). Keep the amounts in the unit the user gave.
- A comparison with another period: `amount_comparison` on each flow.
- Colors and labels: `nodes`, by node name. Leave colors out unless the user asks for them: SankeyArt colors profits, costs and revenue by their names.

Before calling a tool, check that every middle node takes in as much as it passes on and that the final figures match the user's statement.

Don't give investment or financial advice. Describe what the figures show, not what the user should do with them.
