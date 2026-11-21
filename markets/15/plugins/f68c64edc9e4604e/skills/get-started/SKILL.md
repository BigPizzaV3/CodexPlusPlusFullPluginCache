---
name: get-started
description: Connect a VulKill account, inspect the security catalog and credits, and prepare authorized source-code or live website scans.
---

# Getting started with VulKill Security

1. Use the host's VulKill OAuth connection. If sign-in is needed, let the user sign in with an offered identity method and review the requested permissions. For a new member, the site combines membership terms and MCP permission in one explicit consent screen. A website login alone does not install or authorize the host connector. Never request passwords or tokens in chat.
2. Call `vulkill_ai_guide` for the current workflow, modes, requirements and liability statement. Call `vulkill_capabilities` with `query: "all"` when the user asks for all 12 domains and all 260 controls; an empty query returns an overview. Catalog scope is not proof of executed tests.
3. Call `vulkill_wallet_status` for the connected user's actual credits. Use `vulkill_credit_usage` for the current period's usage. Do not describe the account as a demo or reviewer account unless it actually is one.
4. Ask which authorized source contents or verified HTTPS target the user wants to scan. A local filesystem path or GitHub repository URL alone does not transfer files. For website ownership verification, follow the guide's target page/API process. Use `vulkill_estimate_scan` for a read-only estimate; it starts no job and charges no credits.
5. Before calling `vulkill_start_scan`, present the current liability statement and obtain the user's explicit acceptance for the specific scope. Do not accept on their behalf or infer acceptance from signing in. Send actual sourceFiles or a verified targetUrl, the correct authorizationScope, and a stable idempotencyKey. Respect the server's limits and returned errors.
6. Use `vulkill_get_scan_status` to follow the returned scanId and `vulkill_list_reports` for saved account reports. An accepted request, credit reservation or available engine is not proof of completion. Report only actual findings and coverage; zero findings is valid. Never fabricate results or claim all domains ran.
7. `search` searches capabilities and the connected account's saved reports. Pass returned IDs to `fetch`; cap- IDs represent catalog entries, while report IDs represent scan reports. Explain which record type was returned. If no report matches, say so.
