---
name: order-from-local-shops
description: Find local shops and place orders or bookings through OpenAjan — food pickup, haircuts, beauty, flowers, repairs. Use when the user wants to order from or book at a local shop.
---

# Ordering and booking at local shops with OpenAjan

1. **Find options.** If the user names a shop, use `find_shops` / `get_shop`. If they describe a need ("a haircut in Roskilde tomorrow before 10", "pizza near 2100 tonight"), use `find_options` with `service`, `where`, `date`, `after` and `before`. Item names are in the shop's own language (Danish, German, Turkish) — translate the service word if needed.
2. **Show the choice.** Present the shop, the exact items, the total price (incl. VAT), and the pickup or appointment time. For bookings, offer only the free times returned by `find_options` or `get_availability`.
3. **Ask for an explicit yes.** Never place an order before the user clearly confirms items, total and time.
4. **Place the order in two calls.** Call `place_order` with the item ids, `confirmed=true` and a unique `idempotency_key`. The first call returns `status: "quote"` — nothing is ordered yet. Show that exact summary (items, total, time) and ask for the user's yes once. When the yes arrives in the next message (for example "yes", "ja", "evet", "confirm"), call `place_order` again in that same turn with the same items and time plus the `quote` code — do not answer with text only and do not ask the user to repeat the request. If the quote has expired (older than 15 minutes), call `place_order` without `quote` to get a fresh one and show it again. Name and phone are filled in from the user's OpenAjan sign-in; if `place_order` returns `customer_name_and_phone_required`, ask the user once.
5. **Report the result honestly.** An order exists only when `place_order` returns `ok=true`. Share the order id and the signed receipt link. Payment is at the shop; the shop confirms by phone or e-mail. Use `order_status` when the user asks whether it is accepted or ready.
6. **Respect the user's limits.** If `spending_limit_exceeded` or `monthly_budget_exceeded` is returned, tell the user and never split the order to get around it.

For testing, use the sandbox shop "OpenAjan Demo": orders there are confirmed automatically and nothing is prepared or charged.
