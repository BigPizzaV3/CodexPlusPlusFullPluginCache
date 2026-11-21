# bc-bdi

Boomi Companion plugin for BDI (Boomi Data Integration, formerly Rivery) — Boomi's ELT/ETL data-pipeline product. BDI is distinct from Boomi Integration (the application-integration platform), and BDI data flows are distinct from Boomi Flow (the workflow-application product).

> **Important:** Boomi Companion is a publicly available developer offering, not an officially supported Boomi product. It is provided as-is and is not covered by Boomi support agreements or SLAs. Boomi curates and maintains this tool on a best-effort basis — treat it as a self-service resource. Boomi reserves the right to modify or discontinue it at any time without notice.

This project is licensed under the [BSD-2-Clause License](LICENSE). If you fork or modify this code, you should not use the name "Boomi" for your version.

## Feedback & Issues

Found a bug or have a feature idea? Email developer-offerings@boomi.com with a clear description, steps to reproduce, and any relevant error messages.

## Setup

`bc-bdi` plugin and `boomi-bdi` skill read credentials from the workspace `.env`. BDI has its own console, API, and token system — nothing is shared with Boomi Integration platform credentials.

| Key | Notes |
|---|---|
| `BDI_API_URL` | The API host, including `https://` and with no trailing slash — `https://api.rivery.io` for US-console accounts; EU consoles use the EU API host. This is not the console address |
| `BDI_API_TOKEN` | Generate in the BDI console: **My Profile → API Tokens** |
| `BDI_ACCOUNT_ID` | First of the two hex ids in any BDI console URL (see below) |
| `BDI_ENVIRONMENT_ID` | Second of those two ids — the environment the console is showing, so switch to the one you want first. An empty `BDI_ENVIRONMENT_ID=` line blocks the other scripts |

Both ids are 24-character hex strings and both sit in the address bar whenever you are in the console, so you can fill in all four keys in one pass:

```
https://console.rivery.io/dashboard/<account id>/<environment id>/dashboard?...
```

If you don't have the environment id, leave that line out and run `bdi-env-check.sh` — it lists the environments the token can reach and prints the line to add.

A token is scoped to specific environments when created — if `bdi-env-check.sh` authenticates but lists no environments, grant the token environment access in the BDI console. Listing an environment does not mean the token can work inside it: a `403` on one environment usually means another environment is the right target, not that the token is broken. A `401` is the same response for a mistyped token and for the wrong region host, so check the token paste first, then the host.

Optionally, add a `preferred_connections.md` to the workspace listing the BDI connections flows should use (name/id plus a one-line description each) — the agent checks it before proposing connections. Same file convention as bc-integration; a plain hand-written file works.

## BDI documentation

For the BDI product, not this plugin:

- [Data Integration overview](https://help.boomi.com/docs/Atomsphere/Data_Integration/Data_Integration_Overview) — landing page
- [REST API overview](https://help.boomi.com/docs/Atomsphere/Data_Integration/RESTAPI/dataintegration-api-overview) — the API these scripts wrap: auth, tokens, making calls
- [Blueprint](https://help.boomi.com/docs/Atomsphere/Data_Integration/Blueprint/blueprint-intro) — YAML connector builder for custom REST sources
- [Viewing activities](https://help.boomi.com/docs/Atomsphere/Data_Integration/GettingStarted/MonitoryourIntegrations/activities) — run history and activity logs in the console
- [Data Integration support](https://help.boomi.com/docs/Atomsphere/Data_Integration/Support/data-integration-support-overview) — raising a case with Boomi

Every page is also served as markdown: insert `/md` before `/docs` and append `.md`. The skill uses that mirror, indexed at [llms.txt](https://help.boomi.com/md/docs/Atomsphere/Data_Integration/llms.txt).
