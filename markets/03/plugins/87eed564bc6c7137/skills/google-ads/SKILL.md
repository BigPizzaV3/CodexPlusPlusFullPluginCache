---
name: google-ads
description: Analyze and manage Google Ads through Windsor.ai. Use when the user asks about their Google Ads performance — pulling live campaign, ad group, or keyword metrics (cost, impressions, clicks, conversions, CPA, ROAS), comparing date ranges, or finding top or underperforming campaigns — or when they want to pause or enable a campaign or change a campaign budget. Do not use for other ad platforms (Meta/Facebook, TikTok, LinkedIn, Microsoft Ads), organic social, or GA4/website analytics.
---

# Google Ads via Windsor.ai

Windsor.ai exposes live Google Ads data (read) and a small set of campaign
management actions (write) through MCP tools. The connector id is
`google_ads`. On the Google Ads app the connector is already scoped, so you
usually do not need to pass it — but when a tool asks for a connector, use
`google_ads`.

Golden rules:

- **Never guess field, account, action, or option names.** They come from
  `get_fields`, `get_connectors`, `list_actions`, and `get_options`. Call those
  first; do not invent identifiers.
- **Reads are safe; writes change live ad spend.** Only call `execute_action`
  after the user has confirmed the specific change.
- Report numbers the user asked for, concisely. Don't dump raw rows unless asked.

## 1. Ground yourself first

Call `get_connectors` to see which Google Ads accounts are connected (each has
an id and, usually, a name). If none are connected, help the user connect one:
call `get_connector_authorization_url` (or `get_connector_connect_info` for the
auth type and steps) and give them the setup link — do not describe manual
dashboard navigation.

If the user names an account, match it to a connected account id. If several are
connected and the request is ambiguous, ask which account.

## 2. Reading performance data

1. Call `get_fields` for `google_ads` to get valid field ids (e.g. campaign,
   ad_group, date, cost/spend, impressions, clicks, conversions, conversion
   value — use the exact ids returned, not these examples).
2. If the analysis needs attribution or segmentation controls, call
   `get_options` to see the connector's options and valid values.
3. Call `get_data` with:
   - `fields`: the ids you actually need (keep the set small).
   - `accounts`: the target account id(s); omit for all connected accounts.
   - A date range: either `date_from`/`date_to` (`"2026-02-01"`), or
     `date_preset` — `last_7d`, `last_30d`, `last_Xd`/`last_Xw`/`last_Xm`,
     `this_month`, `this_year`, `last_year`. Append `T` to include today
     (e.g. `last_7dT`, `this_monthT`).
   - `options`: only if get_options showed relevant ones.
   - `filters`: optional conditions, e.g. `[["cost", "gt", 100]]`; combine with
     `"and"`/`"or"` and nest as needed.

Common requests → recipe:

- **Overview / trend:** fields `date` + the metrics, over a preset range.
- **By campaign:** fields `campaign` + metrics; sort/aggregate in your answer.
- **Best / worst campaign:** pull campaign + the metric, then rank; return only
  what was asked (e.g. just the campaign name) if the user constrained the
  output format.
- **Efficiency:** cost per conversion = cost ÷ conversions; ROAS = conversion
  value ÷ cost. Compute from returned fields; note if conversions are zero.

Watch out: Google Ads money fields are in the account currency (state it if
known). Conversions can be fractional. If a field the user wants isn't in
`get_fields`, say so rather than substituting a different metric.

## 3. Managing campaigns (write actions)

Google Ads exposes exactly **three** write actions via `list_actions` /
`execute_action`. Always call `list_actions` first to confirm the exact action
ids and parameter schemas — treat the list below as guidance, not gospel:

- **`pause_campaign`** — params: `campaign_id`.
- **`enable_campaign`** — params: `campaign_id`.
- **`set_campaign_budget`** — params: `campaign_id`, `budget_type`
  (`daily` or `lifetime`), `amount_micros`, and `apply_to_shared_budget`
  (default false — set true only to change a budget shared by several
  campaigns). There is **no** ad-group budget action; Google ad groups have no
  budgets.

There is no create-campaign, no bid adjustment, and no offline-conversion
upload — do not claim these exist.

Budget mechanics:

- `amount_micros` is in **micros**: 1,000,000 micros = 1 unit of the account
  currency, so `50000000` = 50.00. Convert the user's amount to micros.
- `set_campaign_budget` sets an **absolute** budget, not a delta. To "raise by
  20%", first read the current budget, compute the new absolute value, and set
  that.

Write workflow — every time:

1. Resolve the campaign to its `campaign_id` (via a `get_data` read on
   `campaign` + id fields if the user gave a name).
2. Build the exact params from the `list_actions` schema.
3. **Show the user the concrete change and ask them to confirm** — e.g.
   "Pause campaign 'Summer Sale' (id 123…) on account 456…?" or "Set daily
   budget for campaign X to €50.00 (50000000 micros)?".
4. Only after an explicit yes, call `execute_action` and report the result.

If the user says "pause the worst campaign", first do the read + ranking, then
name the specific campaign and confirm before pausing — don't pause on the
strength of the aggregate alone.

## 4. Reference the user's data, don't fabricate

If a tool returns an error (unknown field/connector/account), call the relevant
discovery tool (`get_fields`, `get_connectors`, `list_actions`) and retry with
correct ids. Never fill gaps with made-up numbers or campaign names.
