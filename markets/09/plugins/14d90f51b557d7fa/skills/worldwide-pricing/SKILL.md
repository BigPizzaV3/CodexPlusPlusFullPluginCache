---
name: worldwide-pricing
description: >-
  Price an iOS app fairly in every App Store storefront using purchasing
  power parity, the Big Mac index, the Spotify index, or plain conversion,
  then stage the new prices for the person's own app behind a change card.
  Use for "what should my app cost in India", "PPP pricing", "make it
  affordable in Brazil", "reprice worldwide".
---

# Worldwide pricing

## The base price is the person's decision

Never choose a base price for them, and never treat the current price as the
answer. If they have not said one, ask for it (and which storefront it is set
in) before calculating.

## Any app, no account: explore

`calculate_worldwide_prices` takes `basePrice`, `baseTerritory` (default US)
and `strategy` (`ppp`, `bigmac`, `spotify`, `direct`), and returns every
storefront snapped to Apple's real price points, compared with a flat
currency conversion. Pass `focusTerritories` for the countries they asked
about so those lead the card.

## Their own app: stage it

1. `apple_list_apps`, then `apple_get_app_pricing` for the current schedule.
2. `pricing_compute_prices` with the same strategy and base price; it compares
   current against target per storefront and returns `stagedInput`.
3. Pass `stagedInput` unchanged to `apple_preview_set_territory_prices`. The
   change card shows every storefront that moves; the person presses Apply.

New prices become live on the store when applied. Mention any storefront where
the price rises, not only the discounts.
