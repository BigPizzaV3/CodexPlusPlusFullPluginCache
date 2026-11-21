---
name: haulforza
description: Use the HaulForza MCP tools to look up the signed-in user's trucking companies, loads, drivers and company financial summaries, and to create a load or change a load's operational status after the user explicitly confirms. Use when the user asks about their HaulForza loads, dispatch, drivers, revenue, driver pay or expenses.
---

# HaulForza

HaulForza is a trucking management system for carriers, owner-operators and dispatchers. The `haulforza` MCP server exposes only the data of the signed-in HaulForza user, limited to the companies and records that user's HaulForza role allows.

## Tools

Read-only:

- `list_companies`: companies the signed-in user belongs to, with their IDs. Call this first to get a `company_id`.
- `list_loads`: loads for a company, optionally filtered by status or pickup date range (load number, broker, origin, destination, dates, rate, driver pay).
- `get_load`: full detail of one load, including broker, stops, rate breakdown and assigned drivers.
- `list_drivers`: drivers for a company, optionally filtered by active or inactive.
- `company_summary`: load counts by status, total revenue, driver pay and expenses for a company over an optional pickup date range.

Write (only when the user's HaulForza role allows it):

- `create_load`: create a new load. Requires a company and a load number; broker, origin, destination, dates, rate, commodity and notes are optional.
- `update_load_status`: move a load to an operational status: new, booked, assigned, dispatched, at_pickup, loaded, in_transit, at_delivery, delivered, pod_received or cancelled.

## Instructions

1. Call `list_companies` first. If the user belongs to more than one company, ask which one before reading or writing.
2. Prefer read-only tools to answer questions. Quote load numbers, amounts and dates exactly as returned. Never invent loads, drivers or amounts that the tools did not return.
3. To find a load by its load number, call `list_loads` and match `load_number`, then call `get_load` with that load's ID.
4. Before calling `create_load` or `update_load_status`, show the user exactly what will be created or changed (company, load number, route, dates, rate, or the old and new status) and wait for an explicit yes.
5. Invoiced, submitted-to-factoring and paid are controlled by Accounts Receivable in the HaulForza app. They cannot be set through this connector; tell the user to use the HaulForza app.
6. There is no tool to delete loads, drivers or companies. Say so instead of trying another tool.
7. If a tool returns a permission or access error, explain that the user's HaulForza role or company membership does not allow that action. Do not retry with other tools or other company IDs.
