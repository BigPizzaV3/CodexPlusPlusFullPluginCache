# Token Weather - Cloudflare MCP preparation

Version 1.0.0. This is a separate With MCP source/preparation package. The
configured MCP URL has passed production health, initialization, schema and
synthetic calculation checks. Domain verification, recording, scans and
eligibility still require completion before submission.

The budget MCP accepts scalar token counts and fixed source enums only. Ask:

> My reference budget is 100000 tokens. I use 65000. Add 20000 for the task
> and reserve 5000 for output. How much room remains?

For forecasting, give a future per-turn growth estimate. The remote service
accepts no prior-turn arrays or conversation records. It has no filesystem,
account, model API, database or local Codex access. Numbers are supplied-value
arithmetic, not actual context/compaction/quota/currency readings.

## What is retained locally

The optional weather, event-replay and checkpoint Skills use the already
validated privacy revision's local helper scripts. Their scopes and storage
controls are explained in [local data and privacy](docs/PRIVACY.md). Replay
does not execute recorded tools or file edits; it remains on the computer.
The original weather page is unchanged. No hooks or automatic native controls
are included. Existing pure Skills and full local/open-source editions are
separate and are not installed, changed or deleted by this ZIP.

## Verify the prepared Worker locally

From `cloudflare/`, use Node.js 22+:

```sh
npm ci --ignore-scripts --no-audit --no-fund
npm run check
npm test
npm run dev:local
```

This starts `http://127.0.0.1:8787/mcp` only; Ctrl+C stops it. See
[Worker source instructions](cloudflare/README.md), [review cases](docs/REVIEW-CASES.md)
and [recording plan](docs/DEMO-PLAN.md). The recorded protocol-client walkthrough is linked in the recording document.
Natural-language host routing and overall submission readiness remain separate checks.

The later public-package builder requires the actual verified production HTTPS
endpoint and writes a fresh ZIP. No placeholder production address, credentials
or account binding is supplied. Publishing and any deployment require separate
authorisation; creating an archive performs neither.

Original software uses the [MIT License](LICENSE). The current
[website](https://feidawang.github.io/Token-Weather/),
[support](https://feidawang.github.io/Token-Weather/support.html),
[privacy policy](https://feidawang.github.io/Token-Weather/privacy.html) and
[terms](https://feidawang.github.io/Token-Weather/terms.html) describe the broader
project. The revised Cloudflare privacy/usage text is prepared locally and must
be published before a public submission. The package builder does not deploy or verify ownership of the selected
production endpoint; the portal's domain challenge remains separate.

## Recorded walkthrough

[Play the English MCP walkthrough](https://feidawang.github.io/Token-Weather/mcp-walkthrough-20261011.html).
The recording demonstrates actual MCP calls with synthetic inputs; it does not claim directory approval or completed host routing checks.
