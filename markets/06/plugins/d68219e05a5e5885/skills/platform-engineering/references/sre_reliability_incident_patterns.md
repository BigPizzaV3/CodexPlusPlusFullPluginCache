# SRE, Reliability, and Incident Patterns

## SLI / SLO

Start from user-visible service behavior.

Examples:
- successful requests;
- checkout completion;
- API availability;
- latency;
- freshness;
- job completion.

Define:
- SLI formula;
- eligible population;
- SLO target;
- window;
- exclusions;
- data source.

Avoid SLOs that measure only infrastructure health if user experience can fail independently.

## Error budget

Error budget = allowed unreliability implied by the SLO.

Use it as a decision input for:
- release pace;
- reliability work;
- incident follow-up;
- risk acceptance.

Do not use error budgets as punishment.

## Alerting

Good alerts:
- indicate user/business impact;
- have actionable thresholds;
- have owner/runbook;
- minimize duplicates/noise.

Prefer multi-window burn-rate patterns when the organization's SLO system supports them.

## Incident response

### Impact
What users/services are affected?

### Most likely
Working hypothesis, with confidence.

### First decisive check
Highest-information evidence.

### Containment
Smallest reversible mitigation.

### Root cause
Only after evidence.

### Recovery validation
Confirm:
- error rate;
- latency;
- backlog;
- critical journey;
- dependencies;
- data correctness.

### Follow-up
- corrective action;
- regression guard;
- monitoring;
- runbook;
- ownership.

## Chaos / resilience testing

Use controlled failure testing when:
- blast radius is bounded;
- rollback exists;
- observability is ready;
- stakeholders agree.

Do not inject failure into production merely because chaos engineering is fashionable.
