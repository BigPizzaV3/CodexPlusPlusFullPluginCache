# SQL Correctness and Safety Framework

## Purpose

Use this file to reason about query correctness before syntax or performance.

# 1. Output grain

Before writing SQL, complete:

> One output row represents ______.

If this is unclear, joins, aggregation, and deduplication can be wrong even when the query runs.

# 2. Keys

Identify:
- business key;
- technical/surrogate key;
- uniqueness assumptions;
- source vs target key.

Do not assume a column named `id` is globally unique without evidence.

# 3. Join cardinality

For each join, determine whether it is:
- one-to-one;
- one-to-many;
- many-to-one;
- many-to-many.

Check whether a join can multiply rows.

Useful validation:

```sql
SELECT join_key, COUNT(*) AS row_count
FROM source_table
GROUP BY join_key
HAVING COUNT(*) > 1;
```

Run on each side when uniqueness matters.

# 4. NULL semantics

Remember:
- `NULL = NULL` is not true;
- `NOT IN` can behave unexpectedly when the subquery/list contains NULL;
- aggregate functions often ignore NULL;
- outer joins can become effectively inner joins when filters on the optional side are placed in `WHERE`.

Prefer explicit NULL handling when business meaning matters.

# 5. Dates and timestamps

Clarify:
- date vs timestamp;
- time zone;
- source zone;
- reporting zone;
- inclusive/exclusive boundaries.

For timestamp ranges, a half-open interval is often safer:

```sql
WHERE event_ts >= :start_ts
  AND event_ts <  :end_ts
```

Do not use this mechanically when the business definition differs.

# 6. Numeric behavior

Check:
- integer vs decimal division;
- rounding;
- precision/scale;
- overflow;
- currency units.

Do not silently cast high-precision values to floating point when exact arithmetic is required.

# 7. Deduplication

Define:
- duplicate key;
- intended winner;
- ordering;
- tie-breaker.

Example:

```sql
ROW_NUMBER() OVER (
  PARTITION BY business_key
  ORDER BY source_version DESC, ingest_ts DESC, source_file DESC
)
```

The final ordering should be deterministic.

# 8. Aggregation

Check that selected dimensions match the intended group grain.

Avoid mixing row-level and aggregate columns without a clear rule.

# 9. Set operations

For `UNION` vs `UNION ALL`:

- `UNION ALL` preserves duplicates;
- `UNION` removes duplicates and adds work.

Choose based on business semantics, not habit.

# 10. Validation queries

Useful checks:
- row count;
- distinct key count;
- duplicate count;
- null-key count;
- before/after reconciliation;
- sum/amount reconciliation;
- min/max date;
- unmatched joins.

A query is not “correct” merely because it returns rows.
