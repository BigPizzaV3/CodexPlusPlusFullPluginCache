---
name: token-research
description: Research a crypto token, wallet or chain with Unhosted's live on-chain tools — risk and momentum, AI prediction reports, movers, head-to-head comparisons and smart-money flow. Use when the user asks whether a token is risky or moving, what Unhosted predicts for it, what is trending on a chain, how tokens compare, or who is buying.
---

Use this skill for research questions about specific crypto tokens, wallets or a chain's market.

1. Identify the token by contract address and chain. If the user gives only a name or ticker, call `find_token_predictions` first and use the address and chain it returns. If several tokens share the ticker, ask which one the user means instead of guessing.
2. Pick the tool for the question:
   - Unhosted's forecast or report for a token: `get_token_prediction` (after `find_token_predictions` when needed).
   - Is it risky, is it moving, is it worth a closer look: `get_token_intel`.
   - What is moving on a chain: `get_market_movers`. Is the market risk-on or risk-off: `get_market_regime`.
   - Several tokens against each other: `compare_tokens`, with 2 to 8 addresses on one chain.
   - Who is buying a token: `get_smart_money_flow`. How good a wallet is: `get_wallet`. A top trader's profile: `get_leader_dossier`. A Polymarket trader: `get_polymarket_trader`.
3. Pass `chain` on every call: `eth`, `base`, `bsc` or `solana` (the prediction tools also cover Robinhood Chain).
4. Summarize the result in a few sentences, and share the report link when the tool returns one.
5. When a tool says a daily limit is reached, or that a tool is not included in the user's plan, relay that message as written. Do not retry the tool and do not suggest workarounds.

Never present results as financial advice, never promise returns, and never imply the plugin can trade, swap, transfer funds or connect to a wallet: it cannot. The user's explicit instructions take priority over this skill.
