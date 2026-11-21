# The ScaleSKUs request format, field by field

```
ScaleSKUs request
Account: …
Goal: …
Task: …
Scope: …
Window: …
Targets and limits: …
Leave alone: …
Output: …
Changes: …
Start with: …
Repeat: …
```

Account, Goal, Task, Scope, Window, Output and Changes are always present. The other lines appear only when they have something to say.

## Account

Which Amazon Ads account the prompt is about. In ScaleSKUs, each account is one advertiser in one marketplace, with its own currency.

| The user said | Write |
|---|---|
| An account or brand name | The name as they wrote it, plus the marketplace if known: `HearthNest (Amazon.in)` |
| Nothing | `List my accounts and ask me which one (use it directly if I have only one).` |
| Two or three names | List them, then `each account separately` |
| "All my accounts" or "all my clients" | `Every account I can access, each separately; never add up money across currencies.` |
| One brand in two marketplaces | Treat them as two accounts, each in its own currency |

When ScaleSKUs tools are available in the conversation, `list_profiles` returns the exact account names and currencies.

## Goal

One sentence giving the business outcome in the user's terms. Start with a verb such as bring down, grow, find out why, protect, launch, understand, report or automate.

- "Bring ACoS down to 30% without losing profitable sales."
- "Find out why sales fell this week and what it cost."
- "Grow sales from search terms that already sell but aren't targeted yet."

When the words could point to cutting or to growing, decide from what the user said and list the choice as assumed. "ACoS high" means cut. "Sales low" means diagnose first, then grow.

## Task

What to find, judge and propose. Start each task with a verb and be specific.

- **Order.** Number the steps when order matters, for example "1. Find … 2. Work out …". Diagnose before changing anything.
- **Judgement rules.** Include any rule the user cares about. For negatives and new keywords, add: "Judge each search term against what the product actually is (type, size, variant, price), not only on click counts."
- **Named items.** Carry every product, campaign, keyword or ASIN the user named into the task.

## Scope

- **Ad types.** Use the default for the job in [capabilities.md](capabilities.md) unless the user named ad types. Sponsored Display has no keywords or search terms, so keep it out of keyword, search-term and negative jobs.
- **Filters.** Include any filter the user named: campaigns with a word in the name, portfolios, ASINs (B0…), keywords, match types, placements.
- **Whole account.** When there's no filter, write "all campaigns" or "all products", so nobody wonders whether something was left out.

## Window

Always write the window, because ScaleSKUs answers for the last 14 days when none is given. Turn relative words into explicit periods:

| The user said | Window |
|---|---|
| today, aaj | today so far (live data, provisional) |
| yesterday, kal (about the past) | yesterday |
| this week, last week, is hafte, pichle hafte | the last 7 days through yesterday, compared with the 7 days before |
| this month, is mahine | this month to date through yesterday, compared with the same days last month |
| last month, pichle mahine | the previous calendar month |
| "since Tuesday", "after the change on 12 Sep" | from that date to yesterday, compared with the same number of days before it |
| nothing | the default for the job below |

**Default window by job**

| Job | Window |
|---|---|
| A single number or list | last 14 days |
| Account health | last 30 days compared with the 30 before |
| Why sales dropped | the drop period compared with the same number of days before it |
| Cut waste, negatives | last 30 days |
| Fix bids | last 30 days |
| New keywords (harvest) | last 30 days |
| Budget caps | last 14 days, plus today's pacing |
| Placements | last 30 days |
| Search share, competitors | the last 4 complete weeks |
| Did my changes work | 7 days after each change compared with the 7 days before it |
| Profit | the last full month, or this month to date |
| Hour-of-day (day-parting) | the last 28 days |
| Shopper insights (Amazon Marketing Cloud) | the latest complete week |

**Freshness notes**

Add these only when they affect the answer:

- The last ~2 days of ad data are provisional because Amazon attributes sales late.
- Total sales, sessions and TACoS come from Seller or Vendor Central and usually lag ad data by 2–3 days.
- Search share (Brand Analytics) is weekly.
- Market basket and repeat purchase data are monthly.

## Targets and limits

The numbers that bound the answer: target ACoS, ROAS or TACoS, a daily or monthly budget cap, the largest bid change allowed, or the fewest clicks before judging.

- **Source.** Take them only from the user, or write `Use my target ACoS saved in ScaleSKUs.`
- **No extras.** Don't add a threshold, limit, cooldown or cap the user didn't ask for. ScaleSKUs applies its own safety limits to every change.
- **Missing.** If a bid, budget or automation change depends on a target nobody gave, leave `[target ACoS %]` and ask for it under the prompt.
- **Break-even ACoS.** This is the profit left per sale before ad spend, as a share of the price: (price − Amazon fees − product cost) ÷ price. When the user doesn't know a target, you can offer "or work out my break-even ACoS from my product costs in ScaleSKUs".

## Leave alone

Write only what the user said or clearly meant. Examples:

- "Don't touch my brand campaigns"
- "Leave the hero product B0XXXXXXXX alone"
- "Don't pause anything"
- "Nothing in the Prime Day portfolio"

Don't add exclusions of your own. ScaleSKUs already checks recent changes and stock before it recommends anything.

## Output

- **Headline.** Say which number comes first: money at stake per month, the ACoS change, sales lost, or the answer to the question.
- **Table.** Name the columns, the number of rows (top 10, 25 or 50) and the sort order.
- **Money.** Use the account's own currency. When there are several accounts, give one table per account or a currency column, and no grand total across currencies.
- **Format.** A table in the chat is the default. Other options: "Put the full list in a Google Sheet" (needs Google connected in ScaleSKUs), a report, or a chart.
- **Length or language.** Add "Keep it to one screen" if the user wants it short, and "Reply in Hindi" (or their language) when it applies.

## Changes

Use one of these exact lines:

| Line | When |
|---|---|
| `Analysis only.` | Questions, reports, "why", "show me". Also the default. |
| `Show me the plan; queue only the items I pick as pending tasks. Nothing changes on Amazon until I approve.` | Fix, optimize, cut, grow, improve |
| `Queue everything as pending tasks for my approval.` | The user said to queue or apply all of it |
| `Apply live only after I confirm the exact list.` | The user explicitly wants live changes now |
| `Show me the full setup first; create it only on my yes.` | Automation rules, day-parting schedules, strategies, new campaigns |
| `No changes on Amazon. Create the Google Sheet after I've seen sample rows.` | Google Sheet exports and reports that are kept up to date |

How ScaleSKUs handles changes, so the prompt never contradicts it:

- A queued task changes nothing on Amazon. It waits for approval under Tasks in ScaleSKUs, or for the user's explicit go-ahead in the chat.
- A live change needs two-step verification on the user's ScaleSKUs login, and a daily limit per account applies.
- If changes aren't enabled on the user's connection, the assistant gives the plan as a checklist.
- On accounts set to run automations on their own, a new rule or schedule switches on the moment it is created. That is why automations always get "create it only on my yes".

## Start with

The ScaleSKUs workflow or tool the assistant should use first, taken from [capabilities.md](capabilities.md). For example, `Start with: ScaleSKUs workflow cut_waste`, or `Start with: get_profit_loss`.

- Write one or two names at most.
- Leave the line out when no job fits.

## Repeat

Use this only for recurring requests. Give how often, the time and time zone, and where the result goes.

- `Repeat: every Monday at 9:00 IST, updating the same Google Sheet.` ScaleSKUs keeps the sheet up to date with a scheduled sheet report; this needs Google connected in ScaleSKUs.
- `Repeat: every morning at 8:00 IST as a scheduled task in this assistant.` This uses the assistant's own scheduler, for a chat summary rather than a sheet.

## What users say, and what to write

| They say | They mean | Write |
|---|---|---|
| ACoS high, ACoS bahut zyada | ACoS above their target | Goal: bring ACoS down to [target] |
| kharcha, spend | ad spend | Spend |
| sale, sales, bikri | ad sales or total sales | Say which. If unclear: "total sales and ad sales" |
| budget khatam, out of budget, capped | campaigns run out of daily budget | The budget caps job |
| keyword add karo, naye keywords | promote converting search terms to keywords | The new keywords job |
| negative karo, faltu keywords | negatives for search terms that don't fit | The cut waste job |
| band karo, stop, pause | pause | The Changes line for fixes, with the pause as a proposal |
| report bhejo, sheet chahiye | a report or Google Sheet | Output, or Repeat |
| excel, CSV, download | a file they can open in Excel | "Put the full list in a Google Sheet (it opens in Excel)" |
| competitor, dusre brand | other brands on the same searches | The search share job |
| rank, visibility | how often shoppers see the product | Search share: impression, click and purchase share |
| munafa, profit | profit after fees, ads and product cost | The profit job |
| raat ko band, hourly, day-parting | a time-of-day schedule | The day-parting job |
| ROAS acha hai, winner | campaigns or keywords beating the target | Name the target, or leave the blank |

## Metric names

Use these names in Targets and limits and in Output.

- **Spend:** ad cost.
- **Ad sales:** sales Amazon attributes to ads.
- **ACoS:** spend ÷ ad sales.
- **ROAS:** ad sales ÷ spend.
- **TACoS:** spend ÷ total sales. Needs Seller or Vendor Central connected.
- **Impressions, clicks, CTR:** clicks ÷ impressions.
- **CPC:** spend ÷ clicks.
- **Orders, units, CVR:** orders ÷ clicks.
- **Total sales, organic sales:** total sales minus ad sales.
- **Sessions, Buy Box %:** retail traffic.
- **New-to-brand orders:** first purchase from the brand in 12 months.

## Final check

- Account says which account, or how to pick it.
- Window is explicit.
- Output says what comes first and what the table holds.
- Changes is one of the six lines above.
- Every number, name and ASIN came from the user.
- Every line is in English. If the user wrote in Hindi or Hinglish, the Output line ends with "Reply in Hindi" or "Reply in Hinglish".
- There are at most two blanks, and each is asked about under the prompt.
