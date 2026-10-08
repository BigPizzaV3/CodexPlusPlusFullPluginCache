# Event Quality Score

EQS is a 0–10 diagnostic of conversion-event signal quality for a website conversion source. It is computed automatically from received evidence; advertisers do not install, enable, edit, or manually recalculate the score. Instrumentation setup is separate. EQS is not a match rate, attributed conversion count, ad performance prediction, or guarantee of better delivery.

## Read The Assessment

Use only tools allowed by the active skill. Resolve one accessible account and use `list_conversion_sources` to identify source names and **source `id` values, not `pixel_id` values**. Call `get_conversion_event_quality` for the requested sources, at most 100 per call. Read additional batches only when needed for the requested scope. If the tool is absent or access is denied, explain that account-specific EQS cannot be retrieved here; do not infer a score or recommend reconnecting with write permissions.

Report each source's returned score, status, warnings, score date, and relevant assessment window. Preserve zero as a valid score. For null scores, explain the returned reason: `low_volume` means insufficient scoring volume; `no_active_goals` means no active conversion goals; `no_attribution_evidence` means insufficient attribution evidence; `unavailable` means no usable assessment was returned. None of these statuses means a zero score or proves broken tracking. Do not invent reasons beyond the returned evidence.

The tool returns the latest available daily assessment, based on seven complete UTC days with a receipt-maturity day. Use its returned timestamps; do not substitute the current date or an account-local reporting window. It does not accept custom date ranges or return historical trends. An old assessment is dated evidence, not a current or real-time score. Do not reconstruct a score from recent-event samples, warning counts, or coverage percentages.

Request `include_user_data_coverage=true` only when identifier detail is useful. Pixel and CAPI coverage have separate counts and a separate returned window. A field's presence rate is `present_event_count / eligible_event_count` only when `eligible_event_count > 0` and `observed_event_count == eligible_event_count`. Otherwise label coverage unavailable or incomplete; do not report zero or compute a percentage from partial observations. Presence does not establish matching or attribution. Never request or display raw identifier values.

## Recommend The Smallest Supported Check

In Review, tie suggestions to returned warnings and describe them as investigations, not confirmed causes or promised score improvements:

| Warning | Suggested check |
| --- | --- |
| `low_strong_identifiers` | Check whether eligible events include supported, correctly formatted strong identifiers when available and permitted. |
| `low_click_reference_coverage` | Check that the supported click reference is preserved and forwarded with relevant events. |
| `delayed_server_events` | Check server-event send delays and timestamps. |
| `low_cleanup_survival` | Inspect event validation, rejection, and deduplication diagnostics. |
| `high_event_concentration` | Investigate repeated or overly concentrated events; do not assume fraud. |
| `low_additional_identifiers` | Check supported additional user-data fields when available and permitted. |
| `limited_funnel_events` | Check whether relevant, genuine funnel events are being sent. |
| `limited_connection_coverage` | Review whether browser and server connections cover the intended events. |
| `low_goal_volume` | Verify intended conversion goals and allow more genuine goal evidence to accumulate. |

Unknown warnings can be reported without inventing their meaning. Do not fabricate events or recommend extra collection merely to raise EQS. The connector cannot install or change Pixel/CAPI, matching, identifiers, or click-reference forwarding. Keep recommendations manual, and use current Help Center guidance for setup details. Low EQS alone does not justify campaign, bid, budget, or targeting changes.
