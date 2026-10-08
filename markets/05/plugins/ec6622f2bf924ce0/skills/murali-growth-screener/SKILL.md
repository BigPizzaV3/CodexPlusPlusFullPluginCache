---
name: murali-growth-screener
description: Run the Murali Growth Fund v3.0 institutional stock screener using current market, fundamental, technical, catalyst, earnings, valuation, risk, and accessible public-forum evidence. Use when the user asks to screen stocks, find compelling or “screaming” buys, rank opportunities across sectors, check what to buy today, research Reddit/X/Stocktwits/Discord sentiment, or reassess an existing holding or watchlist. Support concise mobile prompts and portfolio-aware screening when a connected brokerage account is available.
---

# Murali Growth Screener

Run a current, evidence-based growth-stock screen. Rank genuine opportunities and explicitly return “no qualifying buy” when none clears the standard.

Read [references/policy.md](references/policy.md) before scoring candidates or recommending an action.

## Interpret the request

- Treat “run the screener,” “find buys,” or “go” as research and reporting only.
- Do not place, replace, or cancel an order unless the current user request explicitly asks for execution.
- If execution is requested, use only an account clearly specified or already established in the conversation. Follow broker review, confirmation, permission, and idempotency requirements.
- Default to a broad US-listed stock and ETF screen when the user supplies no universe.
- Use the connected portfolio, when available, to evaluate cash, overlap, concentration, and position fit. Do not require a brokerage connection for a market-only screen.

## Run the screen

1. Establish the current timestamp, trading session, and data freshness.
2. Classify the market regime as bullish, neutral, or defensive using broad-index trend, breadth, volatility, rates/liquidity, macro conditions, and sector rotation.
3. Scan across technology, semiconductors, communication services, healthcare, industrials, financials, consumer, energy/utilities, and high-quality small caps. Do not return a technology-only list unless it objectively dominates.
4. Gather current quotes, spreads, liquidity, 52-week context, valuation, recent financial results, guidance, earnings timing, catalysts, analyst revisions when accessible, and relevant official filings or company releases.
5. Calculate or retrieve at least the 50-day and 200-day moving averages, RSI, MACD, volume context, and a volatility/risk measure. Avoid chasing extended moves.
6. Search accessible public Reddit, X/Twitter, Stocktwits, public Discord content, and other forums. Use them only for leads and sentiment confirmation. Disclose inaccessible or authentication-gated sources.
7. Trace material social claims to primary sources. Reject rumors, coordinated promotion, low-float manipulation, selective screenshots, and unsupported “insider” claims.
8. Score the best candidates using the policy. A missing material data category lowers confidence; it never earns assumed points.
9. Compare qualifying candidates with existing holdings and cash. Prefer the best risk-adjusted portfolio fit, not the loudest ticker.
10. If execution is explicitly requested, refresh account, quote, spread, market state, position, orders, buying power, catalyst, and risk data immediately before broker review. Never infer a fill.

## Report concisely

Lead with one of:

- `QUALIFYING BUY`
- `WATCHLIST ONLY`
- `NO QUALIFYING BUY`

Then provide:

- Market regime and timestamp
- Ranked candidates with score, current price, thesis, catalyst, valuation context, technical confirmation, invalidation, and main risk
- Existing-position decision when portfolio data is available
- Sources used and inaccessible requested sources
- Order-review and fill status only when execution was explicitly requested

For mobile use, keep the first screen compact. Offer deeper research only after presenting the decision.

Never describe a candidate as a “screaming buy” unless it scores at least 90, has no hard-check failure, and offers acceptable risk/reward at the actual current price.
