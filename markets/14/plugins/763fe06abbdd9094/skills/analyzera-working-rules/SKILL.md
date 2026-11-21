---
name: analyzera-working-rules
description: Rules for any conversation that uses the Analyzera connector, for the client's accounts, strategies, funds, stocks, risk levels, expected returns, backtests or savings plans. Use whenever reporting Analyzera figures, saving or backtesting a strategy, or when the client asks whether something suits them.
---

# Working with Analyzera

## No advice

Analyzera builds what the client specifies. Nothing in it reads a client profile,
suitability assessment or compliance record, and a risk level is a construction
target, not a judgement about what suits anyone. Present alternatives unranked
and recommend none. Asked whether something is suitable, say plainly that
Analyzera does not answer that.

## Ask, do not infer

Personal numbers, horizons, which funds, and which listing of a company all come
from the client. When a match is partial or two listings are similar, ask before
building on it. When a tool is not on the client's plan or its allowance is used
up, say so rather than retrying.

## Saving and backtesting

- Reads are free. Builds, edits and backtests save to a shared production
  database: say so before calling them.
- Stay unsaved while the client explores. The `describe_portfolio_*` reads and
  `describe_holdings` take holdings directly, so nothing needs saving to be
  measured.
- An edit replaces the whole definition. Call `get_strategy_definition` first,
  restate every argument, and change only what was asked.
- Backtest only when the client asks for past returns. It runs in the
  background: follow it with `get_backtest_status`, and when it is done open the
  strategy on the returns tab.

## Ids

Take ids from `list_portfolios`, `find_portfolios`, `find_assets` or a build's
result. Never pass names or ISINs, which can land on another listing. Accounts
and strategies share one numbering, so their id fits any `*_id` argument.

## Reporting results

- Answer in the client's language and keep every number as given.
- An account is money the client holds; a strategy is a construction. Never
  describe a strategy as something they hold.
- The 0-10 risk level is Analyzera's own scale, not the 1-7 risk indicator on
  fund fact sheets. Say so when the client may compare the two.
- A projected return is a modelled long-run average, per annum, meaningful only
  over ten years or more, and not a track record. Quote it with its horizon and
  ranges, never as grounds for a short-term decision.
- Screens, weightings, previews and scenarios save nothing and have no track
  record: say so, and never describe how one would have performed.
- A summary lists the largest lines only: do not state what the rest holds.
- Relay every note, unmatched instrument and caveat a result carries. An import
  with unmatched lines is an incomplete figure, never the account balance.
- Asked how a figure is calculated, use `describe_methodology`.

## Cards

Where the dashboard or screener card is drawn, what it shows never reaches you:
do not describe its charts, complete its tables, or restate what it already
shows. A list from the screener card counts only once the card sends it to the
chat.

## Feedback

The team reads every report, so offer `send_feedback` whenever one of these
comes up, without waiting to be asked:

- **Something looks wrong**, to the client or to you: a figure that is
  implausible or contradicts another, a tool error, a refusal that should not
  have happened, data that is missing or stale, a card that fails to draw or
  shows something odd. Say so plainly first. Categories: `wrong_number`,
  `wrong_refusal`, `missing_data`, `bug`.
- **The client wants something the tools do not do**: a measure, a market, a
  chart, an action. Say it is not available, then offer to pass the wish on as
  a `suggestion`.

Agree the wording first and give them the reference it returns.
