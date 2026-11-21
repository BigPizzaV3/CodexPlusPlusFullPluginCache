# Hotel workflow and field guide

Read this with [SKILL.md](../SKILL.md). **`tourmind-hotel` at `https://mcp-booking.tourmind.com/mcp/oauth/toc` is the sole hotel connection.** OAuth secrets are managed by the connection; this guide contains no credential configuration template. Earlier TourMind hotel field names below are compatibility references, not an authenticated schema capture for this OAuth endpoint. Current exposed schemas, documented semantics and returned data decide which fields may be used. Do not send unsupported fields or reconstruct legacy requests.

## Contents

- [Actual capabilities](#actual-capabilities)
- [Price and occupancy rules](#price-and-occupancy-rules)
- [Location, live rooms and ranking](#location-live-rooms-and-ranking)
- [Results and images](#results-and-images)
- [Final booking review](#final-booking-review)
- [Orders, cancellation and payment](#orders-cancellation-and-payment)
- [Error interpretation](#error-interpretation)

## Actual capabilities

| Operation | Earlier inputs/outputs to look for, only if present in the actual contract |
|---|---|
| Location resolution | Input `keyword`; output matching `regions[]` / `place` / hotel candidates |
| Hotel candidate search | Region ID, keyword or latitude/longitude/radius; dates, per-room occupants, room count and documented price filters |
| Hotel details | `hotel_id`; returned address, facilities, check-in/out, mandatory fees, hotel and static room images |
| Live room rates | `hotel_id`, dates and occupancy; product identifiers, room/meal/cancellation/inventory, original amount/currency |
| Batch live rates | Shared dates/occupancy plus hotel IDs; independently successful, empty or failed items |
| Availability check | Selected returned product identifier plus supported stay/occupancy; latest product/amount/currency/policy |
| Booking | Latest checked product, confirmed stay/occupancy, and only the guest/contact fields required by the actual contract, or a supported confirmed profile reference; actual order reference/status |
| Order query | Exact returned order reference; current status and policy/price/payment evidence |
| Cancellation | Exact queried order, current policy and explicit user confirmation; returned cancellation/refund state |
| Payment, if permitted | Exact queried payable order plus accepted method; actual payable total, fee, expiry and official destination |

Earlier IDs such as `hotel_id` and `region_id` were strings; preserve opaque identifiers exactly when their live schema uses strings. Product codes belong in tool arguments, not customer tables. Earlier order references used `agent_ref_id`; use the current response's actual field rather than assuming that label or synthesizing an identifier.

A tool name alone does not establish permission or side effects. Use exposed annotations/descriptions and actual behavior. If a tool's required credential arguments conflict with host-managed OAuth, stop the affected operation and report that server-side integration is incomplete; do not source a legacy key. A missing booking or payment tool cannot be replaced with a search link, arbitrary browser request, invented API call or different service.

## Price and occupancy rules

Require a destination, exact check-in/check-out, valid occupancy and a later checkout. Resolve dates in the user's timezone. When a year is omitted, use the next future occurrence and disclose the resolved dates. Preserve user values. Default to one room, one adult per room and no children only when those values are absent, with an explicit assumption note.

Earlier occupancy fields `adults`, `children`, `children_ages` described **each room**, while `room_count` repeated the same configuration. Under that contract, provide one child age from 0–17 per child and require `len(children_ages) == children`. Mixed per-room configurations were unsupported. Confirm the new contract before using it; do not send a `room_occupancies` structure unless the actual schema supports it. If total travelers cannot determine the supported room distribution, ask one focused question.

**Confirm price-filter units before sending them.** In the earlier service, `lowest_price` and `highest_price` were CNY totals for all nights and all rooms. Under that confirmed contract:

- For per-room nightly budgets, `request_bound_CNY = source_bound × current_CNY_exchange_rate × night_count × room_count`.
- For an explicit whole-trip budget, `request_bound_CNY = source_total × current_CNY_exchange_rate`; do not multiply again.
- Treat an ordinary hotel range without trip-total wording as per room per night and disclose that assumption.
- For one room over three nights at CNY 300–400 per night, the bounds are 900–1200; for two rooms, 1800–2400.

If the new schema documents different units, use those units. If units are undocumented, do not infer them from old field names or deliberately submit an invalid request to discover them. Explain the missing contract and ask for service documentation, or obtain the user's agreement to search without that filter and enforce the budget using verified live products where possible.

Use a current live exchange rate for non-CNY filtering or requested display conversion, with source and retrieval time. Never use model memory or relabel a number. If no current rate is available, ask for a budget in the tool's accepted currency or offer to proceed without the price filter; returned original-currency rates remain usable. Preserve original transaction currency and amounts internally.

For display, honor the user's explicit currency. Where reliable live conversion is available, the earlier presentation default was CNY for Chinese requests and USD otherwise. If conversion is unavailable, show the actual returned currency and explain the limitation. Clearly label converted figures approximate. Display conversion never changes the amount/currency sent to availability or booking tools. Show per-room nightly and complete-stay totals; do not divide a package total unless the returned price basis supports that calculation.

## Location, live rooms and ranking

For cities, neighborhoods, broad attractions, resorts or islands, prefer a high-confidence returned region over an arbitrary central point. Check the complete name and country/city context; a positive hotel count alone is insufficient. For a precise address, station, entrance, compact landmark or explicit radius, use a matching returned point and preserve the radius. Ask when several plausible matches remain. Never use a hotel as a proxy center or guess coordinates.

If no region exists and a broad destination resolves only to a representative point, disclose that limitation. With no hard radius, supported probes may expand from the returned recommendation through 3, 5, 10 and 20 km, merging by actual hotel ID and preserving nearer candidates. Respect the live endpoint's limits, stop when enough candidates are available, and state the final scope. Do not use this behavior for a user-specified radius or silently jump to a wider area.

Preserve the original candidate pool with all known failed constraints. Cached `min_price`, “from” prices or search availability probes do not establish a matching room for the requested occupancy, meal, refund policy or all nights. Obtain actual live room products before quoting/ranking prices. Batch item failures do not discard other successful items. An empty or failed batch item stays empty/failed; do not replace it automatically through a single-hotel query.

Where the current contract uses `is_on_request`, `false` means immediately bookable inventory and `true` means supplier confirmation is still needed. Only label immediate availability when the live response establishes it; an absent field is not `false`. A request product fails an explicit immediate-bookability requirement. Otherwise it may remain eligible but must be labeled and ranked after immediately bookable products.

Verify hard requirements first, including total budget, occupancy, star level, radius, required meal/bed and facilities. A preference is not a hard constraint unless the user made it one. Rank eligible hotels by the user's chosen sort, or by verified preference match, immediate bookability, distance, live stay total and cancellation flexibility. Give specific reasons backed by compared data; avoid unsupported claims such as “great value” or “convenient.”

Read meals and policies from documented values. Do not infer breakfast from an undocumented meal code or guarantee a meal from an ambiguous count. If a returned room type is `Others`, use “Other / room assigned at check-in” rather than inventing a room. A static room definition or photo is not live inventory.

## Results and images

Keep the user's language. Use this adaptable hotel-list structure; omit unavailable optional fields and links instead of displaying placeholders:

```markdown
Found {candidate_count} candidate hotels; verified live products for {truthful_scope} and selected {selected_count} matching hotels.

Area: {resolved_area_and_radius}
Stay: {check_in} to {check_out}, {nights} nights
Guests: {occupancy_and_room_distribution}
Price basis: per room per night; stay totals cover all requested rooms and nights
Currency: {actual_display_currency_and_conversion_note}

[View hotel results]({returned_list_url})

### 1. {hotel_name}

{supported_hotel_image}

[View hotel details]({this_hotel_returned_url})

| Distance | Stars | Matching room | Meal | Per room/night | Stay total | Cancellation | Inventory |
|---|---|---|---|---|---|---|---|
| {distance} | {stars} | {room} | {meal} | {nightly} | {total} | {policy_and_deadline} | {inventory} |

Why it matches: {two_or_three_verified_reasons}.
Address: {returned_address}
```

Default to five qualifying hotels, or fewer if fewer qualify. Name the ranking dimensions and verified scope accurately: “all candidates” requires live verification of every candidate. State when hard constraints limited results. End with an offer to show remaining candidates or inspect a selected hotel's rooms. When all results are requested, label nonmatches with their failed constraints rather than recommending them.

For a selected hotel, give its details and live rooms together:

```markdown
#### {room_name}

{supported_matching_room_image}

| Bed | Occupancy | Meal | Per room/night | Stay total | Cancellation | Inventory |
|---|---|---|---|---|---|---|
| {bed} | {occupancy} | {meal} | {nightly} | {total} | {policy_and_deadline} | {inventory} |
```

Show up to five distinct matching room products and offer the rest. End by inviting room selection for final availability/price verification.

Prefer native MCP media already shown inline. Otherwise use a returned remote image in Markdown only when the client permits it, or an accessible local file already returned by the tool using its absolute path. Do not download remote images to bypass host display restrictions. Select the hotel's returned hero/primary image; select a room photo only when it maps confidently to that room. Label a generic room-gallery image as generic, and state when a matching image is unavailable. Never substitute an unrelated image.

Use only actual returned public result/detail links and preserve them exactly, including query strings/fragments. Do not show raw access tickets separately, reconstruct URLs, use a hotel-list link as a specific hotel's detail link, or attach a payment link as an image. Apply a locale-path substitution only when the current endpoint's documentation explicitly permits it; an old locale convention does not authorize modifying a new signed link. Read-only hotel pages are browsing aids, not a substitute for tool-based verification or booking. Never infer new page capabilities from an old site version.

## Final booking review

After successful final verification, show the complete review below in the user's language. Use the checked transaction values, not an earlier search or approximate conversion. Include confirmed guest name and email so the user can verify them; do not show an OAuth credential, internal rate code or implementation identifier.

```markdown
### Please confirm your hotel booking

| Item | Verified details |
|---|---|
| Hotel | {hotel_name_and_address} |
| Room / bed / meal | {checked_room_bed_and_meal} |
| Check-in date | {check_in} |
| Check-out date | {check_out} |
| Hotel check-in / check-out times | {returned_times_or_not_provided} |
| Occupancy | {adults_and_children_per_room}; {room_count} rooms |
| Children's ages | {ages_per_room_or_not_applicable} |
| Guest's full legal name | {user_confirmed_name} |
| Contact email | {user_confirmed_email} |
| Room price total | {checked_total} {transaction_currency} |
| Taxes and mandatory charges | {returned_inclusions_exclusions_and_at_property_fees} |
| Cancellation policy | {checked_policy_deadline_and_penalty} |
| Availability | {checked_inventory_status} |

Please confirm the booking details above. I will create the booking only after your explicit confirmation. Payment, if supported, requires a separate review and confirmation.
```

Always show occupancy and children's ages; with no children use “0 children” and “Not applicable.” For missing hotel times use “Not provided by the hotel.” For absent mandatory-fee details say the hotel did not return additional mandatory-fee information; this is not proof that there are no extra charges. Do not claim taxes are included unless current policy establishes it. Surface explicit city/tourism taxes collected at the property without inventing the amount or charging basis. Preserve the exact cancellation timezone/deadline; ask or report ambiguity rather than guessing.

When the current contract requires contact email for booking or cancellation notifications, use a basic plausibility check without claiming deliverability verification. Ask only for missing/invalid required booking information; use a supported confirmed profile reference when available and do not make optional personal fields mandatory. Do not collect optional phone or document data by habit. Show personal fields in the review only when supplied for this booking. A materially changed name, email, room, stay, occupancy, price, policy, account or inventory cancels the earlier booking confirmation.

## Orders, cancellation and payment

Record the real order reference with the authorized connection/account context. Query and mutate only through that binding. Do not probe accounts or a different endpoint to find an order. If ownership/context is unclear, ask the user to reconnect to the relevant account or provide the actual reference; a guessed account cannot authorize order access.

Report statuses as returned and explain their documented meaning. Earlier statuses included `UNPAID`, `PENDING`, `CONFIRMED`, `CANCELLED` and `CONFIRM_FAILED`; do not impose that enum on a new response. Pending supplier confirmation is not confirmed; paid evidence blocks another payment; cancellation acceptance is not refund settlement.

Interpret current cancellation data as documented. Earlier `non_refundable` / `effective_non_refundable=true` meant non-refundable, while `free_cancel_before_deadline` applied only through its exact deadline. In the earlier legacy cancellation object, `refundable=true` meant cancellable, `startDateTime` was the free-cancellation deadline, and `amount` was the fee after that deadline. Do not reinterpret an unfamiliar schema merely because it uses similar field names.

Before cancellation, query the order, show current deadline, penalty/refund and any documented nonrefundable processing fee, confirm the exact reference, and obtain explicit cancellation approval. If the current policy cannot be established, explain the gap before proceeding; do not invent free cancellation.

For payment, require an actually exposed and authorized capability and a host-permitted payment flow. Query the current order, verify its documented payable state and future deadline when present, and block duplicate payment after paid/confirmed-payment evidence. Present only currently supported methods. Show original currency, order amount, additional fee and final payable total. A fee-estimation formula or historical provider name is not an API result. If a material fee is unknown before payment initiation, require a supported quote/review path or explain the limitation; do not invent the fee to obtain confirmation.

Obtain separate explicit payment approval after the review, including any documented nonrefundable-fee rule. Recheck payable state immediately before initiation and invalidate approval if reviewed facts changed. Use the exact returned official payment URL when allowed; do not modify it, invent a return URL, collect payment credentials in chat, or claim that a link proves payment. Unsupported payment or prohibited checkout remains a limitation, not authorization to use another API or browser action.

## Error interpretation

Use the current documented error semantics. Earlier hotel rate reasons provide hints only when the new response actually uses them:

| Observed reason | User-facing interpretation |
|---|---|
| `no_matching_live_room` | Successful empty result for the criteria; offer changes |
| `hotel_not_found` | Hotel missing or unavailable |
| `upstream_timeout` | Live pricing timed out; not proof of no inventory |
| `upstream_error` / `hotel_detail_unavailable` | Service or detail retrieval failed |
| `invalid_request` | Correct the request before another call |

Do not expose raw exceptions, credentials, guest/contact PII, internal rate/access codes or debug payloads. Say which requested operation failed or remains uncertain and the next supported step. Retain successful batch items and the original pool.

Retry safe transient read-only failures at most once. Never automatically retry a booking/payment/cancellation with an ambiguous outcome. Reconcile a known reference through this connection's supported read-only tool; if no reference exists or status remains uncertain, stop and use a verified support route. An absent returned order number is not proof that no order was created. A user request to retry or accept the risk does not resolve this uncertainty; do not repeat or replace the transaction until its original outcome is authoritatively reconciled. Do not invent idempotency support or a query capability; use them only if the live contract actually provides them.
