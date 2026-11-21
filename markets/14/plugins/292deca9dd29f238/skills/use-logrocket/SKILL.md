---
name: use-logrocket
description: Investigate LogRocket session replays, user behavior, issues, recorded network requests, and product analytics through the LogRocket MCP server. Use when the user shares a LogRocket link, reports a problem in their app, wants to triage issues, asks about feature usage, or wants to check for a regression using recorded data.
---

Use the connected LogRocket MCP server. Discover the available tools and their current input schemas before calling them; the exposed tools depend on the connection's scope and toolsets.

## Select the project and time range

Infer organization and project IDs from a supplied `<organizationID>/<projectID>` App ID or LogRocket link. Otherwise use `list_organizations`, then `list_projects`. If discovery returns multiple candidates, ask which organization or project to use. A scoped connection may hide these discovery tools and omit the corresponding ID inputs; honor its scope.

Resolve relative dates using the user's current date and timezone. Include a concrete time range in queries and use ISO 8601 datetimes with offsets for structured date inputs.

`build_metric`, `get_metric`, and `use_logrocket` accept an optional IANA `timezone` that aligns time buckets to that timezone's calendar. Pass the timezone the user asks for, or otherwise the one they are working in when known. If it is unknown, omit it; a UTC offset alone does not identify a timezone. If the connection sets a default timezone, pass one only when the user asks for a different timezone. With neither, buckets align to UTC.

## Choose the tool

| Need | Tool and guidance |
| --- | --- |
| Locate sessions for a user, event, page, error, or date range | `find_sessions` with a precise natural language query. Results provide recording IDs, session IDs, session URLs, and the filters used (`metricDefinition`). Inspect those filters to check that the query matches the request. |
| Understand behavior or extract context from known sessions | `watch_sessions` with a focused query per session. Use IDs from a supplied link or returned session data, passing session IDs as integers. Sessions are analyzed independently. |
| Retrieve recorded network data | `get_network_entries`; prefer it when only network data is needed. Filter by URL, method, status, or time where useful. To investigate across sessions, find the sessions first, then query each. |
| Query a saved metric link | `get_metric` with the full `metricURL`, `startDate`, and `endDate`. This uses the saved definition. Heatmap and path analysis metrics are unsupported. |
| Run new aggregate analytics | `build_metric` with a natural language query. Check the returned metric definition, filters, grouping, and time range before interpreting the data. |
| Find and prioritize issues | `find_issues` with structured time, severity, type, and triage filters, optionally refined by a natural language query. Existing issue analyses are returned inline when available. |
| Broader investigation without a better dedicated tool | `use_logrocket` with a natural language query; include full resource URLs supplied by the user. |

If a dedicated tool is unavailable because the connection restricts toolsets, use `use_logrocket` only if exposed and suitable. Explain missing capabilities rather than inventing tools.

## Complete asynchronous work

`use_logrocket` may return `status: thinking`. Share meaningful progress, keep its `chatID`, and continue calling it with that ID and `pollForResult: true` until completion. Omit the query while polling. Reuse a completed conversation's `chatID` only for a related follow-up; omit it for a new investigation. Queries can take up to ten minutes.

`watch_sessions` returns `pendingResults` and `completedResults`. Accumulate completed results across calls. Poll with `pollForResults: true` and only the remaining fingerprints, omitting `sessions`; do not resubmit the original analyses. Continue until none remain, checking each completed result's `ok` flag. Report failures as failures, not evidence of an application defect. If interrupted or unable to continue, report the pending work and preserve its handles for resumption.

## Interpret results accurately

- Network results contain `total`, `offset`, `limit`, and `har`. If `offset + limit < total`, fetch further pages needed for the request. Disclose partial coverage. HAR data merges browser tabs; `pageref` identifies the tab. Truncated values, missing cookies or timings, and permission-hidden headers or bodies are collection limits, not proof of a bug. Return only network details relevant to the investigation; avoid unnecessarily reproducing secrets or personal data.
- Issue searches default to severe, untriaged issues over the last week. Set `severity: any` and appropriate `triageStatuses` when broader coverage is requested. Issue history is limited to 30 days; an older or empty query cannot establish that no issues occurred. `eventCount` approximates affected sessions, not distinct users. Distinguish an existing AI analysis from independently observed evidence.
- Request `get_metric.sessionLimit` only when example sessions are needed. Tables and retention metrics do not return example sessions. For funnel cohorts, `funnelStep` is zero-based; `DROPPED_OFF` means completed that step but not the next, while `REACHED` means reached at least that step. The final step has no drop-offs.
- Use returned full-range metric values when available; unique users and other non-additive aggregates cannot be reconstructed by summing buckets. Inspect funnel definitions to distinguish session counts from users in cross-session funnels. Describe selected sessions as samples rather than exhaustive populations.

## Ground the investigation

For a user-reported problem, locate relevant sessions, analyze the relevant moments, inspect network evidence when useful, and correlate with issues or aggregate data as the question requires. For regression checks, compare consistent cohorts and time windows before and after the change; separate correlation from causation. If source code is available, connect the evidence to concrete code paths before proposing a fix.

Cite returned session, issue, and metric links near the claims they support. Cite useful session key frames using their provided screenshots or timestamps. A session moment URL has the form `https://app.logrocket.com/<organizationID>/<projectID>/s/<recordingID>/<sessionID>?t=<videoTime>`; use actual returned values. Preserve supplied resource hosts and never invent IDs or evidence.

Summarize the finding, supporting evidence, impact, uncertainty, and practical next action. Clearly distinguish observations from hypotheses and state coverage limits. These tools query and analyze recorded data; do not claim to change issue triage states, save metrics, or fix application code merely by calling them.

For connection setup and supported URL options, consult the package README and [LogRocket MCP documentation](https://docs.logrocket.com/docs/mcp).
