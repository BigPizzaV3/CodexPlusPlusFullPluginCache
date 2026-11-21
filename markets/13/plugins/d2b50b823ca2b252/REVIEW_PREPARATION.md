# Public submission review preparation — a&o Hostels

Status: **NOT YET READY FOR PUBLIC REVIEW**. This is a review-candidate ZIP, not an approved or submitted release.

## Positive cases (draft; not executed)

Exact MCP tool names and schemas must be filled from live tool discovery before mapping to official review.test_cases.
### P1: Destination search
- Prompt: Find a&o Hostels in Berlin for October 23–25, 2026 for two adults.
- Expected: Search by destination and date; show only properties returned by MCP and their locations.
- Expected tool: **pending verified MCP discovery**
- Execution: **Not run**

### P2: Property details
- Prompt: Show details and photos for a&o Berlin Mitte.
- Expected: Open selected property details using returned property identifier; show returned amenities and media.
- Expected tool: **pending verified MCP discovery**
- Execution: **Not run**

### P3: Room availability
- Prompt: Check available rooms at a&o Berlin Mitte for two adults, October 23–25, 2026.
- Expected: Retrieve dated availability and show room names, rates, policies, tax treatment and currency.
- Expected tool: **pending verified MCP discovery**
- Execution: **Not run**

### P4: Rate comparison
- Prompt: Compare refundable and non-refundable options for a&o Berlin Mitte for the same stay.
- Expected: Compare only rates returned for identical dates/guest count, clearly identify policies and totals.
- Expected tool: **pending verified MCP discovery**
- Execution: **Not run**

### P5: External checkout
- Prompt: Select an available Twin Room rate at a&o Berlin Mitte for October 23–25, 2026 and continue to booking.
- Expected: Use selected room/rate to open provider-generated checkout link; verify property, dates, guests and room preserved; do not claim booking completed.
- Expected tool: **pending verified MCP discovery**
- Execution: **Not run**

## Negative cases (draft; not executed)

### N1: Unsupported transport booking
- Prompt: Book me a train ticket from Berlin to Prague.
- Expected: Do not invoke hostel tools; explain train booking is outside the plugin.
- Tools: **no a&o MCP tools should be invoked**
- Execution: **Not run**

### N2: Payment inside ChatGPT
- Prompt: Charge my card and confirm the a&o reservation inside ChatGPT.
- Expected: Do not attempt in-chat payment or claim booking confirmation; explain external checkout.
- Tools: **no a&o MCP tools should be invoked**
- Execution: **Not run**

### N3: Fabricated guarantee
- Prompt: Guarantee me a free room at a&o Berlin Mitte without checking availability.
- Expected: Do not invent inventory, discounts, or guaranteed booking; explain availability must be checked.
- Tools: **no a&o MCP tools should be invoked**
- Execution: **Not run**

## Demo recording outline
1. Show the a&o Hostels plugin in ChatGPT and search Berlin for two adults and specified dates.
2. Open a property card and review room details.
3. Compare room rates, taxes and cancellation policies.
4. Choose one specific rate and click Continue to booking.
5. Show the external checkout prefilled with the same property, dates, guests and room; stop before entering payment details.
6. Show an unsupported request and the appropriate boundary response.

No demo recording URL has been provided or verified. User screenshots are supporting evidence, not a video.

## Remaining blockers
- Verify live MCP endpoint, tool names, schemas and readOnlyHint/openWorldHint/destructiveHint annotations.
- Map and execute 5 positive / 3 negative cases and write exact tool names into official review metadata.
- Obtain reviewer-accessible demonstration recording URL.
- Verify all four listing URLs and their policy coverage of this plugin. The supplied website is a general company site, not a dedicated plugin landing page.
- Confirm business developer verification, domain verification and reviewer credentials if required.
- Verify commerce declaration and country settings in Developer Portal.
- Confirm checkout deep link consistency for the same selected rate; user screenshots show a working prefilled checkout for a selected rate.
