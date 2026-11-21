# OpenAI/Codex Analyst 0.1.32

Prepared 2026-11-20 from the existing `signalaf-analyst-0.1.31-public-review.zip`, matched against the installed 0.1.31 package and the existing published plugin management page. This is the OpenAI/Codex package, not the separate Claude distribution.

Changes: explain the July 31, 2026 frozen 1,642-profile reference field, its proof-of-concept comparison purpose, and its separation from live production; add token telemetry, token counts, token usage and AI operator benchmarks to discovery metadata; route archive questions to the packaged reference and historical website. Subtitle: `Token telemetry & benchmarks` (28 characters). Existing name, assets, default prompts, MCP declaration, authentication and five tools are preserved.

No archive query feature is added. The release does not make `window=all` select July. The current endpoint remains https://analyst.signalaf.com/api/plugins/sigrank/mcp.

The source archive's existing review cases, demo link and country targeting are preserved. Two review prompts cover the added instruction paths. New host behavior tests and portal review state must be reported separately from static validation. No policy attestation is inferred from preparing this package.

Publication status at preparation: not uploaded or published. The live plugin remains 0.1.31 until the existing publisher workflow reports otherwise. Radar server deployment and the official MCP Registry's npm version are separate releases.
