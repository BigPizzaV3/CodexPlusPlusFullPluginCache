# Lensden Explorer — remote edition 0.2.1

Connect to https://lensden.net/api/mcp using Streamable HTTP and **No authentication**. No local executor, API key or Lensden account is needed. Remote availability requires a separately approved production activation; packaging does not activate it.

The four read-only tools are search_devices, get_device_details, compare_devices and find_relevant_guides. Devices come from anonymous published Supabase reads; English guides come from deployed published content. Responses retain freshness, canonical product/Compare/guide links, source evidence, generations, region/variant scopes and Unknown/conflict states. External source links are not fetched live. This is documentary research, not stock, pricing, transactions, ranking or compatibility certification.

Website: https://lensden.net/ · Support: https://lensden.net/contact/ · Privacy: https://lensden.net/privacy/ · Terms: https://lensden.net/terms/

The existing 512×512 icon is reused. Root plugin.json and mcp.json, the research skill and review documents form the remote package. The completed offline server remains in integrations/lensden-explorer in source history; no offline catalog or server is included in this ZIP.

Local checks: node scripts/verify-lensden-plugin.mjs. Package: node scripts/package-lensden-explorer.mjs. Output: artifacts/distribution/lensden-explorer-remote-0.2.1.zip plus SHA-256. These validate local structure, not publisher verification or portal approval. See review/readiness.md for actual owner prerequisites.
