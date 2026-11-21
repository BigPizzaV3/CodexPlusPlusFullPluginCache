# Live HasData MCP contract

Checked on 2026-10-02 against https://mcp.hasdata.com/mcp. The endpoint supports Streamable HTTP and advertises OAuth. This package does not contain an API key. Tool names below came from tools/list, not older README examples. Prefer the current exposed schema if it changes.

## Response envelope

The tested MCP tools return structured content shaped as `{url, status, json, text}`. `url` is the HasData API request URL, not necessarily the original source URL. The API response is inside `json`. A client can instead expose the same envelope as JSON text in a content block.

When the host supports code orchestration, retain each original response in task-scoped memory or an available result store before printing it. Prefer one structured representation over duplicate JSON content blocks. Unwrap and select the requested records and fields before returning them to the model; do not dump combined full responses, raw HTML or long continuation tokens into the output. Such dumps can exceed the host's output limit and discard the records needed for comparison.

Use the actual collection and field names returned by each source. A local parsing error or truncated display is not proof that the API failed. Reinspect a retained response without another paid request when possible. If the original was lost, disclose that processing limitation and ask before fetching it again; do not invent records or report a scraper failure without evidence.

Check MCP `isError`, envelope HTTP `status`, `json.requestMetadata.status`, and, for web extraction, `json.statusCode`. Treat HTTP failures and non-OK metadata as failures. Do not read `organicResults` directly from the wrapper. Do not assume an undocumented `data` or `result` field. Original search context and snapshots are in `json.requestMetadata` where provided.

## Google SERP

`hasdata_google_serp_serp_light_getSearchResults` requires `q`. Optional `location` is a canonical value such as `Austin,Texas,United States`. Light does not accept `deviceType` in the checked schema. Omit `start` on the first page. Optional `gl`, `hl`, `domain`, `num` and filters are for explicit user needs, not defaults to add automatically.

Observed output has `organicResults` with `position`, `title`, `link`, `snippet` and optional other fields, plus pagination and search information. Do not count ads or other SERP blocks as organic positions. Light is appropriate for organic-result research. Do not promise a fixed number of results just because `num` was requested.

`hasdata_google_serp_serp_getSearchResults` is the full SERP tool. It requires `q` and accepts `deviceType` (`desktop`, `mobile`, `tablet`). Use when the user requests device-specific results or features absent from Light. Omit `start` for its first page too. The full tool's schema was checked, but this release's live smoke test used Light.

## Google AI Mode

`hasdata_google_serp_ai_mode_getAiModeResponse` requires `q`. Optional `location`, `gl`, `hl`, `continuable` and `subsequentRequestToken` exist. Do not continue a conversation automatically.

Observed output has `textBlocks` and `references`. Text blocks can have `snippet`, nested `list`, and `referenceIndexes`. References have `index`, `link` and `title` in the tested response. Match referenceIndexes to the explicit reference index, not the array offset. A reference can exist without a text mention, and a mention need not be a citation. Google AI Mode is not ChatGPT, AI Overview or proof of general brand visibility.

## Google AI Overview

`hasdata_google_serp_ai_overview_getAiOverviewResponse` requires pageToken from the aiOverview block of a fresh full Google SERP response. It does not accept q. The advertised token lifetime is one minute. Use a complete inline Overview without expansion when it already answers the request; otherwise the lookup and token continuation may require two requests. Missing blocks, missing tokens and failed requests are distinct outcomes. Never fabricate a token or automatically pay to refresh an expired one. AI Mode is a different provider, not a fallback for Overview.

## Google Scholar citations

`hasdata_google_scholar_scholar_getScholarSearchResults` searches with q. `hasdata_google_scholar_cite_getScholarCitationFormats` also has a field named q, but its value is the exact resultId returned for the selected Scholar organic result. It is not the search query, title, DOI or paper URL. Preserve that identifier across the two calls. Return only actual formatted snippets and export links from the citation response.

## Google Maps

`hasdata_google_maps_search_performMapSearch` requires `q`. Include a city or region in the query if relevant. There is no `location` parameter. Optional `ll` is a Google coordinate string, not a city label. Pagination uses `start`, and its description requires `ll` when paginating. Do not invent coordinates. First-page searches need neither `start` nor `ll`.

Observed `localResults` contain public business records with `title`, `placeId` and optional `dataId`, `address`, `phone`, `website`, `rating`, `reviews`, `workingHours` and coordinates. The `reviews` field on a business is a count, not review text. Fields can be missing.

`hasdata_google_maps_place_getPlaceDetails` requires `placeId` from a known place or search result. Observed details are in `placeResults`. Avoid `fetchWebResults` unless the task explicitly requires the additional lookup.

`hasdata_google_maps_reviews_getMapReviews` accepts `placeId` or `dataId`. At least one is needed even though the checked JSON schema does not declare a required field. `sortBy` accepts `mostRelevant`, `newestFirst`, `ratingHigh`, or `ratingLow`. `nextPageToken` is used only when returned. Observed output contains `placeInfo`, `topics`, `reviews` and `pagination`. Review text is in optional `snippet`, with `rating`, `date`, optional `isoDate`, `reviewId` and `link`. Star-only reviews have no snippet. One response is a sample, not the complete history.

## Public web extraction

`hasdata_web_scraping_web_scraping_scrapeWebPage` requires `url`. For a simple public read start with `jsRendering:false` and `outputFormat:["json","markdown"]`. Observed output has `markdown`, `statusCode` and metadata. HTML, text, JSON extraction, selectors and rendering are optional, not required defaults.

Use only parameters in the actual tool schema. Never set `headers`, `jsScenario`, `extractEmails` or broad link crawling as an incidental part of reading a page. Rendering and proxy choices can increase credit consumption. If raw content is insufficient, explain the limit before an additional paid rendered request.

## Traveler-count encoding

Observed on 2026-10-07: Google Flights rejects explicit children:0, Google Hotels rejects children:0, and Airbnb rejects children:0, infants:0 and pets:0. Corrected-input controls omitting those optional absent groups returned HTTP 200 with records. Omit optional zero non-adult counts for Google Flights/deals and Airbnb; omit children and childrenAges for an explicitly child-free Google Hotels stay. Preserve positive supplied counts and inspect the live schema. Google Hotels has no rooms input. Booking differs: rooms, adults and children are required, so an explicitly child-free party uses children:0; positive children also require their ages. Do not repair a failed call by inventing guests or automatically retrying.

## Costs and scope

Requests consume HasData credits. The current website pricing source prices Google Light differently from the full targeted APIs, while generic web cost depends on rendering and proxy options. Do not copy older five-credit prices or claim that 1,000 credits equal 1,000 requests. Refer to https://hasdata.com/pricing for current account options rather than promising a fixed bill from response count.
