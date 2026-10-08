# Evidence, triage and reporting

## Assertion records

Record stable ID, pass/profile, source fingerprint, suite and adapter hashes, seed, attempt number, input method, prerequisites, expected result, actual result, timestamp/duration and evidence paths. Include route, deepest focus/selection, scroll containers, serialized geometry, relevant events and mock request sequence where useful. Capture a screenshot/trace at failure when the available tool permits it. Screenshots are supporting evidence, not a substitute for an action assertion.

| Status | Meaning |
| --- | --- |
| passed | Executed and observed the stated contract |
| failed | Executed and observed a contract violation; classification still requires triage |
| blocked | Required dependency, access, containment or environment unavailable |
| inconclusive | Action/evidence ambiguous or fixture parity unresolved |
| skipped | Deliberately excluded with an explicit reason |
| not-run | Planned but not reached, including interrupted execution |

Never count a conditional branch that did not run as passed. A catch that swallows an error is not success. Track all relevant runtime/console/network failures; exclusions must be narrow and justified by source, timestamp and relevance. Do not blanket-ignore all 404s, all console errors, or any error containing an overly broad word.

## Failure triage

1. Check preconditions, loaded resource identity, fixture data and expected backend return shape.
2. Confirm active selector, unique target, scroll/reflow timing and hit target. Preserve screenshot/geometry and exact event sequence.
3. Reduce to the smallest fresh action sequence. Retry for a specific question, not until it passes.
4. Compare normal pace and deliberate race conditions. Separate dependent failures from independently reproduced outcomes.
5. Classify as confirmed product defect, harness defect, environment issue, expected behavior or inconclusive. Record why and retain original evidence.

One cause can fail multiple assertions. Do not count assertions as separate defects. A pass on retry remains an intermittent result until explained. Preserve attempt history and reproducibility frequency. If source changes, start a new versioned result set.

## Priority and confidence

Rank by consequence, reach, frequency and recoverability:

- Critical: unintended physical actuation, unauthorized operation or substantial irreversible data loss.
- High: primary workflow broken, save corruption, duplicated consequential actions, unrecoverable draft loss.
- Medium: repeatable navigation/focus/scroll failure, misleading pending state, recoverable operation failure.
- Low: localized cosmetic or usability issue without broken core workflow.

Confidence is a judgment tied to evidence, not a measured probability. For example: high confidence in a twice-reproduced double toggle with matching event trace; moderate confidence in a viewport-specific inference; low confidence in a source-only hypothesis. If the user wants a percent, give a clearly scoped subjective estimate and explain the residual gap. Never assign 99% reliability merely because 139 assertions passed.

## Completion and version integrity

Compute counts from records. Planned equals the sum of all status categories. Show unique assertions separately from total executions, retries and device combinations. Aggregate only compatible source/fixture/suite sets with distinct assertion keys. A changed source fingerprint invalidates affected prior results; retain historical results instead of overwriting them.

The payload builder emits a companion `.expected.json` before execution. Keep one for every planned pass/profile. Supply all of them to `summarize_runs.py <results...> --expected <plans...>` to detect missing whole passes and wrong fixture/suite hashes. Without expected plans the summary covers only supplied pass files and cannot certify campaign completeness. Retain old attempts separately; duplicate assertion keys are rejected rather than silently selecting the latest green attempt.

Persist per-pass results even when later passes fail. On timeout, mark unexecuted IDs not-run, preserve the last checkpoint and stop unsafe work. If the outer provider kills the whole function before it returns, mark that pass interrupted from the coordinator; never fabricate its partial results. Close owned sessions and resume in a fresh context. Check current source identity before continuing.

An audit is complete when its declared coverage has resolved statuses, findings have evidence and scope is explicit. It can be complete with defects or blocked coverage. “All checked behavior passed” requires all required assertions passed and safety/parity gates intact. “No defects anywhere” is never established by a finite suite.

## User report

Lead with the result. Give a compact suite/status table, then prioritized findings with reproduction, expected versus actual behavior, consequence, suspected/confirmed cause, and proposed or completed fix. State live changes actually made, versions, recovery paths, tests actually run, and remaining limitations. Cite saved artifacts/source locations and official docs only for claims they support. Label historical supplied conversation results as historical.

For simulated writes say “N mock mutation intents, all handled in the fixture; X blocked unexpected attempts.” Do not say “zero writes” when mock writes occurred. For live rendering say exactly which routes/profile loaded. It does not imply live mutating workflows ran.

## Checkpoint fields

Use `run_id`, `target`, `mode`, `authorized_scope`, `source_fingerprint`, `suite_fingerprint`, `adapter_fingerprint`, `profile`, `seed`, `completed_passes`, `result_paths`, `findings`, `live_changes`, `recovery`, `owned_sessions`, `last_safe_state`, `next_action` and `interruption_reason`. Save before each production mutation and after each independently meaningful pass. Avoid secrets and live session handles in public artifacts.
