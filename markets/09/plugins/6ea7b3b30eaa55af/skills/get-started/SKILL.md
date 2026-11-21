---
name: get-started
description: Introduce Solana Tracker and show the user what they can ask about Solana tokens, wallets and the memecoin market.
---

# Get started with Solana Tracker

Briefly explain that Solana Tracker gives live, read-only Solana data inside the conversation: market analytics, on-chain RPC reads, and developer help for the Solana Tracker APIs. It cannot trade, swap, send transactions, transfer funds or access private keys or API keys.

Offer three or four things the user can try, adapted to what they seem interested in:

1. **Check a token** – "What's the price and risk score of BONK?" (uses `search_tokens`, then `get_token_overview`).
2. **Analyze a wallet** – "How profitable is wallet `<address>`?" (uses `get_wallet_pnl_summary` and `get_wallet_positions`).
3. **Follow the market** – "What's trending on Solana in the last hour?" or "What are KOLs buying?" (uses `list_trending_tokens` or `get_kol_trades`).
4. **Build or debug** – "How do I stream live prices with Solana Tracker?", "Why did transaction `<signature>` fail?" or "Is the Solana Tracker RPC up?" (uses `search_docs` and `fetch_doc`, `get_transaction`, or `get_service_status`).

If the user already asked a concrete question, skip the tour and answer it directly.

Keep the introduction to a few sentences. Remind the user once that the data is informational and not financial advice.
