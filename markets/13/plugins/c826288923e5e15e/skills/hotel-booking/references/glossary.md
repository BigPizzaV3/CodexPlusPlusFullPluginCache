# Glossary

## Board (meal plan) filter values
Use these in `filter_by.board_types` of `check_room_availability`:

| Value | Meaning |
|---|---|
| `roomonly` | Room only, no meals |
| `breakfast` | Breakfast included |
| `halfboard` | Breakfast and one meal |
| `fullboard` | Breakfast, lunch and dinner |
| `allinclusive` | All inclusive |
| `selfcatering` | Self catering |

The `boards[].name` in a result is the label to show the guest.

## Room types (`filter_by.room_types`)
`SNG` single, `DBL` double, `TRP` triple, `FAM` family, `SUI` suite, `THM` themed, `APT` apartment, `STD` studio, `BNG` bungalow, `RUH` rural house, `JRS` junior suite, `EVT` event space, `NON` unclassified.

## Reservation modes (`filter_by.reservation_modes`)
`room` standard per-room booking, `package` room plus extras, `product` standalone product. Omit to get all.

## Sorting (`check_room_availability`)
`order_by`: `price` (cheapest first), `location` (nearest first), `quantity` (most availability first), `order` (hotel and room merchandising rank), `id`, `hotelid`, `roomid` (stable sort by identifier). Without it results come sorted by price. `order_type`: `asc` or `desc`.

## Amenities in `filter_by`
`search_amenities` returns the codes grouped by type: `hotel` (amenities of the hotel) and `room` (amenities only available in rooms). Never invent codes. In `filter_by`, `hotel_amenity_ids` takes the `hotel` codes and `room_amenity_ids` takes the `room` codes; both filters must be met. To choose hotels by amenity, prefer `search_hotels(amenity_codes)` (only `hotel` codes) as in step 2 of SKILL.md.

## Amounts
- `final`: price to pay, without the tourist tax. Always show it with its `currency`.
- `tourist_tax`: charged in addition to `final`; show it on its own line when greater than 0.
- `before`: original price before offers; show it only when higher than `final`.
- `offers` and `discounts`: amount deducted by offers and by discounts.

## Calendar (`get_calendar_availability`)
Each day can carry:
- `price`: indicative price for that day, not the total of the stay, and with no `avail_id`.
- `availability` and `quota`: availability and remaining quota.
- `min_stay` and `max_stay`: minimum and maximum nights of the stay.
- `release`: minimum advance notice in days to book (release restriction). For example `release` 3 means booking at least 3 days before arrival; do not suggest closer days.
- `inventory_status.restriction`: `closedtoarrival` (closed to arrival, cannot check in that day), `closedtodeparture` (closed to departure, cannot check out that day), `closedboth` (both).
- `inventory_status.stop_sale`: sales stop with its `name`; the day is not bookable.

## Tool statuses
`ok` and `no_results` (search without matches), `card_payment_redirect` (the booking cannot be completed in the chat, see Payment).

## Rates
- `rate_id` -1 is the standard rate.
- There is no refundable or non-refundable flag. Do not infer it from the rate name: use the `cancellation_policies` of the result.
- `cancellation_policies[].type` is `percentage`, `amount` or `nights`, with a `value` and a date range. Explain it as plain text, e.g. "free until 3 days before, then 1 night". The basket summary calls the same list `cancel_penalties`.

## Payment
- `payment_plan: ["accept"]` in the lock response: the room accepts payment plans and `scheduled_payment` entries are listed.
- `scheduled_payment[].when_pay`: `now` (pay now), `establishment` (pay at the hotel), `scheduled` (on `exec_date`).
- `payment_options` keys: `pos` (card terminal), `transfer` (bank transfer), `paypal`, `financed`, `otb` (open-to-buy, deferred payment). They are informational: `confirm_basket` only takes a `payment_plan_id` per room.
- `scheduled_payment[].payment_method`: `credit` (agency or company credit line, no card), `tpv` (payment on the bank's secure gateway), `opentobuy` (card kept as a guarantee on the bank's gateway, no charge now). Plans that would require typing card details are never offered.
- If none of a room's payment options can be completed here, the lock returns `card_payment_redirect`: the booking cannot be completed in the chat and the guest must contact the hotel directly.

## Lock response fields
The lock reports the required fields in the blocks `customer`, `billing` and `guest`. In `confirm_basket` each room entry (`hotel_room_confirm_data[]`) carries them as `customer_data`, `billing_data` and `guest_data`, with the same field names. Each entry needs `hotel_room_rph`, `guest_data` and `payment_plan_id`.
- `customer`: `firstname`, `lastname`, `passport`, `email`, `address`, `postal_code`, `city`, `country`, `state`, `phone`. `arrival_time` and `special_requests` are always optional. `birthdate` belongs only to `guest`, never to `customer`.
- `billing`: `fiscal_name`, `fiscal_id`, `fiscal_address`, `postal_code`, `city`, `country`.
- `guest`: one entry per guest with its `guest_rph` and `required_fields` (`firstname`, `lastname`, `birthdate`, `passport`, `email`).
- `payment_method` (`deposit`, `complete`, `advance`, `establishment`, `installment`) is informational, like `payment_options`: only `payment_plan_id` is sent, per room.

## Basket status
`open` (editable), `locked` (data collection and confirmation; cannot be edited; `confirm_basket` requires it), `deleted`.

## Formats
Dates `YYYY-MM-DD`, arrival time `HH:mm`, `country` ISO 3166-1 alpha-2 (`ES`), `state` ISO 3166-2 (`ES-MD`).
