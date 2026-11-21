# TurbineFi Prediction Bot Maker

powered by TurbineFi

Version 1.0.2 clarifies the tool descriptions flagged during review and adds the supplied video walkthrough. Both package manifests use the same version and listing metadata. The package identity, OAuth MCP endpoint, branding, and simulation-only scope are preserved.

Each supported operation is published as a separate named MCP tool with a description, full input schema, and explicit annotations. Draft, backtest, and research operations use dedicated preview/execution pairs. Preview tools store temporary receipts; execution tools accept only the matching operation-bound confirmation token after explicit user approval. Unknown fields and generic operation selectors are rejected by the matching API implementation.

No automatic trade execution is available. Historical backtests simulate outcomes without submitting orders. The skill cannot deploy or activate live or paper bots, control runners, or transfer funds.

## Release dependency

This ZIP updates instructions and review examples; it does not deploy the MCP server. Deploy the API implementation exposing the named tools, reconnect/rescan the existing MCP connection, and check the complete catalog before testing or resubmitting. Do not use this package against an older server that only publishes generic action tools.

Five positive and three negative review cases are included as drafts. Run them against the deployed release with the reviewer test account. Their inclusion is not a claim that they have passed. Preserve the existing portal's verified publisher identity, country availability, and secure reviewer credentials; those values are not supplied by this source ZIP. The walkthrough URL is supplied in extensions.com.openai.review.demo_recording_url. Update the recording if it shows obsolete tools. Complete the portal checks before resubmitting. This package does not claim approval or a production deployment.

- MCP and support: https://www.turbinefi.com/docs/mcp
- Privacy: https://www.turbinefi.com/privacy
- Terms: https://www.turbinefi.com/terms

## Video walkthrough

[OpenAI Demo: Build a strategy and backtest it with Codex](https://youtu.be/m6dToEubWE8)

The supplied link resolves through YouTube public metadata. Full video playback and coverage of all updated tools have not been verified in this task.

New creation tools marked as needing further review remain subject to OpenAI approval. Deploy the server metadata changes, rescan, and submit or appeal the held definitions through the existing dashboard; the ZIP cannot clear their review state.
