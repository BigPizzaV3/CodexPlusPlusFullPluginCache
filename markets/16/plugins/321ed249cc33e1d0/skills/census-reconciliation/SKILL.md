---
name: census-reconciliation
description: Compare saved daily PCC operational occupancy, PCC billable ledger census, facility-recorded census, and CMS-published census using PBJConnect, with differences and coverage.
---

1. Call `connection_status` and resolve requested facilities with `list_facilities`.
2. Use `census_reconciliation` with an explicit inclusive date range of at most 366 days. Split longer requested history into non-overlapping windows. Request each facility page until complete.
3. Keep PCC physical occupancy and PCC billable ledger census separate. Compare them with facility-recorded and CMS-published daily census only on dates with known, compatible evidence.
4. Preserve `null` as unknown. Never fill missing days with zero or a neighboring day's value. Present known patient-day totals with their covered-day counts and requested-day counts.
5. Include retrieval time, replication freshness when known, connector status, and incomplete or provisional classification flags. A record revision time is not proof of replication freshness.
6. Identify the largest returned discrepancies and their dates. Explain whether they are genuine count differences or missing/incomplete evidence. Do not invent a reason for a discrepancy.

The tool reads saved daily summaries and does not start a new SQL pull. If the connector is offline, report the age of saved data. Resident drilldown is not available through this plugin. MDS-derived census may be unavailable; do not substitute PCC ledger counts for it or call them CMS-accepted MDS census.

For staffing analysis, name the denominator and exclude unverified occupancy days from confirmed calculations. Do not claim that a census comparison alone establishes staffing compliance. The portal provides the detailed reconciliation workflow.
