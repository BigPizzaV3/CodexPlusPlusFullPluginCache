# Fiest Surplus offers

Examples: “Put 8 lunch boxes on surplus for 5 €, pickup today 14–15”, “8
lounaslaatikkoa 5 eurolla, nouto tänään 14–15”, “Add three more portions”, or
“End the soup offer”.

Fiest Surplus sells counted portions of food that is already prepared, at a
fixed price in the Fiest app. Customers pay in the app and collect the food in
a pickup window. Paid orders and pickups stay staff actions in Fiest.

1. Check connection capabilities. Surplus tools require a restaurant owner/admin
   grant and the enabled surplus workflow. Management organization grants are
   not supported by this bridge. Never work around a denied grant.
2. Read `read_surplus_offers`. Use returned product and offer IDs and versions,
   never guessed IDs. If `enabled` is false, nothing can be published: ask the
   user to switch selling on in Fiest app → Surplus.
3. Ask only for missing facts: product, number of portions, price and pickup
   time. Never invent or estimate them, and never invent allergens, ingredients,
   diets, stock or a reference price. Customers see the product's own menu
   information and its menu price automatically.
4. Times are wall-clock `YYYY-MM-DDTHH:mm` in the returned `timeZone`, resolved
   from `currentLocalTime` whether the user writes Finnish or English. “End of
   day” or “päivän loppuun” means `closesToday`, but only when `dayEnd` is
   `closing` or `endOfDay`. When `opensToday` is set, the restaurant is closed
   now and opens then: an end-of-day pickup runs from `opensToday` to
   `closesToday`, never from now. When it is `tooLate` (under 15 minutes left) or
   `dayOver` (closed for the day), or `closesToday` is null, there is no
   end-of-day pickup left today: do not propose one or substitute 23:59 or
   another day's close; ask for an explicit pickup time.
   Pickup lasts at most 24 hours. Leave `sellUntil` null to sell until pickup
   ends.
5. Price is `{type: "fixed", cents}` for a stated price or
   `{type: "percent_off", percent}` for a percentage off the menu price. Money
   fields ending in `Cents` are EUR cents.
6. To resize a live offer, use `change_quantity` with its current `version`:
   `newTotal` is the new total including sold portions and can never be below
   `sold + beingPaid`. To stop selling, use `end`; paid orders stay valid.
7. Call `propose_surplus_change` with a UUID `requestId` kept for exact retries.
   Show the restaurant, product, portions, price and menu price, local pickup
   window and selling deadline, note and expiry, then send the returned
   `reviewUrl`. Nothing is published until a human confirms on that page within
   30 minutes.
8. A verbal yes or `confirmed: true` is not an approval. There is no MCP
   confirm, publish or apply tool. After confirmation, read again to report the
   actual offer. On a timeout, read pending proposals and retry the exact request
   ID and content; never create a replacement because the outcome is unknown.
9. A refusal names one rule (for example `pickupEndPast` or `belowCommitted`).
   Fix that fact with the user and propose again.
