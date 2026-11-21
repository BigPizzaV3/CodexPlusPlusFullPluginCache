---
name: build-and-backtest-a-prediction-market-bot
description: Use when a user asks to turn their own prediction market rules into a simulation-only bot draft, run a historical Turbine backtest, or explain and compare simulated results.
---

# Build and backtest a prediction market bot

This workflow creates simulation-only strategy drafts and evaluates historical results. No automatic trading or bot execution is available. Use TurbineFi MCP for supported draft and backtest operations. Read the complete named tools and input schemas published by the connected server before calling them. Each operation must already be exposed as its own tool; do not use discovery or a generic executor to enable hidden operations. Never invent tool names, argument fields, supported markets, or results.

## Execution boundary

No automatic trade execution is available in this skill or its connected MCP tool catalog. It cannot place orders, deploy or activate live or paper bots, change an active runner, transfer funds, or schedule autonomous trading. Historical backtests compute simulated outcomes; they do not send orders to a venue.

Draft saving, historical backtesting, and research jobs are permitted data operations, not financial transactions. Do not call any execution tool automatically. The user must explicitly approve the exact returned preview before each protected operation; a general request to build or backtest is not that approval. Read-only inspection of existing activity cannot control a runner. Never treat a confirmation token as permission by itself.

## Scope

Build only from rules the user supplies or explicitly chooses for a simulation. Explain the mechanics of those rules and their limitations. Do not prescribe trades, recommend markets to buy, select a personalized investment strategy, or recommend a live capital allocation. Historical comparisons evaluate the simulation and its assumptions; they do not determine suitability for real-money trading.

Do not place orders, deploy or activate a bot or runner, alter an active strategy, initiate real-time paper-trading deployments, transfer money, configure venue accounts or credentials, or guide funding. Deployment controls are disabled in the MCP server, including rejection of previously issued deployment confirmations. Do not try another tool, endpoint, script, schedule, or credential flow to bypass this restriction.

If a user requests live execution, explain that it is outside this simulation workflow. Do not provide an alternative path that executes the same transaction. Do not bypass account eligibility, age requirements, membership rules, or other service restrictions.

## Connect and locate the draft

Use the host's supported OAuth connection flow for https://api.turbinefi.com/api/v1/mcp. The user authenticates directly on TurbineFi; never request passwords, tokens, API keys, private keys, or seed phrases in chat. If access is unavailable, say which work remains unverified.

Use bounded server-side searches and cursor pagination to locate the requested draft or backtest. Read only the resources needed for the user's task. Do not fetch the entire account history, strategy library, live positions, wallet balances, or deployment state for an unrelated backtest request.

Use actual returned resource IDs. If a saved draft is deployed or its active status is uncertain, do not overwrite it. Create a separate simulation draft through a supported operation that cannot affect an active bot. Stop if that separation cannot be established.

## Specify and save the simulation

Capture the user's chosen market scope, signal inputs and timing, entry and exit rules, settlement assumptions, simulated position size, fees, and historical window. Ask only for missing choices that materially affect the test. Label assumptions and hypothetical balances clearly.

Check supported fields and data sources against current Turbine documentation and tool schemas. Save or revise only an undeployed simulation draft. Read the saved rules back and compare them with the user's specification before starting a backtest.

## Preview protected simulation actions

Every operation has a dedicated preview tool and execution tool. Use only the named tools already present in the server's published catalog:

| Operation | Preview tool and required inputs | Execution tool |
| --- | --- | --- |
| Create a simulation draft | `preview_create_strategy`: `platform`, `message` | `create_strategy` |
| Revise an undeployed simulation draft | `preview_update_strategy`: `session_id`, `message` | `update_strategy` |
| Copy an owned session | `preview_copy_session`: `session_id` | `copy_session` |
| Copy a published strategy selected by the user | `preview_copy_shared_strategy`: `strategy_id` | `copy_shared_strategy` |
| Delete an owned draft when requested | `preview_delete_strategy`: `session_id` | `delete_strategy` |
| Run a historical simulation | `preview_start_backtest`: `session_id` | `start_backtest` |
| Save a research draft when requested | `preview_create_research`: `market_type`, `thesis`, `base_dsl` | `create_research` |
| Run research on a selected report | `preview_start_research`: `report_id` | `start_research` |
| Cancel research when requested | `preview_cancel_research`: `report_id` | `cancel_research` |

Pass each preview tool its exact documented fields, without an action selector or unstructured parameters envelope. Backtest previews also support `period_days`, RFC3339 `end_time`, simulated `starting_balance`, simulated `starting_account`, and `runtime_limits`. Research drafts support Kalshi crypto or weather markets, with optional `venue` and numeric `sweep_dims`. Consult the published schema for supported values; never invent fields.

Show the preview's exact parameters, summary, warnings, and affected resource versions. Obtain the user's explicit approval of that specific preview. Then call only the matching execution tool with `confirmation_token` from that preview; execution tools accept no replacement parameters. A token for another operation is rejected without being consumed. Never route a token to a different tool or fall back to a generic executor. If the expected named tool is unavailable, report the missing server update and stop that operation.

Verify that the preview contains no deployment, activation, live-strategy update, order placement, or money movement. Decline a preview that mixes a simulation request with one of those actions.

A token expires after five minutes. If it expires or the parameters or resources change, obtain a fresh preview and approval. Reconcile an ambiguous response by reading the saved draft or job before retrying.

## Run and explain the backtest

Start a historical backtest only for the verified simulation draft. Read its returned job ID, poll according to server guidance, and retrieve completed results. Do not treat pending jobs as successful or restart them merely because they take time. Report failures and unsupported periods explicitly.

Explain the actual data window, sample size, simulated trade count, PnL, drawdown, fee assumptions, spread, slippage, and fill model where returned. Mark missing metrics as unavailable. Examine look-ahead bias, stale signals, selection bias, settlement mismatch, liquidity assumptions, and dependence on outliers. Historical simulation cannot establish future returns.

## Compare user-selected variants

When requested, compare a baseline with user-selected parameter variants using matching periods, datasets, and simulation settings where supported. Preserve the original draft. Discuss sensitivity and uncertainty without choosing an investment for the user or presenting the strongest historical result as a live recommendation.

## Deliver the result

Return the saved simulation rules and identifier, historical window, completed results, execution assumptions, and limitations. Use result links only when returned by the server. Distinguish tested evidence from assumptions. End with the simulation's outcome or a specific missing input; do not transition to deployment or funding.

## Documentation

- MCP: https://www.turbinefi.com/docs/mcp
- Strategy specification: https://www.turbinefi.com/docs/strategy-reference
- Backtesting: https://www.turbinefi.com/docs/backtest
