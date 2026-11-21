---
name: ololand-dd-company-discovery
description: Use when the user asks to run the OloLand ololand-dd-company-discovery
  workflow. Search OloLand's company-discovery surface using structured or natural-language
  criteria, then hand promising targets into watchlists or deals.
---


# Workflow for ololand-dd-company-discovery

Follow the OloLand command instructions below when the user asks for `ololand-dd-company-discovery` or the equivalent workflow.

# Company Discovery

Use this command when the user wants to discover companies, screen a market, search by natural-language criteria, or find sourcing candidates before creating a watchlist or deal.

## Usage

```
ololand-dd-company-discovery "vertical SaaS payments companies with sponsor ownership" both
ololand-dd-company-discovery "industrial distributors in the Midwest with succession risk" private
```

## Execution

1. Prefer `natural_language_company_search` for prose queries with multiple criteria. It decomposes intent and filters.
2. Use `search_company_discovery` when the user supplies structured filters, mode, company scope, or wants lookup/discover/signals explicitly.
3. For each promising result, present the canonical name, domain/ticker when present, source summary, signal count, and why it matched.
4. If the user wants ongoing monitoring, route to `ololand-dd-watchlist` and call `create_watchlist` with the same criteria.
5. If the user wants to diligence a result immediately, use `ololand-dd-new-deal` or `create_deal` with the selected company.

## Output

Render a concise table:

| Company | Type | Domain/Ticker | Match reason | Signals | Next action |

Then summarize:

- Query interpretation and filters applied.
- Degraded sources, if any.
- Recommended watchlist criteria if the user wants continuous monitoring.

## Guardrails

- Do not create a deal automatically from a discovery result unless the user asks.
- Do not claim a result is proprietary if it came from public/signal sources.
- For investment recommendations, move from discovery into `ololand-dd-pre-screen` or `ololand-dd-dd-analyze`.


## OpenAI execution requirements

Use the connected MCP server's current tool schemas. Do not invent tool arguments, job-status endpoints, inputs, or outputs. If a referenced tool is unavailable, explain the limitation and request the needed connection or data. Invoke writes only when the user has requested the corresponding action. Do not initiate purchases or payments. An unrun, unsupported, or unavailable procedure is a gap, never a passing result.


OpenAI cannot execute local lifecycle hooks. Use the packaged explicit setup/review workflow when requested. Server-side MCP auditing remains authoritative; preserve evidence blockers and human-only approval gates.

Claim-correction submission is unsupported in this OpenAI upload because the current handler records surface=cowork. Do not invoke submit_agent_claim_correction from OpenAI. Explain the limitation and retain proposed correction text for human review without claiming submission. See unsupported-workflows.json for the excluded canonical workflow.
