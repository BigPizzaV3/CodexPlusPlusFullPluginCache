---
name: backtest-translation
description: Turn a strategy described in plain language into backtest conditions, run it, and explain the result against buy-and-hold. Use when the user describes an indicator rule ("buy when RSI is oversold", "golden cross", "Bollinger bounce") and wants to know how it would have done.
---

# Backtest a strategy described in words

## 1. Translate the rule

Map the user's words to `backtest_signal_strategy` conditions and state the mapping before calling:

- "Oversold" or "dip" with RSI → RSI(14) below 30; "overbought" → above 70, unless the user gave numbers.
- "Golden cross" → 50-day moving average crosses above the 200-day; "death cross" → the reverse.
- "MACD cross" → MACD line crosses its signal line.
- "Bollinger bounce" → close below the lower band to enter, above the middle band to exit.

Use the coins and period the user named. Default to 180 days if they gave none. The tool accepts one to three coins and 30 to 365 days. If the user asks for more, say so and run the nearest valid request.

## 2. Run and report

Call `backtest_signal_strategy`. Report total and annualized return, max drawdown, Sharpe, win rate, number of trades and profit factor, then the buy-and-hold and BTC benchmarks side by side.

## 3. Interpret honestly

- Fewer than five trades means the sample is too small to draw a conclusion. Say so.
- If the strategy trails buy-and-hold, say that holding would have done better over this window.
- Daily candles cannot test intraday rules, order-book effects or leverage.

State that past performance does not predict future results.

End with: "These are analysis tools, not financial advice."
