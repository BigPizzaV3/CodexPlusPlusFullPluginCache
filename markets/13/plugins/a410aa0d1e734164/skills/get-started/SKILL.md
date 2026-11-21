---
name: get-started
description: Help a new user start using Shipink in ChatGPT and check that their account is ready to ship.
---

Shipink connects a merchant's Shipink account (shipink.io) so they can list, track, quote, create and cancel shipments.

To get started:

1. Call `list_warehouses`. If the list is empty, tell the user to add a sender warehouse in the Shipink panel (Settings → Warehouses) first; quotes and shipments need one.
2. Offer what the user can do next: see recent shipments, track a shipment, compare carrier prices for a parcel, or create a shipment.
3. For a price quote, ask for the recipient address (neighbourhood, street and number, district and province) and the parcel weight and dimensions, then call `get_rates`.
4. Before `create_shipment`, show the carrier, service and price from `get_rates` and wait for the user to confirm. Labels on Shipink-provided carrier accounts are charged to the user's Shipink wallet or default card.

Only shipments in `pending` status can be cancelled.
