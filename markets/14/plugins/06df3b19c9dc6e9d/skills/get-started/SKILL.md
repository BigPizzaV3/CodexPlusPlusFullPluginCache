---
name: get-started
description: Answer questions about a Pimlico account and change its API keys and gas sponsorship policies with the Pimlico tools — balance and invoices, usage, failed user operations, API keys, sponsorship policies, supported chains and ERC-20 paymaster tokens.
---

# Pimlico account

Pimlico is infrastructure for smart accounts (ERC-4337 and EIP-7702): a bundler, a paymaster that sponsors gas, and the same on Solana. These tools read and change the settings of the Pimlico account the user connected. They do not sign transactions, move funds or send tokens.

## Which tool answers what

| Question | Tools |
| --- | --- |
| Which account and organization is connected | `pimlico_whoami` |
| Balance, unbilled usage, invoices | `pimlico_balance`, `pimlico_invoices` |
| Requests, API credits and sponsored gas over a period, by chain, key or day | `pimlico_usage` |
| Why a user operation failed | `pimlico_op` for one hash, `pimlico_ops` for recent operations |
| Operations rejected before they reached the chain | `pimlico_requests` (failed `eth_sendUserOperation` and `pm_*` calls) |
| Solana transactions | `pimlico_solana_txs` |
| API keys | `pimlico_keys_list`, `pimlico_keys_get`, `pimlico_keys_create`, `pimlico_keys_rename`, `pimlico_keys_disable` |
| Sponsorship policies | `pimlico_policies_list`, `pimlico_policies_get`, `pimlico_policies_create`, `pimlico_policies_update`, `pimlico_policies_enable`, `pimlico_policies_disable` |
| Supported chains and ERC-20 paymaster tokens | `pimlico_chains`, `pimlico_erc20_tokens` |

## Facts that shape the answers

- Chains are identified by chain ID. `pimlico_chains` maps names such as "Base Sepolia" to IDs (84532).
- A new API key's secret appears only once, in the result of `pimlico_keys_create`. Existing secrets are never returned.
- Policy caps are in USD, not in the chain's native token.
- Disabling keys or policies and reading billing require the organization admin role; other members get a FORBIDDEN error.
- Usage figures come from hourly aggregates and lag by one to two hours.
- If `warnings` in a result is non-empty, the account has open invoices.

## Example requests

- "Why did my user operations on Base Sepolia fail in the last 24 hours?"
- "Create a sponsorship policy on Base Sepolia with a $20 total budget."
- "What is my balance, and do I have unpaid invoices?"
