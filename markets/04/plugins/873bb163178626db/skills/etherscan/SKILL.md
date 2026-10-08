---
name: etherscan
description: >-
  Use Etherscan's hosted MCP tools to inspect public EVM blockchain data. Use
  for wallet balances and activity, token transfers and holders, transaction
  details or status, contract source and ABI, event logs, blocks, gas, address
  labels, funding sources, and supported-chain discovery.
---

# Etherscan MCP

Use the connected `etherscan` MCP server as the live authority. The server is
hosted at `https://mcp-keyless.etherscan.io/mcp`, is read-only, and requires no API key.
Do not ask the user for a key.

## Workflow

### Interactive Etherscan UI fast path

When the user asks for an interactive Etherscan view, dashboard, card, or
visual result, `render_etherscan_widget` is the complete visualization path.
Do not invoke, inspect, or compose a general visualization skill or a separate
visualization tool. Retrieve only the requested Etherscan facts, then call
`render_etherscan_widget` immediately; do not perform additional analysis or
presentation work between the final data result and the render call.

1. Inspect the currently advertised Etherscan tools and their schemas. Do not
   assume that a documented tool is still available.
2. Identify the target type: address, transaction hash, token contract,
   contract, block, timestamp, or event topic.
3. When the user does not specify a chain, use Ethereum Mainnet (`chainid`
   `"1"`) and state that default briefly. Never guess another chain from the
   first activity found, and never probe or scan multiple chains automatically.
   Use `get_supported_chains` only when the user names a chain but its numeric
   chain ID or Etherscan support is unknown; do not infer support from EVM
   compatibility. Query multiple chains only when the user explicitly asks for
   multichain results.
4. Call the narrowest matching data tool. Optimize for a fast first result:
   do not fetch holdings, transaction history, labels, funding sources, or
   charts merely to decorate a wallet balance response. Use conservative
   pagination when the user actually requests an activity list, and say when
   the result is truncated or paginated.
5. Unless the user requests plain JSON or text only, call
   `render_etherscan_widget` immediately after the minimum data needed for the
   answer is available. Copy only facts present in tool results. For a basic
   wallet request, a balance-only widget is complete; wallet activity and token
   holdings are optional and must not be fetched unless the user asks for them
   or they are necessary to answer the question. Put the primary value first
   in `metrics`; use `sections` with `cards` for requested holdings or summary
   groups, `rows` for requested activity, and `chips` for short tags. Include
   `chart` only when the user needs a trend and every point came from a live
   tool response.
6. After the widget call, explain the returned facts briefly in plain language.
   Preserve addresses, hashes, amounts, status values, timestamps, and API
   errors exactly enough for the user to verify them.

## Presentation rules

- Never invent security scores, risk labels, historical prices, forecasts,
  labels, identities, or audit conclusions.
- Never claim that an address owns an identity unless Etherscan returned that
  label or the user supplied it.
- State units explicitly. Convert Wei or Unix timestamps only when the
  conversion is deterministic, and retain the original value when useful.
- Add an explorer URL to the widget only when the correct explorer host for the
  selected chain is known from live Etherscan data or the user supplied it.
- Treat an empty result as "no records returned for this query," not proof that
  no activity exists outside the requested range or supported data surface.
- Never synthesize chart points from only a current value or a start/end value.

## Boundaries

The MCP server cannot sign or broadcast transactions, verify contracts, manage
API keys, or change blockchain or Etherscan state. If a user asks for a write,
explain this boundary and offer a read-only inspection that helps them prepare
or verify the action.

Keep transport failures, schema validation failures, and Etherscan API errors
distinct. Do not retry repeatedly when the server reports throttling or a plan
restriction. If a throttling error includes `retryAfter`, `rateLimitReset`, or
other rate-limit details, report the available retry timing rather than
guessing one.
