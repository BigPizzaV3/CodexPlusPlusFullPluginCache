# SQL for BI and Data Modeling

## Purpose

Use this file when SQL feeds Power BI, dashboards, semantic models, marts, extracts, or analytics.

# 1. Define grain

Every output table/view should have an explicit grain.

Examples:
- one row per order line;
- one row per customer per day;
- one row per account current state.

Do not mix incompatible grains in one dataset without a deliberate design.

# 2. Fact and dimension thinking

For reusable analytics, consider:

## Facts
Events/measures at a stable grain.

## Dimensions
Descriptive entities used to filter/group.

Avoid duplicating dimension attributes across many fact outputs when a shared dimension is appropriate.

# 3. Keys

Prefer stable keys.

Preserve business identifiers as text when formatting matters, especially account numbers, ZIP/postal codes, and codes with leading zeros.

Do not cast identifiers to numbers just because they contain digits.

# 4. Dates

Use a consistent date dimension/time grain.

Clarify event date, processing date, fiscal date, and UTC vs local date.

Do not derive local reporting dates from UTC timestamps without an explicit zone rule.

# 5. NULLs

Define whether NULL means unknown, not applicable, not yet available, or missing due to data quality.

Do not replace all NULLs with zero/empty string without business meaning.

# 6. Incremental-friendly SQL

For incremental refresh/extracts:
- use stable source timestamps/version fields;
- write sargable/partition-friendly predicates;
- avoid wrapping the incremental column in functions when that breaks pruning/folding;
- define late-arriving behavior.

# 7. Reconciliation

For published marts/views validate:
- source row count;
- target grain uniqueness;
- measure totals;
- date coverage;
- unmatched dimension keys;
- freshness.

# 8. Slowly changing dimensions

Define the actual requirement:
- overwrite current attributes;
- preserve history;
- effective date ranges;
- current-row flag.

Do not implement SCD Type 2 merely because the table is a “dimension.”

# 9. Semantic-model friendliness

Prefer stable column names, consistent types, numeric measures as numeric, reusable dimensions, and clear key relationships.

Avoid embedding display formatting into SQL values when the semantic/report layer should control presentation.

# 10. Relationship safety

Before publishing a BI dataset, check:
- uniqueness on dimension keys;
- expected one-to-many relationships;
- bridge tables for legitimate many-to-many cases;
- no accidental row multiplication.

SQL correctness and semantic-model correctness are connected.
