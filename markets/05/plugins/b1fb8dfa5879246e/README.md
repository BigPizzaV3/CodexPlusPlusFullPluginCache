# Totono for ChatGPT

Connect one Totono workspace to ChatGPT and search records your Totono account can access. Read access is required; write access is optional. Totono permissions, module settings, and subscription restrictions still apply.

The package uses one remote Streamable HTTP MCP server at `https://totono.work/mcp`. The OAuth authorization server is hosted by Totono. Search results and record details appear as concise text with canonical Totono links. A write requires explicit confirmation in chat after its workspace, changes, and possible side effects are shown.

Examples:

- Find my open Totono tickets and show what is due this week.
- Search our accounts for Acme and show related work.
- Show the renewal dates I can access in Vault metadata.
- Prepare a support ticket for my review.

Totono does not offer sending, calling, signing, approvals, deletions, credential changes, or access administration through this plugin. Disconnect in Totono Profile → ChatGPT connections. Support: https://support.totono.work (support@totono.work). Privacy: https://totono.work/privacy. Terms: https://totono.work/terms.

No OAuth credentials are included in this package.
