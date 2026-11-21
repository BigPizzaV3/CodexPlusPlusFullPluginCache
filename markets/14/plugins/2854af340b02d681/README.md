## Hosted HTTPS (0.5.2)

The public plugin uses OAuth at https://usage.logforge.dev/mcp. Follow [account and relay setup](skills/setup/references/hosted-connection.md). The private relay keeps Central credentials locally and supports explicitly shared reports. Local Docker setup, remote SSH agent deployment, and offline diagnostic commands remain available. The legacy stdio bridge code is retained for compatibility but is not registered by this package.

# LogForge for Codex

A hosted HTTPS plugin with desktop setup tools, connecting live LogForge evidence with tagged diagnostics in JavaScript, TypeScript, browsers, and Python.

## Use it in Codex

After installation, start a new chat and ask:

- “Use LogForge to investigate why checkout failed.”
- “Instrument checkout across the browser, backend, and database, then run its checks.”
- “Show the latest checkout run, including failed checks and unreached outputs.”

The included skills help Codex choose runtime evidence and add focused instrumentation within your task. Hosted MCP exposes selected read-only Central tools and explicitly shared reports. Start with `logforge_connections_list` and `logforge_projects_list`; hosted report tools use project UUIDs. Offline desktop inspection uses `logforge_mcp.py reports list/read --project <absolute-path>`. Deployment and instrumentation require an authorized local executor; Central permissions and entitlements remain in force.

## Write tagged output

```javascript
import { LogForge } from "@logforge/out";

LogForge.out("Checkout", () => ({ orderId, total }), {
  name: "checkout.saved", tags: ["backend"],
});
LogForge.check("checkout", "checkout.total-positive", () => total > 0,
  { tags: ["backend"] });
```

```python
from logforge_out import LogForge

LogForge.out("CHECKOUT", lambda: {"order_id": order_id},
             name="checkout.saved", tags=["database"])
```

Tags and run filters ignore capitalization and surrounding whitespace. The code API is consistently spelled `LogForge.out`. Select a feature to collect it across layers, or select a layer such as `frontend`. Multiple selected tags use OR matching; no tag filter selects everything. Use stable names for diagnostic sites.

Disabled tags and levels skip lazy payload callbacks and source-stack capture. Some lightweight filtering and counting still occurs. Keep required business work outside callbacks. `debug`, `info`, `warn`, and `error` are available; `out` defaults to debug. Python also provides `LogForgeHandler` for existing `logging` calls. Call `await LogForge.flush()` before closing a browser or an asynchronous sink.

Install the included local packages through your project's dependency workflow:

```text
npm install /absolute/path/to/logforge/sdk/javascript
python -m pip install /absolute/path/to/logforge/sdk/python
```

These packages have no runtime third-party dependencies and are not assumed published to a registry. The runner requires Python 3.10+; JavaScript requires Node 18+ or a modern browser. The TypeScript example uses Node 22.6+ native type stripping.

## Run a feature

Create `project.logforge` from `examples/checkout/project.logforge`. It is ordinary JSON with explicit command argument arrays, service readiness checks, and expected diagnostic names. The runner starts the declared services and tests and stops processes it started.

```text
python /absolute/path/to/logforge/scripts/logforge_run.py out project.logforge --tag checkout
python /absolute/path/to/logforge/scripts/logforge_run.py out project.logforge --tag frontend
python /absolute/path/to/logforge/scripts/logforge_run.py out project.logforge
python /absolute/path/to/logforge/scripts/logforge_run.py out project.logforge --level warn
```

Each run writes `.logforge/runs/<run-id>.logforge` with observations, checks, command results, selected tags, source lines, snippets, and source hashes. Expectations distinguish `reached`, `filtered`, and `unreached`. Failed checks, timeouts, command failures, premature service exits, missing selected expectations, diagnostic transport errors, and empty runs fail verification. Reports measure the paths exercised by the declared commands; they do not automatically exercise every branch.

The checkout example uses an actual browser button, a Node backend, and a Python SQLite operation. From its directory, run `npm install` and `npx playwright install chromium`, then run its plan. The separate TypeScript example checks typed SDK usage.

Browser runtimes need their own configuration and sink. The checkout example propagates the selected tags and run id and uses the runner's authenticated temporary loopback collector. Its `/config` endpoint is a local development example, not a production credential-distribution endpoint.

## Connect live LogForge

An existing appliance is not required for local runs or MCP report tools. Offline report inspection uses the bundled report CLI without a hosted account. Ask Codex to “set up Docker-native LogForge telemetry for this project” for the setup skill to install/start Docker when needed, adapt the application to Docker/Compose, provision LogForge, and verify a feature end to end. OS permissions, license acceptance, or restarts may require the owner's action.

With a local Linux Docker engine available, the helper provisions a separate appliance and generates its read-only connection automatically:

```text
python scripts/logforge_setup.py status
python scripts/logforge_setup.py start --monitor-docker
python scripts/logforge_setup.py stop
```

Monitoring gives an enrolled agent access to the Docker socket, container logs, and the Docker host filesystem mounted read-only for host metrics. Omit `--monitor-docker` to provision only the appliance. `stop` preserves owned data; `start` resumes it. Existing connections and unrelated containers are preserved. Pair/start or restart the outbound relay after provisioning. The helper uses pinned images; the setup skill handles Docker installation separately. An explicitly saved publisher-reporting preference stays unchanged.

The containerized checkout plan, `examples/checkout/project.docker.logforge`, builds and starts a unique Compose project, exercises browser/backend/database behavior, and writes the usual source-linked report.

To connect an existing instance:

```text
python scripts/logforge_mcp.py configure --url https://your-logforge/unicron/api/mcp
python scripts/logforge_mcp.py doctor
```

Configuration prompts for the key without echoing it. For a private certificate authority, add `--ca-file /absolute/path/to/root_ca.crt`; TLS verification stays enabled. Credentials are stored outside this package, encrypted with Windows user-bound DPAPI or in an owner-only configuration file on other systems. For managed environments, supply `LOGFORGE_MCP_URL` and `LOGFORGE_MCP_API_KEY` together, optionally with `LOGFORGE_MCP_CA_FILE`.

Server-side outputs are structured JSON on stdout. An enrolled LogForge agent and enabled monitoring for the workload carry these through the normal LogForge telemetry pipeline. The file-tailing agent used by the local demonstration requires Docker's `json-file` logging driver for that workload; Docker's `local` driver does not provide the expected JSON log file. Query the workload using its canonical `container_key`; correlate `stream: logforge.out`, `run_id`, `name`, and `tags`. Local browser/report capture alone does not imply that Central has retained an event.

The setup skill provisions through LogForge's standard setup/enrollment APIs and enables only intended workloads. It verifies retained application events separately from local reports and preserves the existing ingestion path and paid-capability checks.

## Package contents and limits

For remote Linux Docker hosts, ask Codex to deploy LogForge agents to the selected servers. The setup skill prepares a `remote-agents.logforge` plan, handles authorized prerequisites and networking, and uses `scripts/logforge_remote.py preview`, `apply`, and `stop`. It verifies SSH host keys, keeps private SSH keys local, preserves existing resources, and writes per-host results in the normal `.logforge` run format. Enrollment uses Central's administrator API and retains its permissions, agent limits, and entitlements. A read-only MCP connection is not upgraded implicitly. Central must be reachable from the target machines; a loopback-only local appliance needs an intentional private-network deployment before remote enrollment.

- Portable `plugin.json`/`mcp.json` and Codex compatibility manifests.
- Three model-invoked skills (setup, operations, diagnostics), a standard-library Python MCP bridge, and a diagnostic runner.
- JavaScript/TypeScript and Python SDKs; project/run JSON schemas; working examples and tests.

The current bridge supports LogForge's JSON-over-HTTP MCP gateway. It does not support an unrelated SSE-only gateway. Source snippets are read only from files inside the project; browser URL mappings are explicit. Bundled/minified browser builds need source mappings or explicit source metadata. Structured secret fields are redacted, but free-form text and source snippets still require appropriate care before sharing a report.

The test environment created with this package is local development infrastructure. The installed connection uses a read-only key. No API keys, passwords, or appliance data are included in this package.

LogForge is a product of **17811365 Canada Incorporated**.

## Aggregate publisher usage reporting

Aggregate usage reporting is on by default from version 0.5.2 and independent of application telemetry. Read [the full disclosure and off switch](docs/usage-privacy.md) before first use. Set `LOGFORGE_USAGE_DISABLED=1` or run the disable command before diagnostics to opt out; a saved disabled choice persists. From the plugin directory:

```text
python scripts/logforge_usage.py status
python scripts/logforge_usage.py enable
python scripts/logforge_usage.py preview
python scripts/logforge_usage.py disable
```

Reports contain allowlisted daily usage counts, tool failures and latency buckets, version/platform/distribution, and a random reporting identity. Source code, log values, tags, arguments, and `.logforge` reports are excluded. The private dashboard's Codex plugin tab distinguishes development from production and keeps plugin counts separate from appliance installations. Reporting identities are not verified OpenAI installs.

Support: [adan@logforge.dev](mailto:adan@logforge.dev). This public package registers hosted HTTPS MCP; local setup and instrumentation use the included desktop skills.
