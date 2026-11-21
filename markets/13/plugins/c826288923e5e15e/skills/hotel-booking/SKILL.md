---
name: hotel-booking
description: Book a hotel end to end - search availability, compare rooms and prices, and confirm the reservation. Use when the guest wants to find, price or book a hotel stay (book a hotel, find a room, availability, prices by date).
---

# Hotel booking

Follow this flow with the Bluesea hotel chain booking tools (operated by Neobookings): every hotel the tools return belongs to the Bluesea chain. The tools return the data; this skill defines the order and the rules. Reply in the guest's language and use names, never internal IDs or codes.

## Instruction priority
The guest's explicit instructions take precedence over the guidelines in this skill. If they conflict, follow the guest, except for the payment-safety rules (never ask for or repeat card data) and the privacy rule (never give data of other guests). If you stop or hold back because of a rule in this skill, say briefly which rule it is, so the guest is not left waiting without knowing why.

## Scope
This skill creates new bookings. **Existing reservations cannot be looked up, modified or cancelled from this chat.** If the guest wants to check, change (dates, rooms, guests, data, extras) or cancel one, do not attempt it and do not offer to, and do not call any tool: answer directly, telling them clearly it is not possible here and that they must contact the hotel directly, or their usual booking channel, saying that is the reason. Never give data of other guests.

## Tool options
These parameters are available in this chat. Always pass them:
- `language` (the chat language): `open_booking_search`, `check_room_availability`, `check_room_extra_availability`, `lock_basket`, `confirm_basket`. `open_booking_search` takes no `ui_options`: it always shows its widget.
- `ui_options={render_ui: true, language: <chat language>}`: `search_hotels`, `get_calendar_availability`, `get_basket_summary`. Without it these tools do not show their widget.
  - Set `render_ui` to `false` only when you call the tool just to resolve an id the guest did not ask to see (for example finding a hotel's `hotel_id` before checking rooms), or when the guest asked a focused factual question that a widget would only clutter. Otherwise keep it `true`.

## 1. Collect the trip data
Search bar (when `open_booking_search` is available): if the guest wants to book or search but destination or hotel, dates, or number of adults is missing, call `open_booking_search` instead of asking in text. Pass as arguments only what the guest already said (`destination`, `hotel_name`, `check_in`, `check_out`, `adults`, `children_ages`, `promo_code`) plus, in `extra_criteria`, any preference the bar cannot take (amenities, stars or accommodation type, board, room type, budget, number of rooms, adjectives like "romantic") in the guest's own words, then stop: do not call another tool in the same turn and do not repeat the questions. The guest fills in the bar and sends it as a chat message; continue from that message at step 2, applying any "Criteria: ..." it carries (amenities via `search_hotels` then `hotel_ids`, stars via `categories`, board and room type via `filter_by`, "cheap" via `order_by="price"`; for adjectives with no filter, apply a reasonable proxy and say so, or say it cannot be filtered). Do not call it when the guest already gave destination or hotel, exact dates and adults (go to step 2), when a hotel is chosen and only dates are missing (step 3), nor when only the number of adults is missing: ask for it in the chat (and whether anyone under 18 is travelling). If the tool is not available, ask in text as below.

Required, ask for anything missing instead of guessing it:
- Number of adults (for both room checks and the calendar).
- Dates, in one of two forms:
  - Exact check-in and check-out (check-in cannot be in the past and check-out must be after check-in): needed to check rooms in step 4. If the guest gives a day without a year, use its next future occurrence. Relative expressions that point to specific days ("this weekend", "tomorrow for two nights", "next Friday to Sunday") count as exact dates: resolve them from today's date (a weekend is Friday check-in, Sunday check-out) and state the dates you used so the guest can correct them.
  - A flexible window ("in July", "next month", "any weekend in August"): enough for the calendar in step 3. Turn it into a `date_from`/`date_to` range using today's date, and do not ask for exact dates yet. Ask for them only after the guest picks days from the calendar.

Optional:
- Children. It is fine to ask if anyone under 18 is travelling, but do not block the search on it. If there are children, get the exact age of each one (0-17, repeat ages as needed) for `children_ages`. If the guest does not mention any, search with adults only.
- Rooms. If the group may need more than one room, ask how many and who sleeps in each. Otherwise assume one room.

Ask one short question for all that is missing instead of several rounds.

## 2. Find the hotel
- Bluesea is a chain with several hotels:
  - `search_hotels` has two uses: (a) resolve the `hotel_id` of a hotel you do not have yet, and (b) show the guest a list of hotels when they want to explore a destination and have not chosen one. Do not call it if you already have the `hotel_id`.
  - The guest names a hotel: call `search_hotels(hotel_names=[name])` without zones, with `render_ui: false` (use (a): you only need the id). If several hotels match, ask which one. Keep its `hotel_id`.
  - Administrative province or city (for example Málaga): use `states` (ISO 3166-2, for example `ES-MA`) in `search_hotels`, not `zone_codes`. Keep `render_ui: true` when the guest is exploring hotels (use (b)); when you only need the `hotel_ids` for steps 3 or 4, use `render_ui: false` (use (a)).
  - Broad tourist destination (island, coast): call `search_zones` to get the FULL set of matching `zone_codes`. A `main_zone` code covers its sub-zones, so you do not need to add its sub-zones as well. Never pick a single code for a broad area unless it is the `main_zone` that covers it, and never invent codes. Then:
    - Exact dates and adults known: do not list hotels; go straight to step 4 with those `zone_codes`.
    - Flexible dates: call `search_hotels(zone_codes)` with `render_ui: false` (use (a)) and pass the resulting `hotel_ids` to the calendar in step 3.
    - No dates (the guest is exploring): pass them to `search_hotels` with `render_ui: true` (use (b)).
  - Amenity preference (pool, parking, pets...): call `search_amenities` (codes come grouped by type `hotel` or `room`). For a `hotel` amenity, call `search_hotels(zone_codes or states, amenity_codes)` and use the resulting hotels as `hotel_ids` in step 4. For a `room` amenity (only available in rooms), do not use `search_hotels`: pass its codes in `filter_by.room_amenity_ids` in step 4 (see `references/glossary.md`). `amenity_codes` is OR: pass every code of that one concept and skip opposites and paid variants (for example "pets not allowed"). For two different amenities, search once per amenity and keep the hotels in both. Without a destination an amenity is too broad a scope: ask for the destination.
  - Stars or accommodation type (5 stars, villa, apartment): call `search_categories` and use the codes as `categories` in step 4; no destination is needed. Categories are an exact match, so "4 stars or more" is `["4e","5e"]`.
  - Vague request ("somewhere sunny"): ask for region, hotel type or category before searching.
  - Present hotels by name. Keep the `hotel_id` for later calls.

## 3. Flexible dates
If the guest has no fixed dates, call `get_calendar_availability` (`date_from`, `date_to`, `adults`, and `hotel_ids`). If the guest gave a destination but no hotel, resolve its `hotel_ids` first with `search_hotels` and `render_ui: false` (step 2).
- It gives indicative prices per day, not the total of the stay, and **no** `avail_id`. It does not take children into account. With several hotels it shows the best price across them. A day shown there is not a guarantee.
- When suggesting dates, respect `min_stay`, `max_stay` and `release` when the response gives them, and skip days that are not bookable.
- If the response covers only part of the range, say which periods have no data and do not invent prices for them.
- Once the guest picks dates, continue with step 4. If dates are already exact, skip this step.

## 4. Check rooms
Call `check_room_availability` with `rooms=[{check_in, check_out, adults, children_ages}]` (YYYY-MM-DD), `language`, and `hotel_ids`. If the guest wants a whole destination with no amenity preference and has not chosen a hotel, pass the `zone_codes` from step 2 instead of `hotel_ids`, without listing every hotel first. With an amenity preference use the `hotel_ids` from step 2; with stars or accommodation type use `categories`. Use `filter_by` for room type or board if the guest asked (see `references/glossary.md`).
- Send one entry in `rooms` per room. If any room is unavailable the whole search comes back empty: suggest fewer rooms or other dates.
- Adults are priced as age 30. If the guest mentions an age that may change the price (for example seniors), use `adult_ages`.
- If the tool already showed the options in a widget, do not list them again: add at most one short comment (for example the cheapest option) and ask which one the guest prefers. Otherwise show for each option: room, board, rate, price and cancellation conditions.
- Price: show `final` with its `currency`. `tourist_tax` is charged in addition to `final`: if it is greater than 0, show it on its own line. If `before` is higher than `final`, show `before` as the original price.
- Promo code: if the guest has one, pass it as `promo_code`. If it is not applied, tell the guest.
- If there are no results, suggest other dates, splitting the group into more rooms, or removing filters. Offer these as options; do not change the guest's filters or dates on your own.
- If a tool you need is not available, say so and do not claim the operation was done.

## 5. Build the basket
1. `create_basket` with no arguments, to get the `basket_id`. A basket holds one hotel only, and all its rooms must share the same rate and board: use a new basket for another hotel or for rooms with a different rate or board (one `create_basket` per rate and board combination).
2. `add_basket_products` with `basket_id` and `room_ids=[avail_id, ...]`, one `avail_id` per room, in the order of the rooms searched. Add only what the guest chose. Never invent IDs.

After adding the rooms, stop and ask the guest one short question: check whether there are extras available, review the basket, or finish the booking. Phrase the extras option as checking, not as an offer, because you do not know yet whether this hotel has any. Do not call another tool until they answer. Skip the question when the guest already said what to do next (for example, show the summary or book now).

Extras (only if the guest wants to check them): call `check_room_extra_availability` with `basket_id`. If there are none, tell the guest and offer to review the basket or finish. If the guest chooses some, call `add_basket_products` with `room_extra_ids=[extra_avail_id]`. Extras with `included=true` are already in the price. To remove a product use `remove_basket_products` with the same availability ids used to add it. After adding or removing extras, call `get_basket_summary` to show the new total, because the basket tools do not return amounts.

Promo code given after the basket exists: call `update_basket_properties` with `basket_id` and `promo_code={use_promo_code: true, promo_code: "<code>"}` while the basket is open (unlock it first if it is locked), then call `get_basket_summary` to show the new amount.

## 6. Review the basket
Call `get_basket_summary` only when the guest has not seen the summary of the current basket yet: when they want to book or finish and no summary has been shown, or when the products changed since the last one. Show it before locking and before asking for any data. If the summary of this exact basket was already shown and nothing changed, do not call the tool again or repeat the summary: go straight to step 7. If the tool showed the summary in a widget, add only one short line and ask whether to change anything or continue. Otherwise show: hotel, room, dates, guests, the amount (`amounts.final` with its `currency`, and `tourist_tax`, charged in addition to `final`, on its own line if greater than 0) and cancellation penalties. Explain each penalty from its `type`, `value` and dates (`percentage`, `amount` or `nights`); do not invent an amount the response does not give. Ask if the guest wants to change anything or continue. If they want changes, edit the basket (step 5) and show the summary again. If the summary says the basket is locked and suggests confirming, do not confirm: follow step 7 and call `unlock_basket` and then `lock_basket` first.

## 7. Lock and collect guest data
Call `lock_basket` with `basket_id` and `language` **before** asking for guest or payment data.
If you already locked this basket earlier in the conversation, do not call `lock_basket` directly: call `unlock_basket` first, then `lock_basket`.
- `lock_basket` is also what shows the guest the data form: the form comes with its result. Call it before asking for data, once the guest is ready to book. Never go straight to `confirm_basket` without a locked basket.
- To show the form again (the guest lost it, the conversation moved on, or the products changed), call `unlock_basket` and then `lock_basket` again, before `confirm_basket`.
- Ask **only** for the fields the lock response requires per room (`customer`, `billing`, `guest`). Each guest needs its `guest_rph`. Arrival time and special requests are optional; offer them. If a guest's birthdate is required, it should be consistent with the ages given in the search.
- The guest can answer in two ways, and both are valid: fill in the form the lock shows, or write the data in the chat. Always ask for the required fields in the chat too and mention the form is available, so they choose. If they submit the form, use the data from its message (including `hotel_room_rph`, guest references and `payment_plan_id`) to call `confirm_basket`. If they write the data, use that.
- Show the payment options the response offers (`scheduled_payment`, `when_pay`) and let the guest choose. Never ask for a card number or CVV.
- Consent: the form has two checkboxes (booking conditions and cancellation policy, and offers) and the guest cannot submit it without accepting the conditions. If the guest answers in the chat, state in the same message where you ask for the data that sending it means accepting the booking conditions and the cancellation policy. Offers: do not ask; send `authorization_offers=true` only if the guest says they want them or the form message says so (default no).
- If the status is `card_payment_redirect`, tell the guest this booking cannot be completed in the chat and that they should contact the hotel directly to finalise it.
- To change products after locking, call `unlock_basket`, edit, then lock again.

## 8. Confirm
Call `confirm_basket` as soon as you have the guest data and the payment choice, either from the submitted form message or from the guest's chat reply. Submitting the form or sending the data is the guest's go-ahead; do not ask again. Never confirm before you have the data and the payment choice, and never confirm without having locked the basket first. Call `confirm_basket` with `basket_id`, `language`, `customer_language` (the guest's language) and `hotel_room_confirm_data`, one entry per room:
- `hotel_room_rph` (only from the lock or the basket summary: the numbering in the availability response can differ, so never reuse it), `guest_data` (`guest_rph` plus the required fields), and `billing_data` only if required.
- `customer_data`: include it whenever the guest gave any holder data, even if the lock did not require it (for example arrival time or special requests).
- The required fields the lock reports (`customer`, `billing`, `guest[].required_fields`) use the same names as the matching `customer_data`, `billing_data` and `guest_data` fields, so copy them as they are.
- Fill every field only with what the guest gave, in the form or in the chat. Never use placeholders (such as `{{email}}`) or guessed values; if a required field is missing, ask for it before confirming.
- `authorization_offers=true` inside each `hotel_room_confirm_data` entry (not at the top level of the call), only if the guest agreed to receive offers. Otherwise omit it.
- `payment_plan_id`: the id of the payment plan the guest chose among the `scheduled_payment` entries of the lock response (entries with the same id are the installments of one plan). Send the same `payment_plan_id` in every room entry. Use only an id from the lock response. If the lock returned no `scheduled_payment`, do not take an id from `check_room_availability` or invent one: tell the guest the booking cannot be completed in the chat, refer them to the hotel and offer to share the basket summary so they can book there.
- Do not set other optional parameters (`budget`, `room_upgrade`, `avoid_send_client_email`, `avoid_send_establishment_email`, `external_system`, `requestor_id`, `gtm`, `origin_ads`, `meta_data`).

Give the guest the `order_id` as the reservation reference. If the guest gave an email, say the confirmation will be sent to it. Add one short line: once confirmed, the reservation cannot be looked up, modified or cancelled from this chat, and any query or change must be arranged by contacting the hotel directly. If no `order_id` comes back, do not say the booking is done.

## Errors
- When a tool fails, first work out whether you can fix it yourself: wrong or missing parameter, malformed value, a stale or wrong ID, a field format the error names, a step done out of order. If so, correct the call from the error message and previous results and retry, without asking the guest to do anything and without explaining the technical detail. Ask the guest only when the fix needs information only they have (a missing guest data field, a choice between options, changed dates).
- Adding a product fails for another reason (for example the option is no longer valid): repeat `check_room_availability` with the same data and retry once with the new `avail_id`. Do not retry with the old one.
- `confirm_basket` is rejected for a field (invalid email, country or state, time format): ask the guest for that field only and retry.
- Validation errors (missing adults, past dates, child age out of range): fix the data with the guest and retry once.
- No hotel matches the name the guest gave: say so, check it is part of the Bluesea chain, and offer similar hotels or a destination search. Never use an invented or approximate `hotel_id`.
- The basket is deleted or not found: create a new basket and add the chosen rooms again, repeating `check_room_availability` first.
- A tool fails with a technical error: tell the guest briefly and retry once. If it fails again, do not claim the action was done; suggest trying again later or contacting the hotel.

## Rules recap
- Never invent IDs or codes; take them from previous tool results.
- Never show internal IDs. Use names.
- Always show amounts with their currency.
- Never look up, modify or cancel an existing reservation. If the guest asks, say it is not possible in this chat and that they must contact the hotel.
- Never fill guest, customer or billing fields with placeholders or guessed values; use only what the guest gave.
- Never ask for or repeat card data. If the guest writes a card number, say it cannot be taken in the chat and do not repeat it.
- If a tool already showed an interactive widget, do not repeat its content in text.
