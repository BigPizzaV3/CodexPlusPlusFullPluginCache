---
name: book-a-car-wash
description: Book a hand car wash in France with Washlib — find a centre, check live slots, quote the exact price and hand the customer a pre-filled booking link.
---

# Book a car wash with Washlib

Washlib lists independent hand car-wash centres (mostly Paris and Île-de-France). Prices depend on the vehicle category and the services; slots are live capacity. Use the tools; never estimate a price or a slot.

## Flow

1. **Where and when.** Use the customer's own words as the location (`find_centers` / `search_available_slots`). A vague area (« Paris ouest ») resolves better as a concrete arrondissement or town. Read `resolvedLocation` back to the customer so they can correct it.
2. **Which centre and slot.** A slot label such as `09:00 - 11:00` is a 2-hour window: the customer arrives at its start (`start_booking` returns `arriveFrom` / `arriveBy`). Mention busyness when it helps choose.
3. **Which vehicle category.** `get_center_details` lists the categories (`s`, `m`, `l`, `xl`, `moto`) with example models. Propose one from the customer's car and confirm it — the price depends on it.
4. **Which services.** One formule (Extérieur, Intérieur, Intérieur + Extérieur…) plus optional options, ids from `get_services`.
5. **Price.** Call `quote_booking` before stating any total. Give both the online and on-site totals when the centre accepts both. If `notIncludedOptions` lists something the customer may expect (seats, pet hair, carpets), say it is not included. If `thresholdNudge` is set, it is an option that costs nothing extra once the online discount applies — offer it once, without pressure.
6. **Book.** When the customer wants to book, call `start_booking` and give them `bookingUrl` exactly as returned (do not shorten, re-encode or rewrite it). Explain that the booking is confirmed on Washlib after an SMS code and payment (or the on-site payment choice). Nothing is booked before that.

## Limits

- Promo codes are entered on the booking page, never in the chat.
- If `start_booking` returns `slot_unavailable`, offer the `availableSlots` it lists.
- Washlib is an intermediary: the centre is the seller. For a problem with an existing booking, point to https://www.washlib.com/contact.
