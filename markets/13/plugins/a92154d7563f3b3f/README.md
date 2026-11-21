# HotelUse consumer connector

Streamable HTTP: https://www.hoteluse.dev/mcp/search — no authentication.

Three tools: `search_hotels` (destination and explicit stay dates, hotel summaries and provider minima only), `get_room_rates` (HotelUse ID or unique hotel name plus explicit dates, separate grouped Room options view), and `get_hotel` (undated traveler-facing hotel facts). Search and rooms have an MCP Apps comparison UI. Provider price clicks go directly to booking platforms; ask a follow-up question to compare a particular hotel’s room options. Hotel information is text and structured facts, without live prices or a price widget. No HotelUse API key, account, prepaid balance or per-user credit allowance is required. Provider links preserve affiliate tracking; the connector does not reserve or pay for rooms.

The standard MCP Apps bridge is used for tool calls and external links, with optional ChatGPT compatibility APIs. Clients without UI support can use structured results and booking URLs. Resource URI: `ui://hoteluse/hotel-comparison/v16.html`.

Developer API access remains separate at `/mcp` and `/v1/*`, with bearer keys and usage billing. The public connector does not expose raw static records or ID batch tools. Service capacity, concurrency and upstream protections apply independently of account quotas.

This package is prepared for installation and platform review. A running endpoint is not a directory listing; ChatGPT/Claude publication and in-host acceptance must be verified separately.

The comparison UI uses four compact Expedia / Booking / Agoda / Brek rows for hotels and server-grouped rooms, sorted by comparable stay total from lowest to highest; unavailable quotes appear last. Comparable prices include confirmed mandatory fees. Click a price to open its provider booking link; no booking is made by this connector.

Stay dates use the destination or hotel local calendar, including same-day check-in. For tonight, pass `date_intent: "tonight"` instead of `check_in` / `check_out`; the server resolves one local night and returns explicit dates plus `date_context`. Keep the returned dates for room follow-ups. Never calculate tonight using UTC.

Claude can pass optional `user_locale` and `user_location_country` from its traveler context when host metadata is absent. For room follow-ups, pass the exact `hotel_id` and `search_quote_session_id`; omitted dates, rooms, preferences, provider selection and rate filters inherit from that search. Explicit arguments can change a new quote, except its device remains consistent. Use `rate_filters: {}` to clear inherited rate constraints. A complete hotel name also works without a destination if the catalog match is unique and confident.
