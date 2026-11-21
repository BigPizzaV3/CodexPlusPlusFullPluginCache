---
name: insidercat-research
description: Use InsiderCat MCP tools for researching publicly disclosed U.S. politician and corporate insider trades, reconstructed portfolio holdings and performance, and stock ownership.
---

# InsiderCat research

Use the connected InsiderCat MCP server for user requests about U.S. congressional and corporate insider stock disclosures, estimated portfolios, Trump and Trump-administration holdings, stock-level disclosed ownership, aggregate sentiment, and performance of those disclosed positions.

## Getting started

If InsiderCat is not connected, guide the user through the host's standard connection and InsiderCat OAuth sign-in. Users access data under their existing InsiderCat account entitlements. Do not ask users to paste API keys, passwords, or access tokens into chat. Do not promote subscription upgrades or launch checkout flows.

## Research workflow

- Select a matching read-only MCP tool and use its documented arguments. Do not claim to have queried InsiderCat unless a tool returned relevant data.
- For congressional trades, distinguish transaction/traded date from disclosure/reported date and retain the reported buy/sell direction and disclosed value range. Do not treat disclosure as contemporaneous trading intent.
- For portfolio holdings and performance, label reconstructed positions and returns as estimates. When comparing strategies, differentiate original versus reporting-delay-adjusted return calculations.
- Preserve ticker, time period, report date, and calculation mode when stating results. Avoid inventing current prices, positions, missing values, or source links.
- Use page limits and pagination when the user requests more results. If an answer would require unavailable data (e.g. prices on a precise day), state the limitation rather than making up the value.
- For corporate-insider data, distinguish transaction direction from aggregate sentiment. Where applicable, note that ownership and filing data may be delayed or amended.
- Present information neutrally. Do not imply any politician traded on confidential information without independent evidence.
- Cite or attribute the dataset to InsiderCat and, where provided by a tool, link to original public disclosures. Explain that research content is not investment, legal, or tax advice.

## Boundaries

- The plugin retrieves disclosure research data only. It does not place stock orders, manage brokerage accounts, move money, contact politicians, send messages, or access private banking records.
- Never guarantee future returns, suggest that past performance ensures outcomes, or fabricate exact portfolio values when only estimates or ranges are available.
- If a user does not have access to a feature, explain the entitlement limitation neutrally. Do not initiate purchases, direct users to checkout, advertise pricing, or solicit upgrades.
