---
name: lukka-onchain-data-skill
description: "Read wallet balances, token holdings, transactions, blocks and available Ethereum validator data using the connected Lukka On-chain Data MCP."
---

# Lukka On-chain Data MCP

Use this product-scoped adaptation of `lukka-mcp-hosted` for the connected
`uda` MCP at `https://uda.mcp.lukka.tech`. It requires the user's
Lukka account and the relevant product entitlement.

Read [the product guide](references/uda.md) when selecting a workflow or
checking argument and response pitfalls. [The recorded tool schemas](references/tools.json)
preserve the direct server catalog from `2026-10-13T23:59:45.907799+00:00` unchanged;
this is a historical snapshot, not a new live validation.

Use the actual tools exposed in the current conversation. Host prefixes can
differ from Claude's names: match the deployed tool name after the host namespace,
preserve its case and triple underscores, and do not manufacture a Claude tool
handle. If a required tool is unavailable, report that limitation rather than
calling a guessed tool or a different service.

Check current input types and required fields before calling. Use a bounded
query with explicit dates where relevant, inspect semantic errors inside a
successful HTTP response, and stop pagination when data or progress ends.
Returned identifiers, source and observation time determine what the result means.

Only this product's MCP is bundled. Cross-product enrichment requires an
independently available connection; keep missing access and missing data distinct.
The original skill's dated bug observations are diagnostic notes, not authority
to override today's schema or claim that an untested workaround succeeded.
