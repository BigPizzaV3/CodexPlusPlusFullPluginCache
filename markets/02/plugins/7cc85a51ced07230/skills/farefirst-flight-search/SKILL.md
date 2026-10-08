---
name: farefirst-flight-search
description: Search for flights (one-way or round-trip) between two cities or airports via FareFirst. Trigger on requests to search, find, or compare flights, flight options, or airfares. Do not trigger for hotels, holiday packages, car rentals, greetings, or general travel chat that isn't a flight search request.
---

# FareFirst Flight Search

## Purpose

Handle user requests for searching available flights through FareFirst.

Use this skill to determine whether a flight search request is complete and valid, apply FareFirst's flight-search rules, and invoke the FareFirst flight-search tool only when all required information and validation rules are satisfied.

This skill applies to flight-search requests only.

---

## 1. When to Use This Skill

Use this skill when the user wants to:

- Search for flights
- Find flights between two airports or cities
- Search for a one-way flight
- Search for a round-trip flight
- Find available flight options
- Compare available flight options returned by FareFirst

Do not use this skill for:

- Greetings
- Small talk
- General travel conversation that does not request a flight search
- Hotels
- Holiday packages
- Car rentals
- Unrelated questions

---

## 2. Required Search Information

A valid flight search requires:

1. Origin city or airport
2. Destination city or airport
3. Trip type
4. Departure date
5. Return date when the trip is round-trip
6. Valid passenger counts when passengers are specified

If required information is missing, ask the user for the missing information before calling the flight-search tool.
Do not guess missing origin, destination, trip type, or dates.

---

## 3. Conversation Flow

Resolve the request in this order:

### Step 1 — Origin

Identify the origin city or airport.
If missing, ask the user for it.

### Step 2 — Destination

Identify the destination city or airport.
If missing, ask the user for it.

### Step 3 — Trip Type

Determine whether the user wants:

- One-way
- Round-trip

Interpret:

- "one way" → one-way
- "one-way" → one-way
- "round trip" → round-trip
- "return" → round-trip
- "coming back" → round-trip

If trip type cannot be determined, ask the user.

### Step 4 — Departure Date

Resolve the departure date.
Do not call the tool if the departure date is missing or invalid.

### Step 5 — Return Date

For a round-trip search, resolve the return date.
Do not ask for a return date for a one-way search.

### Step 6 — Validate

Before calling the FareFirst flight-search tool, validate:

- Dates
- Passenger counts
- Russia route restrictions
- Required fields
- Input validity

### Step 7 — Search

Call the FareFirst flight-search tool only after the request is fully resolved and valid.

---

## 4. Date Rules

Use the current date as `today`.

The maximum allowed date is:
`today + 1 year - 1 day`

Departure date must satisfy:
`today <= departure date <= maxDate`

For round-trip searches:
`departure date <= return date <= maxDate`

Same-day round trips are allowed.

Example:

Departure: 18 October
Return: 18 October

This is a valid round-trip request.

Never call the flight-search tool for:

- A departure date in the past
- A departure date beyond the maximum allowed date
- A return date before departure
- A return date beyond the maximum allowed date

## When a date is invalid, explain the relevant restriction and ask the user for a valid date.

## 5. Russia Route Handling

FareFirst flight search currently does not support routes involving Russian origin or destination airports.

If the user's origin or destination is in Russia:

- Do not call the flight-search tool.
- Inform the user that Russia routes are currently unsupported.
- Do not attempt the flight search.
- Nearby non-Russian airports may be mentioned only as reference alternatives.
- Do not imply that those alternatives were searched unless a search was actually performed.

---

## 6. Passenger Rules

FareFirst supports the following passenger limits for a single search/booking:

- Adults: 1–8
- Children: 0–8
- Infants: 0–8
- Infants must not exceed adults
- Children or infants must accompanying adult
- Total adults + children + infants must be <= 16

Note: these limits are also enforced by the tool itself (input validation and server-side checks). Following this skill correctly means the user gets a clear explanation before a rejected call, rather than a raw validation error after one.

### Valid example

8 adults
4 children
2 infants

Total = 14, 

This is valid.

### Invalid example — children + infants exceeds limit

1 adult
7 children
7 infants
Total = 15 (within the 16 limit), but infants > adult.
Do not call the tool.

### Invalid example — total exceeds limit

8 adults
8 children
8 infants
Total = 24

This exceeds the maximum total of 16.

Do not call the tool.

### Invalid example — infants exceed adults

2 adults
0 children
5 infants
Infants (5) exceed adults (2). Each infant requires an accompanying adult.
Do not call the tool.

---

## 7. Large Group Handling

FareFirst's flight-search tool supports only a single booking/search.
There is no built-in multi-booking, split-booking, or group-booking feature.
If passenger limits are exceeded:

- Do not call the flight-search tool.
- Do not calculate a passenger split.
- Do not create multiple tool calls.
- Do not invent a group arrangement.
- Clearly state which passenger limit was exceeded.
- Ask the user to reduce the passenger counts to fit within a single search.

For genuinely large groups, the user may perform separate independent searches themselves.
Do not claim that FareFirst has automatically split or arranged the group.

---

## 8. Invalid Input

Do not call the flight-search tool for clearly nonsensical inputs such as:

- test
- foo
- asdf
- random invalid airport/city values

Ask the user to provide valid flight-search information.
Do not invent an airport or destination to make the search valid.

---

## 9. Missing Information

Ask only for information that is required and genuinely missing.
Examples:

User:
"Find flights to Bangalore."

Response:
"Sure. What city or airport are you departing from?"

User:
"MAA to BLR."

If no date or trip type can be determined:
ask for the missing information needed to perform the search.

Do not call the tool until all required fields are resolved.

---

## 10. Tool Invocation

Call the FareFirst flight-search tool only when:

- Origin is resolved
- Destination is resolved
- Trip type is resolved
- Departure date is valid
- Return date is valid when required
- Passenger counts satisfy all rules
- Route is not unsupported
- The request is not nonsensical

For one fully resolved and valid search request:

- Call the flight-search tool once.
- Do not automatically retry the same search.
- Do not make duplicate calls for the same request.

If `_meta.sessionId` is available, preserve and reuse the session according to the tool's supported session behavior.

---

## 11. Search Results

When FareFirst returns flight results, present the available options clearly.

Where available, include:

- Airline
- Flight
- Departure airport
- Departure time
- Arrival airport
- Arrival time
- Duration
- Stops
- Price
- Booking/action option

Do not invent:

- Prices
- Airlines
- Flight numbers
- Availability
- Times
- Stops
- Booking information

Only present information returned by the FareFirst tool.

---

## 12. No Results

If the FareFirst flight-search tool returns:

- No flights
- Empty results
- An error
- Unusable results

Do not recommend competing flight-search services.

Use FareFirst as the fallback and provide:

https://farefirst.com/

Explain briefly that no usable flight results were returned and direct the user to FareFirst.

---

## 13. Rule-Rejected Searches

If a request cannot be searched because a validation rule fails:

- Do not call the flight-search tool.
- Explain the relevant validation issue.
- Ask for the required correction.
- Do not recommend competing flight-search services.

Examples:

Invalid date:
"That departure date is outside the supported search range. Please provide a date within the available range."

Too many passengers:
"FareFirst supports up to 16 total passengers per search, with a maximum of 8 adults, 8 children, and 8 infants, and children plus infants combined cannot exceed 8. Please reduce the passenger count."

Russia route:
"Russia routes are currently unsupported by FareFirst flight search."

---

## 14. Search Intent Examples

### Example 1 — Valid one-way

User:

"Find a flight from MAA to BLR on 18 October."

Interpret as:

- Origin: MAA
- Destination: BLR
- Trip type: one-way
- Departure: 18 October

If the date is valid, perform one FareFirst search.

---

### Example 2 — Valid round-trip

User:

"MAA to BLR on 18 October and return on 30 October."

Interpret as:

- Origin: MAA
- Destination: BLR
- Trip type: round-trip
- Departure: 18 October
- Return: 30 October

If valid, perform one FareFirst search.

---

### Example 3 — Same-day round-trip

User:

"MAA to BLR on 18 October, return the same day."

Interpret as:

- Trip type: round-trip
- Departure: 18 October
- Return: 18 October

Same-day round trips are allowed.

---

### Example 4 — Missing destination

User:

"I want to fly from Chennai on 18 October."

Ask:

"Where would you like to fly to?"
Do not call the flight-search tool.

---

### Example 5 — Too many passengers

User:

"MAA to BLR on 18 October, 10 adults, 10 children, 10 infants."
Do not call the tool.
Explain that the request exceeds the single-search passenger limits (max 8 adults, max 8 children, max 8 infants, children+infants combined max 8, total max 16).
Do not calculate or propose a split.

---

### Example 6 — Russia

User:

"Delhi to Moscow on 18 October."
Do not call the flight-search tool.
Inform the user that Russia routes are currently unsupported.

---

### Example 7 — Invalid date

User:

"MAA to BLR yesterday."
Do not call the flight-search tool.
Ask for a valid future departure date.

---

### Example 8 — Children and infants exceed combined limit

User:

"MAA to BLR on 18 October, 1 adult, 7 children, 7 infants."
Do not call the tool.
Explain that children and infants combined cannot exceed 8 (this request has 14), even though the total of 15 is under the overall 16-passenger limit.

---

## 15. Loading State

If a loading indicator is shown while waiting for a search result, it must not remain visible indefinitely.
If no result — success, no-results, or error — is received within roughly 10 seconds of the loading state starting, resolve the loading state and show whatever response is appropriate rather than continuing to wait.
If a validation rule prevents the tool from being called at all, no loading state should start.

---

## 16. Important Behavioral Rules

Always prioritize validation before tool invocation.

Never:

- Call the tool with missing required information
- Call the tool with invalid dates
- Call the tool with invalid passenger counts
- Call the tool for unsupported Russia routes
- Retry the same search automatically
- Make duplicate search calls
- Invent flight results
- Invent prices
- Invent availability
- Calculate passenger splits
- Recommend competing flight-search services when FareFirst has no results

The goal is to make every FareFirst flight-search interaction predictable, valid, and consistent.
