# SQL Performance Patterns

## Purpose

Use this file after correctness is established.

Optimization should be evidence-driven and platform-aware.

# 1. Start with evidence

Collect when available:
- execution plan/profile;
- rows/bytes scanned;
- rows after each stage;
- join strategy;
- shuffle/data movement;
- spill;
- partition pruning;
- sort/index usage;
- concurrency/queueing;
- runtime by stage.

Do not optimize from query text alone when plan evidence is available.

# 2. Reduce work

Common principles:
- select only required columns;
- filter as early as semantics allow;
- reduce rows before expensive joins;
- pre-aggregate when that preserves meaning;
- avoid repeated scans;
- avoid unnecessary sorting/distinct;
- preserve partition/index/clustering pruning.

# 3. Join performance

Check:
- join cardinality;
- size of each side after filters;
- join keys/types;
- skew;
- statistics;
- distribution/shuffle.

Do not force a broadcast/hash/merge join without platform evidence.

# 4. CTEs

A CTE improves readability but does not universally guarantee materialization or better performance.

Its execution behavior depends on platform/optimizer/version.

Do not recommend “use a CTE for performance” without evidence.

# 5. Indexes

For row-store systems, index usefulness depends on:
- predicate;
- selectivity;
- join/order pattern;
- write overhead;
- existing indexes;
- statistics.

Do not recommend indexes generically for warehouses that use different storage/optimization models.

# 6. Partitioning and clustering

Use when repeated access patterns can prune meaningful data.

Bad partitioning can create metadata overhead, tiny partitions, poor distribution, or weak pruning.

Choose from real filter patterns and table scale.

# 7. Materialization

Use materialized views/summary tables when:
- the computation is expensive;
- reuse is high;
- freshness requirements permit it.

Include refresh/maintenance cost in the decision.

# 8. Window functions

Windows can replace self-joins and simplify row-relative logic, but can still require large sorts/shuffles.

Check partition size, order keys, and whether the window is necessary.

# 9. Pagination

For large result sets, keyset/seek pagination is often more scalable than large OFFSET values when stable ordering and a suitable key exist.

Do not use it when arbitrary page jumping is a hard requirement without explaining trade-offs.

# 10. Platform evidence

## BigQuery
Inspect bytes processed, stages, shuffle, partition/clustering pruning, and slot behavior.

## Databricks
Inspect Query Profile/physical plan, scans, shuffles, join type, spill, statistics, and file layout.

## Snowflake
Inspect Query Profile, partitions scanned/pruned, spill, joins, queueing, warehouse load, and clustering only when pruning evidence supports it.

## Redshift/Synapse
Inspect data movement/distribution, scans, statistics, skew, sort/columnstore health, and concurrency.

Optimization is complete only when correctness is unchanged and runtime/cost improve.
