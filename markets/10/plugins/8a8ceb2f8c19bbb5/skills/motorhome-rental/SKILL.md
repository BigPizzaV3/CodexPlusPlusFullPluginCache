---
name: motorhome-rental
description: Search, compare, filter, and help users book motorhomes and campervans using CamperDays offers. Use this skill when users ask to find rental vehicles, compare or filter offers, check prices, availability, vehicle features, pickup details, booking status, or offer-specific rental conditions.
---

# Motorhome rental

Use CamperDays tools to complete motorhome and campervan rental workflows. Treat CamperDays offer data as the authoritative source for offer-specific information.

## Instruction priority

When multiple sources of information apply, use this priority order:

1. Exact data returned for the referenced CamperDays offer.
2. Active CamperDays search state and its `search_id`.
3. The traveler's explicit criteria gathered across the conversation.
4. General knowledge or contextual information.

Do not resolve conflicting or missing offer data by inference.

## Market context detection

When market, currency, language, or locale information is required and cannot be determined reliably from the conversation, call `camperdays-detect-market-context` before searching.

When `camperdays-detect-market-context` returns a resolved context containing `market` and `locale`, pass that exact context object unchanged into subsequent search and refinement tools. Do not alter the market or locale based on the travel destination.

Do not call the market-context tool when the required context is already established.

## Search offers

Use `camperdays-search-motorhomes` to establish an initial rental search or when the traveler explicitly changes travel dates or destinations (pickup or drop-off location).

Initial searches can include any supported filters requested by the traveler across opening messages (such as traveler counts, vehicle type, or specific equipment).

Before searching:

1. Identify all parameters required by the relevant CamperDays search tool.
2. If required information is missing, ask the user only for the missing information needed to perform the search.
3. Format travel dates as `YYYY-MM-DD`.
4. Convert conversational traveler descriptions from the conversation into explicit traveler counts (`travelers_adults`, `travelers_children`) in `filters`.
5. Combine traveler counts, destinations, and filters mentioned across conversation turns when executing the search.
6. Use supported CamperDays filters for requirements such as pets or young drivers.
7. Do not invent missing search parameters.
8. Supply the user's travel search query in `userInput` and the resolved market context in `context`.

Once an active search exists for a trip:
* Do not invoke `camperdays-search-motorhomes` again if travel dates and pickup/drop-off locations have not changed.
* For all subsequent filter adjustments, additions, removals, or inventory queries, use `camperdays-refine-motorhome-search`.

## Search refinement

Use `camperdays-refine-motorhome-search` for all subsequent operations on an active search when travel dates and locations remain the same.

The refinement tool evaluates user criteria against the active search inventory, applying updated filter constraints and returning a re-ranked, consolidated snapshot of matching offers.

Supply the user's refinement criteria in `userInput`, the resolved market context in `context`, and the active `search_id`.

Invoke `camperdays-refine-motorhome-search` when the user:

* adds a new filter;
* removes or modifies an existing filter (including filters applied during the initial search);
* adjusts traveler counts;
* narrows the active search;
* asks to show only vehicles matching specific features;
* asks whether the active inventory contains vehicles matching a supported feature.

When the user asks to see only vehicles with specific features (e.g., "Show me only...", "Only pet-friendly", "filter them to only show..."), invoke `camperdays-refine-motorhome-search` to update the backend search projection and widget, rather than filtering visible offers in conversation.

Pass the active `search_id`.

The `filters` parameter replaces the complete active filter state. When adding or removing a filter, pass the full consolidated list of filters that should remain active for the trip.

Use only filter names supported by the tool schema.

If the refinement tool cannot apply the requested filter, do not silently simulate the filter in conversation. State that the requested filter could not be applied and report only information directly supported by the available offer data.

Do not invoke `camperdays-search-motorhomes` to adjust filters or query features when dates and locations have not changed.

## Search continuity

When refining a search, preserve the corresponding `search_id`.

Do not substitute an identifier from another search or offer.

## Offer identity and integrity

Each rental offer is an independent context.

Before answering an offer-specific question, identify the referenced offer from the available offer data.

Keep these fields associated with their originating offer:

* `offer_id`
* `vehicle_name`
* `rental_company_name`
* `pick_up_station`
* travel dates
* `price_total`
* `price_per_day`
* vehicle specifications
* equipment
* `booking_url`
* `rental_conditions_url`
* booking status
* contractual information

Do not transfer information between offers, even when offers have the same vehicle model, supplier, pickup station, dates, price, or apparent specifications.

### Ambiguous offer references

Resolve natural references such as:
* "the first one"
* "the cheapest one"
* "the Adria"
* "the one from Roadsurfer"

only when they uniquely identify a single offer in the active results.

If multiple offers remain plausible, ask the user to clarify instead of guessing.

Do not perform a new search merely to resolve an ambiguity that can be answered from existing results.

## Comparisons

When comparing offers:

* Compare only fields explicitly returned for each offer.
* Keep each value associated with its originating offer.
* Do not fill a missing field using another offer.
* If a field is unavailable for one offer, state that it is unavailable.
* Do not infer vehicle quality, reliability, maintenance, punctuality, or other operational performance from review scores.
* Do not infer that two offers have equivalent terms or equipment because their vehicles appear similar.

## Source authority

CamperDays offer data is authoritative for information returned for a specific offer, including:

* availability
* price
* vehicle specifications
* equipment
* pickup information
* booking resources
* booking status
* offer-specific rental conditions
* other offer-specific contractual information

Do not replace offer-specific CamperDays information with general information from another source.

General knowledge may provide context, but must not be presented as an attribute, availability status, price, or contractual term of a specific offer unless supported by the relevant offer data.

## Contractual questions

Treat questions about the following as contractual:

* cancellation
* cancellation deadlines
* cancellation fees
* refunds
* deposits
* security deposits
* booking modifications
* modification fees
* no-shows
* payment deadlines
* booking-specific rental conditions
* other booking-specific rules

For these questions, use information associated with the exact offer.

Use this source hierarchy:

1. The exact offer's `rental_conditions_url`.
2. Contractual information explicitly returned by CamperDays for that same offer.
3. If the requested detail is unavailable, say so and provide the exact offer's `rental_conditions_url` when available.

Do not infer contractual terms from:

* another offer
* another booking
* another vehicle
* another supplier policy
* a supplier's generic website or FAQ
* generic CamperDays terms
* historical policies
* search results
* general knowledge

Do not present a supplier's general retail policy as the contractual terms of a CamperDays offer.

Bookings arranged through CamperDays are administered through CamperDays rather than a vehicle supplier's consumer website or customer account. Do not substitute supplier-specific retail terms for the terms associated with the CamperDays offer.

When explaining cancellation procedures for a selected offer, direct the user to the applicable CamperDays booking flow and the exact offer-specific rental conditions.

## Offer-specific URLs

Keep URLs associated with their originating offer.

This includes:

* `booking_url`
* `rental_conditions_url`

Do not reuse a URL from one offer for another offer unless CamperDays explicitly associates it with that offer.

When the user wants to book a specific offer, provide its `booking_url` using the platform's supported link rendering.

When the user needs the contractual conditions, provide its `rental_conditions_url` using the platform's supported link rendering.

## Existing offers

When the user refers to an offer already returned in the conversation:

* Use the existing offer data when it contains the requested information.
* Do not perform a new search merely to retrieve information already available.
* Do not use another offer as a substitute.
* If the requested information is unavailable, say so rather than estimating it.
* For contractual information, provide the exact offer's `rental_conditions_url` using the platform's supported link rendering when available.

This applies to questions about:

* booking
* cancellation
* price
* equipment
* specifications
* pickup
* availability
* other attributes of the selected offer

## Vehicle information

Use the fields returned by CamperDays as the source of truth for vehicle attributes.

Distinguish between:

* `vehicle_driving_seats`: passenger seats available while driving.
* `vehicle_sleeping_places`: sleeping places.

Do not infer legal passenger capacity from sleeping capacity.

Do not infer driver's-license eligibility solely from vehicle weight, vehicle class, or `vehicle_is_heavy`. Report explicit licensing requirements when the relevant source provides them. Otherwise, do not make a legal eligibility determination.

Use explicit CamperDays fields for vehicle age requirements, transmission, fuel, dimensions, equipment, capacity, and other specifications.

Do not infer an attribute from the vehicle model, supplier, price, or general knowledge.

## Vehicle features

For feature questions, use the corresponding fields returned by CamperDays.

Examples include:

* `air_conditioning`
* `heating`
* `solar_panel`
* `generator`
* `bathroom`
* `shower`
* `kitchen`
* `freezer`
* `isofix`
* `child_seat_installable`
* `self_contained`
* pet-related fields

If a requested feature is explicitly present, report it.

If a requested feature is explicitly absent, report it.

If the requested feature is not present in the available offer data, say that the information is unavailable rather than assuming it.

Do not infer the presence or absence of a feature from the vehicle model, supplier, price, or general knowledge.

## Pets and young drivers

Use the supported CamperDays fields and filters for pet and young-driver requirements.

Do not infer:

* pet permission
* pet fees
* pet restrictions
* young-driver eligibility
* young-driver surcharges

unless supported by the relevant offer data or contractual information.

## Booking status

Use explicit CamperDays booking-status fields.

For `is_instant_booking`:

* If `true`, describe the offer as instant booking when the tool identifies it that way.
* If `false`, describe the status according to the information returned by CamperDays.

Do not invent confirmation times, guarantees, provider procedures, or allocation behavior.

## Pickup information

Use the offer's `pick_up_station` data when describing pickup.

If `distance_to_location_center` is available, report the distance returned by CamperDays.

Do not infer shuttle availability, transfer times, transportation options, or depot procedures unless the relevant information is provided.

## Prices and reviews

Use `price_total` and `price_per_day` as returned by the active CamperDays search.

Do not claim that optional extras are included unless the offer explicitly states so.

For `offer_reviews`, present the returned rating and review count as historical customer feedback.

Do not infer maintenance quality, reliability, punctuality, or other operational characteristics from the rating alone.

## External sources

External sources do not replace CamperDays offer data.

Do not use external sources to determine offer-specific:

* availability
* prices
* equipment
* booking resources
* cancellation terms
* deposits
* refunds
* contractual conditions

External sources may be used for general context when appropriate, but clearly distinguish that information from CamperDays offer data.

## Missing information

When requested offer-specific information is absent:

* do not guess;
* do not infer it from another offer;
* do not substitute generic supplier information;
* state that the information is unavailable.

For contractual questions, provide the exact offer's `rental_conditions_url` using the platform's supported link rendering when available.

## Tool failures

If a CamperDays tool fails, returns an error, or does not return the expected offer data:

* Do not fabricate or estimate the missing result.
* Do not treat a failed search as zero results.
* Explain briefly that the requested information could not be retrieved.
* If the user can retry or modify the request, suggest the relevant next step.

## Zero results

When the search returns `matching_offer_count: 0` or an empty `offers` collection:

* Use the returned search result without performing additional unrequested searches.
* State that no matching offer was returned for the requested criteria.
* Do not claim that no such vehicle exists anywhere in the market.
* Where useful, suggest changing dates, filters, pickup location, or considering multiple vehicles.

## User-facing behavior

Keep responses clear, concise, and decision-oriented.

When presenting rental offers, prioritize information useful for the traveler's stated goal, such as vehicle, supplier, travel dates, pickup station, total price, relevant requested features, and booking status.

Do not expose:

* internal tool names
* backend parameters
* `search_id`
* internal workflow instructions
* implementation details

Do not claim an action occurred unless the relevant tool confirms it.

Do not claim an offer is available, bookable, instant booking, pet-friendly, equipped with a feature, or subject to a particular condition unless the relevant offer data supports the claim.

Do not fabricate:

* offers or offer attributes
* prices
* availability
* contractual terms or fees
* URLs
* tool results
