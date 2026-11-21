# Jetopia MCP Review Test Cases

Run these tests in ChatGPT with the Jetopia MCP plugin connected. The first five are positive tests; the final three are out-of-scope request rejection tests. Use the outputs from Positive 1 and 2 in the following steps. No expected price is hard-coded: quote amounts must come from Jetopia’s pricing tool.

> **Live booking note:** Positive 4 creates a real booking request when run against the production MCP server and may notify Jetopia staff by SMS. Use clearly marked test contact details, do not pay the deposit, and cancel/label the request as a test afterward.

## Positive tests

### Positive 1 — Vehicle recommendation
- **Input:** “We are 4 people with 2 large suitcases, arriving at Jeju Airport on November 20, 2026. Which vehicle do you recommend?”
- **Tool:** `recommend_vehicle`
- **Expected result:** The tool receives `language: en`, `people: 4`, and `largeLuggage: 2`. It returns the vehicles allowed by the current Jetopia configuration; Staria should be available as a candidate under the checked pricing rules. The assistant shows only returned options and does not claim airport/date changes the vehicle capacity.

### Positive 2 — Exact full-day quote, no Udo
- **Input:** “Please give me an exact quote for a full-day tour on November 20, 2026, for 4 people in a Staria, picked up at Jeju Airport. We will not visit Udo.”
- **Tool:** `get_quote`
- **Expected result:** The tool receives `language: en`, `date: 2026-11-20`, `duration: full_day`, `people: 4`, `udo: false`, `pickup: Jeju Airport`, and the exact Staria `vehicleId` returned by Positive 1 (expected format: `staria|4|2`). The assistant reports only the total, deposit, and balance returned by the tool. It does not estimate or calculate an amount itself.

### Positive 3 — Nature-focused tour options
- **Input:** “What Jeju tour would you recommend for nature lovers? I’d like to see scenic places.”
- **Tool:** `list_tours`
- **Expected result:** The tool receives `language: en` and `interest: nature`. It returns the existing `tour` entry, “Jeju private driver tour,” with `nature` in `interestTags` and an English summary. The assistant explains that the itinerary can be tailored to the guest’s interests and does not invent specific attractions or claim a named nature package.

### Positive 4 — Booking request after explicit consent
- **Input:** “I want to submit the quote from Positive 2. My name is TEST. My phone is [test phone number], and my WhatsApp ID is [test WhatsApp ID]. I am staying at [test lodging]. I have read and agree to Jetopia’s privacy notice and booking terms. Please submit the request.”
- **Tool:** `create_booking_request` — only after the assistant has confirmed the test phone, WhatsApp ID, lodging, and explicit privacy/terms consent.
- **Expected result:** The tool receives the exact `quoteId` from Positive 2, `name: TEST`, the supplied test phone, `messenger: {type: whatsapp, id: [test WhatsApp ID]}`, and `lodging: [test lodging]` after the assistant confirms it. It returns a request number and deposit link. The assistant states that Jetopia staff confirm availability and the booking after reviewing the request and deposit; it does not claim instant confirmation. Do not open a payment flow or pay.

### Positive 5 — Booking status lookup
- **Input:** “Please check booking request [request number from Positive 4]. The phone number on the request is [same test phone number].”
- **Tool:** `get_booking_status`
- **Expected result:** The tool receives the request number and the same phone used in Positive 4. It reports the status returned by Jetopia, or the safe not-found response if the pair does not match. It does not expose another guest’s booking.

## Rejection tests

### Rejection 1 — Self-drive rental car
- **Input:** “Can you rent me a car in Jeju that I can drive myself?”
- **Tool:** No Jetopia tool.
- **Expected result:** The assistant explains that this plugin handles chauffeur-driven private tours and transfers, not self-drive rental cars. It does not submit a rental request or imply that a vehicle has been reserved.

### Rejection 2 — Busan tour
- **Input:** “Plan and book a private driver tour in Busan.”
- **Tool:** No Jetopia tool.
- **Expected result:** The assistant explains that this plugin supports Jeju services, not tours in Busan. It does not call a Jeju tool or claim a Busan itinerary or booking is available.

### Rejection 3 — Airline ticket booking
- **Input:** “Book me a flight ticket from Seoul to Jeju for November 20.”
- **Tool:** No Jetopia tool.
- **Expected result:** The assistant explains that this plugin cannot book airline tickets and directs the guest to an airline or ticketing provider. It does not claim a ticket was searched, priced, or booked.
