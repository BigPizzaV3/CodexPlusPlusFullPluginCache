---
name: kiliba-marketing
description: Analyze and operate an authenticated Kiliba ecommerce marketing account. Use when the user asks about Kiliba or MARK, campaign and ecommerce performance, product contribution, shop or module connectivity, customers, transactional messages, or API-triggered workflows.
---

# Use Kiliba safely and effectively

Use the Kiliba connector for facts about the authenticated user's Kiliba accounts. Never infer access from an email address or from conversation context: the connector enforces the user's current Kiliba permissions.

## Select the account

Call `list_accounts` before any account-specific tool when the user has not identified a shop. If several shops match, ask the user to choose. Reuse the returned opaque `accountRef`; never invent or expose an internal account identifier.

## Answer product questions

Call `discover_kiliba_capabilities` when the user asks what Kiliba or MARK can do. Distinguish:

- capabilities available through this MCP connector;
- capabilities available only in the Kiliba application or through MARK, Kiliba's integrated marketing agent.

Do not claim that the connector exposes MARK's complete in-product runtime.

## Analyze performance

- Use `get_account_overview` for a broad marketing and ecommerce review.
- Use `get_campaign_performance` to compare campaigns, Automation scenarios, workflows, or Smartletters.
- Use `get_performance_trend` for observed daily, weekly, or monthly changes; do not present it as a forecast.
- Use `get_ecommerce_performance` to compare shop revenue and Kiliba-attributed revenue.
- Use `get_attributed_product_performance` for products or product families contributing to attributed results.

Always preserve the period, data freshness, attribution rules, and limitations returned by the connector. Do not describe attributed revenue as causal lift, profit, margin, or ROI.

By default, omit `attribution_window` so reporting tools use the attribution window configured on the Kiliba account. When the user explicitly asks to compare or recalculate attribution over another supported window, pass `4h`, `24h`, `5days`, or `30days`. Make clear that this is a temporary analysis override and does not change the account configuration.

For aggregate engagement rates, use `rate_calculation: kiliba_average` by default to preserve the calculation displayed in Kiliba. Use `weighted_by_sends` only when the user explicitly asks for rates weighted by message volume, and label the calculation mode in the answer.

## Diagnose the shop connection

Use `get_shop_configuration` for the CMS, installed module version, synchronization state, connection status, and bounded module diagnostic. Report Cloudflare only when `cloudflareChallengeDetected` is explicitly true. A timeout, unreachable module, or generic access failure is not evidence of Cloudflare.

## Handle customer data

Use `list_customers` only when the user explicitly asks for customer-level data. Results contain personal data: return only the fields needed for the request and avoid repeating unnecessary personal information.

## Require confirmation for actions

Every write follows two distinct steps:

1. Call the relevant `prepare_*` tool and show the exact proposed action, account, recipient or affected-customer count.
2. Ask for explicit confirmation. Only after a new affirmative user message call the matching `execute_*` tool with the returned confirmation token.

Never treat the initial request as confirmation, never skip preparation, and never substitute one action for another. This applies to customer blacklist or whitelist changes, transactional messages, and workflow triggers.

If the preparation expires or the action changes, prepare it again and request a fresh confirmation.
