# Official SQL Source Registry

Use current official documentation when syntax, transaction behavior, optimizer behavior, platform limits, or performance features may vary by engine/version.

## PostgreSQL
- Documentation: https://www.postgresql.org/docs/current/
- Queries: https://www.postgresql.org/docs/current/queries.html

## MySQL
- MySQL 8.4 Reference Manual: https://dev.mysql.com/doc/refman/8.4/en/
- SQL statement optimization: https://dev.mysql.com/doc/refman/8.4/en/statement-optimization.html

## Microsoft SQL Server / Azure SQL / Synapse / Fabric SQL
- Transact-SQL reference: https://learn.microsoft.com/en-us/sql/t-sql/language-reference
- SELECT: https://learn.microsoft.com/en-us/sql/t-sql/queries/select-transact-sql
- Transactions: https://learn.microsoft.com/en-us/sql/t-sql/language-elements/transactions-transact-sql

## Oracle
- SQL Language Reference: https://docs.oracle.com/en/database/oracle/oracle-database/26/sqlrf/

## Snowflake
- SQL reference: https://docs.snowflake.com/en/sql-reference
- QUALIFY: https://docs.snowflake.com/en/sql-reference/constructs/qualify
- Querying/query details: https://docs.snowflake.com/en/user-guide/ui-snowsight-query

## BigQuery
- GoogleSQL query syntax: https://cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax
- Query plan/performance guidance: https://cloud.google.com/bigquery/docs/best-practices-performance-overview

## Databricks SQL
- Databricks SQL: https://docs.databricks.com/en/sql/
- Query profile: https://docs.databricks.com/en/sql/user/queries/query-profile

## Rule
Do not copy syntax or performance advice from one dialect into another without verifying compatibility. If the user supplies a platform/version, prefer its official current documentation.
