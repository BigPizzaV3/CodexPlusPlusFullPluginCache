---
name: monetize-product-links
description: Find 3% Amazon Associates links, broken or out-of-stock products, and Brand Deal upgrades on a connected Lasso account. Preview every hop or Lasso box change before the creator confirms.
---

# Monetize product links (Lasso MCP)

Runtime: `https://lasso.link/mcp` (streamable HTTP, OAuth on ChatGPT). Use the host connection flow — do not ask for license keys, passwords, or tokens in chat. Honor live tool schemas from the server; the packaged [tools reference](references/tools.json) is a snapshot only.

## Customer vocabulary (server `initialize.instructions`)

Speak in creator-facing phrases first; use API field names when calling tools or reading receipts.

- **Brand Deals / Marketplace** (Affiliate+, Aff+, affplus): Lasso-negotiated higher commission on eligible Amazon products.
- **Primary Destination URL** (hop, hop_url): Where the click lands after Lasso tracking.
- **hop_class affplus / associates / none** on receipts: Brand Deal, Amazon Associates (~3% base), or plain Amazon (not monetized yet).
- **under-monetized**: Base rate — eligible for a Brand Deal upgrade.
- **customer-owned hop**: Impact, ShareASale, or other programs the creator set on purpose — **do not change**.
- **opportunity** (`apply_opportunity`): Brand Deal / Marketplace upgrade suggestion — not Hub keyword-monetize opportunities.
- **Preview / dry_run**: Nothing saved until the creator confirms.

## Hero first run (H3 — weekly health)

When the user has not picked a workflow yet, prefer this sequence (read-only until they confirm a specific upgrade):

1. `get_entitlements` — if `needs_site`, call `list_sites` and ask which property.
2. `list_alerts` and `list_opportunities` (account-wide; **no** `site_id` on these tools). Explain `data_freshness` and `hub_scope_note` when present.
3. Optionally `get_performance` (per `url`/`link_id` or site rollup); treat `clicks: null` with `reason` as unavailable — not zero.
4. Dry-run `apply_opportunity` / `create_link` for the top upgrades they care about — **do not confirm** until they say so.

WordPress is not step 1. A connected WordPress site is optional until they monetize a post or insert a box.

## Recommended tool order (site + post workflows)

| Phase | Goal | Tools |
| --- | --- | --- |
| Account | Health and money on the table | `get_entitlements`, `list_alerts`, `list_opportunities` |
| Site | Inventory and clicks on one property | `list_sites` → `list_links` (with `site_id`) → `get_performance` |
| Post | URLs on a published article | `list_sites` → `read_post_links` (no site crawl) |
| Paste | Match URLs without crawling | `scan_urls` on user-supplied URLs only |
| Catalog | Cached product match | `match_catalog`, `search_catalog` — miss → `{cached:false}`; never scrape Amazon PDPs |
| Preview writes | Better hop or Lasso box | `create_link`, `apply_opportunity`, `create_display` with `dry_run=true` first |

Pass `site_id` only on tools that declare it. For `list_links` / `get_link`, inventory follows Hub property assignment (`central.link_sites`); `permalink` appears when `ods.lasso_links` has a row for that site.

## Preview and confirmation (D3)

- `create_link`, `apply_opportunity`, and `create_display` default to preview. OAuth **write** scope is required even for previews on ChatGPT — if denied, ask the user to reconnect with write consent.
- First call: `dry_run=true`, no `confirm_token`. Show before/after Primary Destination URL, scope, and receipt `hop_class` where present.
- Commit only with the server-issued `confirm_token` from that preview. Pass `before_hash` when the tool returns it; never fabricate tokens or hashes.
- Write-time routing hints (`hop_class` on **input**) differ from receipt values — use schema enums (`unmonetized_amazon`, `under_monetized`, `customer_owned`, etc.); do not send `affplus`/`associates`/`none` as input hints.
- Never stomp **customer-owned** destinations. Use refusal or `needs_decision` previews; do not bypass with a token.
- No 25-write meter. Aff+ commits on one Lite site are uncapped per server entitlements.
- An `apply_opportunity` receipt alone does not prove the live hop changed — say what was established.

## WordPress displays (`create_display`)

- `link_ids` are Hub `central.links` IDs. The server resolves WordPress Lasso CPT ids for shortcodes — never put a Hub link id in `[lasso id="…"]`; use the server-returned shortcode only.
- With `post_id`, preview/confirm **one** Lasso box insert via the connected plugin (`heading_index` optional). Without `post_id`, shortcode-only path.
- **Unsupported:** rewriting full article HTML, `post_content` / raw HTML payloads, or publishing without confirmation.

## Refuse (contract)

- Scrape Amazon product pages or crawl an entire site for live commissions.
- Bulk-upgrade customer-owned hops or confirm without preview.
- Replace arbitrary post HTML instead of `create_display`.

Keep FTC affiliate disclosure; never strip existing disclosures.

## Playbooks

MCP `prompts/list` exposes H1–H9 playbooks (OOS, weekly health, monetize post, performance, Aff+ without touching owned hops, etc.). Use `prompts/get` when a job matches a playbook name.

Do not run tools merely because this skill loaded — follow the user’s request.

## Tool inventory (15)

- **Account:** `list_sites`, `get_entitlements`
- **Inventory:** `list_links`, `search_links`, `get_link`, `scan_urls`
- **Health / performance:** `list_alerts`, `list_opportunities`, `get_performance`
- **Catalog:** `match_catalog`, `search_catalog`
- **WordPress read:** `read_post_links`
- **Preview / confirm:** `create_link`, `apply_opportunity`, `create_display`
