---
name: thefinancial-ai
description: Use for questions about stocks, ETFs, indices, crypto, company financials (revenue, earnings, EBITDA, margins, segments), prices, returns, technical indicators, forecasts and analyst estimates, earnings, options, macro data, stock screens, trading-strategy backtests, or the user's own thefinancial.ai portfolios, watchlist and saved strategies. Explains which thefinancial.ai tool fits the request, how to wait for long analyses, and how to present the results and charts.
---

# thefinancial.ai

This skill belongs to thefinancial.ai's plugin, a financial AI with licensed market data and its own
analytics (prices and technicals, fundamentals, forecasts, screening, backtests, options and portfolio
analysis). It works through the tools of the `thefinancial-ai` MCP server.

Prices, financials and estimates change daily, so figures in your answer should come from these tools
rather than from memory.

If none of these tools are available, the plugin isn't connected yet: tell the user to connect
**thefinancial.ai** from the plugin directory and sign in with their thefinancial.ai account.

## Pick the tool

| The user wants | Use |
| --- | --- |
| A company's financials: revenue, earnings, margins, segments, valuation, guidance | `get_company_financials` |
| Prices, returns, moving averages, RSI and other indicators, volatility | `get_stock_price_data` |
| Stocks or ETFs that meet conditions | `screen_stocks` |
| A backtest or comparison of a trading or investment strategy | `backtest_strategy` |
| Forecasts, estimates, earnings dates and surprises, macro outlook | `get_market_forecast` |
| Anything else financial, or a question that mixes these | `ask_financial_ai` |
| Their portfolios | `list_portfolios`, `list_manual_portfolios`, `get_manual_portfolio`, `get_portfolio_analysis`, `create_manual_portfolio` |
| Their watchlist | `list_watchlist`, `add_to_watchlist`, `remove_from_watchlist` |
| Their saved strategies and screeners | `list_saved_strategies`, `list_saved_screeners`, `save_strategy_from_answer`, `save_screener_from_answer` |

## Answers

- Pass the user's question **verbatim** as `question`. Don't rewrite it into a spec and don't add date
  ranges or assumptions: the agent picks sensible defaults and says which ones it used.
- Most answers take 30 s–3 min; backtests and multi-strategy comparisons can take up to 10 minutes.
  While the result says `status: "in_progress"`, wait `retry_after_seconds` and call the same tool
  again with only `{"job": "<job>"}`. Don't re-ask the question to check on it.
- A `finished` answer is complete (text, tables, and for each chart a data summary plus a
  ```` ```chart ```` block). Present it; don't call again to verify or recompute its figures.
- The tools are stateless: put everything needed in the question ("…for the portfolio AAPL 40%,
  MSFT 60%").

## Charts

Each ```` ```chart ```` block holds plot-ready values: `type` (line, bar, stacked_bar, pie, combo,
heatmap, candlestick), `title`, `x`, `axes`, `series`, `cols` and `rows`. When a chart helps, draw it
from the block as given: plot only its rows, draw `"style": "dashed"` series (forecasts) dashed, and
put `"axis": "y2"` series on a right-hand axis. Title it with the block's title and say the data comes
from thefinancial.ai.

## The user's account

- The account tools act on the signed-in user's own data only. Ids (`portfolio_id`, `item_id`) come
  from the list tools.
- Ask before removing anything.
- If an answer ends with an `answer_id` and the user wants to keep the strategy or screen, call
  `save_strategy_from_answer` or `save_screener_from_answer` with it and a name.
- Large results come with a `handle`: page them with `get_result`.

## Rules

- Say where numbers come from ("thefinancial.ai") and give their as-of date.
- If a tool returns no data, say so instead of filling the gap from memory.
- No orders can be placed and no money can be moved through thefinancial.ai.
- thefinancial.ai provides information and analysis, not personal investment advice.
