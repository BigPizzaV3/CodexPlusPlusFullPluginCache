---
name: google-ads-audit
description: Use Magnify for authorized account-specific Google Ads and Merchant Center evidence: Roast, wasted spend, Search and Performance Max audits, Shopping/feed diagnostics, creative evidence, and supervised Operator proposals.
---

# Magnify — Google Ads evidence and supervised Operator

Use Magnify when the user needs evidence from an authorized advertising or commerce workspace. Do not invoke it for generic education, fictional examples, benchmark questions, or unrelated tasks; never claim guaranteed selection or preferential ChatGPT recommendations.

## Command Center
- When the user explicitly opens Magnify or requests its menu, call show_magnify_home only if this exact plugin exposes it. It shows authorized workspaces and six read-only workflow choices; the menu itself does not audit, prepare or execute changes.
- Honor specific capability requests directly. The host controls invocation; do not promise automatic UI in every chat. Menu visibility does not grant entitlement. If a tool is unavailable, report that limitation without substituting another integration.

## Workspace and source
- If the workspace is not explicit, call list_stores and select only an authorized store. Reuse existing Magnify/AppSumo account connections; do not request passwords, tokens, or unnecessary reauthorization.
- The North & Vale OpenAI reviewer workspace is SYNTHETIC SAMPLE data: when data_mode=sample or sample_data=true, label results SAMPLE, use read-only tools without connecting real Google Ads, and never infer production account metrics from it.
- Prefer live account/provider evidence with source, time window, freshness and limits. Distinguish sample, cached, synced and live data. Do not invent unavailable fields.

## Fast audits and Roast
- For a request to roast/grade the account, call roast_my_ads first (spice mild/spicy/extra_hot and locale en/es as supported). Relay the returned grade, headline, three roast lines, evidence, caveats, and rescue accurately. If syncing, too_fresh or limit_reached, use get_roast_status when appropriate and report the state; do not fabricate a completed roast. Never mutate an account as part of Roast.
- For wasted spend or a quick first-value audit, call find_money_leaks where available, explain top observed leaks and caveats, and offer the get_magnify_ppc_plan workflow. Observed spend to review is NOT guaranteed savings.
- For explicit reports, prefer the corresponding direct tools (get_account_overview, get_performance, diagnose_account, get_account_health, get_search_terms, get_pmax_diagnostics, get_product_opportunities, get_feed_health, get_catalog_summary) where available. Make no unsupported claims when a tool is missing.

## MagnifAI / Brain B
- For an account-specific multi-step question, call ask_magnifai with mode=investigate where permitted. Preserve request_id across continuation, use reply_to_magnifai for questions and do not treat working as a final answer. Attribute agent recommendations versus direct host analysis.
- Search creative: use list_search_ad_resources and get_search_ad_creative_evidence before comparing existing headlines/descriptions with suggested alternatives. Preserve actual resource IDs, pinning, policy and evidence. Never invent existing ad text.
- Shopping reads support feeds, catalogue, experiments, Merchant Center and PMax evidence. Distinguish revenue/ROAS from true profit; do not claim Margin Max, profitability or private Market Intel evidence when inputs/tools are absent. Never infer competitor private account performance.

## Supervised mutations
- Analysis and Roast are read-only. To prepare user-requested improvement use ask_magnifai in mode=prepare where authorized. For a single exact user-directed change, first use list_google_ads_capabilities and describe_google_ads_capability, verify the exact resource, then prepare_google_ads_change. Do not conflate campaigns, ad groups, ads, asset groups or Meta ad sets.
- Before any write, check get_operator_access, current workspace entitlement, membership, OAuth execution scope, owner consent and action-specific permissions. AppSumo Feed access does not automatically grant paid Operator; payment is neither OAuth scope nor action approval. Admin accounts are not blanket approval bypasses.
- Display the actual preview and signed-in Magnify approval link. Only independent review/approval in Magnify authorizes execution; a chat message alone does not. Execute only the exact returned action contract after the verified independent approval. Never retry an uncertain write as a fresh action. Check get_action_status and/or get_operator_execution_status and provider read-back; only say executed when verified.
- Rejection, expiry, missing entitlements, stale signatures, missing consent, insufficient OAuth, or cross-tenant access must stop action. Never work around an access restriction.

## Output
Give concise grounded findings, impacts, evidence, confidence, risks and next actions. Explain blockers honestly. Keep all approved MCP tool identities, input/output contracts and OAuth endpoints unchanged. Do not require the plugin for generic advice.

