---
name: developer-support
description: Help developers build on the Solana Tracker Data API, Solana RPC, Datastream WebSockets and Yellowstone gRPC. Find the right endpoint or RPC method, write working code from the official docs, debug API errors and failed transactions, and check service status. Use when the user is writing code against Solana Tracker or asks how an endpoint, method, rate limit or error works.
---

# Solana Tracker developer support

Use this workflow when someone is building with Solana Tracker's APIs or Solana RPC.

## Answer "how do I…" questions

1. Call `search_docs` with the user's goal (for example "wallet token accounts", "live price websocket", "getPriorityFeeEstimate"). Add `product` when it's clear (data-api, solana-rpc, datastream, yellowstone-grpc, raptor, prediction-markets).
2. Call `fetch_doc` on the best match. For endpoint and RPC method pages, use its structured `reference` (exact endpoint URL, authentication, parameters with types and allowed values, request and response fields, examples, error codes) instead of relying on memory. For long guides, read the relevant part with the `section` input.
3. Answer with a short explanation, a runnable example in the user's language (default: TypeScript with `fetch`, or `curl`), and the doc link.

When writing code:
- Put API keys in environment variables such as `SOLANA_TRACKER_API_KEY` or `SOLANA_RPC_API_KEY`, and use placeholders. Never ask the user to paste a key and never repeat one they paste; tell them to rotate a key that was shared in chat.
- Data API: header `x-api-key`. Solana RPC: `https://rpc-mainnet.solanatracker.io/?api_key=...`. Note that some doc pages show an older `rpc-data` hostname; use `rpc-mainnet`. Confirm details in the docs page you fetched.
- Prefer credit-efficient options the docs recommend, such as the V2 RPC queries (`getTokenAccountsByOwnerV2`, `getProgramAccountsV2`), batch endpoints and WebSocket streams instead of polling.
- Handle HTTP 429 with exponential backoff and jitter, and check JSON-RPC `error` objects, which arrive with HTTP 200.

## Debug errors

1. Call `troubleshoot_api_error` with the product, HTTP status, JSON-RPC code and the message (with any secrets removed).
2. If the error is about a transaction:
   - Already sent and the user has the signature: call `get_transaction` for its status, error and logs, and `get_transaction_status` to see whether it landed.
   - Not sent yet, or the user can share the serialized transaction (base64 or base58): call `simulate_transaction`. It dry-runs on the RPC node and never submits, then reports the failing program, logs, compute units and likely fixes.
3. If several requests fail at once, call `get_service_status` to check for an incident.
4. Explain the most likely cause first, then the fix, with a corrected code snippet when useful.

## Live chain checks

To confirm what code should return, use the read-only RPC tools: `get_sol_balance`, `get_wallet_token_accounts`, `get_account_info`, `get_address_transactions`, `get_network_status`, `get_priority_fee_estimate`, `resolve_sol_domain` and `get_wallet_sol_domains`.

## Limits

- The plugin can't read the user's Solana Tracker account, credits, usage or keys; point them to their dashboard for that.
- Don't discuss plan prices or suggest upgrades. If a limit depends on the plan, say so and link the docs page that lists limits.
- The plugin never sends transactions or executes swaps. You can explain how Solana Tracker's swap or sendTransaction APIs work from the docs, but the user runs that code themselves.
