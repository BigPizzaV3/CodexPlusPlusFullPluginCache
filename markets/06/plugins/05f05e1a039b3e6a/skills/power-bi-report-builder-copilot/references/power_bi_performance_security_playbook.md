# Power BI Performance and Security Playbook

## Purpose

Use this file for slow reports, large models, refresh failures, DirectQuery issues, memory pressure, security, and regulated reporting.

# 1. Performance triage

Establish the slow layer:

1. source;
2. Power Query;
3. semantic model;
4. DAX;
5. visual/report;
6. capacity/service.

Do not optimize everything at once.

# 2. Evidence

Useful evidence:
- Performance Analyzer;
- DAX Studio;
- VertiPaq Analyzer;
- Power Query diagnostics;
- source execution plan;
- refresh history;
- Fabric/Capacity monitoring;
- model size/cardinality;
- visual query count.

# 3. Import model checks

Inspect:
- unused columns;
- high-cardinality text/GUID fields;
- data types;
- calculated columns;
- relationship complexity;
- auto date/time;
- large fact grain;
- unnecessary duplicate dimensions.

Remove columns before rows when cardinality/memory indicates that is valuable.

# 4. DAX checks

Look for:
- iterators over large tables;
- repeated expensive expressions;
- unnecessary context transitions;
- high-cardinality filters;
- large virtual tables;
- incorrect relationship reliance.

Optimize only after confirming the measure is correct.

# 5. DirectQuery checks

Inspect:
- source query latency;
- folding;
- generated SQL;
- source indexes/partitioning;
- visuals issuing many queries;
- relationships;
- transformations;
- concurrency.

Do not solve a slow source by blindly adding Power BI capacity.

# 6. Refresh checks

Inspect:
- source extraction time;
- gateway/network;
- Power Query;
- partition strategy;
- capacity/memory;
- concurrent refreshes;
- source throttling.

For incremental refresh, verify that the intended filters fold and partitions behave as expected.

# 7. Paginated performance

Check:
- dataset size;
- parameter selectivity;
- source-side filtering;
- subreports;
- lookup expressions;
- nested data regions;
- repeated dataset executions;
- large images;
- renderer/output.

Export performance can differ from interactive preview.

# 8. RLS/security

Define the authoritative security boundary.

Possible controls:
- source authorization;
- semantic-model RLS;
- OLS/CLS where supported;
- report-level user filtering.

Do not treat report-layout hiding as security.

For paginated reports using `UserID`, confirm identity behavior in the actual execution environment; preview identity can differ from Power BI service identity.

# 9. Regulated exports

For PII/PHI/financial data:
- minimize fields;
- restrict recipients/destinations;
- apply least privilege;
- use approved subscription/delivery routes;
- consider audit/logging;
- avoid exposing sensitive parameter values in URLs.

# 10. No-action case

If correctness is intact, SLA is met, and cost impact is immaterial, do not recommend speculative optimization.

Define the metric/threshold that would justify action.
