---
name: instagram
description: Analyze Instagram organic performance through Windsor.ai. Use when the user asks about their Instagram Business or Creator account's insights — followers, reach, impressions, profile or website clicks, engagement, or the performance of individual media/posts. Do not use for Instagram Ads (those live in the Meta/Facebook Ads connector), other platforms, or GA4/website analytics.
---

# Instagram (organic) via Windsor.ai

Windsor.ai pulls Instagram **organic** insights from the Instagram Graph API. The
connector id is `instagram`. On the Instagram app the connector is already
scoped, so you usually do not need to pass it; when a tool asks for a connector,
use `instagram`.

This connector is for **organic** Instagram analytics only — profile and media
insights. It has **no ad or cost data** (Instagram Ads live in the Meta/Facebook
Ads connector, so route ad-spend questions there), and **publishing is not
currently enabled**, so treat it as read-only: if the user asks to post or
publish, tell them that isn't available here rather than attempting it.

Golden rules:

- **Never guess field, account, or option names** — get them from `get_fields`,
  `get_connectors`, and `get_options`. Call those first.
- This connector is read-only; there are no live write actions to run.
- Report what the user asked for, concisely.

## 1. Ground yourself first

Call `get_connectors` to see which Instagram accounts are connected (each has an
id and usually a name/username). The account must be an Instagram Professional
account (Business or Creator) linked to a Facebook Page. If none is connected,
help the user connect: `get_connector_authorization_url` (or
`get_connector_connect_info` for the auth type and steps) and give them the
setup link — don't describe manual dashboard navigation.

If several accounts are connected and the request is ambiguous, ask which one.

## 2. Reading insights

1. Call `get_fields` for `instagram` to get valid field ids. Typical ones
   include account-level metrics (e.g. `followers_count`, `follows_count`,
   `media_count`, reach, impressions, profile/website clicks, engagement) and
   per-media metrics — use the exact ids returned, not these examples.
2. Call `get_data` with `fields`, the target `account`(s), and a date range
   (`date_from`/`date_to` or a `date_preset` like `last_7d`, `last_30d`,
   `this_month`; append `T` to include today).

Instagram date behaviour to keep in mind:

- **Lifetime metrics** (e.g. total followers) ignore the date range — the API
  always returns the latest value. Don't present them as period-specific.
- **Daily metrics** are only available for roughly the **last 30 days**. Requests
  for older daily data will return nothing.
- **Stories** insights exist only for the **last 24 hours**.

If a metric the user wants isn't in `get_fields`, say so rather than
substituting a different one. There is no cost/spend data here.

## 3. Reference real data, don't fabricate

On an error (unknown field/connector/account), call the relevant discovery tool
and retry with correct values or report the specific error. Never invent
follower counts, engagement numbers, or media ids.
