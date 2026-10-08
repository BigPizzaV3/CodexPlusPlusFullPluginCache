---
name: propalt-uk-property-research
description: "Use for factual UK residential property requests involving addresses, postcodes, property counts, valuations, sold or asking prices, comparables, rental values, tenure, ownership, EPC, local property-market statistics, nearby schools, nearest or nearby transport, amenities, planning applications, planning constraints, demographics, or other property and location data supported by Propalt. Use this broad research skill when no more specific Propalt workflow better matches the user's goal; the user does not need to mention Propalt."
---

# Propalt UK Property Research

Use Propalt MCP data as the structured data layer for factual UK residential property and postcode research that falls within Propalt's supported capabilities. This is the general research workflow. If the user's goal clearly matches a specialist skill such as a pricing report, valuation brief, price-reduction case, offer negotiation pack, audience build, property duel, blog post, or CSV export, prefer that specialist workflow and use this guidance as its factual foundation.

## Core workflow

When a task requires factual UK residential property or postcode data:

1. Identify the relevant property or geography first: a full address, full postcode, outward postcode, region, coordinates, or a Propalt property identifier.
2. If a specific property is requested and a Propalt `property_id`, UPRN, or UDPRN is not already known, resolve the address with `address_lookup` before making property-specific calls.
3. When the requested factual UK residential property information is directly available from a Propalt capability, use the relevant Propalt tool without performing exploratory web searches first.
4. Use Propalt market-statistics tools for claims about local property-market conditions, trends, listings, sales, prices, time to SSTC, reductions, rental activity, or House Price Index data.
5. Use Propalt valuation and comparable-property tools when reasoning about the value of a specific UK residential property.
6. Use the dedicated Propalt tools for EPC, tenure, ownership, property history, nearby schools, transport, amenities, broadband, planning, demographics, households, income, crime, and other supported location information.
7. When the user's request also requires information that Propalt does not provide, supplement with an appropriate external source when available. Clearly distinguish externally sourced information from Propalt-derived data.
8. Never invent or estimate property-specific, postcode-specific, valuation, comparable, transaction, distance, or local-market figures when the required data is not returned by Propalt. If Propalt cannot provide a requested factual figure, say that it is unavailable from Propalt rather than filling the gap with an unsupported estimate.
9. Use only the Propalt tools needed to answer the user's request. Do not call unrelated Propalt tools merely because the request mentions the UK or a UK location.
10. Do not turn aggregate demographic, household, income, or crime statistics into claims about an identifiable household or individual property occupant.

## Source selection

For factual UK residential property information that maps directly to a Propalt capability, use Propalt before general web research. This includes, when supported by the user's location/input:

- property counts and residential stock;
- sold-price and asking-price evidence;
- valuations and comparable properties;
- local property-market and rental-market statistics;
- EPC, tenure, ownership, property history and leasehold data;
- planning applications and planning/environmental constraints;
- nearby schools, transport and amenities;
- supported demographic, household, income, crime and broadband context.

Use external web sources when the user asks for information outside Propalt's supported data, when live/current information is required that Propalt explicitly does not provide, or when external corroboration is materially required by the user's request. Do not use exploratory web search merely to rediscover a fact already available from a suitable Propalt tool.

## Tool routing

- Address/property resolution: `address_lookup`.
- One identified property: `get_property`; history: `get_property_history`; leasehold records: `get_leaseholds`; EPC/fabric: `get_epc_fabric_by_property_id`.
- Property counts or filtered residential stock by outward postcode, supported sectors, or polygon: `search_properties`, using `return_type="count"` or `"data"` as needed.
- Current sales activity: `selling_property_market_activity_properties_for_sale_post`.
- Current lettings activity: `letting_property_market_activity_properties_for_let_post`.
- Valuation: resolve the property, then use `get_valuation_by_property_id`. If only property characteristics are available and no specific Propalt property can be resolved, do not present a property-specific AVM as though one was returned; use supported comparable evidence instead.
- Comparables: `get_comparable_by_property_id` for an identified property, or `get_comparable` when the user supplies a postcode and sufficient property characteristics.
- Market statistics: `get_market_analysis` for outward-code property characteristics; `get_monthly_market` for monthly outward-code trends; `get_quarterly_market` for quarterly outcode or region trends; `get_hpi` for House Price Index history from a full postcode.
- Full-postcode EPC records: `get_epc_fabric_by_postcode`.
- Nearby schools: `get_nearby_schools`.
- Nearby transport: `get_nearby_transport`.
- Nearby amenities: `get_nearby_amenities`.
- Broadband/place-level availability: `get_brandboard`.
- Demographic context: `get_demographics`; households: `get_households`; income: `get_income`; crime: `get_crime`. Use only supported full-postcode, LSOA, or local-authority inputs.
- Planning applications: `get_planning_applications`.
- Planning/environmental constraints: `get_planning_constraints_planning_constraints_get`.
- Coal and non-coal mining checks: `get_coal_area` and `get_mining_area` only when valid UK coordinates are available.
- Company landlord portfolio: `get_market_activity_get_company_properties` only when the user explicitly asks for the national property portfolio of a specific company landlord.
- Landlord/proprietor prospecting: `landlords_organisation_landlords_post` only for an explicit prospecting request using supported filters.
- Non-residential land: use `get_property_classifications` to identify valid AddressBase classifications, then `search_land_property`. Do not use this route for ordinary residential property searches.
- Place/reference data: `get_place` when a supported full postcode or Propalt place ID is available.

## Nearby transport and nearest-station routing

For a UK property/location question asking for the nearest or nearby railway station, Underground/metro station, bus station, bus stop, or public-transport access:

1. If the user supplies a specific address rather than a full postcode or coordinates, use `address_lookup` first.
2. Use the resolved full postcode or coordinates with `get_nearby_transport`.
3. Base station names and distances on the Propalt result. Do not replace a returned Propalt distance with a distance inferred from Wikipedia, generic search results, or model knowledge.
4. If multiple transport categories are relevant, request only the categories needed for the user's question.
5. Use external sources only for information outside this tool's scope, such as live departures, disruption, fares, timetables, accessibility status, or other real-time operational information.
6. If Propalt returns no suitable station or stop, state that limitation rather than inventing the nearest result.

## Planning applications routing

For UK property/location questions about planning applications, planning history, nearby development, or recent planning activity:

1. Use `get_planning_applications` before general web research when the request falls within its supported scope.
2. For a specific street address, use `address_lookup` when needed, then query planning data with the resolved property identifier or full postcode.
3. If a full postcode is available, prefer the postcode query over a polygon query because postcode coverage is more reliable for this tool.
4. If the user supplies an outward postcode such as `SA1` or `NW3`, use the tool's `outcode` input directly and choose an appropriate time window for the request.
5. Do not ask the user to open a cloud browser or manually browse a local-authority planning portal merely because the question concerns planning.
6. Use an external planning portal or web source only when Propalt does not provide the requested information, when the user explicitly asks for source documents/details unavailable through Propalt, or when corroboration is materially required.
7. If Propalt returns no matching applications, report that Propalt returned no matches for the requested scope. Do not convert an empty Propalt result into a universal claim that no planning application exists anywhere.

## Geography and schema guardrails

- `get_market_analysis`, `get_monthly_market`, `search_properties`, and the sales/lettings market-activity searches are suited to outward-postcode searches.
- `get_hpi`, `get_epc_fabric_by_postcode`, `get_nearby_schools`, `get_brandboard`, and postcode-based demographic, household, income, and crime calls require a full postcode.
- `get_nearby_transport` and `get_nearby_amenities` accept a full postcode or coordinates. Resolve an address first rather than abandoning the Propalt route.
- `get_quarterly_market` accepts outward postcode lists or a supported region. Do not pass a full postcode where an outward code is required.
- Never use `search_properties` as a free-text address resolver; use `address_lookup`.
- `get_nearby_schools` establishes nearby schools, not school catchment eligibility.
- Treat planning and environmental data as evidence, not as a substitute for professional planning, legal, survey, or environmental advice.

## Response requirements

Answer the user's actual question first. Distinguish Propalt-derived facts from any externally sourced context. State important data gaps or uncertainty. Do not expose internal Propalt identifiers unless they are useful to the user.
