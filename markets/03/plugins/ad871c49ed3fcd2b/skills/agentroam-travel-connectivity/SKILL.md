---
name: agentroam-travel-connectivity
description: Buy travel eSIM data plans, travel gift cards, and mobile airtime top-ups paid with stablecoins and crypto (USDC, USDT, BTC, ETH, SOL and more) through the AgentRoam MCP server. Trigger when the user wants an eSIM or mobile data for a trip ("eSIM for Japan", "data plan for my trip"), a travel or brand gift card paid with crypto, or to top up a prepaid phone number abroad, and for questions about AgentRoam's supported coins, networks, prices or order status. Do NOT trigger for booking flights or hotels (AgentRoam sells connectivity, not travel bookings), for crypto prices, trading or investment advice (crypto is only a payment method here), or for managing/reading an eSIM already installed on the user's device.
---

# AgentRoam — travel connectivity for humans and AI agents

AgentRoam sells three things, all paid with stablecoins and crypto straight from the
user's own wallet:

- **eSIM data plans** — 110+ countries and regions, plus Europe ("eu") and Global ("ww")
  multi-country plans. QR delivered by email, usually within minutes of payment confirmation.
- **Travel & brand gift cards** — Airbnb, Uber, airlines and 500+ US brands.
- **Mobile top-ups** — prepaid carriers in 100+ countries.

Purchases are fulfilled by **Cryptorefills B.V.** as merchant of record. AgentRoam never
holds funds or documents. Codes and eSIM QR codes are delivered by email, never through
the API.

## Tool selection

| The user wants… | Call |
| --- | --- |
| An eSIM for a country/region | `list_esim_plans` (destination = ISO code, or `eu` / `ww`) — PREFERRED for any eSIM ask; renders the interactive plan picker |
| A brand's gift-card options | `search_products` → `list_products` |
| To top up a phone abroad | `list_brands` (country) → `list_products` |
| "How much does X cost in <coin>?" | `get_price` |
| "Which coins/networks can I pay with?" | `get_payment_methods` (live matrix — currently 21 coins across 18 networks, 64 combinations; always report the live result, never a memorized list) |
| To actually buy | `validate_order` → show summary → user approves → `create_order` |
| To check an existing order | `get_order_status` (needs the status_token) |
| Text-only client without widgets | `purchase_wizard` (stateful fallback flow) |

## The confirm gate — REQUIRED before any purchase

1. `validate_order` mints a **local draft only** (no real order, no funds moved) and
   returns a human-readable summary plus a one-time `confirm_token` (10-minute TTL).
2. **Show the summary to the user and get explicit approval.**
3. Only then call `create_order` with that token. It returns the wallet address, the
   EXACT amount, the network, a QR and a status URL. The user pays from their own
   wallet within a 30-minute window; the code/QR is emailed after payment confirms.

Never call `create_order` from exploration or without explicit user approval.

## Presentation rules (learned from live sessions)

- **Present full lists.** `list_brands` results are already filtered to the requested
  country — bare-named majors (e.g. "Telcel", "AT&T", "Movistar" in Mexico) are the
  local operations. Do not drop them.
- **Dynamic amounts are normal.** Many gift cards are amount ranges (e.g. $50–$500),
  not fixed denominations. `get_price`/`validate_order` accept any `amount_usd` within
  the live range.
- **Quote live, don't memorize.** Plans, prices, fees, coins and networks all change —
  always answer from the tool response of THIS conversation.
- **Exact network strings matter.** Use the `network` strings from
  `get_payment_methods` verbatim on orders ("Solana", "Tron", "ETH Mainnet"…). Funds
  sent on the wrong network are lost — repeat the network warning near any address.
- The purchased code/QR arrives **by email only**; never promise to display it in chat.

## Do not

- **Do not book flights or hotels** — AgentRoam is connectivity + gift cards, not an OTA.
- **Do not give crypto prices, trading signals, or investment advice.**
- **Do not try to read or manage an eSIM already on the user's device.**
- **Do not invent** products, prices, coverage or order states — always use the tools.

## Notes

- Coverage: 110+ eSIM destinations; gift cards are US-only today; top-ups span 100+ countries.
- Verification (KYC) is requested only by the merchant of record above regulatory
  limits and happens on Cryptorefills' own hosted pages.
- Site: https://agentroam.ai · MCP endpoint: https://agentroam.ai/api/mcp
