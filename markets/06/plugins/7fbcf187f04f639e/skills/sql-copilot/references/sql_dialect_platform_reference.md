# SQL Dialect and Platform Reference

## Purpose

Use this file to avoid mixing syntax/optimization advice across SQL engines.

Always prefer the user’s actual platform and current official documentation for version-sensitive behavior.

# PostgreSQL

Common characteristics:
- rich SQL/window support;
- `RETURNING`;
- `ON CONFLICT`;
- `EXPLAIN (ANALYZE, BUFFERS)` for plan evidence.

Check indexes, statistics, join methods, row estimates, and actual vs estimated rows.

# MySQL

Common considerations:
- version-specific CTE/window support;
- transaction behavior depends on storage engine/operation;
- `EXPLAIN`/`EXPLAIN ANALYZE` availability varies by version;
- collations and implicit casts can affect behavior.

Do not write PostgreSQL-specific syntax by accident.

# SQL Server

Common characteristics:
- T-SQL;
- `TOP`;
- `TRY_CONVERT`/`TRY_CAST`;
- temp tables/table variables;
- execution plans/statistics IO;
- transaction/locking behavior for large writes.

Multi-value reporting parameters require source/provider-specific handling; do not assume generic `IN (@Param)` expansion.

# Oracle

Common characteristics:
- Oracle SQL/PLSQL ecosystem;
- version-sensitive row limiting syntax;
- empty string/NULL behavior is distinctive;
- transaction semantics differ from SQL Server/PostgreSQL assumptions.

Use Oracle-native date/string syntax.

# Snowflake

Use Snowflake SQL.

Useful features include `QUALIFY`, semi-structured VARIANT functions, and Query Profile.

Performance diagnosis should look at pruning, bytes/partitions scanned, joins, spill, queueing, and warehouse load.

Do not recommend clustering without repeated filter patterns and pruning evidence.

# BigQuery

Use GoogleSQL.

Important principles:
- projected columns affect bytes read;
- `LIMIT` does not by itself reduce bytes scanned for `SELECT *`;
- partition filters can reduce scanned data;
- clustering works best when filters align with clustering order/pattern;
- use Query Plan / Execution Details for evidence.

Use `SAFE_CAST` when conversion failure should yield NULL rather than error.

# Databricks SQL

Use Databricks/Spark SQL.

Check physical/query profile, pruning, join type/order, shuffle, spill, statistics, and file layout.

Do not force broadcast or maintenance operations without evidence.

Current runtimes can change optimizer behavior, so verify version-specific recommendations.

# Amazon Redshift

Think MPP.

Check distribution, sort keys, statistics, data skew, scan volume, and concurrency.

VACUUM/ANALYZE can be useful but are not universal first steps; use table/system evidence.

# Azure Synapse dedicated SQL pool

Think MPP/dedicated warehouse.

Check distribution strategy, data movement, clustered columnstore health, statistics, partitioning, and concurrency.

Current Microsoft guidance identifies statistics and columnstore health as common performance factors, but diagnose the actual query/request before maintenance.

# General rule

Syntax that looks similar can have different:
- NULL semantics;
- identifier quoting;
- date functions;
- merge/upsert behavior;
- transaction behavior;
- temporary table behavior;
- JSON/semi-structured syntax;
- limit/pagination syntax;
- optimization controls.

State the dialect whenever ambiguity could cause incorrect SQL.
