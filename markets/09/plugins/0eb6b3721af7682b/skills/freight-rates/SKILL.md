---
name: freight-rates
description: Fetch live Cargors European pallet freight rates. Use whenever a user asks what it costs to ship pallets between two places.
---

# Cargors freight rates

## Tool

Call `get_freight_rate` with:

| Argument | Required | Notes |
| --- | --- | --- |
| `from` | yes | e.g. `Amsterdam, NL`, `Sparti, GR`, `5473VG, Netherlands` |
| `to` | yes | e.g. `Antwerp, BE`, `Amersfoort, NL` |
| `pallets` | no | default 1 |
| `weight_kg` | no | total kg; plain number, no thousands separator |
| `height_cm` | no | default 120 |
| `pallet_type` | no | `euro` (default), `block`, or `mini` |
| `pickup_date` | no | `YYYY-MM-DD` |

Use only the shipment details needed for this lookup. Prefer city or postcode plus country; do not request exact street addresses or device location. Do not include contact details, payment data, passwords, API keys, full conversation history, or unrelated personal information in any argument.

The tool uses the standard dimensions for the selected pallet type and supports standard dry transport without special equipment. It does not expose a dedicated FTL mode, custom length/width, or special transport requirements. Do not promise those capabilities or silently treat a special requirement as supported.

## Response rules

1. Use the tool result — never invent a market estimate.
2. Report **only** option count + cheapest all-in EUR excl. VAT (use `summary` when present).
3. Mention assumptions (height/date/weight defaults) briefly if relevant.
4. Never name carriers.
5. Booking URL: https://portal.cargors.com/#/public/public-quotes

## Examples

- “2 pallets 400 kg Amsterdam to Antwerp” → `from=Amsterdam, NL`, `to=Antwerp, BE`, `pallets=2`, `weight_kg=400`
- “400 kg pallet Sparti Greece to Amersfoort” → `from=Sparti, GR`, `to=Amersfoort, NL`, `pallets=1`, `weight_kg=400`
