# Healthcare Public Data telemetry

This plugin uses the shared plugin and connector telemetry contracts. Do not
create healthcare-only install, link, or invocation analytics events. The
manifest name is `healthcare-public-data`; the canonical analytics plugin ID is
`healthcare-public-data@oai-maintained-plugins`. For analysis spanning the rename,
include the legacy `healthcare-search@oai-maintained-plugins` ID through the
0.1.1 release and the new ID from 0.1.2 onward, plus the connector IDs listed
below.

## Cohort

| App | Connector ID |
| --- | --- |
| ClinicalTrials.gov | `connector_openai_clinical_trials` |
| PubMed | `connector_openai_pubmed` |
| DailyMed | `connector_openai_dailymed` |
| RxNorm | `connector_openai_rxnorm` |
| openFDA | `connector_openai_openfda` |
| NPI Registry | `connector_openai_npi_registry` |
| Medicare Care Compare | `connector_openai_medicare_care_compare` |
| CMS Coverage | `connector_openai_cms_coverage` |
| CMS Open Data | `connector_openai_cms_open_data` |

All nine apps are optional. A plugin install is not a connector connection.

## Product analytics

Use `fact_plugin_product_events` for normalized directory impressions, plugin
page views, install initiated/success/failure/blocked actions, connector
initiated/success/failure actions, and reconciled install/enable/disable/
uninstall lifecycle events. Use `dim_plugin_users` for current installation
state and `dim_plugin_users_history` for date-correct historical state. These
canonical tables retain governed user, workspace, plan, product-surface, and
client dimensions.

The canonical fact does **not** retain the raw `source`, `surface`, or
`error_type` fields from plugin-action events. When acquisition-source or
failure-reason analysis needs them, read the raw Codex/ChatGPT plugin-action
events in a healthcare-filtered query rather than changing the shared fact.
`codex_plugin_install_requested` additionally supplies request/suggestion
context. Do not claim an `@plugin`, `@app`, marketplace-directory, or detail-page
breakdown until the observed source enums and coverage have been validated.

Use `fact_app_message_events` for conversation-level connector use and
explicit, implicit, or unknown invocation attribution. Use
`base_app_turn_calls` for connector/action calls, terminal error context, and
latency. The governed identifiers in these datasets support unique-user,
first-use, retention, and multi-connector analyses without adding identifiers
to metric labels.

Attribution definitions:

- `explicit`: the invoked connector was selected through the user message's
  connector-backed system hint.
- `implicit`: attribution context was available and the connector was not
  explicitly selected.
- `unknown`: the user-message attribution context was unavailable. Never fold
  this cohort into implicit use.

Install-source attribution uses this precedence:

1. `direct`: source/surface is present on the terminal plugin action.
2. `inferred`: a request or page-view event for the same plugin, governed user
   or workspace, product client, and bounded time window is matched to the
   terminal action.
3. `unknown`: no trustworthy match exists.

Every source breakdown must show the `attribution_method` mix and the unknown
rate. Inferred attribution is useful for directional funnel analysis, but must
not be presented as exact request-to-result correlation.

### Adoption metric definitions

| Metric | Definition |
| --- | --- |
| Install attempts | Count of normalized `install_initiated` actions; reconcile against raw install-request events as a coverage check. |
| Successful installs | Count of normalized `install_success`; report events separately from distinct installing users/workspaces. |
| Failed installs | Count of `install_failure` and `install_blocked`, split by bounded raw `error_type` only when populated. |
| Currently installed | Distinct governed users/workspaces with current installed state in `dim_plugin_users`; do not derive this by subtracting aggregate installs and uninstalls. |
| Connector attachment | Plugin installers with a connector-success action or date-correct available/linked app state for one of the nine connector IDs. |
| Activation | An installed user with a first successful healthcare connector call after installation. |
| Time to value | Duration from installation to first successful healthcare connector call. |
| D1/D7/D28 retention | Activated users with another successful healthcare connector call on the exact cohort-relative day. |
| Explicit share | Explicit invocations divided by invocations with known explicit/implicit attribution; always report unknown share beside it. |
| Multi-connector conversation | Conversation with successful calls to at least two distinct healthcare connector IDs. |

The healthcare product view should expose install funnel, current installs,
connector attachment, activation, time to value, DAU/WAU/MAU, D1/D7/D28,
explicit/implicit/unknown use, connector mix, multi-connector conversations,
and source attribution quality. Each query must filter by the exact plugin or
connector cohort above and use an explicit date/hour partition predicate.

## Operational metrics

The shared `apps.connector.invoke` and connector HTTP metrics own request,
success, failure, cancellation, provider status, latency, and action-level
reliability. Use the existing generated **Connectors Breakdown** dashboard's
custom connector selector with one of the exact connector IDs above. **Run
Action** and **Service, MCP, Ecosystem App Breakdowns** remain the detailed
owners for execution and failure-cause investigation. This avoids changing a
shared dashboard generator only to register healthcare names.

Healthcare tools also emit
`ecosystem_apps.healthcare.tool_result`, with only these bounded tags:

- `connector_id`
- `action_name`
- `outcome`: `success`, `empty_success`, `failure`, or `cancelled`
- `failure_class`: `none`, `invalid_argument`, `platform_internal`,
  `upstream_rate_limited`, `upstream_timeout`, `upstream_4xx`, `upstream_5xx`,
  `upstream_malformed_response`, `result_too_large`, `cancelled`, or `unknown`
- `result_shape`: `empty`, `single`, `multiple`, or `unknown`
- `result_count_bucket`: `0`, `1`, `2_10`, `11_100`, `100_plus`, or `unknown`
- `truncated`: `true`, `false`, or `unknown`
- `freshness_bucket`: `future`, `0_1d`, `2_7d`, `8_30d`, `31_90d`,
  `90d_plus`, or `unknown`

The shared tool-invocation alerts provide rate-limit and 5xx failure monitoring
with minimum-volume gates. Do not add a healthcare traffic-absence or paging
alert until production volume has been measured and the Connectors
observability owner has validated the exact live query, grouping, threshold,
and notification route. A later traffic-absence advisory should remain
non-blocking, use a prior-period baseline, and evaluate only connector series
that meet a documented minimum-volume gate.

### Operational review

Review the following in order:

1. Requests, errors, success percentage, empty-result percentage, and p95
   latency for the nine-connector cohort.
2. Connector and action breakdowns for the affected series.
3. Bounded `failure_class`, provider status, rate-limit, timeout, malformed
   response, truncation, and freshness buckets.
4. Existing Run Action, connector HTTP, quota/cache, logs, and deploy views for
   the owning failure domain.

Treat zero-result responses as successful product outcomes. Alert on empty
result rate only after an action-specific baseline shows that a change is
actionable; searches legitimately return no public records.

## Data-quality gates

Before relying on the product view, verify:

- plugin-action event IDs are unique at event grain;
- current installation state is unique at plugin/user/workspace grain;
- connector calls are unique at the documented `base_app_turn_calls` grain;
- direct, inferred, and unknown attribution shares sum to 100%;
- install-request-to-terminal reconciliation is reported as a rate, not hidden;
- source/surface and bounded failure enums are profiled before accepted-value
  checks are enabled;
- daily event volume, unknown attribution, and join coverage are monitored for
  abrupt changes;
- recent partitions are treated as incomplete until the normal source lag has
  elapsed.

## Privacy boundary

Healthcare searches may reveal sensitive interests even though the sources are
public. Telemetry must never contain prompts, search terms, tool arguments,
result bodies, raw URLs or query strings, raw exception messages, result
identifiers, or user/workspace IDs as metric labels. The result metric derives
only counts, booleans, and age buckets from typed response models. User and
workspace identifiers remain in the governed analytics event pipeline only.
