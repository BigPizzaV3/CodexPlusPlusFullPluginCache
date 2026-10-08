# SQL Copilot Plugin — Research Notes

Research date: 2026-09-23

## OpenAI plugin architecture

Current OpenAI plugin documentation supports three public plugin shapes: skills-only, MCP-only, or skills plus MCP. SQL Copilot v0.1 is intentionally skills-only because its core value is reusable SQL reasoning, review, safety, and optimization guidance rather than authenticated access to a live database.

A skill requires `SKILL.md`; supporting material belongs in `references/`, `assets/`, and optional `scripts/`. SQL Copilot uses references and an icon but no scripts or MCP tools.

The upload package is intentionally flat at ZIP root:

```text
plugin.json
skills/
assets/
...
```

This avoids the extra-parent-folder packaging problem that can prevent skill discovery.

Declared plugin paths use `./` and remain inside the bundle. The skill icon is referenced as `./assets/icon.svg` from the skill root.

Public submission materials currently include listing details, skills, starter prompts, five positive tests, three negative tests, availability, release notes, and policy attestations. Public publishers also need an appropriate verified identity and plugin-submission permissions.

## Why no MCP in v0.1

The skills-only version can:
- write SQL;
- debug SQL;
- review correctness;
- produce safe write previews;
- interpret user-supplied errors/plans;
- recommend platform-specific tuning.

It cannot truthfully claim to:
- connect to a database;
- inspect a live schema;
- execute queries;
- retrieve execution plans on its own;
- modify data.

A future MCP-backed version could add tools such as `list_tables`, `describe_table`, `run_read_query`, `explain_query`, and controlled write workflows with explicit permissions and confirmations.

## SQL platform research

The skill preserves dialect boundaries and directs version-sensitive claims to current official documentation.

Primary official references reviewed:
- PostgreSQL 18 documentation and query reference.
- MySQL 8.4 Reference Manual and SQL optimization documentation.
- Microsoft Transact-SQL reference and transaction documentation.
- Oracle SQL Language Reference, Release 26.
- Snowflake SQL reference, QUALIFY, and query-profile surfaces.
- BigQuery GoogleSQL query syntax.
- Databricks SQL and Query Profile documentation.

The main design rule remains: establish correctness and business semantics before applying optimizer-specific advice.
