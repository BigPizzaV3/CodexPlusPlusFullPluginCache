---
name: uptook
description: Use Uptook for B2B lead and trade research, contact lookup, requested outreach, or help connecting and troubleshooting the Uptook plugin.
---

# Uptook

Use the connected Uptook MCP tools for the user's request. The tool names below are business names; call the names actually exposed by the client, without inventing a prefix or parameters. Current tool schemas, `get_search_guidance`, and `get_tool_help` take precedence over examples here. Reply in the user's language. Uptook monetary integer values are USD cents; divide by 100 when showing dollars.

## Connect and get started

When the user asks to set up Uptook or check its connection, call the free `auth_info` tool once. A successful response confirms the account connection; it does not authorize a paid query.

If the client requests login or returns `login_required` or 401, guide the user to the Uptook plugin settings in the ChatGPT or Codex account they are using, select **Connect account**, and complete Uptook's browser authorization. After installing the plugin, start a new conversation and check `auth_info` again. Never ask the user to paste a password, token, OAuth code, or cookie into chat.

For `Unknown tool`, `Connector not found`, or missing Uptook tools, first check whether the plugin is installed and enabled and whether an Uptook account is connected in that client. If the user connects it, retry only the free `auth_info` check once. If the error persists, stop and give the user the tool name, the exact nonsecret error, and the client in which it happened so support can investigate. Do not repeat authorization in a loop or silently present another data source as Uptook results.

## Research workflow

- Choose the tool for the user's actual goal: company or person discovery, customs buyers and suppliers or transactions, map businesses, existing result details, or contact lookup. A company search cannot establish an importer or distributor role; offer customs trade research when that is the intended question.
- Uptook does not sell plans or credits through this plugin. Direct purchase requests to the user's own Uptook account without looking up prices or preparing a checkout.
- Before the first paid search, call the free `get_search_guidance`, `get_tool_pricing`, `auth_info`, and, when available, `get_plan_quota`. Use `get_tool_help` for advanced parameters. Explain the search terms and filters, tool, planned calls or IDs, result limit, billing source, and maximum cash charge or expected plan quota use. Keep USD balance prices separate from plan quota. End the reply and wait for explicit consent in a later turn; the initial request and account balance are not consent.
- Run only the approved scope. Do not automatically retry a paid call, expand a search, or switch from plan quota to balance billing. Quote and confirm any additional contact unlock before calling it. A record marked as having a phone or email does not contain the actual contact value until it is returned by the relevant lookup.
- Preserve real IDs and `resultSetId`. Once the approved steps are complete, call `render_search_results` for the final result set. Briefly summarize a visible MCP App panel without copying its rows into Markdown. If the user cannot see the panel, use the free text display or result-set readback; do not repeat the paid search.

## Sending and recovery

For email or SMS, show the exact recipients, message, and applicable cost before requesting a separate send confirmation. Promotional SMS also requires a recipient list the user says has consented; found or unlocked phone numbers do not establish consent. For SMS with consented recipients, use `get_tool_pricing` with `smsQuote` for the exact numbers, body, and channel when that parameter is available. Never send merely because the user approved a search or contact lookup.

If a required balance price is unavailable, do not guess it or execute balance billing. A plan-funded action may proceed only when its applicable quota use and remaining quota are known and the user confirms that plan. After a timeout or uncertain result from a paid or sending tool, do not call it again automatically; use free status or result readback when an identifier exists, then report what remains unknown.
