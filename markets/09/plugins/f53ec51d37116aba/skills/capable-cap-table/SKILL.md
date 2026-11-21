---
name: capable-cap-table
description: Answer questions about a company's cap table, vesting, 409A and exit scenarios from Capable, and draft changes for an admin to approve. Use when the user asks who owns what, what their equity is worth, when options vest, or wants to model a round or draft a grant.
---

# Capable cap table

Capable holds a company's cap table. Two kinds of people connect: company admins (founders, finance, legal, HR) and stakeholders (employees, advisors, investors) who see only their own equity.

## How to work

1. If you do not know which company or what kind of access the person has, call `list_companies` first.
2. Company admins: use `get_cap_table`, `list_stakeholders`, `get_stakeholder`, `list_securities`, `get_vesting_schedule`, `get_409a`, `recent_activity`, `model_round` and `exit_waterfall`. `companyId` accepts the company's name and can be left out when the person administers one company.
3. Employees, advisors and investors: use `my_equity`. It shows only the signed-in person's own holdings.
4. Link to the Capable page a result includes so the person can check the numbers.

## Rules

- Quantities are shares or options, except SAFEs and notes, where the quantity is the US dollar principal. Percentages are fully diluted unless a field says otherwise. A holder field that is missing means zero.
- Every `propose_*` tool creates a proposal and changes nothing. Tell the person an admin must approve it in Capable and share the review link.
- `model_round` and `exit_waterfall` are planning estimates. Do not give tax, legal or investment advice; point to the company's counsel or tax adviser.
- Never ask for or repeat passwords, tax identification numbers or bank details. Capable does not move money or place trades.
- If a result says the company has no active plan or the person has no access, report that plainly and suggest `my_equity` or contacting the company admin.
