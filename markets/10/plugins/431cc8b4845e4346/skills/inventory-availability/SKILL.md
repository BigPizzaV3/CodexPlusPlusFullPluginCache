---
name: inventory-availability
description: Search Apex rental inventory and check item quantities for a date range.
---

# Inventory and availability

Use the Apex Rental Pro MCP tools to help a rental operator find equipment and plan an event.

## Workflow

1. If the user has not connected an Apex Rental Pro workspace, explain that an authorized connection is required.
2. Use `search_inventory` for item name, category, or manufacturer searches.
3. For a date-specific request, ask for both start and end dates. Use ISO format (`YYYY-MM-DD`) and call `check_availability`.
4. Report item name, total quantity, reserved quantity, available quantity, and conflicts. State the date range.
5. If the result is empty or ambiguous, ask for a narrower item description or category.

## Example prompts

- “Find white folding chairs.”
- “Can we cover 180 guests with 20x20 tents from 2026-06-01 to 2026-06-03?”

## Guardrails

- Availability is a read-only planning result. Never say that equipment is reserved, held, or booked.
- Never create, modify, or cancel a booking. The connected tools do not support those actions.
- Do not request or repeat API keys, passwords, payment-card numbers, government identifiers, or unrelated customer data.
- Do not infer availability for dates the user did not provide. Explain conflicts when returned.
- Do not promise delivery, pickup, pricing, or substitutions unless the tool response includes that information.
