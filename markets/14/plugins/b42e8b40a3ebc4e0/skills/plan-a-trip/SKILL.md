---
name: plan-a-trip
description: Plan a trip with one or more legs and overnight stops using Foyard's tools. Use when someone wants to work out how to travel between places and where to stay, compare the options, and open a Foyard checkout for the ones they choose.
---

# Plan a trip

Use this workflow when someone asks for help with a journey that may need several transport
legs, places to stay, or both. The user's explicit instructions come first: if they ask for only
one part (just a train, just a hotel) or want things done in a different order, do that and skip
the steps that don't apply.

## 1. Work out the essentials

Before searching, work out:

- every place on the route, in order, and where the traveller sleeps each night;
- the date of each transport leg, and the check-in and check-out dates of each stay;
- how many people are travelling, and the age of each child;
- any constraints they gave: only trains and buses, a cabin class, refundable stays only, a
  budget, a neighbourhood or landmark, a property type.

Ask one short question only when a date a search needs cannot be worked out from the request.
Turn relative dates into calendar dates ("next Friday", "the 15th of next month"; for "next
weekend", travel on the Saturday) and say which dates you used. If the number of travellers is
not given, search for one adult (one `passengers` entry for `search_transport`, `adults: 1` for
`search_stays`) and say that you assumed one adult, so they can ask again for more people. If
children are mentioned without their ages, ask for the ages. Do not invent constraints the
traveller did not give.

## 2. Search transport: one call per leg and date

`search_transport` covers one route on one date. Call it once for each leg (A to B, then B to C)
and once more for each other date the traveller wants to compare. A return journey is a leg of
its own: search it with origin and destination swapped. Pass `modes` when the traveller rules
out a mode, and `passengers` with one entry per traveller (ages for children).

## 3. Search stays: one call per overnight stop

Call `search_stays` once for each place the traveller stays, with that stop's `check_in` and
`check_out`, `adults`, `children_ages` and `rooms`. Put the area or landmark in `location`, and
pass `refundable_only`, `accommodation_type` or `star_ratings` when the traveller asks for them.
Check-in at a stop should be the day the traveller arrives there. For more results at the same
stop, call `search_stays` again with `exclude_ids` set to the previous result's
`pagination.next_exclude_ids`.

## 4. Compare and summarise

- For each leg, give the cheapest and the fastest option with carrier, departure and arrival
  times, duration, number of transfers and price.
- For each stay, give a few options with the total price for the stay, the address, and whether
  the rate is refundable and until when.
- Check that the plan fits together: each leg arrives before the next one departs, with time to
  change, and each stay covers the nights between legs.
- When you give a price, say that Foyard's checkout adds a service fee on top: 10% on hotel stays
  (rates with `service_fee_rate` 0.1; Foyard's own apartments and rates paid at the hotel have
  none) and 1% on flights, trains and buses.
- If a total is useful, label it an estimate made from the prices shown.
- Use only offers, prices and availability that the tools returned. If a leg or stop has no
  results, say so and offer another date or a nearby place.

## 5. Open checkout only for what the traveller chooses

Call `create_checkout_link` only after the traveller picks a specific offer, and only for that
offer, using the `search_id` and `offer_id` from the result that contained it (plus `hotel_id`
for a stay). Each call creates a new pending order, so each chosen offer gets exactly one
checkout link. Do not create links for options nobody chose.

Hotels marked `live_rates: true` are the exception: their prices are previews, and they are
booked from the hotel's live rates, which the traveller opens with "See rates" on the hotel's
card in the stays results. Never call `create_checkout_link` with only `search_id`, `offer_id`
and `hotel_id` for them. If no results view is shown, tell the traveller to book that hotel on
foyard.ai, or offer one of the other hotels.

When you share a checkout link, say that:

- payment and the final confirmation happen on the Foyard checkout page, and nothing is booked
  or charged until the traveller completes that page;
- the price and availability are checked again at checkout and can change;
- Foyard's checkout adds its service fee to the price shown (10% on hotel stays that carry it,
  1% on flights, trains and buses);
- confirmations, tickets and vouchers arrive by email after payment.

Search results expire after about 30 minutes, and a checkout link works for 60 minutes. If a
checkout link can no longer be created for an older search, or an old link has expired, run that
search again and use the new result.

## Never

- Never ask for, accept, repeat or pass on payment card numbers or other payment details in the
  conversation. If someone shares them, do not repeat them; explain that payment is taken only
  on the Foyard checkout page.
- Never say a trip is booked or confirmed because a checkout link was created.
- These tools cannot look up, change or cancel an existing booking. For that, suggest contacting
  Foyard support.
