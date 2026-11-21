# PageLantern for Codex and ChatGPT

Connect your PageLantern workspace to inspect monitor status, settings, check history, observed uptime, graphs and results by monitoring location. Read existing client report packs and frozen report metrics. With additional authorization, run an HTTP check, create public HTTP uptime monitoring, or pause and resume scheduled monitoring. Workspace permissions, plan limits and retention apply.

Try “Show a response-time graph for my homepage,” “Compare my homepage results by location,” or “Summarize my latest approved client report.” The setup skill verifies access with a read-only request. Recorded status is not a fresh check; history and location samples may be truncated; graphs preserve missing-data gaps. Uptime and reports describe observed check success rather than elapsed-time availability. History, uptime, graphs and location results do not support Page Speed monitors.

## Connect with the right permissions

| Access | Scopes | Workspace role |
| --- | --- | --- |
| Monitors, history, uptime, graphs and locations | `monitors:read` | Any workspace role |
| Existing client report packs and frozen metrics | `reports:read` | Any workspace role; Members/Viewers see approved editions only |
| Default hosted read access | `monitors:read reports:read` | Current workspace permissions apply |
| Run an HTTP check | `monitors:read monitors:run` | Owner/Admin |
| Create, pause, resume | `monitors:read monitors:write` | Owner/Admin |
| All fourteen tools | `monitors:read reports:read monitors:run monitors:write` | Owner/Admin |

Hosted ChatGPT's portable manifest starts with `monitors:read` and `reports:read` in `baseScopes` and `defaultScopes`. Older connections do not acquire report permission automatically; renew consent when needed. It uses public client `pagelantern-chatgpt`, PKCE, and the registered hosted callback. For an action that needs more access, reconnect or approve expanded scopes if the host supports it; otherwise configure a separate elevated connection. An `insufficient_scope` response does not guarantee automatic permission upgrades.

The separate native Codex artifact uses public client `pagelantern-codex` and `oauth.callbackUrl: http://127.0.0.1/callback`. Codex inserts its chosen listener port during authorization. The server must advertise issuer-bound callbacks and return matching `iss`. This uses the [documented native plugin OAuth fields](https://learn.chatgpt.com/docs/extend/mcp#plugin-provided-mcp-servers). The native ZIP omits root portable manifests, avoiding any assumption that native clients merge portable and compatibility configuration.

Native Codex can request the server's advertised scopes, so plugin installation alone does not guarantee a read-only grant. To request read-only access independently of plugin installation, use the following configuration in your Codex `config.toml`, then log in with explicit scopes. Inspect the actual consent screen and resulting grant for each connection; the manual read-only configuration below is a separate path from the packaged native connection tested for this release. Do not approve broader access when read-only access is required. Do not create a duplicate entry if one already exists, and avoid enabling both manual and plugin connections for the same task.

```toml
[mcp_servers.pagelantern]
url = "https://pagelantern.com/api/chatgpt/mcp"

[mcp_servers.pagelantern.oauth]
client_id = "pagelantern-codex"
callback_url = "http://127.0.0.1/callback"
```

```sh
codex mcp login pagelantern --scopes monitors:read,reports:read
```

For an Owner/Admin who deliberately needs all actions, authorize the expanded set:

```sh
codex mcp login pagelantern --scopes monitors:read,reports:read,monitors:run,monitors:write
```

The installed CLI also supports `codex mcp add pagelantern --url https://pagelantern.com/api/chatgpt/mcp --oauth-client-id pagelantern-codex --oauth-resource https://pagelantern.com/api/chatgpt/mcp`. Adding can immediately start authorization using discovered scopes. The explicit configuration/login route requests a limited scope set, but still verify consent. See [native registration and callbacks](https://learn.chatgpt.com/docs/extend/mcp#oauth-client-registration-and-callbacks). A successful live login and tool call are release checks, not established by command help or package validation.

Credentials remain in PageLantern's sign-in flow and the host's token store. Never paste passwords, tokens, or API keys into chat. If access expires, reconnect. No scope grants access to another workspace or bypasses a Viewer role.

## Supported actions

The fourteen tools are `list_monitors`, `get_monitor`, `get_monitor_history`, `get_monitor_uptime`, `list_locations`, `get_monitor_location_results`, `get_monitor_graph`, `list_report_packs`, `get_report_pack`, `get_report`, `run_monitor`, `create_uptime_monitor`, `pause_monitor`, and `resume_monitor`. [Tool contracts](skills/monitoring/references/tool-contracts.md) describe inputs, outputs, boundaries and errors.

Graphs return a PNG plus bounded structured observations. Location results distinguish requested and actual probes. Client reports expose frozen metrics and signed-in PageLantern links; they do not generate, approve, publish, download or email reports, and do not expose recipients, private notes or public-share tokens.

Creation starts an enabled HTTP GET monitor for a public website you are authorized to monitor. On-demand checks consume check usage and can alert. Pausing stops scheduled checks and may close incidents; resuming schedules the next check. The plugin cannot delete monitors, edit other settings, change billing, configure alerts, or create browser, Page Speed, SSL, or DNS monitors.

## Package status

Version 1.2.0 targets the production PageLantern service. The release runbook records current deployment, client acceptance, review, and publication status; package validation alone does not establish any of those steps or make the plugin available in a public directory.

A new 1.2.0 walkthrough and fresh hosted acceptance are required before resubmission. The old 1.0.1 video does not demonstrate the six added tools; its URL is omitted from the current review metadata until an accurate replacement is recorded and verified.

The repository contains both formats. Build `pagelantern-1.2.0.zip` for hosted portable review (11 files) and `pagelantern-codex-1.2.0.zip` for native local testing (9 files). The native artifact contains only `.codex-plugin/plugin.json` and `.mcp.json` as manifests. Do not install the mixed source directory for native testing: portable manifests take precedence over compatibility files, and the host-specific OAuth clients intentionally differ. The portable manifest selects `skills/setup/SKILL.md` for onboarding; native loaders can invoke setup explicitly. Both skills declare the same remote MCP dependency. The package contains no credentials, local executable server, hooks, or app bundle.

## Validate and try the native plugin locally

From the repository root, use a disposable validation environment:

```sh
plugin_venv=$(mktemp -d)/venv
python3 -m venv "$plugin_venv"
"$plugin_venv/bin/python" -m pip install -r scripts/plugin-requirements.txt
"$plugin_venv/bin/python" -m unittest discover -s scripts -p 'test_*plugin*.py' -v
"$plugin_venv/bin/python" scripts/package-chatgpt-plugin.py --check --schema-check
"$plugin_venv/bin/python" scripts/package-chatgpt-plugin.py --schema-check
```

The builder writes both ZIPs and SHA256 sidecars under `plugins/.artifacts/`. For an optional check using installed Codex authoring skills, run their validators if those paths exist:

```sh
"$plugin_venv/bin/python" "${CODEX_HOME:-$HOME/.codex}/skills/.system/plugin-creator/scripts/validate_plugin.py" plugins/pagelantern
"$plugin_venv/bin/python" "${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-creator/scripts/quick_validate.py" plugins/pagelantern/skills/setup
"$plugin_venv/bin/python" "${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-creator/scripts/quick_validate.py" plugins/pagelantern/skills/monitoring
```

To install for local testing, first deploy and verify the intended service. The packaged endpoint is production; use a separate reviewed test copy with matching test URLs for staging. The following steps register a named local marketplace only when you execute them; they do not publish the plugin or edit your personal marketplace. Keep the temporary directory until testing is finished.

```sh
plugin_marketplace=$(mktemp -d)
mkdir -p "$plugin_marketplace/plugins/pagelantern" "$plugin_marketplace/.agents/plugins"
python3 -m zipfile -e plugins/.artifacts/pagelantern-codex-1.2.0.zip "$plugin_marketplace/plugins/pagelantern"
cat > "$plugin_marketplace/.agents/plugins/marketplace.json" <<'JSON'
{
  "name": "pagelantern-local-test",
  "interface": {"displayName": "PageLantern local test"},
  "plugins": [{
    "name": "pagelantern",
    "source": {"source": "local", "path": "./plugins/pagelantern"},
    "policy": {"installation": "AVAILABLE", "authentication": "ON_USE"},
    "category": "Developer Tools"
  }]
}
JSON
codex plugin marketplace add "$plugin_marketplace"
codex plugin add pagelantern@pagelantern-local-test
```

These commands follow the [local marketplace workflow](https://developers.openai.com/plugins/build/plugins#add-a-marketplace-from-the-cli) and the installed CLI's `plugin add` interface. Where CLI plugin installation is unavailable, open the desktop plugin directory and install PageLantern from the registered local marketplace. Start a new task, invoke PageLantern setup, complete OAuth, and verify a read-only monitor list. Verify the approved scopes before trying actions. The runbook covers separate role, mutation, and hosted ChatGPT acceptance tests.

After testing, uninstall `pagelantern@pagelantern-local-test` through the host, then remove the local source with `codex plugin marketplace remove pagelantern-local-test`. No local installation or publication is performed by the build script.

The listing's five positive and three negative review scenarios are prepared test plans, not executed acceptance results. Consult the release runbook for recorded hosted and native acceptance and the remaining role, scope, reviewer, publisher, submission, and publication checks. Build and validation instructions live in the repository's release guide.

[PageLantern](https://pagelantern.com) · [Support](https://pagelantern.com/contact) · [Privacy](https://pagelantern.com/privacy) · [Terms](https://pagelantern.com/terms)
