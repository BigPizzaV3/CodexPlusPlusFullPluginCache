---
name: event-network-directory
description: Search public Event Network directories and, with New Systems OAuth consent, read the user's accessible profiles, jobs, listings, purchase groups, riders, and shared availability.
---

# Event Network directory workflow

Use the Event Network MCP tools whenever the user asks for current companies, specialists, equipment listings, public profiles, jobs, purchase groups, technical riders, venues, or shared availability. Do not fabricate results from general knowledge. Respond in the language used by the user and include a clickable Markdown link using profileUrl for every result you present: companies and teams, specialists (including speakers and artists), venues, rental equipment and used-equipment listings. Use the item name as the link label. A photoUrl or external website is not a substitute for the Event Network page. Do not invent a link if profileUrl is missing. Public search tools work without signing in. Use protected account tools only after the user asks for their own data and completes New Systems OAuth consent.

## Company searches

- Call `search_companies` with the requested profile city and country when known.
- For a rental request, use relevant search words such as `rental` or the user's local-language equivalent, then inspect the returned `companyType`, specializations, and public profile evidence.
- The directory does not define a universal rental category in this tool contract. Do not label a company a rental company based only on a loose keyword match; call it a candidate and state the evidence if the profile is ambiguous.
- A city's company filter matches the city saved on the profile, not a geographic radius.

## Specialist searches and equipment skill claims

- Call `search_specialists` for public specialist profiles. Use `city` for the profile city, `worksInCountries` for country-level work coverage, `specializations` for Event Network specialization keys, and `skills` only for public certificate/skill names.
- For a console or software such as grandMA3, search for the exact term in public profile data and listed equipment as appropriate. A returned equipment entry proves only that the item appears in the profile's active equipment list; it does not prove that the specialist can operate it. State this distinction unless a returned skill, certificate, or profile statement explicitly confirms proficiency.
- Use the returned `specialistId` for follow-up profile and availability calls. Do not use an ID guessed from a name.

## Public equipment listings

- Call `search_equipment` with `manufacturer` and `model` in separate fields when both are known. For example, search Robe MegaPointe with `manufacturer: "Robe"` and `model: "MegaPointe"`. The `query` field searches model text only; do not combine the manufacturer and model in `query`.
- Group listings by returned `companyId` when the user asks which companies have the equipment. Call `get_company_profile` only when more company details are needed.
- A result is an active public listing. Report `quantityTotal` as the published listing quantity and `availabilitySharingEnabled` as the company’s sharing setting. These values do not reveal a reservation.
- When the user asks about a date, pass `dateFrom`, `dateTo` when a range is requested, and the locality’s IANA timezone. If only one date is requested, pass it as `dateFrom`; `dateTo` defaults to that date. The maximum range is 31 inclusive dates.
- Report `quantityAvailable` only when `availabilityStatus` is `available` or `unavailable`. `unknown` means no confirmed quantity was returned; never turn it into zero or infer availability from a general company calendar. The tool returns aggregate quantities only, not booking details.

## Used-equipment marketplace

- Use `search_equipment_marketplace` for second-hand equipment being offered for sale. Use `search_equipment` for rental listings; do not mix the two results.
- When the user gives both manufacturer and model, pass them separately as `manufacturer` and `query` (the marketplace query matches the listing name/model).
- The marketplace returns active public listings and may include listed price, condition, city, and a public seller company name. It omits personal seller contacts and quantity counts. Do not infer stock quantity or date-specific availability for sale listings.

## Public venues and geographic searches

- Use `search_locations` for venues. Pass a public type name such as `hotel`, `minStars` for a minimum rating, and `minCapacity` for a minimum largest-room value.
- For a request such as “a hotel with at least 4 stars for 500 people near Warsaw,” search with `locationType: "hotel"`, `minStars: 4`, `minCapacity: 500`, `nearCity: "Warszawa"`, `country: "PL"`. The geographic radius defaults to 50 km; use `radiusKm` when the user specifies another radius.
- `minCapacity` filters Event Network’s `biggest_room` field. Call it the largest-room value or a capacity proxy; it does not verify the seating layout or guarantee that 500 people fit. Recommend confirming the exact room setup with the venue.
- City-radius searches resolve a public city center through Event Network’s location-search service. If the city cannot be resolved unambiguously, report that and ask which city/country to use. The result does not expose an exact distance for each venue.
- Return the venue’s name, type, stars, largest-room value, city/region, and profile link when present. Do not expose exact street addresses, coordinates, private contacts, or internal owner IDs.

## Specialist availability and location

- First search for candidate specialists. For a job in Germany, `worksInCountries: ["DE"]` means the profile says the specialist works in Germany; it does not mean Berlin-specific coverage.
- The `city` search matches the profile's saved city. It does not verify travel to the job location. The availability tool checks calendar status and does not accept a venue or city parameter; disclose this when the user asks about a specific job location.
- Call `check_specialist_availability` using each candidate's returned `specialistId`, inclusive `dateFrom` and `dateTo` in `YYYY-MM-DD`, and the IANA timezone for the requested locality (for Berlin, `Europe/Berlin`).
- Report `available` only for status `available`, `busy` only for `busy`, and explain that `unknown` cannot be confirmed. Never describe `unknown` as free.
- If the user omits the year and context does not establish it safely, ask for the year. If the date has passed this year, do not silently change it to next year.

## Account data and profile context

- Call `list_account_contexts` after OAuth to show the personal and company profiles the authenticated user can access. If more than one context could match the request, ask which to use.
- Pass both `contextType` and `contextId` explicitly to `get_my_jobs`, `get_my_job_detail`, `get_my_listings`, `find_matching_jobs`, `search_purchase_groups`, `search_technical_riders`, and `get_my_calendar` whenever their schema requires a context. Never guess an ID or silently switch profiles.
- Context selection applies only to the current request. It does not change the user's active Event Network profile or the selection in another conversation.
- Treat authorization failures as final for that context. Do not retry by guessing another profile ID or broaden access. The server rechecks the user's existing Event Network permissions on every request.
- Account reads use `eventnetwork:read`; job publication additionally requires `eventnetwork:write`. Ask one question at a time about profile context, contractor type, specialization, title/description, date/location, transport/compensation, contract/logistics, extra criteria and public/private visibility. Use `list_filter_values` for IDs. Call `prepare_job` only when required fields are complete; present its full preview and wait for explicit confirmation before `publish_job`. The encrypted preview has no time-based expiry, is bound to the selected context and is single-use. File/photo attachments are not supported. Do not submit applications or messages, book equipment, change calendars or edit existing records. Calendar results are summaries only; never request or reveal event names or details.

## Search quality, pagination, and privacy

- Search results are public directory matches, not an endorsement or independent validation. Separate returned facts from your interpretation.
- If `nextPage` is non-null and more results are needed, continue with that page number; do not repeat page one.
- Use only fields returned by the MCP tools and the context authorized for the call. Do not seek or infer private contacts, exact addresses, or calendar event details. Do not infer an available equipment quantity when the result is unknown.
- Search pages default to 20 records and cap at 50; rental availability pages cap at 10. Return the first useful page and mention when more results are available. Continue pagination only when the user needs more results; never fetch the whole directory automatically.
- Public searches are read-only. Do not claim to book equipment, contact a company, or edit existing Event Network records.

## Confirmed collaborations

For every company/team or specialist profile (including speakers and artists) you present, include the returned confirmedCollaborationsCount alongside its profile link. Use only this confirmed total, not ratings, posts or follower counts. Null means the API did not provide the number; say it is unavailable instead of inventing zero.
