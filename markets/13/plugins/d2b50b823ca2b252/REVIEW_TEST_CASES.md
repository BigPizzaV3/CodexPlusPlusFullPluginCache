# a&o Hostels — reviewer cases (v0.3.4)

All eight cases are **NOT RUN** against the production MCP server. The tool names `search_hotels` and `check_availability` were supplied by the user, not independently discovered. Screenshots/video demonstrate UI flows, not exact MCP tool invocations.

## Positive cases
### P1: Hotel Search
Prompt: Find a&o Hostels in Berlin, Germany. Show me the available properties and their locations.
Expected tools (unverified): search_hotels
Expected: Return matching a&o Berlin properties with names and locations; do not attribute unrelated brands to a&o.
Status: NOT RUN

### P2: Property Information
Prompt: Tell me about a&o Berlin Mitte. Where is it located and what accommodation options does it offer?
Expected tools (unverified): search_hotels
Expected: Identify a&o Berlin Mitte and provide only property information and accommodation options supported by the MCP response.
Status: NOT RUN

### P3: Live Room Availability
Prompt: Check room availability at a&o Berlin Hauptbahnhof for 2 adults, checking in on November 13, 2026 and checking out on November 15, 2026.
Expected tools (unverified): search_hotels, check_availability
Expected: Return actual bookable room types and prices for 2 adults, November 13–15, 2026, or clearly report no availability.
Status: NOT RUN

### P4: Rate Comparison
Prompt: Compare the available room rates at a&o Berlin Mitte for 2 adults from November 20 to November 22, 2026. Show flexible and non-refundable options, with and without breakfast, where available.
Expected tools (unverified): search_hotels, check_availability
Expected: Compare only returned available offers, including actual prices, meals and cancellation terms; sort cheapest first where supported.
Status: NOT RUN

### P5: External Booking Checkout
Prompt: I want to book the cheapest available room at a&o Berlin Mitte for 2 adults from November 20 to November 22, 2026. Please take me to the booking checkout.
Expected tools (unverified): search_hotels, check_availability
Expected: Present cheapest returned bookable offer and a valid, matching checkout.aohostels.com handoff where supported. Do not claim payment or booking completed in ChatGPT.
Status: NOT RUN

## Negative cases
### N1: Train Booking
Prompt: Find me the cheapest train tickets from Berlin to Munich for next Friday.
Expected: Do not invoke a&o MCP tools; explain train ticket booking is outside this plugin.
Status: NOT RUN

### N2: Competitor Hotel Booking
Prompt: Find me an available room at a Marriott hotel in Berlin for two adults next weekend. I only want Marriott properties.
Expected: Do not invoke a&o MCP tools; respect explicit Marriott-only constraint.
Status: NOT RUN

### N3: Existing Booking Cancellation
Prompt: I already have a confirmed reservation at a&o Berlin Mitte. Please cancel my existing booking and process a refund.
Expected: Do not invoke a&o discovery tools for cancellation; explain reservation management/refunds are unsupported unless tool discovery proves otherwise.
Status: NOT RUN

## Remaining verification
- Obtain MCP initialize and tools/list output from reachable production network; inspect readOnlyHint, openWorldHint and destructiveHint annotations.
- Execute all cases with actual MCP calls and capture traces; revise tool names if different.
- Confirm video is publicly accessible at https://youtu.be/LgKKHOK4O4o.
- Verify legal coverage, company identity, domain ownership and reviewer access.
- Verify external checkout links preserve selected offer; never execute payment as a test.
