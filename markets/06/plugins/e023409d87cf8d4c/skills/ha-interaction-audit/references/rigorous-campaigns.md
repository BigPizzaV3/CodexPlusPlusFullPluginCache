# Rigorous interaction campaigns

## Coverage contract

Use this procedure for broad/deep audits. Start with the user's journeys and consequences, then assess every family in the catalog. Do not use a fixed assertion count as a stopping rule. Preserve a small fast regression pass, then execute the applicable independent deep passes. A timer dashboard deserves sustained timer usability; a climate dashboard deserves exact setpoint/target and confirmation semantics; neither needs fictional recipe tests.

`new_audit.py` writes `campaign.json` with every family unassessed. Each family must become `applicable`, `excluded` with a concrete reason, or `blocked` with the exact missing capability. Map applicable families to case IDs. A case contains `id`, `assertionId`, `passId`, `profile`, `risk`, `precondition`, `action`, `expected`, `oracle`, `inputMode`, `evidence`, and `dependsOn`. Use the real ledger assertion ID and execution profile, not an aspirational test title. List mapped IDs in each pass's `audit.json` plan. Keep expected-plan files for all passes and compare them with the campaign before the final report.

Run `scripts/validate_campaign.py <workspace>/campaign.json`. It checks schema, complete family assessment, evidence plans, mappings, duplicate execution keys and dependency cycles. Exit 0 means the plan is ready; it does not mean any action ran or any dashboard passed. The script cannot judge whether an exclusion is sensible or an oracle is independent. Review those decisions. A blocked family prevents an unqualified complete-audit claim even if runnable cases pass.

For every critical/high-consequence workflow, require a successful journey, invalid/denied action, cancellation, delayed or failed response, relevant state change, unrelated update, repeated input, and reload/navigation durability when promised. Add accessible operation and a relevant narrow/touch profile. Mark unsupported native paths as gaps. Use lower-risk pairwise combinations after critical cases; check selected three-way combinations where shared state or timing creates a plausible interaction. Do not claim exhaustive state-space coverage.

## Independent model and realistic actions

Define a small reference state independently of the app: route, selected record ID, draft revision, committed revision, latest request ID, timer deadline, and cancellation token as applicable. Derive expected transitions from intended behavior and data contracts. Do not copy the app's implementation into the oracle or read its current property to invent the expected value.

`sequence-engine.mjs` provides `generateSequence({seed,length,initial,commands})`. A command has a unique `id`, pure `enabled(model)`, pure `next(model,args)`, optional `generate(model,random)`, and positive `weight`. It generates legal commands and concrete arguments without interacting with HA. Record every generated action, not just the seed. A seed reproduces the planner; actual browser/network scheduling still needs a recorded release schedule and action trace.

The Browserless suite receives `advanced` with `generateSequence`, `runModelSequence`, `minimizeFailure`, and `assessTemporalTrace`. Run model sequences using `perform(action)` for permitted browser input and `observe()` for serializable evidence. Each independent invariant returns `{pass:boolean,evidence:{expected,actual,...}}`. The engine checks initial state and every completed action. If initial state fails, diagnose setup before claiming the first action caused the defect. It classifies invalid command guards and harness exceptions separately from observed contract failures. Observe transient behavior separately while an action is in flight; an after-action check alone misses it.

Begin with hand-authored critical journeys and targeted race pairs. Then use a few explicit seeds and short bounded sequences covering actual missing transitions. Expand only to resolve an untested meaningful interaction. Track transition/branch coverage, sequence lengths and repeated executions separately. A random tap storm with no reference model is not rigorous testing.

## Controlled response ordering

The fixture exposes `faults`, connected to `createMockHass({faults,...contracts})`. Arm exact surface/key rules before the relevant browser action:

```js
await page.evaluate(() => window.__HA_AUDIT.faults.arm({
  surface:'api', key:'PUT audit/record', mode:'hold-after'
}));
// Use a browser-driven Save action here, then observe pending UI.
const held = await page.evaluate(() => window.__HA_AUDIT.faults.snapshot());
// After a second action or observation, release the recorded ready request ID.
await page.evaluate(id => window.__HA_AUDIT.faults.release(id), held.pending[0].id);
```

Rules are consumed FIFO among exact surface/key matches. They do not supply missing mock contracts. `hold-before` delays execution of the contract; `hold-after` executes it and holds the result. Wait for the held request's `ready` flag before release. Use two rules and release the second ready request first to reproduce reversed delivery. Preserve request IDs and every phase in evidence.

`reject-before` rejects without executing the handler. `commit-then-reject` executes the handler then rejects the response, modeling lost acknowledgment. A release can use `outcome:'reject'` or `'commit-then-reject'` as well. A handler error records commit status as unknown because a handler may have partially changed its store. Inspect actual store state. The helper does not fabricate HTTP status bodies; explicit contracts must return/throw the shapes the app expects.

Test cancel/unmount, retry, back/new intent, and reconnect around these boundaries. Do not assume retrying a device action is safe after a lost acknowledgment. Assert an app's documented idempotency/reconciliation policy against exact payloads and store effects. A service response is not confirmation that a real device changed.

Finish each scenario with no unexplained held requests or unconsumed fault rules; the runner checks these in its mock-contract gate. `dispose()` rejects held promises and clears rules; it cannot roll back executed writes or interrupt arbitrary asynchronous handler code. Keep mock commits synchronous when modeling an atomic operation, and split async phases explicitly when testing partial completion. Use one fault controller per mock unless sharing and teardown ownership are deliberately modeled.

## Timing boundaries and replay

Exercise a meaningful action just before, at, and after a known debounce/restore/expiry boundary. Verify actual event ordering using monotonic timestamps; requested delay is not evidence the action hit the boundary. For deliberately immediate input, do not silently run a helper that waits away the race. First establish the control is reachable, then perform the scheduled real input and record whether it landed. A missed hit is ambiguous/harness evidence, not an automatic product defect.

Minimize a confirmed failure with `minimizeFailure({sequence,replay,signature,maxReplays})`. `replay` must reset a fresh contained fixture, perform the sequence, return the model result, and close its owned context. It must preserve source, fixture, profile, controlled timing and fault schedule. The reducer requires the same failure signature, confirms baseline twice, rejects invalid sequences and searches bounded contiguous deletions. It reports its budget; it does not prove a globally minimal case. Preserve the original and reduced trace. Never remove prerequisites or replace actions with state assignment to make reproduction convenient.

## Multi-session, lifecycle and completion

Treat reload, component remount, a new tab in the same context, and a new context as different persistence boundaries. The starter runner owns one page. Multi-tab testing requires an explicit adapter/runner extension applying containment to every new page before app code and sharing only synthetic backend state. Do not claim the starter already models it. Test version conflicts, stale subscription events, corrupt storage, storage failure, role change and removed entities when relevant. No production browser storage corruption or permission changes.

Use staged soak passes with actual elapsed duration, action counts, pending queues, timer/subscription/listener ownership and resource trends. A heap snapshot alone is not a leak; compare warmed repeat cycles under consistent conditions. A 30-second pass repeated independently is not an uninterrupted background-hour test. Save checkpoints below observed tool deadlines and resume explicitly. Complete only when required cases ran with valid evidence, all remaining failures are classified, source parity holds, and gaps are named.
