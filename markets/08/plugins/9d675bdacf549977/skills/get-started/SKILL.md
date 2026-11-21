---
name: get-started
description: Help the user order a bouquet from independent Prague florists with Pinflower — search bouquets, check delivery or pickup times, price the order and hand over a payment link on pinflower.cz.
---

# Ordering flowers in Prague with Pinflower

Pinflower is a marketplace of independent florists in Prague, Czech Republic. Delivery is inside Prague (or pickup at the studio); prices are in CZK. The buyer can order from abroad.

1. Search with what the user said — occasion, budget, district or address, date and deliver-by time (`pinflower_search_bouquets`). Show a few real options; never invent a bouquet, price or time.
2. For the chosen bouquet, get details and exact times (`pinflower_get_bouquet`).
3. Ask only for what is missing: delivery address (with house number) or pickup, time, card message, the buyer's contact, the recipient if it is someone else, and whether they have a promo code.
4. Price it with `pinflower_quote_order`, read the breakdown back together with the terms link, and wait for an explicit yes.
5. Place the order with `pinflower_create_order` (pass the confirmed total) and give the user the payment link. Payment always happens on pinflower.cz; the amount is only held until the florist hands the bouquet over.
6. Follow up with `pinflower_get_order_status`; a new link with `pinflower_new_pay_link`; cancel with `pinflower_cancel_order` (a code is sent to the order's e-mail).

Outside Prague: say so plainly and offer pickup in Prague — do not promise delivery elsewhere.
