# Lukka Blockchain Analytics & Compliance MCP — hosted workflows

Adapted from the publisher-provided `lukka-mcp-hosted` product reference. Old deployment observations must be checked against current discovery and returned data.

## Select an available report tier

Use `AML___generateAmlScoringReport` for a light scoring request. Standard and Enhanced reports use `AML___generateAmlStandardReport` and `AML___generateAmlEnhancedReport`; Simplified uses `AML___generateAmlSimplifiedReport`.

The supplied hosted notes distinguish chains with on-chain data from those without it: Standard/Enhanced need supported on-chain coverage, whereas Simplified is intended for supported chains without that coverage. Verify current coverage and account entitlement; a deeper tier is not universally available. Do not downgrade or request another report automatically after an error without considering the user's requested depth and access.

Read the live schema for report arguments. The hosted tools use `address` and uppercase `address_type` such as `ETH`; do not substitute UDA's lowercase `blockchain` field. Ask for a missing address or chain before issuing a report request.

## Interpret the result

Identify report tier, chain, address, report time, score/category and returned risk factors. Distinguish numeric scores and observed exposure from a compliance determination. Do not invent sanctions matches or conclude that a wallet is legally cleared from a low score.

Standard/Enhanced responses can be large. Use the host's actual file/export or local processing capability when available, retain the relevant sections, and say what was actually inspected. This package does not supply `process_aml_report.py` or require a separate processing skill. Do not pretend a missing helper ran.

The hosted catalog contains report tools, not transaction execution, standing monitoring or the internal dev graph/screening flow. Asset holdings require an independently available on-chain connection; do not imply that this plugin bundles it.
