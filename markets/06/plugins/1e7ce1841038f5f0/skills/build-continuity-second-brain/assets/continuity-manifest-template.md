# CONTINUITY MANIFEST — {{COMPANY_OR_PROJECT}}

## Scope and control

- Manifest version: {{VERSION}}
- Scope: {{SCOPE}}
- Owner: {{OWNER}}
- Backup owner: {{BACKUP_OWNER}}
- Last reconciled: {{DATE_TIME_TIMEZONE}}
- Next review or event trigger: {{REVIEW}}
- Classification: {{CLASSIFICATION}}

## Critical capability register

| ID | Capability | Impact | Owner / alternate | Canonical source | Dependencies | RTO | RPO | Recovery status | Last test | Evidence | Gap / next action |
|---|---|---|---|---|---|---|---|---|---|---|---|
| CAP-001 | {{CAPABILITY}} | {{IMPACT}} | {{OWNERS}} | {{SOURCE}} | {{DEPENDENCIES}} | {{RTO_OR_UNDEFINED}} | {{RPO_OR_UNDEFINED}} | {{STATUS}} | {{DATE_OR_UNTESTED}} | {{EVIDENCE}} | {{GAP}}

## Artifact and source-of-truth register

| ID | Artifact/system | Purpose | Canonical locator | Version/state | Truth status | Owner | Sensitivity | Last verified | Update trigger | Dependencies | Recovery importance | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ART-001 | {{ARTIFACT}} | {{PURPOSE}} | {{LOCATOR}} | {{VERSION}} | {{TRUTH_STATUS}} | {{OWNER}} | {{CLASS}} | {{DATE}} | {{TRIGGER}} | {{DEPENDENCIES}} | {{IMPORTANCE}} | {{EVIDENCE}}

## Account and access recovery register

| ID | System | Purpose | Workspace/org | Owner / alternate | Role coverage | Secret-manager item reference | Recovery route | Identity/domain dependency | Last reviewed | Risk/gap |
|---|---|---|---|---|---|---|---|---|---|---|
| ACC-001 | {{SYSTEM}} | {{PURPOSE}} | {{WORKSPACE}} | {{OWNERS}} | {{ROLES}} | {{REFERENCE_NOT_SECRET}} | {{ROUTE}} | {{DEPENDENCY}} | {{DATE}} | {{GAP}}

## Backup and restore register

| ID | Protected asset | Method | Location/provider class | Owner | Frequency | Retention | RPO/RTO | Last success | Last restore test | Integrity evidence | Fallback | Gap |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| BAK-001 | {{ASSET}} | {{METHOD}} | {{LOCATION}} | {{OWNER}} | {{FREQUENCY}} | {{RETENTION}} | {{OBJECTIVES}} | {{DATE}} | {{DATE_OR_UNTESTED}} | {{EVIDENCE}} | {{FALLBACK}} | {{GAP}}

## Current work and continuation

| ID | Work item | Current state | Evidence | Owner | Dependency | Blocker | Approval needed | Exact next safe action | Definition of done |
|---|---|---|---|---|---|---|---|---|---|
| WRK-001 | {{ITEM}} | {{STATE}} | {{EVIDENCE}} | {{OWNER}} | {{DEPENDENCY}} | {{BLOCKER}} | {{APPROVAL}} | {{NEXT}} | {{DONE}}

## Coverage summary

| Domain | Status | Evidence | Critical gaps | Owner | Due/review trigger |
|---|---|---|---|---|---|
| {{DOMAIN}} | {{COVERED_PARTIAL_MISSING_INACCESSIBLE_STALE_CONFLICTING_UNTESTED_NA}} | {{EVIDENCE}} | {{GAPS}} | {{OWNER}} | {{TRIGGER}}

## Verification log

| Test/drill | Scope | Date/environment | Result | Evidence | Assistance required | Failure/corrective action | Retest due |
|---|---|---|---|---|---|---|---|
| {{TEST}} | {{SCOPE}} | {{DATE_ENV}} | {{RESULT}} | {{EVIDENCE}} | {{ASSISTANCE}} | {{ACTION}} | {{DUE}}

## Change log

| Date | Change | Reason | Evidence | Approved by | Affected records | Follow-up |
|---|---|---|---|---|---|---|
| {{DATE}} | {{CHANGE}} | {{REASON}} | {{EVIDENCE}} | {{APPROVER}} | {{RECORDS}} | {{FOLLOW_UP}}

