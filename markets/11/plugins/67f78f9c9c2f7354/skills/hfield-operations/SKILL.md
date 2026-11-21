---
name: hfield-operations
description: Use for HField carrier truck management, load reports, move suggestions, and broker shipment order creation through the HField MCP tools.
---

# HField operations

When the user's intent is clear and the HField tool is available, call it directly. Do not run tool discovery or a roster check before every request. Respect any discovery or approval step the host requires.

- "My trucks" or a fleet status request: call `list_trucks`.
- "Last week loads" or a load, revenue, or payment report: call `get_loads_report`. The default period runs from seven days ago through today in New York time. Omit dates for that period; supply explicit dates for a different requested period.
- Truck status, pickup radius, or distance limits: call `update_truck_params`.
- Truck ZIP, availability, or next-day offers: call `update_truck_location`.
- State restrictions: call `update_truck_states`; use `enable_all_states` to remove every restriction.
- Move suggestions: call `where_to_move` with a known truck or an explicit ZIP and equipment type.

For a truck write, use its ID from a fresh `list_trucks` result. Reuse a fresh result already in the conversation; otherwise list once to identify the truck. Ask only when the truck or a required value is ambiguous. A ZIP update requires an explicit availability time with UTC offset. Apply only the requested changes.

Inspect each write result before confirming success. If the result is unverified, say so and do not automatically retry the write. Keep routine replies brief and report only values returned by the tools.

For broker order creation, call `create_order` with one shipment’s details in `text`, including answers to earlier clarification questions. Do not run a truck roster check before creating an order. If the result is `needs_info`, ask the returned clarification.

For `created`, if the order card is shown, reply with only the clickable order link and its expiration if provided. Do not repeat shipment details or the matching truck count in a separate summary or table. If the card is unavailable, show the returned message and order link, including the matching truck count when available.

For `rejected`, `error`, or `unverified`, explain the returned outcome without claiming success. Never automatically retry order creation.
