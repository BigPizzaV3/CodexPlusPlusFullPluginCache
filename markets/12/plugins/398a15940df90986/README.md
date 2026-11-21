# ReportAste ChatGPT review candidate 0.2.0

This package connects ChatGPT to the hosted ReportAste MCP endpoint at
`https://mcp.reportaste.it/mcp` using OAuth Dynamic Client Registration. It is
prepared for a controlled reviewer account and is not evidence of OpenAI portal
ingestion, a public directory listing or publication.

The declared default scopes are `catalogo:read`, `analisi:read` and
`gestionale:read`. The ReportAste authorization server separately caps
ChatGPT client registrations to read-only permissions. The package field alone
does not enforce that cap. Other ReportAste clients may have separately
consented `gestionale:write`; this ChatGPT review connection cannot register
sales or purchases, bid on auctions or make payments. `offline_access` refresh
behavior beyond the five-minute access-token lifetime remains unverified.

The reviewer video is at `https://auth.reportaste.it/support` and requires
sign-in with the dedicated reviewer account. Reviewer credentials and login
instructions belong only in the OpenAI dashboard's private Review details,
never in this ZIP. Account owners can inspect and revoke AI grants from
Collegamenti AI. Logout alone does not revoke a grant.

The root `plugin.json` includes five positive and three negative cases and
release notes. The full pinned Agent Plugins MCP 1.0.0 schema currently rejects
the documented per-server `extensions` field in `mcp.json`; the local validation
report records the unmodified schema result. This package must be evaluated by
the portal before any claim of ingestion or review approval.
