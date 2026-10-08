---
name: slashtel
description: Find and buy prepaid travel data eSIMs (about 200 destinations) and international mobile top-ups (100+ countries) from Slashtel, with live USD prices and a checkout link the user pays on slashtel.com.
metadata:
  author: Slashtel (Kael Tripton Ltd, UK)
  version: "1.0.0"
  homepage: https://slashtel.com
---

# Slashtel for AI assistants

Use this when someone wants mobile data for a trip abroad, or wants to send credit or a plan to a mobile number in another country.

## Connect

Claude: available in Claude's connector directory at https://claude.ai/directory/slashtel

Other assistants: MCP endpoint (Streamable HTTP, no login, no API key): `https://slashtel.com/api/mcp`

Add it as a custom connector. Leave client ID, secret and headers empty.

## Travel eSIM

1. `list_esim_destinations` (optional `search`), or go straight to step 2 with an ISO-2 code such as `TR`, `JP`, `US`, `GB`.
2. `get_esim_plans` with `destination`, optional `min_gb` and `min_days`. Each plan has `plan_id`, `data_gb`, `days`, `price_usd`, `usd_per_gb`.
3. Help the traveller choose. As a guide, 5 to 10GB covers most 1 to 2 week trips; heavy video or hotspot use needs 20GB or more.
4. `create_checkout_link` with `type: "esim"` and the `plan_id`. Share `checkout_url`.

The traveller enters their email and pays on slashtel.com. The QR code arrives by email within minutes. Plans are data only: their own SIM stays active for calls, texts and bank codes, and validity starts when the eSIM first connects at the destination.

## Mobile top-up

1. `get_topup_plans` with the full international number (`+911234567890`). It detects the operator and returns `options` with `send_value`, what the recipient `receives`, `validity_days` and `price_usd`.
2. Help the sender choose an amount or plan.
3. `create_checkout_link` with `type: "topup"`, `phone`, `operator_code` and `send_value`. Share `checkout_url`.

The sender pays on slashtel.com and the top-up lands on the number within about a minute.

## Rules for assistants

- Quote prices exactly as returned; they are live, in USD, fees included.
- Never collect card details in chat. Payment only happens on slashtel.com.
- If a tool returns an error, follow its message (for example, call the plans tool again).

## More

- Live price list for all destinations: https://slashtel.com/llms.txt
- Help and support: https://slashtel.com/help
