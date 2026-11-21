---
name: travel-esim-selector
description: Compare SimVoro public travel eSIM options by destination, data allowance, validity and price using the connected read-only MCP catalog when available.
---
# SimVoro travel eSIM catalog finder

1. Understand the destination, trip length, likely data usage and hotspot requirements from the user's prompt. Ask only for material missing details when required to compare relevant plans.
2. If MCP tools are connected, call `list_travel_esim_destinations` to confirm the destination slug and `search_travel_esim_plans` with that slug. Do not claim a live quote without a successful response. Do not invent plans for empty results.
3. For each returned offer, describe publicly reported data allowance (MB vs unlimited), validity days, currency and price, network and speed, hotspot availability, and relevant restrictions. Include the SimVoro URL returned by the tool.
4. For cross-border travel, verify coverage rather than assuming a regional plan contains every country.
5. If MCP is not connected or fails, optionally verify the public website https://simvoro.com/esim through an available browser; if neither can be checked, explicitly say live plans and prices are unverified.
6. The eSIM typically offers mobile data only unless the specific product states it includes a voice number or SMS. Explain that compatibility, region and carrier unlock need verification.
7. Ordering, payment and activation are website-only, not plugin actions. Never ask for passwords, private activation codes or customer data.

Avoid unsupported 'cheapest' claims or comparisons with competing providers without verifiable evidence.
