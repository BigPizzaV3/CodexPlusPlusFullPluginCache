# PageLantern MCP tool contracts

The connected workspace and current role bound every request. Seven monitor/location/graph read tools require `monitors:read`; three client-report read tools require `reports:read`; run requires `monitors:run`; create/pause/resume require `monitors:write`. Run and write actions additionally require Owner/Admin. Arguments reject unsupported fields. Monitor IDs are positive integers; report and pack IDs are canonical UUID strings.

## Read tools

| Tool | Arguments | Result |
| --- | --- | --- |
| `list_monitors` | `page`: integer 0–1,000,000, default 0; `size`: integer 1–100, default 50 | `monitors`, `page`, `size`, `total_items`, `next_page` (null at end) |
| `get_monitor` | `monitor_id` | `monitor` summary and `settings`: `enabled`, `timeout_ms`, `expected_status`, `request_method`. Last two fields are null for non-HTTP monitors. |
| `get_monitor_history` | `monitor_id`; `range`: `1h`, `6h`, `24h`, `7d`, or `30d`, default `24h`; `limit`: integer 1–100, default 20 | `monitor_id`, `range`, `since`, `until`, `checks`, `truncated` |
| `get_monitor_uptime` | `monitor_id` only | `monitor_id`, `window: "24h"`, `total_checks`, `uptime_percent`, `last_checked_at` |
| `list_locations` | No arguments | `observed_at`, `locations` (at most 100), `truncated`. Each location has `code`, `name`, `country`, `home`, `probe_available`. |
| `get_monitor_location_results` | `monitor_id`; `range`: `1h`, `6h`, `24h`, `7d`, or `30d`, default `24h` | Window, `sample_size`, `sample_limit` (2000), `requested_locations`, grouped `locations` (at most 100), `truncated` |
| `get_monitor_graph` | `monitor_id`; same `range` choices, default `24h`; `metric`: `response_time` (default) or `availability` | PNG image plus structured primary-location observations in at most 120 time buckets, counts, summary, window, coverage/retention notes and `truncated` |
| `list_report_packs` | Optional nonempty `cursor` string, at most 256 characters | `packs` (at most 50) and `next_cursor`; safe pack metadata, latest report summary and signed-in `ui_url` |
| `get_report_pack` | `pack_id` UUID; optional bounded `cursor` | Safe pack metadata, `reports` (at most 100 existing editions), `next_cursor` and signed-in `ui_url` |
| `get_report` | `report_id` UUID | Edition status/revision/period/timestamps, signed-in `ui_url`, `methodology` and frozen `metrics` or null |

A monitor summary contains `id`, `name`, a redacted `url`, `monitor_type`, `status`, `interval_seconds`, `last_checked_at`, `last_status_code`, and `last_response_time_ms`. Status is `paused`, `blocked`, `unknown`, `up`, or `down`. Unknown means no usable recorded status; Page Speed status is unknown unless paused/blocked. URLs omit credentials, queries, and fragments. Do not attempt to reconstruct omitted values.

History returns the newest limited observations in chronological order. Each check contains `checked_at` (nullable timestamp), `success` (nullable boolean; null is an unclassified outcome, not success or failure), `status_code` (nullable integer), `response_time_ms` (nullable integer), `location` (nullable string), and `primary_location` (boolean). It deliberately omits error messages, bodies, and headers. `truncated: true` means the requested limit or service's 2,000-result retrieval cap omitted observations. Include the returned `since` and `until` window; do not imply the sample contains all checks.

Uptime is the percentage of successful primary-location observations over the full preceding 24 hours, using an aggregate independent of the recent-history limit. It is not duration-weighted availability, an SLA measurement, or a guarantee about unobserved time. `uptime_percent: null` with no measurements means unavailable, not zero. Do not accept a `range` argument for this tool. History and uptime reject `PAGE_SPEED`; its reports use a separate model unavailable through these tools.

Location catalogue availability describes probe infrastructure at `observed_at`, not website health or guaranteed future routing. Results group actual location, requested location and primary/secondary role separately. Each group includes successful, failed and unclassified counts; observed success percentage excludes unclassified outcomes. Average latency uses nonnegative recorded durations. A requested location may differ from the actual location after fallback. Results use at most 2000 retained checks, not a full-window aggregate; `truncated` also covers omitted groups/configured locations. No agent hosts, credentials or routing configuration are returned. Location results reject Page Speed monitors.

Graphs aggregate the retained primary-location rows into up to 120 buckets without further row sampling. Response-time values are mean nonnegative recorded durations, including failed checks; missing/negative durations are excluded. Availability values count successful checks among known outcomes. Buckets without a usable value remain null gaps. `observed_checks`, `classified_checks`, `unknown_checks`, `valid_latency_checks`, `excluded_checks`, represented/empty bucket counts and first/last timestamps explain coverage. Read `summary`, `coverage_note`, `retention_note` and `truncated`; a requested window is not a guarantee of complete retention. The PNG visualizes this same bounded data. These are observed successful checks, not continuous uptime. Page Speed is unsupported.

Report tools read existing workspace-bound packs and editions. Owners/Admins can read their accessible drafts; Members/Viewers see approved editions only. Follow `next_cursor` until null when more results are needed. `get_report` returns frozen metrics with `metric_version`, capture/cutoff timestamps, coverage, successful/failed/unclassified counts, success percentage, observed/total days and up to 100 monitor metrics (`monitor_metrics_truncated` indicates omitted entries). Per-monitor metrics include public label/type, availability eligibility, captured enabled/blocked state, counts, average latency and estimated p95. These metrics are not current health or an SLA. Expired or ungenerated snapshots have null metrics. No recipients, addresses, delivery settings, private notes, raw URLs, PDF content or public-share tokens are returned. `ui_url` requires normal PageLantern sign-in; it does not grant access or download a PDF. Reports are never generated, approved, published, downloaded or sent by these tools.

## Actions

| Tool | Arguments | Effect and result |
| --- | --- | --- |
| `run_monitor` | `monitor_id` | Executes one existing HTTP GET/HEAD check without API workflow steps. Returns `monitor_id`, `success`, `checked_at`, `status_code`, `response_time_ms`. Makes a network request, consumes check usage, and can trigger alerts. |
| `create_uptime_monitor` | `name`: 1–255 characters; `url`: public HTTP(S), at most 1,024 characters; `interval_seconds`: integer 30–86,400, default 300; `expected_status`: integer 100–599, default 200 | Creates an enabled HTTP GET monitor with a 10,000 ms timeout and returns `monitor`. No custom request headers, body, or credentials. Existing plan minimum intervals and monitor limits still apply. |
| `pause_monitor` | `monitor_id` | Disables scheduled monitoring; may close incidents. Returns `monitor`, `changed` (boolean). |
| `resume_monitor` | `monitor_id` | Enables monitoring and schedules the next check. Returns `monitor`, `changed` (boolean). |

Pause/resume support all monitor types and are idempotent: `changed: false` means the desired state was already set. Changes are audited. A resumed or newly created monitor has not necessarily completed a successful check. URLs with embedded credentials, fragments, loopback/private addresses, or non-HTTP(S) schemes are not supported creation targets.

## Failures and retries

Inspect the MCP error result rather than treating an HTTP 200 transport response as tool success. Do not claim a change succeeded without its tool result or a confirming read.

- `401`, or a tool error with `_meta["mcp/www_authenticate"]` and `invalid_token`: reconnect through the host and PageLantern authorization flow.
- Tool error with `insufficient_scope`: identify the required scope from the authentication challenge and request fresh consent through the host. These errors use HTTP 200 with `isError: true`; they never mean the tool ran. Expanded approval depends on host support; otherwise configure an elevated connection.
- `403`: the current workspace role or another access restriction forbids the operation. A Viewer cannot bypass the Owner/Admin requirement by requesting more scopes; do not repeatedly offer consent for a role denial.
- Not found: report that the monitor is unavailable to this connection, without guessing another workspace's data.
- Validation, unsupported monitor type, or `402` plan limits: explain the actual restriction; do not change subscriptions or silently alter requested settings.
- `429`: respect returned retry guidance; do not start a retry loop.
- Uncertain creation outcome: list/search before any retry to avoid duplicate monitors. Uncertain run outcome: report uncertainty; do not blindly repeat a network check. Uncertain pause/resume: use `get_monitor` to verify the desired state before retrying.

The server does not expose report generation/approval/publication/download/delivery; delete; general monitor editing; billing; incident management; notification configuration; response bodies; or credentials. Do not manufacture another endpoint to simulate these capabilities.
