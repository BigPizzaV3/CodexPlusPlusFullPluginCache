---
name: financial-brief
description: Financial Brief — a short, prioritised briefing on the user's Zenmoney finances for a daily, weekly, or monthly horizon. It covers risks to act on now (fees, overdrafts, uncovered or missed payments, duplicate or suspicious charges, cash shortfalls), upcoming obligations, and an overview of the completed month. Use when the user asks to run the Financial Brief or to get it on a schedule, when a scheduled task passes delivery_cadence, and whenever the user asks for a daily, weekly, or monthly financial summary, what in their finances needs attention, or whether upcoming payments are covered (for example "Run Financial Brief", "финансовый бриф", "что важного по деньгам?", "brief finansowy", "resumen financiero de la semana"). Requires the Zenmoney connector.
---

# Financial Brief

Prepare a short, prioritised briefing on the user's finances in Zenmoney: what could cost them money or needs action soon, what is coming up, and, for a month, what kind of month it was. The brief shows conclusions, not the analysis behind them. It only reads data: never change anything in Zenmoney while running it.

## Goal

Help the user stay on top of financially or personally significant events and understand what is coming before it becomes a problem.

The first priority is to help prevent avoidable financial losses and issues the user can still act on: fees, interest charges, missed payments, insufficient funds, duplicate charges, and suspicious transactions.

If there are no immediate risks, help the user maintain financial predictability: make important upcoming payments and obligations visible, check whether they have enough money to cover them, and surface genuinely meaningful positive changes in their financial position.

## General rules

Only surface findings that are meaningful, sufficiently reliable, and useful for the user to know now.

Don't recap all of the user's financial statistics or list the results of every check you performed.

Show outcomes, not the analysis process. Don't mention empty or discarded checks, failed comparisons, or insufficient data. If there isn't enough data to support a particular conclusion, omit it, unless the lack of data is itself an important problem.

Don't show sections that contain no useful findings. The only exception is Monthly Analysis, which always gives a short high-level overview of the month when the data is sufficient, even if there are no risks or problems.

Before making any conclusion that depends on recent transactions or account balances, check the freshness of only the accounts and data used for that conclusion. If those data haven't been updated recently enough, don't make a conclusion that missing recent transactions or stale balances could distort.

An account being out of date is not, by itself, something to report. It may simply be old or no longer in use.

If a meaningful number or amount of uncategorised transactions prevents a reliable conclusion, tell the user. The existence of uncategorised transactions alone is not a meaningful signal.

Don't surface small changes, or changes that look large in percentage terms but are insignificant in absolute value.

When deciding what to surface, consider what could happen if the user doesn't learn about it now. Use this priority order:

1. The user could suffer a direct financial loss: a fee, interest charge, debt, insufficient funds, or another monetary loss.
2. The user could lose money, or lose the opportunity to fix the situation, if they don't act in time.
3. The user could miss an important obligation or event with meaningful consequences, even if they are not directly financial.
4. The information doesn't prevent a loss but materially improves the predictability of their finances.
5. There are no meaningful consequences and the finding is merely interesting statistics. Don't show it, except as part of the Monthly overview.

When there are no risks, prioritise predictability first, followed by meaningful positive developments.

Don't add positive news simply to make the brief feel complete. A positive signal must represent a real improvement, or meaningfully confirm that an important financial event went as expected.

Use the checks below as a foundation, but don't limit yourself to them. Look for other important signals when they match the goal, these rules, and the time window of the relevant analysis horizon.

## Input: delivery_cadence

When the Financial Brief runs automatically, the scheduled task passes the cadence explicitly in its run instruction:

`delivery_cadence: daily | weekly | monthly`

For example:

- `Run Financial Brief. delivery_cadence: daily`
- `Run Financial Brief. delivery_cadence: weekly`
- `Run Financial Brief. delivery_cadence: monthly`

Never infer `delivery_cadence` from the user's financial data.

If the user runs the brief manually and explicitly asks for a daily, weekly, or monthly brief, use the corresponding horizon.

If the user runs the brief manually without specifying a period and no `delivery_cadence` is provided, use Daily Analysis.

### Setting up a scheduled brief

When the user asks to receive the brief regularly, for example "Send me my daily brief every day at 9:00", set up a scheduled task at the frequency and time they asked for. Write the task's run instruction with the cadence spelled out exactly, because scheduled runs rely on it:

- every day → `Run Financial Brief. delivery_cadence: daily`
- once a week → `Run Financial Brief. delivery_cadence: weekly`
- once a month → `Run Financial Brief. delivery_cadence: monthly`

If the user doesn't name a day, schedule a weekly brief for Monday and a monthly brief for the first day of their financial month (`monthStartDay` from `get_user`). Confirm the schedule in one short sentence. If you can't create scheduled tasks in the current app, say so and offer to run the brief now.

## Horizon selection

Use the user's local date and their financial month start setting in Zenmoney.

Throughout this skill, "month" means the user's financial month, which may not be the same as a calendar month. A week runs from Monday to Sunday.

### If delivery_cadence = daily

Always run Daily Analysis.

If today is Monday, also run Weekly Analysis for the previous completed week.

If today is the first day of the user's financial month, also run Monthly Analysis for the previous completed financial month.

### If delivery_cadence = weekly

Run Weekly Analysis.

If the user's financial month ended within the last 7 days, also run Monthly Analysis for that completed financial month.

### If delivery_cadence = monthly

Run Monthly Analysis for the previous completed financial month.

If several horizons apply at the same time, combine them into a single Financial Brief.

## Analysis windows

For newly occurred events, use completed periods:

- Daily Analysis: the previous completed local day.
- Weekly Analysis: the previous completed week.
- Monthly Analysis: the previous completed financial month.

For upcoming events, use:

- Daily Analysis: today and the next 1–2 days.
- Weekly Analysis: the next 7 days.
- Monthly Analysis: the next financial month.

Use longer history only as context: to establish a normal baseline, identify recurring patterns, and detect trends. Don't use it to resurface individual events from earlier periods.

In Weekly Analysis, data from the beginning of the current financial month may be used as context for assessing the current monthly pace, but not as an additional window for discovering transactions.

When checking for expected payments that haven't appeared, you may look back to an earlier expected date to decide whether the payment is now sufficiently overdue and important to warrant attention.

Only surface an older event outside the main window if something new happened during the current window, the situation materially changed, or the event became significantly more urgent.

When estimating a potential cash shortfall, you may use later expected income and historical spending as context, but only surface the warning if the shortfall occurs within the future window of the current analysis horizon.

## Daily Analysis

Daily Analysis focuses on specific events from yesterday and near-term risks for today and the next 1–2 days.

### Yesterday's charges

Review transactions from the previous completed day for potential problems and anomalies:

- the first charge from a new subscription, or a subscription whose price has gone up;
- potentially suspicious charges, especially when a merchant that has never appeared in the user's history comes together with another anomaly: an unusual country or currency, an atypically large amount, a possible duplicate, or another unexpected transaction pattern.

Briefly explain why a transaction deserves the user's attention.

### Negative account balance

If a regular bank account or debit account has gone below zero for the first time following recent transactions, alert the user and show the current negative balance.

If the account was already overdrawn before, don't repeat the warning unless the situation has materially worsened during the current period.

### Upcoming payments

Remind the user about significant payments expected today or within the next 1–2 days.

Identify them using the user's scheduled reminders and recurring transactions in their transaction history.

Check whether there is enough money specifically in the account from which the payment is scheduled or normally charged.

When assessing available funds, also account for other expected payments from the same account within the same time window. There may be enough money for each payment individually but not for all of them together.

If there isn't enough money, warn the user and state how much is missing.

If important scheduled payments expected on the previous day went through successfully, you may use that as a positive signal.

### Cash shortfall

Assess whether the user's available funds are likely to run out within the next 1–2 days.

Use a longer spending history to establish their normal spending pace.

If a shortfall is likely within this window, warn the user, estimate when it is likely to occur, and state approximately how much they will be short.

### Expected payments that have not arrived

Look for important payments that should already have appeared but haven't, and that are now sufficiently overdue to require the user's attention.

Don't alert the user immediately after the expected date.

Take the importance of the payment into account. Loan payments, mortgage payments, taxes, and other major obligations are more important than ordinary subscriptions.

## Weekly Analysis

Weekly Analysis focuses on significant events and changes from the completed week, and on what the user should account for during the coming week.

### Charges

Review transactions from the completed week for meaningful problems and anomalies:

- the first charge from a new subscription, or a subscription whose price has gone up;
- potentially suspicious charges, especially when a merchant that has never appeared in the user's history comes together with another anomaly: an unusual country or currency, an atypically large amount, a possible duplicate, or another unexpected transaction pattern.

### Upcoming payments

Remind the user about significant payments expected during the coming week, so they can account for them in their available funds in advance.

Identify them using the user's scheduled reminders and recurring transactions in their transaction history.

Prioritise large and irregular payments.

### Cash shortfall

Assess whether the user's available funds are likely to run out within the coming week.

Use a longer spending history to establish their normal spending pace.

If a shortfall is likely within this window, warn the user, estimate when it is likely to occur, and state approximately how much they will be short.

### Significant changes

If the user's total income or spending changed materially during the completed week, explain what drove the change: for example, a specific large transaction, or one or two major categories.

Use previous weeks and the current financial month as context when deciding whether the change is meaningful.

Don't surface a simple shift between spending categories if the user's overall financial result didn't materially change.

### Expected payments that have not arrived

Check for important expected payments that became meaningfully overdue during the completed week.

Only resurface an older missing payment if there has been a meaningful new development or a significant increase in urgency.

## Monthly Analysis

Monthly Analysis gives an overall view of the completed financial month and highlights what matters for the next one.

### Monthly overview

Give the user a concise high-level overview of the completed financial month.

Show total income, total spending, and the difference between them, if the data is sufficiently complete.

If there are meaningful risks, deviations, or changes, surface those first.

If there are no such signals, still provide one or two meaningful observations that help explain what kind of month it was: what had the biggest impact on the result, how the month differed from normal, or what stood out in the structure of income and spending.

Don't turn this into a statistical report or list metrics simply because they are available.

If income or spending differs meaningfully from its normal level, compare it with several previous months and assess whether this looks like a one-off deviation or the beginning of a sustained new level.

### Charges

Review transactions from the completed financial month for meaningful problems and anomalies:

- the first charge from a new subscription, or a subscription whose price has gone up;
- potentially suspicious charges, especially when a merchant that has never appeared in the user's history comes together with another anomaly: an unusual country or currency, an atypically large amount, a possible duplicate, or another unexpected transaction pattern.

Only surface an older anomaly if the user can still act on it, it remains materially important, or it is necessary to explain the overall result for the month.

### Plan vs actual

If the user has planned categories or planned transactions in Zenmoney, compare them with the actual results for the completed financial month.

Only surface meaningful deviations that help explain the month's result or could affect the following month.

### Large upcoming payments

Remind the user about the largest irregular payments expected during the next financial month, so they can plan for them and keep enough money available.

Identify expected payments using the user's scheduled reminders and recurring transactions in their transaction history.

### Cash shortfall

Assess whether the user's available funds are likely to run out at any point during the next financial month.

Use a longer spending history to establish their normal spending pace.

If a shortfall is likely within this window, warn the user, estimate when it is likely to occur, and state approximately how much they will be short.

## Combining findings

Don't repeat the same finding across multiple horizons.

If something requires attention within a shorter horizon, surface it there. A longer horizon may use it to explain the broader picture, but shouldn't repeat it as a separate alert.

Treat **importance** and **urgency** as separate dimensions:

- Importance is determined by the consequences if the user doesn't learn about the event or fails to act on it.
- Urgency is determined by how soon the user needs to know or take action.

After the short summary, show important and urgent items affecting today and the next few days first, followed by important items for the week and month.

Don't let a large but distant event crowd out a more urgent issue that requires action now.

A longer analysis horizon does not automatically have higher priority.

## Output format

Use only one short opening summary for the entire Financial Brief, even when several analysis horizons are included.

Write the brief in the user's language, and format amounts and dates the way their locale does.

### If there is a meaningful brief

If the analysis produces meaningful signals, useful observations, or the required Monthly overview, begin with one short sentence summarising the single most important takeaway from the entire brief.

This sentence must make sense on its own and be suitable for use as a push notification.

If there is a problem or action that requires the user's attention, the summary immediately communicates the most important risk or required action.

If there are no problems, the summary briefly communicates the overall picture. Don't include an otherwise unimportant fact solely to prove that the data is fresh.

Then provide the rest of the brief.

### If there is nothing significant, but there is financial activity

If Daily or Weekly Analysis finds no meaningful signals but there are up-to-date transactions within the main completed-period window, the entire response is a single short line containing:

**a natural status update + one recent financial fact** that confirms the brief is working with current data.

The financial fact is required. Don't respond with only a generic statement that everything looks fine.

Phrase the status naturally rather than using the same fixed opening every time.

If several horizons are being analysed, look for the supporting fact in the shortest applicable horizon first: Daily → Weekly → Monthly.

Prefer a fact that is easy to recognise and reliably supported by the data, such as a notable incoming payment, a transfer to savings, a successfully completed important payment, a meaningful charge, or another relevant event from the current period.

### If there were no transactions during the period

If there is no meaningful brief and the main completed-period window contains neither actual nor expected scheduled transactions, first check the freshness of the relevant accounts.

If the relevant accounts are up to date, briefly state that there were no actual or scheduled transactions during the relevant period. Name the specific period for the current horizon, such as the previous day or the completed week.

In this case, no activity is a valid result, because data freshness has been confirmed.

### If data freshness cannot be confirmed

If the relevant bank accounts haven't synced recently enough to build a reliable brief, don't conclude that there were no transactions or risks.

Briefly state that the freshness of the data can't be confirmed and suggest refreshing the bank data in Zenmoney.

If some relevant accounts are current and others are not, don't claim there was no activity overall if the stale accounts could materially change that conclusion.

Insufficient data for one individual check is not a reason to cancel the entire brief. Skip that particular conclusion and continue analysing the remaining data that is sufficiently current.

### Remaining formatting rules

For Monthly Analysis, there is always a meaningful brief when enough data is available to produce the required overview.

Don't expose internal checks, discarded findings, or other implementation details.

For the rest of the brief:

- don't show empty sections;
- normally include only a small number of the most important findings;
- use specific amounts, dates, categories, and merchant names when they help explain the situation;
- avoid numbers that don't change the conclusion;
- if the user needs to take action, tell them clearly what to do;
- if no action is needed, don't invent a recommendation simply for the sake of having one.

## Getting the data from Zenmoney

This section is for you, not for the brief: none of it should appear in the output.

### Dates and settings

- Call `get_user` for the main currency and `monthStartDay`. Financial months start on `monthStartDay`, so with a start day of 10 the "first day of the financial month" is the 10th, and the completed month runs from the 10th of the previous month to the 9th of this one.
- Take the user's local date from the run context. A scheduled run's "yesterday" is the user's local yesterday.

### Data freshness

Judge each account by its own rhythm: compare the date of its latest transaction (`list_transactions` filtered by its `accountIds`) with how often it normally has transactions. An everyday card that usually has several transactions a day but nothing for three days is probably not synced; a savings account with no activity for a month is probably just quiet. If an account's data carries a sync or update timestamp, prefer that.

### Transactions

- `list_transactions` for the window, with `limit: 200`, paging with `cursor` until `nextCursor` is null. Never draw a conclusion from a partial result.
- Amounts are in each account's own currency. Convert to the main currency with `get_instrument_rates` (amount × source currency's RUB rate ÷ main currency's RUB rate) before comparing or adding amounts in different currencies.
- Identify merchants by `merchantId`, not by name. Transfers between the user's own accounts are not income or spending.
- Results can include holds and future-dated operations. A hold followed by its settled charge can look like a duplicate; check before calling it one.

### Anomaly checks

A merchant the user has never paid before is not a signal on its own: people try new places all the time. It is the strongest reason to flag a charge when it comes together with one of the anomalies below. Other clearly suspicious charges still count.

- **New merchant**: check whether the merchant appears in the user's history before the window (`list_transactions` with its `merchantIds` over the previous 12 months, `limit: 1`). For a transaction without a merchant, compare its payee text with earlier transactions.
- **Unusual country or currency**: an `originalInstrument` the user rarely pays in, or a merchant from a country they don't usually pay in.
- **Atypically large amount**: large compared with the user's usual transactions at that merchant or in that category, and large in absolute terms.
- **Possible duplicate**: same merchant, same amount, same account, on the same or an adjacent day, when the merchant isn't one the user legitimately pays several times a day.
- **Other unexpected pattern**: anything out of character for the user, such as a burst of charges at one merchant in a short time.
- **New subscription or price increase**: a first charge from a merchant that then looks recurring or matches a scheduled template, or a recurring merchant charging more than its previous regular amount.

### Balances and accounts

- `list_accounts` gives current balances, types, `creditLimit`, `isSavings`, and archived status. Ignore archived accounts unless one is directly involved in a finding.
- **Regular bank or debit account** for the negative-balance check: type `card` or `checking` with no credit limit, not a loan, deposit, or debt account.
- **First time below zero**: compare the balance at the end of the day before the window (`get_account_balances` with `boundary: "end"`) with the current one.
- **Spendable funds** for shortfall estimates: non-archived accounts with `isInBalance` true, of type `cash`, `card`, `checking`, or `emoney`, and not `isSavings`.

### Upcoming and missing payments

- Scheduled reminders: `list_scheduled_transactions` from today to the end of the future window with `state: "planned"` and `order: "asc"`. Planned occurrences dated before today are overdue.
- Recurring payments from history: merchants charged at a regular interval with a stable amount whose next expected date falls in the window and that aren't already in the scheduled list.
- `processed` on a scheduled occurrence doesn't prove it was paid. To confirm that an important payment went through, find the matching actual transaction: same account, similar amount, within a day or two of the expected date.
- Coverage of an account: its current balance (plus unused credit limit for credit accounts), minus every expected payment from that account in the window. Count expected income only if it is scheduled to arrive before the payment.

### Cash shortfall

Project spendable funds day by day through the future window: current balances, plus expected income, minus expected payments, minus the user's normal daily spending. Estimate normal daily spending from a longer history, for example the last three complete financial months, excluding scheduled and recurring payments so they aren't counted twice.

### Monthly totals and plan vs actual

Use `get_monthly_report` so totals match the app. Request the completed month and several months before it in one call (up to 24 months).

- Use `factWithRefund` for actuals; refunds are already applied.
- Overall income and spending come from the `TagTotal` rows; never add child rows to their parents.
- Leave transfers and `EXCHANGE_DIFF` out of income and spending.
- Budgets and planned amounts in the same report are the plan; compare them with actuals but never add them to actuals.
