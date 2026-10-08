# Monitoring and controlled refresh

Monitoring keeps the continuity package trustworthy between full audits. It must detect change without turning an observation into approved truth or expanding access authority.

## Monitoring layers

1. **Source coverage** — identify every source whose change can invalidate a critical record: local files, repositories, deployments, task systems, cloud storage, domains, accounts, contracts, vendors, backups, finance records, people, and physical assets.
2. **Signals** — define observable evidence for each source: inventory delta, commit/release, export timestamp, API response, provider notice, renewal date, owner attestation, restore result, or manual inspection.
3. **Detection** — compare the signal with the last approved baseline and apply a delta status.
4. **Review** — route each material delta to an owner with evidence, deadline, impact, and approval requirement.
5. **Reconciliation** — update the controlled record only after the evidence and authority requirements are satisfied.
6. **History** — retain the previous approved state, reason, source, approver, affected records, and rollback reference.

## Source monitor contract

For each source record:

- stable monitor ID and covered continuity records;
- source and canonical locator;
- owner and backup owner;
- sensitivity and permitted audience;
- collection method: local scan, authorized connector/API, export, webhook/event, notification, or manual review;
- credential reference and minimum permission when a connector is used, never the credential itself;
- event triggers and scheduled fallback cadence;
- expected signal and comparison method;
- last successful observation and evidence;
- stale-after and due-soon thresholds;
- failure behavior, retry boundary, escalation, and manual fallback;
- whether the monitor is configured, reachable, tested, paused, or merely proposed;
- approval policy for updating the canonical record;
- retention and audit-log rule.

Do not label a proposed connector or written schedule as active monitoring. `ACTIVE_TESTED` requires evidence of a successful observation and a verified route into the review queue.

## Delta statuses

- `NEW`: observable item absent from the approved baseline.
- `CHANGED`: reliable evidence proves the item differs from baseline.
- `POSSIBLY_CHANGED`: metadata differs but content-level proof is unavailable.
- `REMOVED_OR_INACCESSIBLE`: baseline item cannot be observed; distinguish verified deletion from access failure before reconciliation.
- `UNCHANGED`: comparison method found no material difference.
- `STALE`: its maximum verified age has expired.
- `DUE_SOON`: it is inside the configured warning window.
- `CONFLICTING`: sources disagree about current truth.
- `REQUIRES_REVIEW`: the effect or authority cannot be resolved automatically.

Never infer deletion from a missing API response, expired permission, moved path, provider outage, or incomplete scan.

## Safe automation classes

### May be automated after configuration and authorization

- read-only inventories, hashes, repository commit/release observations, expiry calculations, link/access checks, export age checks, backup-job evidence collection, and review-queue generation;
- reminders and reports that remain inside the approved audience;
- creation of a proposed snapshot that cannot replace the approved baseline by itself.

### Require review before controlled truth changes

- purpose, ownership, responsibility, current operational status, selected architecture, business decisions, contractual meaning, risk acceptance, legal/compliance conclusions, and removal of canonical records;
- any ambiguous or conflicting evidence;
- any change that would cause downstream automation or external action.

### Never automate merely for documentation upkeep

- password or MFA changes, recovery flows, role/permission changes, production deployment/failover, payments, contract acceptance, public communication, deletion, destructive migration, or transmission of restricted data.

## Cadence model

Use both event-driven and scheduled checks. Event triggers reduce delay; scheduled checks catch missed events and silent drift.

- Immediate or next-run: security incidents, lost devices/accounts, production changes, critical ownership or access changes, failed backups, releases, migrations, contractual commitments.
- Weekly where active: current work, blockers, next actions, release/deployment state, unresolved review queue.
- Monthly or risk-based: critical accounts, providers, integrations, exports, backup evidence, domain/license/renewal horizon.
- Quarterly or risk-based: role coverage, contracts, architecture maps, recovery dependencies, data and retention maps.
- Semiannual or risk-based: clean-room continuation and representative restore/rebuild drill.
- Annual minimum: full declared-scope audit, provided no domain requires a shorter interval.

These are starting points, not proof that a cadence is appropriate. Shorten them for high change velocity, high impact, regulation, short RTO/RPO, or poor historical reliability.

## Review queue contract

Each queue item requires:

- queue ID, detected timestamp, monitor/source, affected record IDs;
- baseline observation and current observation;
- delta status, evidence locator, comparison method, and confidence;
- operational/recovery impact and urgency;
- proposed disposition: verify, update, supersede, archive, relink, investigate, accept risk, or no change;
- owner, reviewer/approver, due date, dependencies, and required authority;
- status: open, investigating, awaiting evidence, awaiting approval, approved, rejected, applied, or closed-no-change;
- reconciliation evidence, approved baseline version, and change-log reference after closure.

The monitor may propose a disposition. It may not approve its own interpretation.

## Scheduler and connector truth

Record scheduler platform, task identifier, owner, timezone, frequency, input scope, output destination, last run, last success, failure notification, retry limit, and pause/disable procedure. Record connected source, permission scope, credential reference, rate limit, export/exit path, privacy boundary, and revocation procedure.

If no scheduler or connector exists, output an implementation-ready proposal and manual checklist. Do not claim that future runs will occur.

## Refresh transaction

For every approved update:

1. confirm authority and source freshness;
2. preserve the prior approved record or snapshot;
3. update the smallest controlled surface;
4. propagate only to registered dependents;
5. validate links, manifests, current-state summaries, recovery steps, and next actions;
6. record approver, reason, evidence, affected records, version, timestamp, and rollback path;
7. mark the queue item applied only after verification.

If propagation cannot be completed, mark the package `PARTIALLY_RECONCILED` and list every inconsistent dependent.

## Monitoring health report

Report separately:

- source coverage: monitored, manual, inaccessible, or absent;
- monitor health: active-tested, active-failing, stale, paused, proposed, or unknown;
- detection results by delta status;
- overdue reviews and unresolved critical deltas;
- last approved baseline and reconciliation date;
- false-positive/false-negative limitations;
- exact next safe actions.
