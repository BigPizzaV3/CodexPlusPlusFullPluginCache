---
name: token-due-diligence
description: Produce a structured due-diligence report on a Solana token covering market data, safety signals, holder concentration, developer history and smart-money activity. Use when the user asks whether a token is safe, legit, a rug, or worth researching.
---

# Solana token due diligence

Use this workflow when the user wants a thorough check of a Solana token.

## Steps

1. **Resolve the token.** If you only have a name or symbol, call `search_tokens`. Many tokens reuse popular symbols; prefer the match with the highest liquidity and tell the user which mint you picked. Ask them to confirm if two or more candidates look plausible.
2. **Profile.** Call `get_token_overview` with the mint.
3. **Holders.** Call `get_token_holders` (limit 20). Note holders labeled as liquidity pools, exchanges or the developer so they are not mistaken for whales.
4. **Developer history.** If the overview has a `creator`, call `get_tokens_by_deployer` to see how many other tokens that wallet launched and how they fared.
5. **Activity.** Call `get_token_trading_stats` for buy/sell pressure. Optionally call `get_kol_trades` with the token to see if known traders are involved.

## Report format

- **Snapshot:** price, market cap, liquidity, 24h volume, holders, age, primary market.
- **Safety signals:** risk score (0 = lowest, 10 = highest) and each warning; mint and freeze authority (null means revoked); LP burn; top-10 holder share; developer, sniper, insider and bundler holdings.
- **Holders:** the largest non-pool holders and anything unusual.
- **Developer track record:** number of prior launches and notable outcomes.
- **Trading activity:** buyers vs sellers and volume trend.
- **Summary:** 2-3 neutral sentences on the main risks and positives.

Stay factual. Do not tell the user to buy or sell, do not predict prices, and state that the risk score is a heuristic and not financial advice. Include the Solana Tracker link for the token.
