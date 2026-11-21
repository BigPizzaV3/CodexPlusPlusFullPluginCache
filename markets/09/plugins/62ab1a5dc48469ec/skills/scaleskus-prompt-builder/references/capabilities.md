# What ScaleSKUs can answer

ScaleSKUs connects Claude or ChatGPT to the user's Amazon Ads data, and to their Seller Central or Vendor Central data when that is connected too. Every prompt you build maps to one of the jobs below.

For each job the tables give:

- **Users say:** typical phrasings.
- **Start with:** the ScaleSKUs workflow or tool for the Start with line. A workflow runs as `run_workflow` with that name.
- **The prompt needs:** what makes the answer right.
- **Watch for:** what to write around.

## Know your numbers

| Job | Users say | Start with | The prompt needs | Watch for |
|---|---|---|---|---|
| A number or a list | "ACoS last week?", "top 10 campaigns by spend", "kitna kharcha hua" | `get_profile_summary` for account totals; `get_campaign_performance`, `get_keyword_performance`, `get_product_performance` for lists | metric, window, ad types, top N and sort | a blank ACoS means spend with no sales, not 0% |
| Brief me | "what's going on", "kya chal raha hai", "morning update" | `get_briefing` | account | |
| Account health | "how is my account doing", "account kaisa chal raha" | workflow `health_check` | account; window (default 30 days compared with the 30 before) | TACoS and total sales need Seller or Vendor Central |
| Why sales dropped | "sales down", "orders kam ho gaye" | workflow `sales_drop` | the drop period; ad sales, total sales or both | name both periods |
| Today and pacing | "aaj kitna spend hua", "which campaigns are out of budget right now" | `get_realtime_budget_usage` | today so far | today's numbers are provisional |
| Is my data up to date | "is data synced", "numbers look old" | `get_sync_status` | account | |

## Stop the leaks

| Job | Users say | Start with | The prompt needs | Watch for |
|---|---|---|---|---|
| Cut wasted spend | "ACoS too high", "wasting money", "negatives", "faltu kharcha" | workflow `cut_waste`, and again for Sponsored Brands if the account runs them | target ACoS if known; last 30 days | a relevant search that hasn't sold yet is a bid question, not a negative; judge fit, not only clicks |
| Stock running low | "stock khatam hone wala hai", "low inventory", "restock is 3 weeks away" | `get_inventory` (days of stock left), then `get_product_performance` | the product (ASIN or name) | slow spend so stock lasts until the restock arrives; never raise budgets on it |
| Ads on out-of-stock or broken products | "spending on out of stock", "listing suppressed", "no Buy Box" | workflow `stock_leak` | account | needs Seller or Vendor Central |

## Tune and grow

| Job | Users say | Start with | The prompt needs | Watch for |
|---|---|---|---|---|
| Fix bids | "bids too high", "CPC too high", "keywords losing money" | workflow `fix_bids` | target ACoS | ScaleSKUs moves bids in capped steps |
| New keywords | "add keywords", "grow sales", "scale winners", "sales badhao" | workflow `harvest_winners` | target ACoS (it sets starting bids) | each term goes to the ad group that advertises the product it sells, with a starting bid and a price check; with no such ad group, it suggests a new campaign |
| Budget caps | "budget khatam ho jata hai", "campaigns run out of budget" | workflow `uncap_budgets`; `get_realtime_budget_usage` for today | the most extra budget per day, if the user has a limit | only efficient, in-stock campaigns get more budget |
| Placements | "top of search", "product pages", "placement boost" | workflow `placements` | account; Sponsored Products | |
| Full review | "optimize my account", "what should I do this week", "how do I get more sales", "help me grow" | workflow `weekly_review` | target ACoS if known | the answer is one numbered plan across all levers |

## Go deeper

| Job | Users say | Start with | The prompt needs | Watch for |
|---|---|---|---|---|
| Search share and competitors | "competitors", "market share", "who's winning my keywords" | workflow `market_share`; `get_keyword_competition` for named search terms; `get_asin_competitors` | search terms or products; last 4 complete weeks | needs Brand Analytics (brand-registered) |
| Did my changes work | "did the negatives work", "results of last week's changes" | workflow `measure_results`; `get_optimization_history` for what changed | which changes, or since when | measures changes made through ScaleSKUs |
| Profit | "am I making money", "munafa kitna", "P&L" | `get_profit_loss` | window (last full month by default) | net profit needs product costs in ScaleSKUs (`set_product_costs`); Amazon fees are estimates |
| One product (ASIN) | "how is B0… doing", "why isn't my new product selling" | `get_product_performance`, `get_asin_traffic`, `get_inventory`, `get_product_health` | ASINs | sessions, Buy Box and stock need Seller or Vendor Central |
| Which products and targets carry the account | "my best products", "hero products" | `get_entity_tiers` | account | |
| Search terms | "which search terms bring orders", "search term report" | `get_search_term_analysis` | window, ad types, sort | Sponsored Display has no search terms |
| Structure | "is my account structured right", "duplicate keywords" | `get_campaign_structure`, `get_duplicate_targeting`, `get_audit_scores` | account | |
| Shopper insights (Amazon Marketing Cloud) | "new customers from ads", "path to purchase", "reach and frequency" | `get_shopper_insights` | week | may report data as loading or not available for the account |
| Bought together, repeat buyers | "what do people buy with my product", "repeat customers" | `get_market_basket`, `get_repeat_purchase` | products; month | Brand Analytics, monthly |
| Hour of day | "which hours convert", "should I stop ads at night" | `run_analysis_query` on the hourly ad data (read the `data-dictionary` guide first) | last 28 days; spend, orders and ACoS by hour | the same analysis is on the Day-parting page in ScaleSKUs |

## Build and automate

| Job | Users say | Start with | The prompt needs | Watch for |
|---|---|---|---|---|
| Automation rule | "auto increase budget when ROAS is good", "auto-pause bad keywords" | `read_guide` `automation-architect`, then `create_automation_rule` | condition, action, limits, scope; thresholds from the user, or "suggest them from my last 30 days and show me first" | on accounts set to run automations on their own, a new rule switches on at once |
| Ready-made automations | "set up automations for my account", "best rules for me" | `list_automation_library`, then `create_strategy` | scope (products, categories or portfolios); target ACoS | same as rules |
| Day-parting schedule | "run ads only in the evening", "lower bids at night" | `read_guide` `automation-architect`, then `create_dayparting_schedule` | hours and days, or "take them from my hour-of-day analysis"; bid, budget or pause | windows are in the marketplace's local time |
| New campaign | "launch a campaign for B0…", "new auto campaign" | `create_campaign` | ASINs; Sponsored Products, Brands or Display; auto or manual; keywords or product targets; daily budget; default bid | a new campaign starts spending once it's live; Sponsored Brands needs a brand creative |
| Sale event | "Prime Day prep", "Diwali sale", "Great Indian Festival" | `get_started` with node `obj_event`, then workflows `stock_leak` and `uncap_budgets` | event dates; budget headroom | stock first, then budgets, then bids |
| New product launch | "launching a new product" | `get_started` with node `launch` | ASIN, price, target ACoS during launch | |

## Reports, memory and help

| Job | Users say | Start with | The prompt needs | Watch for |
|---|---|---|---|---|
| One-off Google Sheet | "export all search terms to a sheet" | `export_to_sheet` | columns, window, filters | needs Google connected in ScaleSKUs |
| Sheet kept up to date | "daily sheet of spend, sales, ACoS", "weekly report every Monday" | `read_guide` `sheet-reports`, then `schedule_sheet_report` | the column headers in order; one row per day, campaign or product; how often and at what time | ScaleSKUs shows sample rows before scheduling |
| Remember my targets | "remember my target ACoS is 25%" | `memory_remember` | the fact to save | saved only when the user asks |
| What can ScaleSKUs do | "how do I start", "what can you do" | `get_started` | account | |
| Anything else | a custom question none of the above answers | `read_guide` `data-dictionary`, then `run_analysis_query` | account, window, the exact figures wanted | keep results small |

## What each data source needs

| To answer about | The user needs in ScaleSKUs |
|---|---|
| Ads: spend, ad sales, ACoS, keywords, search terms, campaigns | Amazon Ads connected (always there) |
| Total sales, organic sales, TACoS, sessions, conversion, Buy Box, stock, profit | Seller Central or Vendor Central connected |
| Search query share, market share, keyword demand, market basket, repeat purchase | Brand Analytics (brand-registered sellers and vendors) |
| Shopper insights | Amazon Marketing Cloud available for the account |
| Google Sheets | a ScaleSKUs plan that includes Google Sheets reports, and the Google account connected in ScaleSKUs |
| Queuing or applying changes | changes enabled for the organization; live changes also need two-step verification on the login |

## Limits to write around

- Sponsored Display has no keywords or search terms.
- Vendor accounts have no stock report.
- The last ~2 days of ad data are provisional.
- Retail data lags ad data by 2–3 days.
- Brand Analytics is weekly or monthly, and Amazon Marketing Cloud data comes by week.
- Money is never added up across currencies. Agencies get each account separately.
- ScaleSKUs never changes Amazon on its own. Fixes are queued as tasks, and a live change needs the user's explicit go-ahead.
- Automation rules, strategies and day-parting schedules switch on at creation on accounts set to run automations. That's why their prompts say "create it only on my yes".
