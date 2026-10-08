# Prompt for @plugin-creator — SQL Copilot

Create/validate a plugin named **SQL Copilot** from the attached ZIP package.

## Important

This should be a **skills-only plugin** for v0.1.

Do **not** add:
- MCP servers;
- external apps/connectors;
- authentication;
- network dependencies;
- custom UI;
- database credentials;
- database execution tools;
- hooks.

Preserve the existing plugin identity, skill instructions, reference files, listing metadata, test cases, and supplied icon/logo.

## Required package behavior

The plugin should use the `sql-copilot` skill for SQL and database-query requests and should automatically adapt to the user's actual dialect when supplied.

It should:
1. establish the intended output grain and important keys;
2. check join cardinality, duplication, NULL semantics, date/time boundaries, and deterministic ordering;
3. generate one clear, copy-ready query by default;
4. avoid mixing SQL dialects;
5. review pasted SQL for correctness before performance;
6. treat UPDATE, DELETE, MERGE, TRUNCATE, DROP, ALTER, permission changes, and broad schema changes conservatively;
7. provide read-only previews and validation before high-risk writes;
8. use platform/execution evidence for performance guidance instead of generic tuning claims;
9. preserve identifiers and data types when business meaning depends on them;
10. never claim a query was executed, a database inspected, or a result verified unless a connected execution tool actually did it.

## Supported SQL contexts

The packaged references cover:
- PostgreSQL;
- MySQL;
- SQL Server / Azure SQL;
- Oracle;
- Snowflake;
- BigQuery;
- Databricks SQL;
- Amazon Redshift;
- Azure Synapse dedicated SQL pool;
- BI/reporting SQL;
- incremental/CDC logic;
- query-performance reasoning;
- safe database changes.

## Validation requirements

Validate that:
- `plugin.json` is at the ZIP root;
- `skills/sql-copilot/SKILL.md` is discovered;
- `skills` resolves from `./skills/`;
- `skills/sql-copilot/agents/openai.yaml` is valid;
- `icon_small: ./assets/icon.svg` resolves to `skills/sql-copilot/assets/icon.svg`;
- no declared asset path contains `..`;
- the root icon and logo exist;
- starter prompts and listing metadata are accepted;
- the skill activates for SQL work but does not hijack unrelated requests.

Create only the plugin/package setup needed for testing. Do not add capabilities that are not in the uploaded package.
