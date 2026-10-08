# Release Readiness and Regression Framework

## Purpose

Use this file to scope regression, define release gates, and make a justified release decision.

# 1. Release scope

Capture:
- release/build;
- changed features;
- affected services/components;
- schema/config/dependency changes;
- supported browsers/devices;
- intended audience;
- rollback path.

Do not test unrelated areas by habit.

# 2. Blast-radius regression

For each change classify:

## Must retest
Directly affected behavior.

## Targeted regression
Adjacent flows/dependencies likely to be affected.

## Smoke only
Important but low-coupling areas.

## Out of scope
No meaningful dependency on the change.

# 3. Smoke suite

A release smoke suite should prove:
- app loads;
- auth works if required;
- primary journey works;
- critical write/read path works;
- major dependency is reachable;
- monitoring/health is normal.

Keep smoke tests short enough to run reliably after deployment.

# 4. Release gates

Possible gates:
- required journeys pass;
- no P0/P1 defects;
- accessibility-critical flows verified;
- performance budget/SLO acceptable;
- security-critical checks pass;
- dependencies reviewed;
- migrations verified;
- deployment succeeds;
- rollback ready;
- monitoring active.

Match gates to release risk.

# 5. Deployment safety

Check:
- artifact/version;
- config/environment;
- secrets;
- migrations;
- feature flags;
- environment protections/approvals;
- rollback/forward fix;
- observability.

A green test suite is not proof of safe deployment.

# 6. Staged rollout

For risky changes consider feature flag, canary, percentage rollout, limited beta, or environment promotion.

Define success signal, observation window, and rollback trigger.

# 7. Post-release verification

After deploy verify:
- health/errors;
- primary journey;
- critical API;
- auth;
- data writes;
- major integration;
- performance;
- alerting.

Deployment success does not equal application success.

# 8. Release verdict

## Ready
Evidence is sufficient and no material blocker remains.

## Ready with known limitations
Limitations are documented, bounded, and acceptable for intended scope.

## Not ready
A material blocker remains.

# 9. Known limitations

For each accepted limitation record:
- issue;
- affected users;
- workaround;
- risk;
- owner;
- follow-up date/trigger.

# 10. Final report

A concise release report can use:

## Verdict
## P0/P1 blockers
## Important P2 issues
## Evidence completed
## Evidence still missing
## Known limitations
## Rollback readiness
## Post-release monitoring

Keep it decision-oriented.
