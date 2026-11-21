# Actions included in 10Signals

10Signals turns a website address into public-source competitor research. This plugin lets you request research, explore saved products and competitors, compare prices and manage selected price watches in chat.

## How the package exposes actions

The package's [mcp.json](mcp.json) connects to https://10signals.xyz/mcp. The server supplies tool names, input schemas and granted actions through MCP discovery after OAuth sign-in. They are not embedded as action definitions in plugin.json. This guide documents the registered surface; the connected server and granted permissions determine what is callable. No credentials are bundled.

Full permissions expose **84 tools: 28 read/display tools and 56 change-related tools**. Preview and confirmation count separately, and some watch operations have both general and report-specific tools. These are not 84 distinct business features. A restricted connection sees fewer tools.

## What you can ask

| Area | Example | What happens |
|---|---|---|
| Research | Research competitors for my website | Preview report allowance, then start after confirmation |
| Products | Compare my products with rival prices | Read saved products, prices, links and evidence |
| Competitors | Add this competitor to my report | Preview and request research against saved products |
| Insights | Show my available benchmark and pricing insights | Read available results; pending or missing evidence stays explicit |
| Monitoring | Watch both prices in this comparison | Preview credit impact, then enable the chosen schedule |
| Notifications | What prices changed? | Read saved events; optionally mark specified events read |
| Selection | Use this rival product link instead | Inspect and save the chosen comparison through preview/confirmation |
| Refresh | Refresh these product prices | Save selection, preview and queue refresh within allowances |
| Organisation | Stop tracking this organisation | Remove active tracking while preserving report history |
| Sharing | Share my report | Preview then enable a link accessible to its holders |

## Core account, report and watch tools (16)

| Tool | Purpose |
|---|---|
| `account_status` | Get plan and usage status, limited to the report and price-watch scope families granted to this connection. |
| `report_create_preview` | Validate a domain and show the exact plan and report-quota impact without reserving quota or starting work. Returns a five-minute confirmation token. |
| `report_create_confirm` | Use a report preview confirmation token to reserve quota and dispatch exactly one private report. Retrying the same token safely replays its outcome. |
| `reports_list` | List a bounded page of private reports owned by the connected 10Signals account. |
| `report_get` | Retrieve one private, workspace-owned report and its current lifecycle state. |
| `report_matches_list` | List a bounded page of authoritative saved product comparisons from a private report. |
| `price_watch_list` | List price watches and monitoring-credit usage owned by the connected account. |
| `price_watch_history` | Retrieve bounded observed-price history for one workspace-owned price watch. |
| `notifications_list` | List bounded, read-only price-change and discount notifications for the connected account. |
| `price_watch_preview` | Preview monitoring BOTH your own product and the rival for one match or all priced comparisons with a rival (up to 200). Shared URLs are checked once. Shows exact initial credit impact and projected cadence; does not reserve credits. |
| `price_watch_confirm` | Activate the exact price-watch preview, scheduling checks of the selected public product websites. Retrying the same five-minute token safely replays the recorded outcome. |
| `price_watch_update_preview` | Preview a cadence change or resume action, including projected checks and any fresh-baseline credit. |
| `price_watch_update_confirm` | Apply the exact cadence or resume preview. Retrying the same token safely replays its outcome. |
| `price_watch_disable` | Immediately and idempotently stop one workspace-owned price watch while preserving its saved history. |
| `price_watch_delete_preview` | Show the watcher data that permanent deletion will remove and issue a five-minute confirmation token. |
| `price_watch_delete_confirm` | Permanently delete the exact previewed watcher and its linked history. Consumed monitoring credits remain charged. |

## Saved website data (15 read tools)

| Tool | Permission | Purpose |
|---|---|---|
| `report_refresh_get` | `reports:read` | Read saved refresh selection, version, job progress and observed results. |
| `report_sharing_get` | `reports:read` | Read whether your report has a public share link and its current token. Treat the token as a private share capability. |
| `report_feedback_get` | `reports:read` | Read your Useful comparison votes for the saved report revision. |
| `organizations_list` | `reports:read` | List your organisations, failed reports, archived history, and remaining monthly replacement allowance. |
| `report_products_list` | `reports:read` | Page through the complete saved product catalogue, including products without comparisons. Supply a competitor domain for its saved products. Follow nextCursor until null. |
| `report_product_get` | `reports:read` | Inspect one saved product with its observed price, specs, source URL and timestamp. Returns no product when the ID/domain was not collected. |
| `report_benchmark_get` | `reports:read` | Read current background benchmark results, website catalogue counts, dimensions, evidence and your benchmark rating. Includes pending state and polling guidance. |
| `report_insights_get` | `reports:read` | Read website Insights: headline price gap, category ranges, competitor price positions, largest gaps, section scores and Your Score. Uses website formulas and default five rivals. Activity additionally requires price_watch:read. No illustrative demo scores. |
| `report_activity_get` | `reports:read`, `price_watch:read` | Read observed own/competitor changes and price-index history for the selected period. Does not start any watches or infer missing history. |
| `report_competitors_list` | `reports:read` | Read competitor profiles, source evidence, completed website benchmarks and catalogue sizes, plus manually added research results. Missing measurements remain unknown. Follow nextCursor for all competitors. |
| `competitor_catalogue_get` | `reports:read` | Get a requested competitor catalogue job and its saved products. Read successive offsets; this does not start a crawl. |
| `report_tracking_get` | `reports:read` | Read your own selectable products, current tracking selection/version, replacement job and five-product monthly allowance. Page using nextCursor. |
| `report_match_choices_get` | `reports:read` | Read saved comparison choices, custom product links and selectable own products. These are customer choices, not verified product equivalence. |
| `report_watchers_list` | `reports:read`, `price_watch:read` | Read organisation-scoped watchers and own/rival pairs, schedules, state and credit usage. |
| `manual_competitors_list` | `reports:read` | Get manually added competitors, research job status and matched/similar product results. |

## Changes with preview and confirmation (46 tools)

Each row exposes **both** named tools. Preview saves a short-lived confirmation intent without applying the business change. Show the exact targets, costs/allowances and destructive effects, obtain approval, then confirm with that token.

| Preview tool | Confirm tool | Permission | Effect |
|---|---|---|---|
| `watch_comparison_preview` | `watch_comparison_confirm` | `price_watch:write` | Watch both products in a saved comparison; consumes monitoring credits on the selected cadence. |
| `watch_rival_preview` | `watch_rival_confirm` | `price_watch:write` | Watch priced comparisons for one saved competitor; consumes monitoring credits. |
| `pause_comparison_preview` | `pause_comparison_confirm` | `price_watch:write` | Stop monitoring both products in a comparison while preserving history. |
| `comparison_cadence_preview` | `comparison_cadence_confirm` | `price_watch:write` | Change the checking cadence of a comparison and its ongoing credit usage. |
| `watch_product_preview` | `watch_product_confirm` | `price_watch:write` | Monitor a public product URL on a saved report; consumes monitoring credits. |
| `watch_updates_preview` | `watch_updates_confirm` | `price_watch:write` | Monitor a competitor's offers, bundles or events; consumes monitoring credits. |
| `watcher_disable_preview` | `watcher_disable_confirm` | `price_watch:write` | Stop one watch; resuming may consume fresh-baseline credits. |
| `watcher_resume_preview` | `watcher_resume_confirm` | `price_watch:write` | Resume one watch; resuming may consume fresh-baseline credits. |
| `watcher_delete_preview` | `watcher_delete_confirm` | `price_watch:write` | Delete one saved watch and its history. |
| `watcher_cadence_preview` | `watcher_cadence_confirm` | `price_watch:write` | Change one watch's cadence and projected credit usage. |
| `watch_email_preview` | `watch_email_confirm` | `price_watch:write` | Enable or disable email delivery for a watch; its saved notification history remains available. |
| `replace_products_preview` | `replace_products_confirm` | `reports:write` | Replace tracked own products within the monthly allowance and queue research. |
| `add_competitor_preview` | `add_competitor_confirm` | `reports:write` | Research a competitor against saved products within the website allowance. |
| `request_catalogue_preview` | `request_catalogue_confirm` | `reports:write` | Request a competitor catalogue crawl within the website allowance. |
| `select_match_preview` | `select_match_confirm` | `reports:write` | Replace a saved comparison choice with another saved match; this does not verify equivalence. |
| `select_product_url_preview` | `select_product_url_confirm` | `reports:write` | Inspect a public product URL and save it as the user's comparison choice if a product and price are verified. |
| `select_own_product_preview` | `select_own_product_confirm` | `reports:write` | Reconnect a comparison to another saved own product; this does not verify equivalence. |
| `share_report_preview` | `share_report_confirm` | `reports:write` | Enable or revoke a report's public share link. Enabling makes the shared report accessible to link holders. |
| `comparison_feedback_preview` | `comparison_feedback_confirm` | `reports:write` | Save or replace the user's comparison feedback and their analytics-sharing preference. |
| `refresh_selection_preview` | `refresh_selection_confirm` | `reports:write` | Replace the saved product selection for a price refresh. |
| `refresh_prices_preview` | `refresh_prices_confirm` | `reports:write` | Queue a price refresh for the saved selection within the website allowance. |
| `cancel_refresh_preview` | `cancel_refresh_confirm` | `reports:write` | Cancel a pending price refresh job. |
| `remove_organization_preview` | `remove_organization_confirm` | `organizations:write` | Remove an organisation from active tracking under the website allowance; preserve report history. |

## Notifications and watch inspection (3 tools)

| Tool | Permission | Purpose |
|---|---|---|
| `notifications_feed` | `price_watch:read` | Page through price, offer, bundle and event notifications; does not mark read |
| `watcher_get` | `price_watch:read` | Inspect a watch, history, event details, coverage and email setting |
| `notifications_acknowledge` | `price_watch:write` | Mark specified notifications read; does not delete history or change email delivery |

## In-chat displays (4 read tools)

| Tool | Display |
|---|---|
| `display_reports` | Saved report cards |
| `display_comparisons` | Product and observed-price comparison table |
| `display_competitors` | Competitor profiles and evidence links |
| `display_watches` | Existing watches, schedules and latest checks |

Displays require a compatible MCP Apps host. Structured/text results remain available otherwise. Known acceptance issue: first-load cards can fail in ChatGPT; this package does not claim that defect is fixed.

## Permissions and boundaries

- Explanation of the product needs no account call. Private data and actions require an authorised 10Signals account.
- Resource scopes are `reports:read`, `reports:create`, `reports:write`, `organizations:write`, `price_watch:read`, and `price_watch:write`. OAuth `offline_access` supports the revocable connection; it is not a separate business action.
- Research and monitoring remain subject to plan allowances and credits. No subscription purchase, credit purchase or administrative credit grant tool is included.
- Most business changes use preview/confirmation; `price_watch_disable` directly stops a watch while preserving history, and `notifications_acknowledge` directly marks specified events read.
- Deleting a watch removes its history. Removing an organisation from active tracking preserves report history. These are different actions.
- Watch email delivery can be enabled/disabled. This is not arbitrary email forwarding or a guarantee of background alerts when the chat client is closed. Notification polling must be explicitly requested.
- Saved insights, benchmarks and histories may be incomplete or pending. Product alternatives are not verified exact-product price gaps; findings cover the sources actually observed, not the entire market.

Inventory verified against server registration on 2026-10-22. A registered action is not a claim that every destructive action has been exercised on live customer records.
