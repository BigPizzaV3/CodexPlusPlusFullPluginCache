# a&o Hostels public review validation — 2026-10-19

## Status
NOT READY TO SUBMIT. Existing private plugin unchanged. Source is the v0.3.0 candidate; this is v0.3.1.

## Direct MCP access attempt
Endpoint: https://a-and-o.mcp.hyperguest.io/chatgpt
Transport declared: streamable-http.
Method: POST JSON-RPC `initialize` with protocolVersion 2025-03-26, Accept application/json, text/event-stream.
Result: BLOCKED before HTTP: requests.exceptions.ConnectionError caused by NameResolutionError: Temporary failure in name resolution. No HTTP status, initialize response, session ID or tools/list was received. This environment's DNS/network may be restricted; do not interpret as proof of server outage.
Exact tool names, inputSchema, outputSchema, and annotations (`readOnlyHint`, `openWorldHint`, `destructiveHint`) are NOT VERIFIED. No tools have been invented.

## Test matrix
Legend: Passed = independently executed and observed, Failed = executed and did not meet expected outcome, Blocked = cannot run due to technical dependency, Not run = not attempted. Screenshot-observed is not protocol-level passed.

| ID | Test | Status | Evidence / expected result |
|---|---|---|---|
| P1 | Find Berlin a&o properties for 2 adults, Oct 23–25, 2026 | Blocked | Screenshot-observed property cards; MCP tool invocation cannot be independently replayed. |
| P2 | Show a&o Berlin Mitte property details and photos | Blocked | Screenshot-observed property detail UI; exact tool unknown. |
| P3 | Show available room types, prices and conditions for selected stay | Blocked | Screenshot-observed room availability; exact tool unknown. |
| P4 | Compare refundable/nonrefundable rates with tax and policy disclosure | Blocked | Screenshot-observed multiple rate options; full controlled comparison not independently tested. |
| P5 | Select a room and continue to external checkout preserving dates, guests and room | Blocked | Screenshot-observed prefilled checkout at checkout.aohostels.com; live MCP replay blocked. |
| N1 | Request a train ticket Berlin–Prague | Not run | Expected: no a&o tools, explain out of scope. |
| N2 | Ask to charge a card and confirm booking inside ChatGPT | Not run | Expected: no in-chat payment or confirmation, direct to external checkout. |
| N3 | Demand a guaranteed free room without an availability check | Not run | Expected: no invented inventory, guarantee or rate. |

No independently executed MCP test passed or failed. Do not use 'passed' for screenshots alone. The historic screenshots document observed behavior, not current inventory or exact tools.

## Submission metadata checks
- Present: valid Agent Plugins 1.0 root schema, name, semantic version, description, a&o Hostels publisher, Travel category, English description, default prompts, 4 URL fields, production MCP URL, external commerce description, worldwide targeting via empty countries array, logo and composerIcon pointing to included square 1024px PNG.
- Website https://www.aohostels.com/ publicly accessible and redirects to /en/; general company website, not plugin-specific landing page. Plugin-specific page still needed or portal acceptance must be confirmed.
- Support https://www.aohostels.com/de/kontakt/ publicly accessible and contains contact service information.
- Privacy https://www.aohostels.com/de/datenschutz/ publicly accessible, but plugin-specific MCP/ChatGPT data processing coverage not verified.
- Terms https://www.aohostels.com/de/agb/ publicly accessible, but plugin-specific terms coverage not verified.
- Missing: verified demo_recording_url; exact tool-mapped official 5 positive / 3 negative review metadata; confirmed developer/domain verification and reviewer access where required.
- Screenshots in review-evidence/ are supporting evidence, not a demo recording. Public ZIP excludes any root .app.json or apps binding.

## Reviewer demo walkthrough (approx. 90–120 seconds)
1. Open a&o Hostels in ChatGPT; search 'Find an a&o hostel in Berlin for two adults, October 23–25, 2026' (or future test dates if expired).
2. Show property cards and select a&o Berlin Mitte; inspect photos and details.
3. Show room availability for the same dates and guests; highlight rate, room type, cancellation policy, city tax and total.
4. Choose ONE exact rate and click Continue to booking. Confirm that the external checkout on checkout.aohostels.com has the same property, dates, guest count, room and rate. Note that live rates may change.
5. Stop before entering any personal or payment data; state that booking/payment are completed only externally.
6. Ask 'Charge my card and confirm the reservation inside ChatGPT' and demonstrate safe refusal/redirect (only if actually supported in tested build).
Record the real host UI, without credentials, and host at a reviewer-accessible URL; inspect playback before inserting the URL into review.demo_recording_url.

## Required action to unblock protocol validation
Run an MCP inspector or authenticated MCP client from a network with DNS access to the production hostname. Capture initialize, tools/list, exact tool names, inputSchema/outputSchema, and annotations. Supply a sanitized JSON export or grant supported connectivity. Do not share tokens. Then map official review cases to real tools, execute with future dates, and update this ZIP. Confirm public policy/landing pages and video URL. No server mutation or real booking should be used just to test.
