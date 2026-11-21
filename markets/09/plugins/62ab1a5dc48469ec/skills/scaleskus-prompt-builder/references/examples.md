# Examples: rough request → ScaleSKUs request

Each example shows what the user typed, the prompt to hand back, what was assumed, and the closing line. Brands and ASINs are made up.

## 1. "my acos is too high, fix it"

```
ScaleSKUs request
Account: List my accounts and ask me which one (use it directly if I have only one).
Goal: Bring ACoS down to [target ACoS %] without losing profitable sales.
Task:
1. Find search terms and targets that spent money with no orders and don't fit the product. Judge each against what the product actually is, not only on click counts.
2. Find keywords running above the target ACoS and work out lower bids.
Scope: Sponsored Products and Sponsored Brands, all campaigns.
Window: Last 30 days through yesterday; treat the last 2 days as provisional.
Targets and limits: Target ACoS [target ACoS %].
Output: First, the spend at stake per month. Then one numbered table: search term or keyword · campaign · spend · orders · ACoS · proposed change · reason. Top 25 by spend.
Changes: Show me the plan; queue only the items I pick as pending tasks. Nothing changes on Amazon until I approve.
Start with: ScaleSKUs workflows cut_waste, then fix_bids.
```

Assumed:
- Last 30 days.
- Both wasted search terms and high bids.
- Sponsored Products and Sponsored Brands.

What ACoS are you aiming for? Tell me and I'll fill it in, or paste the prompt into Claude or ChatGPT with ScaleSKUs switched on.

## 2. "is hafte sales bahut kam ho gayi, kya hua?"

```
ScaleSKUs request
Account: List my accounts and ask me which one (use it directly if I have only one).
Goal: Find out why sales fell in the last 7 days and what it cost.
Task: Compare the last 7 days with the 7 days before. Find the causes (bid or budget changes, campaigns out of budget, paused ads, stock-outs or suppressed listings, lower organic sales) and rank them by sales lost.
Scope: All ad types, total sales and ad sales, all campaigns and products.
Window: Last 7 days through yesterday compared with the 7 days before; the last 2 days are provisional.
Output: First, total sales and ad sales for both weeks with the change. Then the causes ranked by sales lost, each naming the product or campaign and the number behind it. Reply in Hinglish.
Changes: Analysis only.
Start with: ScaleSKUs workflow sales_drop.
```

Assumed:
- "Is hafte" means the last 7 days.
- Both total sales and ad sales are checked.

Ise Claude ya ChatGPT mein ScaleSKUs connector ke saath paste kijiye. Account ka naam bataiye to main bhar deta hoon.

## 3. "add more keywords for my almonds"

```
ScaleSKUs request
Account: List my accounts and ask me which one (use it directly if I have only one).
Goal: Grow sales of my almond products from search terms that already sell but aren't targeted yet.
Task: Find converting search terms for the almond products that aren't keywords yet. Place each as an exact keyword in the ad group that advertises that product, with a starting bid. Check that each search fits the product (type, size, price).
Scope: Sponsored Products; campaigns and products with "almond" in the name or title.
Window: Last 30 days through yesterday.
Targets and limits: Target ACoS [target ACoS %].
Output: First, the sales these search terms brought in the window. Then a numbered table: search term · product (ASIN) · orders · ACoS · destination ad group · starting bid. Top 25 by orders.
Changes: Show me the plan; queue only the items I pick as pending tasks. Nothing changes on Amazon until I approve.
Start with: ScaleSKUs workflow harvest_winners.
```

Assumed:
- "Almonds" means products and campaigns with "almond" in the name.
- Sponsored Products only.

What ACoS should new keywords aim for?

## 4. "mera budget dopahar tak khatam ho jata hai, kya karu"

```
ScaleSKUs request
Account: List my accounts and ask me which one (use it directly if I have only one).
Goal: Stop my best campaigns from running out of budget before the day ends, without wasting money.
Task:
1. Find the campaigns that run out of budget and the time of day they do.
2. Of those, pick the ones that are efficient and in stock, and propose safe budget raises.
Scope: All ad types, all campaigns.
Window: Last 14 days through yesterday, plus today's pacing so far.
Targets and limits: Extra budget at most [₹ per day, all campaigns together].
Output: First, the sales Amazon estimates I miss while capped. Then a table: campaign · daily budget · time it runs out · ACoS · proposed new budget. Reply in Hinglish.
Changes: Show me the plan; queue only the items I pick as pending tasks. Nothing changes on Amazon until I approve.
Start with: ScaleSKUs workflow uncap_budgets, then get_realtime_budget_usage.
```

Assumed:
- Every efficient campaign qualifies, not only the one you noticed.
- The last 14 days.

Roz ka kitna extra budget chalega? Bataiye, main prompt mein bhar deta hoon.

## 5. "give me status of all my clients" (agency)

```
ScaleSKUs request
Account: Every account I can access, each separately; never add up money across currencies.
Goal: See which accounts need attention this week.
Task: For each account, compare the last 7 days with the 7 days before (spend, ad sales, ACoS, TACoS) and flag the biggest issue: a sales drop, an ACoS jump, budget caps or stock problems.
Scope: All ad types, all campaigns.
Window: Last 7 days through yesterday compared with the 7 days before.
Output: One table, one row per account: account · currency · spend · ad sales · ACoS · change vs last week · biggest issue. Sort by how serious the issue is. Then the three accounts to act on first.
Changes: Analysis only.
Start with: list_profiles, then get_briefing for each account.
```

Assumed:
- The last 7 days.
- TACoS only for accounts with Seller or Vendor Central connected.

## 6. "Improve my prompt: 'Analyze my campaigns and tell me what to do'"

```
ScaleSKUs request
Account: List my accounts and ask me which one (use it directly if I have only one).
Goal: Get one prioritised plan for this week across the whole account.
Task: Review every lever (wasted spend, converting search terms not targeted yet, bids above target, winners held back by budget, stock problems) and rank the actions by money at stake.
Scope: All ad types, all campaigns.
Window: Last 30 days through yesterday.
Targets and limits: Use my target ACoS saved in ScaleSKUs; if none is saved, ask me.
Output: First, where I stand: spend, sales, ACoS and TACoS against the 30 days before. Then a numbered plan: action · campaign, keyword or product · the number behind it · expected result. Top 10 by money.
Changes: Show me the plan; queue only the items I pick as pending tasks. Nothing changes on Amazon until I approve.
Start with: ScaleSKUs workflow weekly_review.
```

What it was missing: which account, the period, what "what to do" should cover, how to show the answer, and whether anything may change.

## 7. "auto increase budget when roas is good"

```
ScaleSKUs request
Account: List my accounts and ask me which one (use it directly if I have only one).
Goal: Keep campaigns that sell efficiently from running out of budget, automatically.
Task: Draft an automation rule: when a campaign's ROAS over the last 7 days is above [ROAS threshold] and it has used most of today's budget, raise the daily budget by a set percentage, up to a cap, and reset it to the normal budget every day. If I leave the numbers blank, suggest them from my last 30 days.
Scope: Sponsored Products, all enabled campaigns.
Window: The rule looks at the last 7 days; suggestions use the last 30 days.
Targets and limits: ROAS above [ROAS threshold]; daily budget never above [budget cap: an amount, or a multiple of the normal budget].
Output: The rule in plain words: when it fires, what it changes, the cap, and which campaigns it covers. Then any automation that already changes these budgets.
Changes: Show me the full setup first; create it only on my yes.
Start with: read_guide automation-architect, then create_automation_rule.
```

Assumed:
- Sponsored Products.
- A daily reset, so raises don't pile up.

What ROAS counts as good for you, and how high may a budget go?

## 8. "launch sp campaign for my new HearthNest product B0HEARTH01"

```
ScaleSKUs request
Account: HearthNest
Goal: Launch Sponsored Products for my new product B0HEARTH01 so it starts getting sales and data.
Task: Propose a launch setup:
1. An automatic campaign to discover search terms.
2. A manual exact campaign on the most relevant high-demand search terms for this product, checked against its type, size and price.
For each campaign give the name, daily budget, default bid, and the keywords with their bids.
Scope: Sponsored Products; product B0HEARTH01.
Window: The last 30 days of search data for this product's category.
Targets and limits: Total daily budget [₹ per day]; target ACoS during launch [target ACoS %].
Output: The full setup as one table per campaign, then what to watch in the first 14 days.
Changes: Show me the full setup first; create it only on my yes.
Start with: get_started with node launch, then create_campaign.
```

Assumed:
- An auto campaign plus a manual exact campaign.
- The last 30 days of category search data.

What daily budget and launch ACoS do you want?

## 9. "send me daily spend sales acos in google sheet every morning"

```
ScaleSKUs request
Account: List my accounts and ask me which one (use it directly if I have only one).
Goal: A Google Sheet with my daily ad numbers, updated every morning.
Task: Set up a sheet report with one row per day: date · spend · ad sales · orders · ACoS · total sales · TACoS. Keep older days, and refresh recent days as Amazon finalises them.
Scope: All ad types, whole account.
Window: From the first day of last month onwards.
Output: Sample rows first, then the sheet link, the next run time and where to manage it.
Changes: No changes on Amazon. Create the Google Sheet after I've seen sample rows.
Start with: read_guide sheet-reports, then schedule_sheet_report.
Repeat: Every day at 8:00 IST, updating the same Google Sheet.
```

Assumed:
- 8:00 IST.
- History from the start of last month.
- Total sales and TACoS need Seller or Vendor Central connected in ScaleSKUs, and the sheet needs your Google account connected there.

## 10. "am i actually making money after ads?"

```
ScaleSKUs request
Account: List my accounts and ask me which one (use it directly if I have only one).
Goal: Find out whether I make a profit after Amazon fees, ad spend and product costs.
Task: Give my profit and loss for last month (sales, Amazon fees, ad spend, product costs and what's left), for the account and for my top products. Say whether product costs are entered in ScaleSKUs. If they aren't, show the result before product costs and tell me how to add them.
Scope: Whole account, all products.
Window: The previous calendar month.
Output: First, the bottom line. Then a table by product: product · sales · fees · ad spend · product cost · profit · profit %. Top 15 by sales.
Changes: Analysis only.
Start with: get_profit_loss.
```

Assumed:
- Last full month.
- Top 15 products.

## 11. "who is taking my sales on almonds 1kg"

```
ScaleSKUs request
Account: List my accounts and ask me which one (use it directly if I have only one).
Goal: See who wins the search "almonds 1kg" and where I lose shoppers to them.
Task: For "almonds 1kg" and close variants, show search volume, my share of impressions, clicks and purchases, the top competing products, the median price shoppers pay against my price, and my ad spend and ACoS on these searches. Then say whether to bid up, hold or stop.
Scope: Sponsored Products; my almond products.
Window: The last 4 complete weeks.
Output: First, my purchase share against my click share. Then one table per search term. End with one recommendation.
Changes: Analysis only.
Start with: get_keyword_competition.
```

Assumed:
- Close variants are included.
- The last 4 complete weeks, because this data is weekly.

## 12. "did the negatives we added last week help?"

```
ScaleSKUs request
Account: List my accounts and ask me which one (use it directly if I have only one).
Goal: Check whether the negatives added recently cut waste without hurting sales.
Task: Take the negatives added through ScaleSKUs 7 to 14 days ago. For each campaign they touched, compare spend, sales and ACoS after the change with the same number of days before it.
Scope: Sponsored Products and Sponsored Brands.
Window: 7 days after each change compared with the 7 days before it.
Output: First, the total spend saved and any sales lost. Then a table: campaign · negatives added · spend before → after · sales before → after · ACoS before → after · verdict.
Changes: Analysis only.
Start with: ScaleSKUs workflow measure_results.
```

Assumed:
- "Last week" means changes made 7 to 14 days ago, so each has a full 7 days of results.

## 13. Two asks at once: "Prime Day is 12 July, get my account ready. also my ads keep stopping in the evening"

Two prompts, in this order.

**Prompt 1: sale readiness**

```
ScaleSKUs request
Account: List my accounts and ask me which one (use it directly if I have only one).
Goal: Get my account ready for Prime Day on 12 July so my best products don't run out of stock or budget.
Task:
1. Check stock and listing health for my top products, and flag any that could run out before or during the sale.
2. Find the campaigns that will need more budget during the sale, and propose extra budget for the sale days only.
3. Propose bid increases on proven winners for the sale days only.
Scope: All ad types; my top 20 products by sales.
Window: The last 30 days as the baseline; the sale on 12 July.
Targets and limits: Extra budget during the sale at most [₹ per day, all campaigns together]; target ACoS during the sale [target ACoS %].
Output: A dated plan in three parts (before the sale, the sale days, after the sale), each listing the actions, the product or campaign, and the numbers behind them.
Changes: Show me the plan; queue only the items I pick as pending tasks. Nothing changes on Amazon until I approve.
Start with: get_started with node obj_event, then ScaleSKUs workflows stock_leak and uncap_budgets.
```

**Prompt 2: evening budget caps**

```
ScaleSKUs request
Account: List my accounts and ask me which one (use it directly if I have only one).
Goal: Keep my ads running through the evening when evening hours sell.
Task: Find the campaigns that run out of budget in the evening and when they cap, and check how evening hours convert for them. Propose budget raises for the efficient ones. Where money is wasted earlier in the day, propose lower bids for those hours instead.
Scope: All ad types, all campaigns.
Window: Last 14 days through yesterday plus today's pacing; the last 28 days for hour-of-day results.
Output: First, the sales missed in the evening. Then a table: campaign · daily budget · time it runs out · evening ACoS · proposed change.
Changes: Show me the plan; queue only the items I pick as pending tasks. Nothing changes on Amazon until I approve.
Start with: ScaleSKUs workflow uncap_budgets.
```

Assumed:
- The sale is one day.
- The same account for both prompts.

How much extra budget per day can you spend on Prime Day, and what ACoS is acceptable?

## 14. Team template: "make a weekly review prompt for my team"

Use it every Monday, once for each account.

```
ScaleSKUs request
Account: [account name, marketplace]
Goal: Weekly check-up: what changed, and what to fix this week.
Task:
1. Compare last week with the week before: spend, ad sales, orders, ACoS, TACoS.
2. List the three biggest problems and the three biggest opportunities, each with the campaign, keyword or product and the number behind it.
3. Put the fixes into one numbered plan, ranked by money at stake.
Scope: All ad types, all campaigns.
Window: The last 7 days through yesterday compared with the 7 days before.
Targets and limits: Target ACoS [target ACoS %].
Output: First, a five-line summary. Then the problems, the opportunities and the plan as tables.
Changes: Show me the plan; queue only the items I pick as pending tasks. Nothing changes on Amazon until I approve.
Start with: ScaleSKUs workflow weekly_review.
Repeat: Every Monday at 10:00 IST as a scheduled task in this assistant.
```

## 15. "whats my best keyword on amazon us last month"

```
ScaleSKUs request
Account: Trailmint (Amazon.com)
Goal: Find my best-performing keywords last month.
Task: Rank keywords by ad sales, with their efficiency, and flag any whose campaign ran out of budget.
Scope: Sponsored Products and Sponsored Brands, all campaigns.
Window: The previous calendar month.
Output: A table: keyword · match type · campaign · spend · ad sales · orders · ACoS · CVR. Top 20 by ad sales, in US dollars.
Changes: Analysis only.
Start with: get_keyword_performance.
```

Assumed:
- "Best" means the most ad sales.
- Sponsored Products and Sponsored Brands.

## Starter prompts for "what can I ask?"

These short asks already carry the essentials. Offer the ones that fit the user, and structure whichever they pick.

- "Brief me on my account: what changed this week and what needs attention first."
- "Cut my wasted ad spend over the last 30 days. My target ACoS is [x]%. Show me the plan before changing anything."
- "Which converting search terms am I not targeting yet? Last 30 days, target ACoS [x]%."
- "Which campaigns ran out of budget in the last 14 days, and what did it cost me?"
- "Why did my sales drop in the last 7 days compared with the 7 days before?"
- "Am I spending on ads for products that are out of stock or suppressed?"
- "Show my profit after fees, ads and product costs for last month, by product."
- "Did the changes made in the last 14 days work? Before against after for each."
- "Who am I losing to on my top 5 search terms over the last 4 weeks?"
- "Send me a Google Sheet every Monday with last week's spend, sales and ACoS by campaign."

## 16. "make a rule: pause keywords with 20 clicks and no orders in last 30 days"

The user gave every number, so there are no blanks and no extra conditions.

```
ScaleSKUs request
Account: List my accounts and ask me which one (use it directly if I have only one).
Goal: Automatically stop paying for keywords that get clicks but never sell.
Task: Draft an automation rule: when a keyword has 20 or more clicks and no orders over the last 30 days, pause it.
Scope: Sponsored Products, all enabled campaigns.
Window: The rule looks at the last 30 days.
Targets and limits: 20 clicks, 0 orders, 30 days.
Output: The rule in plain words: when it fires, what it changes, and which keywords it covers.
Changes: Show me the full setup first; create it only on my yes.
Start with: read_guide automation-architect, then create_automation_rule.
```

Assumed:
- Sponsored Products.
- Keywords only, not product targets.
