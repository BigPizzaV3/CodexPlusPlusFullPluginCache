# Review observed evidence toward the mission

Read live profile, execution brief/workspace and relevant previous results, then follow [MCP workflow](mcp-workflow.md). The task is an interpretable decision: repeat, repair or stop based on observed mission-relevant events, effort and uncertainty.

## Define before counting

- **Event:** State the exact behavior that counts. Activation is first meaningful use, not signup. Define a qualified conversation, retained use and paid outcome in the founder's context.
- **Cohort:** Name inclusion/exclusion criteria, recruitment/source and unique people/teams. Avoid duplicate counting across attempts or channels.
- **Window:** State both start/end dates and any retention interval. A future follow-up is not observed retention.
- **Denominator:** State eligible users/visitors/contacted people and missing records. Rates need a known nonzero denominator; when it is unknown, report the rate as unknown.
- **Provenance:** Cite actual authorized data/source/export, check date, method and definitions. Identify founder-reported data separately from direct inspection.
- **Effort/economics:** Include actual hours/cost, period/currency and real variable/support costs when known. Distinguish estimates and assumptions from measured revenue/contribution.

## Preparation and verification

For activation/tracking strategies, produce a concrete operational definition, event/attribution plan and verification evidence. Use an authorized real test journey when possible, exclude internal/test traffic, and check tracking link preservation and duplicate events. A plan is not working instrumentation; inspection alone does not authorize product changes or external tests.

For cohort/launch/partner/retention reviews, show source-backed counts and calculations together with the cohort/window and missing data. Likes, visits, profiles, invitations, scheduled calls, stars and wishlists are separate events from qualified use, real interviews, paid orders or retained customers.

For economics, make assumptions editable and show sensitivity to usage, refunds/fulfillment, fees and support. A forecast is not measured revenue. A useful commercial decision may be defer/repair even when top-line attention increased.

Without analytics access, audit the proposed measurement and actual supplied notes; request the smallest relevant export or observation. Do not turn an unavailable report into a zero.

## Result-write gate

Prepare a summary before any necessary clarification. A summary or notes save leaves the current attempt open. The following are different instructions:

| Founder wording | Intended response |
| --- | --- |
| “Review this experiment” / “save the review” | Analyze and save authorized preparation; no result-ending call |
| “Wrap up this interview task” / “we're done” | Summarize actual progress and missing evidence; clarify recording intent and completed/failed verdict if unclear |
| “Record the actual results as failed/completed” with real outcome data | Use the specified verdict without asking again; reread current attempt/revision and validate measurements before writing |

`record_action_result` ends the current attempt and replaces its outcome. Before calling, require explicit actual-result recording instruction and explicit completed/failed intent, current `attemptNumber` and `outcomeRevision` from `get_action_workspace`, and data matching the tool's live schema. If a conflict occurs, reread/merge the intended outcome only for the same attempt; do not clobber a concurrent result or a new attempt. Verify after saving.

`measuredMetrics` lists only actually measured `visits`, `signups`, `conversations`, `activations`, `qualified`, `retained`, `paying`, `revenue`. Optional unknown metric values stay omitted; unknown required fields may require numeric `0` placeholders outside this list. Clearly label those unmeasured. A measured zero belongs in the list only when the evidence shows zero under its operational definition and window.

Example: the founder confirms no completed interviews during a known window, but analytics was not collected. Under a definition where completed interviews count as conversations, `conversations: 0` with `measuredMetrics: ["conversations"]` can represent a measured zero. Required `visits`, `signups`, `qualified`, `retained` and `revenue` may be zero placeholders outside that list. Do not add those keys to the list or report them as measured zero. Without the founder's confirmation or other actual evidence, the interview count also remains unknown.

Two public discussion sources and five old candidate URLs do not measure completed interviews. Do not infer failed execution, completed status, a useful vote or zero responses from that preparation. Use `record_action_feedback` only for the founder's explicit thumbs-up/down.

## Output

Return real counts/rates and denominators, source/cohort/window, unknowns and limitations, actual time/cost, supported recommendation, effect on the mission and one next step. State whether work was saved, the attempt was explicitly ended, or persistence was unavailable. Never imply that a result draft is a recorded outcome.
