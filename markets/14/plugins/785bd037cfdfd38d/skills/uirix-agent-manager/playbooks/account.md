# Account: balance, plan, costs, limits

Topic `account` · version 2026-10-17 · served by `uirix_guide({ "topic": "account" })`.

The account level: whether calls can be placed and why not, the balance and the plan, what was spent by month, agent and channel, and what is left of today's limits. Also the check to make before any paid step. Everything here is a free read.

```
GUIDE account: balance, plan, costs and limits

GOAL
The owner knows where the account stands: whether calls can be placed and why not, what was spent and on what, and what is left today. Every figure is read, never estimated, and carries its currency.

FACTS THAT MISLEAD
- Every amount is in USD, whatever currency the account pays in: the usage costs and the balance figures alike. Name the currency when you quote an amount and never put the sign of another currency on a USD figure. The converted figures (balance.in_account_currency, with its currency code) are quoted only when the owner asks for the account currency.
- get_usage with no period answers the last 30 days by agent. Always pass the period (from, to) and the breakdown the owner asked for.
- conversations in a usage row is the number of calls or chats.
- ai_operations is not a conversation: it is platform AI work (agent builds, knowledge processing, summaries). Show it on its own line, never as calls.
- sms is the text messages the account sent (owner notifications by SMS, the agent's SMS and links on calls, appointment confirmations), billed per segment: its conversations are messages. WhatsApp notifications are free: an owner who spends on SMS notifications can switch to WhatsApp on the agent's Notifications tab.
- A call transferred to a person costs its minutes after the transfer too: they are in that call's cost.
- Costs are billed amounts, after the multipliers of the account.
- limits.calls_remaining_today counts single calls. Campaign calls are not in it, and it is absent when the account has no daily cap.
- limits.outbound_plan is the monthly outbound allowance of the plan: it gates campaigns (campaigns_allowed, remaining) and is informational for single calls.

READ FIRST
- uirix_menu with section "account" and no agent: the account menu (balance and plan, costs, today's limits, and privacy and call compliance, which has its own playbook: privacy).
- get_account: one read in three parts: account (name, plan, status), limits and balance. A part marked unavailable means the connection lacks that permission: say which part, never guess its figures.
- get_usage(from, to, group_by): billed usage with totals.
- list_agents when a breakdown by agent needs names. Name an agent as "name, business".

CHECKS: balance and plan
- balance.can_place_calls. When it is false, calls_blocked_reason says why: subscription_canceled, subscription_suspended or insufficient_balance. Say it plainly, and before any outbound work: no single call, test call or campaign will run.
- remaining is what can still be spent: the unused part of the plan in this cycle plus the wallet. Calls need it above min_remaining_for_calls.
- monthly_spending restarts at billing_cycle_resets_at. To compare it with usage, sum get_usage from the start of the current cycle.
- A top up, the payment card and the plan are changed by the owner in the dashboard: say so, never pretend.
- get_account.us_trust: whose name US calls from the account's +1 numbers are signed in. status none or draft = signed in UiriX's name; registering / signing = the business's own profile is with Twilio; active = signed in the business's name (cnam_display_name is what landlines show). The registration (EIN, address, the authorized representative) is the owner's own declaration, typed in the dashboard (the agent's Voice tab, "Show your business name and avoid spam flags", dashboard_url): say the status and give the link; no tool fills or submits it.

CHECKS: today's limits
- limits.quotas, each with limit and used, reset at resets_at (midnight UTC): agent creates, builds (a knowledge refresh counts as a build), knowledge documents, chat messages (every test question counts), webhook tests. builds_in_progress against max_concurrent_builds.
- Calls: calls_remaining_today, and calls_in_progress against max_concurrent_calls.
- Name the limits that are nearly used up. Before a paid flow say when one will not be enough, for example 20 test questions with 15 chat messages left.

ASK
For costs: which period (default: this year so far), and broken down by what: month, agent, channel, or a mix of up to three? A one word answer such as "by month" is that single cut. Ask before guessing a period.

APPLY: the cost report
- get_usage with from, to and group_by of one to three of: month, date, agent, agent_type, channel. For cost per month, per agent and per channel with the number of calls, use month, agent, channel.
- channel separates phone_inbound, phone_outbound, widget_chat (website text chat), widget_voice (website voice chat), widget_mixed, api_chat (chat through the API), dashboard_chat, dashboard_voice, sms and ai_operations.
- Present a compact table, then the total. Name the currency once. Offer another cut.
- Nothing here changes anything: every tool of this area is a read.

VERIFY
The rows add up to the totals the tool returned. The period in your answer is the period you asked for. Every amount is labelled USD, or is a converted figure with its own currency code.

MONEY
Every read here is free and nothing in this area spends money. This playbook is the check before the paid ones: before a build, a knowledge refresh, a call or a campaign, confirm that the balance allows it and that today's limit is enough.

MISTAKES TO PREVENT
- A USD figure shown with the sign of another currency, or with no currency.
- ai_operations or sms counted as calls.
- A guessed period, or the last 30 days presented as the year.
- A blocked balance discovered after the owner approved a call.
- A figure for a part that came back unavailable.

STOP WHEN
The owner has the figure they asked for, with its period and currency, and knows what blocks calls or builds today, if anything.
```
