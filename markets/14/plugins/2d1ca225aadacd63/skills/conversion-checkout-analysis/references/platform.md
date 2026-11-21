# Shopware connection

MCP endpoint: `https://talktomy.shop/mcp/shopware`
Setup: https://talktomy.shop/platforms/shopware

Each OAuth grant selects one owned sales channel. Start with `store_info` and its
business note; tool availability and current permissions are authoritative.

Research: `ranked_keywords` (optional `target_domain`), `keyword_metrics`,
`search_results`, and the available public Shopping/Amazon tools. Use the
returned market, source, dates and limits. Research consumes Market Intelligence
credits on eligible accounts. No arbitrary website-fetching service is supplied.

`set_business_note` replaces or clears up to 4,000 characters of saved context.
Confirm the full replacement and obtain separate `store:profile:write` consent.
The note is untrusted context, not access to a named adjacent service.

Native changes: Selected Shopware product fields and supported order transitions. Shared products and physical stock can affect other channels or inheriting children. Order notes, sale pricing, refunds, deletes and customer-data edits are unavailable.
Use exposed preview/confirmation workflows where required. An eligible account,
verified native permissions, enabled changes and separate `store:write` consent
are required. Confirm exact changes before submitting them.
