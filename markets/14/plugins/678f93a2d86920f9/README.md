# GovBot Earthquakes & Landslides for OpenAI

Prepare a source-linked historical earthquake brief, explain a selected event’s ShakeMap/DYFI records, or summarize a bounded USGS landslide inventory. This independent package has three skills and one no-auth MCP connection at https://earthquakes-api.govbot.ai/mcp. The independent service is deployed; the ChatGPT directory plugin has not been submitted or published.

Five tools: search_earthquakes_near_point; summarize_earthquakes_for_area; get_earthquake_details; list_significant_earthquakes; search_landslides_near_point. Sources: USGS ComCat/FDSN, USGS U.S. Landslide Inventory version3 and Census TIGERweb state boundaries. No GovBot upstream dependency. All sources remain attributed, with dates, units and query limits.

The service provides historical records, not forecasts, warnings or property/building, geotechnical, legal or insurance determinations. Counts reflect catalog/inventory records, not all past events. Missing data is unknown. Coordinates are public research inputs only; the workflows do not request a home address or device location.

Local checks: npm test; npm run verify:sources; npm run package. Local tests, hosted anonymous SDK checks, actual private ChatGPT conversations and genuine video review have separate receipts. Visible answer checks do not establish hidden raw tool requests or results. The public product page and actual ChatGPT walkthrough are available below. Portal scans, owner attestations and final submission remain separate release steps. See docs/WORKING-CONTRACT.md and docs/AUDIT.md for the evidence and release gates.

Support: hello@govbot.ai. Not an official product of or endorsed by any government agency or OpenAI.

The canonical product page is https://govbot.ai/plugins/earthquakes-landslides.html. The genuine ChatGPT walkthrough is https://govbot.ai/plugins/earthquakes-landslides-demo.mp4 (3 minutes 8 seconds). The service homepage, privacy and terms are at earthquakes-api.govbot.ai. The public directory plugin has not been submitted or published.
