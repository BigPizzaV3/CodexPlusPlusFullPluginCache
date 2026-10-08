# Repair and regression

Use only when fixes are requested or already authorized. Preserve exact restrictions and approved items. Do not ask again simply because this reference says to verify authorization.

## Recovery and patch ownership

Read current source immediately before changes. Save exact bytes of affected code/config and verify recovery files exist with matching hashes. A timed-out backup call is not a verified backup. Prefer the smallest recovery unit; use a full system backup only when justified by scope. Keep backups outside web-served paths if they contain private information.

Identify the authoritative implementation and downstream overrides. Fix source ownership rather than adding another patch to a patch when feasible. If an additive layer is the narrowest safe choice, document its load order, compatibility, identity, and removal path. Avoid registering the same class/listener more than once. Do not delete seemingly dead code until consumers and lazy imports are checked.

## Change and verification sequence

1. Retain a minimal failing reproduction and its original expected outcome.
2. Implement the scoped fix locally/in the isolated fixture. Keep production data and behavior out of the test store.
3. Demonstrate the reproduction now passes. Retest associated race windows, error behavior, and prior regressions that share changed logic.
4. For a major change or an explicit full-rerun request, rerun the declared full suite on the same candidate version. For a small isolated fix, use the smallest sufficient impacted regression set and disclose its scope.
5. Deploy only if authorized and the required gates pass. Verify actual resource registration/order and fresh code loading, not just that a file write succeeded.
6. Render affected live routes read-only; check new logs/traces since the change where relevant. Do not manufacture device activity merely to validate a frontend change.
7. Run required post-deployment fixture regressions against newly verified source bytes. Report simulation and live integration results separately.

If a required gate fails, pause deployment and preserve the candidate/evidence. If an authorized deployment produces a new severe issue, revert only the owned change when safe. Do not overwrite intervening user edits. Restoring a whole system backup is not a default response to one JavaScript defect.

## Regression principles from the reference audits

- Avoid replacing a whole editor DOM for unrelated HA events; update relevant pieces and preserve legitimate draft state.
- Restore focus/caret, expanded details and the correct scroll containers when redraw really is needed.
- Resolve route restoration conflicts with explicit ownership/cancellation; latest user intent wins over old async work.
- Handle nested controls once through clear event delegation or propagation policy. Avoid broad suppression that breaks accessibility.
- Verify slider preview/cancel/Apply semantics from actual request logs, not just labels.
- Preserve timer deadlines and clear expired/cancelled state exactly once when persistence is promised.
- Do not use massive CSS offsets, global touch locks or universally longer sleeps as substitutes for diagnosing containing blocks and race conditions.

These are candidates to investigate, not universal required implementation patterns.
