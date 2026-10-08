# SECOND BRAIN MAINTENANCE CONTROL — {{COMPANY_OR_PROJECT}}

## Control status

- Declared scope: {{SCOPE}}
- Approved baseline version: {{VERSION}}
- Baseline approved at: {{DATE_TIME_TIMEZONE}}
- Maintenance owner: {{OWNER}}
- Backup owner: {{BACKUP_OWNER}}
- Scheduler status: {{ACTIVE_TESTED_ACTIVE_FAILING_PAUSED_PROPOSED_NONE}}
- Overall monitoring status: {{PASS_PASS_WITH_RISKS_NOT_OPERATIONAL}}

## Source monitoring register

| Monitor ID | Source / locator | Covered records | Method | Owner / backup | Event trigger | Fallback cadence | Stale after | Status | Last success | Evidence | Failure escalation | Approval policy |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| MON-001 | {{SOURCE}} | {{RECORD_IDS}} | {{SCAN_CONNECTOR_EXPORT_EVENT_MANUAL}} | {{OWNERS}} | {{TRIGGER}} | {{CADENCE}} | {{THRESHOLD}} | {{STATUS}} | {{DATE}} | {{EVIDENCE}} | {{ESCALATION}} | {{POLICY}} |

## Scheduler register

| Task ID | Platform | Timezone / cadence | Input scope | Output destination | Owner | Last run / success | Failure notice | Retry limit | Pause procedure | Test evidence |
|---|---|---|---|---|---|---|---|---|---|---|
| JOB-001 | {{PLATFORM_OR_PROPOSED}} | {{SCHEDULE}} | {{SCOPE}} | {{DESTINATION}} | {{OWNER}} | {{RUN_STATUS}} | {{NOTICE}} | {{LIMIT}} | {{PROCEDURE}} | {{EVIDENCE}} |

## Change review queue

| Queue ID | Detected | Source | Affected records | Delta status | Baseline → current | Evidence / method | Impact / urgency | Proposed disposition | Owner / approver | Due | Status | Reconciliation evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| CRQ-001 | {{DATE}} | {{SOURCE}} | {{RECORD_IDS}} | {{DELTA}} | {{OBSERVATIONS}} | {{EVIDENCE}} | {{IMPACT}} | {{PROPOSAL}} | {{OWNERS}} | {{DUE}} | {{STATUS}} | {{EVIDENCE_OR_PENDING}} |

## Freshness register

| Record ID | Owner | Last verified | Maximum age | Warning window | Computed state | Evidence | Required action | Due |
|---|---|---|---|---|---|---|---|---|
| {{ID}} | {{OWNER}} | {{DATE}} | {{DAYS}} | {{DAYS}} | {{CURRENT_DUE_SOON_STALE_INVALID}} | {{EVIDENCE}} | {{ACTION}} | {{DUE}} |

## Reconciliation log

| Date | Queue ID | Approved change | Previous baseline | New baseline | Approver | Affected records | Validation | Rollback reference |
|---|---|---|---|---|---|---|---|---|
| {{DATE}} | {{QUEUE_ID}} | {{CHANGE}} | {{OLD}} | {{NEW}} | {{APPROVER}} | {{RECORDS}} | {{EVIDENCE}} | {{ROLLBACK}} |

## Monitoring gaps and limitations

| Gap | Cause | Possible missed change | Risk | Manual fallback | Owner | Due |
|---|---|---|---|---|---|---|
| {{GAP}} | {{CAUSE}} | {{MISS}} | {{RISK}} | {{FALLBACK}} | {{OWNER}} | {{DUE}} |
