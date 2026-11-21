# Metrics and tools

Read everything through ScaleSKUs tools. Each metric has one correct source; don't re-derive it from other numbers. When a definition is in doubt, `search_guides` and then `read_guide` return ScaleSKUs' own canonical definition.

## Metric definitions

| Metric | Meaning | Where to read it |
|---|---|---|
| Ad spend, ad sales, ACoS, ROAS | spend and ad-attributed sales; ACoS = spend ÷ ad sales; ROAS = ad sales ÷ spend | `get_campaign_performance` for authoritative campaign totals; `get_product_performance` per ASIN (Sponsored Products and Display only) |
| Total sales, TACoS | all store sales, not only ad-attributed; TACoS = ad spend ÷ total sales | `get_account_daily_trend`; `run_workflow` with `workflow="health_check"` compares the last 30 days with the 30 before |
| Organic sales | sales not attributed to ads | `get_account_daily_trend` |
| Sessions, conversion, buy box | retail traffic and conversion per ASIN, all channels | `get_asin_traffic` |
| Today | provisional, intraday | `get_realtime_budget_usage` for pacing; daily reports run through yesterday |
| Profit | after Amazon fees, ad spend and, when entered, product cost | `get_profit_loss`: quote its `bottom_line` and check `profit_state` |

Reading the numbers:

- A blank ACoS means spend with no attributed sales, not 0% ACoS.
- Several reads flag the freshest ~2 days as provisional. Base verdicts on settled days.
- Money is in each account's own currency. Never mix currencies across accounts.
- Amazon's fee figures in `get_profit_loss` are estimates and can differ from settlement.

## Which tool for which question

| Question | Start with |
|---|---|
| Which accounts can I see? | `list_profiles` |
| New user, "what can you do?" | `get_started` |
| Is my data up to date? | `get_sync_status` |
| Where do I stand? Brief me | `get_briefing`, `get_profile_summary`, `run_workflow` `health_check` |
| What should I do next? | `get_next_actions`, `run_workflow` `weekly_review` |
| Products | `get_product_performance`, `get_asin_traffic`, `get_entity_tiers`, `get_inventory`, `get_product_health`, `get_product_taxonomy` |
| Campaigns and trends | `get_campaign_performance`, `get_campaign_structure`, `get_adgroup_performance`, `get_daily_trends`, `get_account_daily_trend`, `get_portfolios` |
| Keywords and targets, raw | `get_keyword_performance`, `get_target_performance` |
| Wasted spend (A) | `run_workflow` `cut_waste` / `stock_leak`, `get_waste_search_terms`, `get_negative_opportunities`, `get_search_term_analysis`, `check_negation_status` |
| Under-funded winners (B) | `run_workflow` `uncap_budgets` / `fix_bids`, `get_budget_constrained_campaigns`, `get_budget_analysis`, `get_realtime_budget_usage`, `get_keyword_efficiency`, `get_target_efficiency` |
| Unadvertised demand (C) | `run_workflow` `harvest_winners` / `market_share`, `get_sqp_share_of_voice`, `get_sqp_performance`, `get_search_catalog_performance`, `get_harvest_opportunities`, `get_keyword_competition`, `get_asin_competitors` |
| Efficiency and structure (D) | `run_workflow` `placements`, `get_placement_performance`, `get_duplicate_targeting`, `get_audit_scores`, `get_growth_audit_findings` |
| Why did sales drop? | `run_workflow` `sales_drop`, `get_sales_dips`, `get_optimization_history` |
| Did my changes work? | `run_workflow` `measure_results`, `get_optimization_history` |
| Profit and fees | `get_profit_loss` |
| A queued or applied change | `get_change_task` |
| Past team decisions | `memory_recall`, `memory_timeline` |

## Conventions

- `run_workflow` takes `profile_id`, a `workflow` name, and optionally `max_acos` (the user's target ACoS) or `request` (the user's own words, when the right workflow is unclear). Without `max_acos`, workflows use a default target and say so in their answer; give them the user's target when they have one. Prefer `run_workflow` to chaining many reads for a standard job.
- Many performance reads cover one ad product per call (for example `ad_product="SB"`), and Sponsored Display has no keyword or search-term report. Run each ad product the account uses and skip the ones it doesn't.
- Rate-sorted rankings apply a minimum-clicks floor (default 10) so tiny samples can't top a list. Keep it on for verdicts.
- Keep reads focused: the account, a date range, and a limit (the top 25–50 movers) rather than whole tails. Page large lists instead of asking for everything at once.
- Budget reads disagree by design: `get_budget_analysis` is the account's own history, `get_budget_constrained_campaigns` is Amazon's missed-sales estimate, and `get_realtime_budget_usage` is right now. Name the source of each number.
- For a custom question the fixed tools don't answer, ScaleSKUs has a read-only analysis tool (`run_analysis_query`). Read its guide first (`read_guide` with `guide_id="data-dictionary"`), scope the analysis to the account and a date range, and keep results small. Use it only when no purpose-built tool fits.
- If a tool isn't available on this connection, say so in the answer (for example "Search Query Performance isn't available for this account; coverage is based on harvest data only") rather than guessing.
