# Dealfinderr plugin

This package connects ChatGPT to Dealfinderr's hosted `/mcp` endpoint. The
server implementation and OAuth account-linking flow live in the parent
Dealfinderr web application. It supports R2SA for rental listings and BTL,
HMO, Refurb, BRRR BTL, BRRR SA, BRRR HMO, and flip for eligible sale listings from
supported Rightmove URLs. The resolver also recognizes OpenRent URLs, but the
production server currently receives a CAPTCHA response from OpenRent, so
the public listing does not promise that source.

The `research_market` MCP tool also runs the site's Market Research for a UK
full postcode or postcode district. Rent to SA (`r2sa`) returns low, expected,
and high nightly accommodation rates, annual occupancy, projected revenue,
and the separate local monthly landlord rent. The tool also supports buy to
let (`btl`, with property type and 1–5 bedrooms) and HMO (`hmo`) rent
estimates. Cached research uses no new AI credit; a fresh estimate may use one.

The read-only `search_deals` tool queries the indexed Below Last Sold and
Refurb Potential feeds. It supports the site's location, postcode, map,
price, bedroom, property type, SSTC, and sort filters, plus limit/offset
paging and a marker view. Results can be passed to `inspect_listing` and
`analyze_deal` for underwriting.

Users can also paste a supported listing URL and run Deal AI without searching.
`get_deal_result` retrieves a completed cached analysis without another AI
credit. Completed calculator results are automatically saved in `ChatGPT`
(or their existing group). Completed Refurb exits update the same saved purchase case,
including background completions. Return `fullAnalysisUrl` unchanged; saved
links use `/deal-ai?saved=...`. `save_deal` stores the result in a named group,
creating the group if needed; it reads the server-stored figures rather than accepting
figures from the model. `list_deal_groups`, `list_saved_deals`, and
`get_saved_deal` let users find and reopen their own saved work.

For the two-step Refurb workflow, `analyze_deal` with `strategy: refurb`
establishes the purchase case. `analyze_refurb_exit` then evaluates BTL,
HMO, serviced accommodation, or flip using that saved case. Rental exits can
return a run ID; `get_refurb_exit_result` reads the original result without
another analysis or AI credit. Flip is calculated without a fresh AI credit.
The saved result can include a completed Refurb exit and its locked purchase
case.

Connecting and using the plugin requires a current Dealfinderr plan or trial,
lifetime access, or a super-user account. Access is checked again when tokens
are used, so expired or canceled access stops working.

The web application and OAuth flow are deployed at `https://dealfinderr.com`.
The remote MCP server has been connected and tested in ChatGPT developer
mode. Before public submission, verify the publisher identity and domain,
test the review cases with a dedicated account, provide a reviewer-accessible
demo recording, and resolve any dashboard findings. Reviewer credentials
belong in the secure submission form, never in this package.

See [the implementation guide](../../docs/chatgpt-deal-ai-plugin.md) for the
tool contract, launch checks, and remaining live validation.
