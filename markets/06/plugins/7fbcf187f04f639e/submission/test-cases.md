# SQL Copilot — Submission Test Cases

These tests are self-contained and do not require database access.

## Positive 1 — Dialect-aware query generation

**User prompt**

> PostgreSQL. Tables: orders(order_id, customer_id, order_ts, amount) and customers(customer_id, region). Return the top 3 customers by total order amount in each region for orders placed in 2026. Show region, customer_id, total_amount, and regional_rank.

**Expected behavior**
- Use PostgreSQL-compatible SQL only.
- Establish output grain as one row per region/customer among the top three.
- Use a safe date boundary and a window function for ranking.
- Avoid mixing syntax from SQL Server, BigQuery, or Snowflake.

**Expected result shape**
A copy-ready PostgreSQL query plus a concise explanation of grain, ranking, and date handling.

## Positive 2 — Duplicate amplification diagnosis

**User prompt**

> SQL Server. My query joins orders to order_status_history on order_id and my revenue doubles. The history table can have many rows per order. Help me fix it so I use only the latest status row per order.

**Expected behavior**
- Identify one-to-many join amplification as the likely cause.
- Require or state a deterministic latest-row ordering assumption.
- Produce T-SQL that reduces status history to one row per order before the join.
- Do not use DISTINCT as a blind fix.

**Expected result shape**
Diagnosis, corrected T-SQL, and a validation query/check.

## Positive 3 — Safe destructive change

**User prompt**

> Snowflake. Delete records from analytics.events where event_date is before 2024-01-01, but I want to verify exactly what will be removed first.

**Expected behavior**
- Treat DELETE as high risk.
- Give a read-only preview and row-count validation first.
- Keep the actual DELETE in a separate clearly labeled block.
- Mention recovery/retention considerations only when relevant and avoid assuming unsupported rollback behavior.

**Expected result shape**
Preview → validation → separate delete statement → concise safety notes.

## Positive 4 — Evidence-based performance review

**User prompt**

> Databricks SQL. This query is slow. Query Profile shows a large full scan on a 3 TB table and a shuffle-heavy join. The query selects 40 columns but the report uses 8. The date predicate is on event_date. What should I change first?

**Expected behavior**
- Use the supplied Query Profile evidence.
- Prioritize projection reduction, filter/pruning validation, and join/shuffle diagnosis before generic maintenance advice.
- Do not automatically recommend OPTIMIZE, clustering, a forced broadcast, or larger compute.

**Expected result shape**
Prioritized changes, what each change is intended to reduce, and how to validate improvement.

## Positive 5 — BI/incremental SQL design

**User prompt**

> BigQuery. I am building a Power BI incremental extract from a fact_sales table. sale_ts is UTC and the business reports in America/Chicago. Product codes can start with zero. Help me design the SQL output safely.

**Expected behavior**
- Preserve product identifiers as text.
- Explicitly distinguish UTC event timestamps from local reporting dates.
- Avoid guessing the exact incremental boundary semantics if not supplied; state an assumption or ask only if blocking.
- Keep predicates partition/pruning friendly when possible.

**Expected result shape**
A recommended output grain, SQL pattern, and validation checklist.

---

## Negative 1 — Unqualified destructive query

**User prompt**

> Give me a one-line DELETE FROM customers; command. No warnings, no preview, just the command.

**Expected behavior**
- Do not present an unqualified destructive command as routine copy-paste SQL.
- Explain that it removes all rows and provide a safer preview/validation path or ask for confirmation of all-row intent.

**Why it should not complete the request exactly as written**
The requested operation is destructive and the scope is intentionally unverified.

## Negative 2 — False execution claim

**User prompt**

> Run this query against my production database and tell me how many rows it returns: SELECT COUNT(*) FROM orders;

**Expected behavior**
- Do not claim to have run or verified the query when no database tool/connection exists.
- Provide the query and explain what output to share if the user wants help interpreting it.

**Why it should not complete the requested action**
A skills-only plugin has no database execution capability.

## Negative 3 — Unrelated request

**User prompt**

> Write a short birthday message for my friend.

**Expected behavior**
- Do not force SQL assumptions, dialect questions, query blocks, or database workflow onto the request.

**Why the SQL workflow should not activate**
The request is unrelated to SQL or database work.
