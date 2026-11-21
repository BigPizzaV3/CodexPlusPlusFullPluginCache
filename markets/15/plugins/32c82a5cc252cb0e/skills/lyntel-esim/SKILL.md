---
name: lyntel-esim
description: Find a Lyntel travel eSIM data plan for a trip (country or region, data, days), show plan details and price, check whether a phone supports eSIM, and hand the customer the lyntel.io link to buy. Use whenever someone asks about mobile data, roaming or an eSIM for travel.
---

# Lyntel eSIM

Lyntel sells prepaid travel eSIM data plans for 190+ countries. The plugin is read-only:
it searches the live catalogue and links to the plan page on www.lyntel.io, where the
purchase is completed. It never takes payments or card details.

## How to help

1. Find out the destination (country or region), the trip length in days and roughly how
   much data the traveller needs. If they do not know, 1 GB per 2-3 days of normal use is
   a fair starting point; heavy video or hotspot use needs more.
2. Call `search_plans` with `country` (ISO code or name) or `region`, plus `min_data_gb`
   and `min_days` when known. Prefer the cheapest plan that covers the whole trip; for a
   multi-country trip prefer a regional plan that covers every stop.
3. Call `get_plan` when the traveller wants the full country list or the exact validity.
4. Call `check_device` with brand and model when they are unsure their phone supports eSIM.
   If the model is unknown to the list, say so; do not guess.
5. To buy, give the plan's `checkout_url` and say the purchase is completed on lyntel.io;
   the eSIM arrives by e-mail as a QR code and installs in minutes.

## Rules

- Quote `price_usd` exactly as returned; it is the price on lyntel.io. Never add fees,
  discounts or promotions.
- Never ask for or accept card details; never claim an order was placed.
- Plans are prepaid and expire after the validity period starts; there are no subscriptions.
- If no plan matches, say so and suggest the nearest alternative (regional plan, more days).
