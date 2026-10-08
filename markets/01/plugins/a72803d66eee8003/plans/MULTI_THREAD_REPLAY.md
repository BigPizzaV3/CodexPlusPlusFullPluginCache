# Multiple threads in the existing Replay flow

## Agreed behavior

- Select one or more threads in the existing picker, then choose models once.
- Keep each thread's historical setup and approval checks. Multiple selected
  threads replay whole conversations; one selected thread keeps the existing
  whole-thread and chunk options.
- Prepare every selected configuration before approving the batch. Each
  thread/model runs in its own existing isolated workspace.
- The controller owns the queue and applies the existing limit of eight active
  model runs. Closing or reloading the browser does not discard queued work.
- Make each completed report available immediately. The Results surface offers
  all-thread totals and the existing individual comparison, while pending runs
  continue. Refreshing results must not change the user's selected report.
- Aggregate separately for each Codex model. Sum paired, comparable historical
  and replay task costs; report coverage and quality outcomes. Missing costs,
  shared historical usage, failures, and pending work do not become zero-cost
  successes. Review overhead is separate from task costs.
- Keep failed and cancelled entries visible. Reload restores the same run set;
  repeated starts do not launch another batch. A controller restart marks
  unfinished work interrupted rather than automatically replaying it.

## Scope

Reuse the controller, configuration, approval, execution, review, and report
surfaces. No automatic sampling, organizational dashboard, or new app entry
point. Aggregate estimates describe the selected tasks, not invoice savings.

Preserve the current invocation telemetry contract: the final observer reports
one model group. A multi-thread batch reports the first selected thread; split
threads retain their existing single-group scope. The controller
and local reports retain every thread; subsequent groups must not overwrite
the observed group's attempt metadata. Expanding warehouse telemetry is separate.

## Validation

Cover single-thread and chunk regressions, batch approval and idempotency,
bounded queue execution and cancellation, paired aggregation, partial-result
navigation and reload. Then install the worktree plugin, invoke it through
Codex, and complete real one-thread and multiple-thread browser runs. Verify
the installed files and MCP ownership before counting either E2E result.
