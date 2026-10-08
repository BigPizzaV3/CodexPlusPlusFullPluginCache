# SQL Copilot Plugin

Version: 0.1.0

SQL Copilot is a skills-only plugin for writing, debugging, reviewing, and tuning SQL across major database platforms. It emphasizes correctness, dialect fidelity, safe data changes, BI/data-modeling compatibility, and evidence-based performance work.

## Architecture

```text
SQL Copilot Plugin
└── SQL Copilot Skill
    ├── correctness & validation
    ├── dialect routing
    ├── read/query review
    ├── safe writes & schema changes
    ├── BI/data-modeling SQL
    └── performance analysis
```

No MCP server is required for v0.1. The plugin does not connect to databases or execute SQL.

## Package structure

```text
plugin.json
assets/
  icon.svg
  logo.svg
skills/
  sql-copilot/
    SKILL.md
    agents/
      openai.yaml
    assets/
      icon.svg
    references/
      official_source_registry.md
      sql_correctness_safety_framework.md
      sql_dialect_platform_reference.md
      sql_performance_patterns.md
      sql_write_change_playbook.md
      sql_bi_modeling_patterns.md
submission/
  listing-and-prompts.md
  test-cases.md
  public-submission-checklist.md
  release-notes.md
docs/
  RESEARCH_NOTES.md
PLUGIN_CREATOR_PROMPT.md
README.md
```

## Recommended next step

Upload `sql-copilot-plugin.zip` to the OpenAI plugin workflow or pass it to `@plugin-creator` with `PLUGIN_CREATOR_PROMPT.md`.

This package has deliberately **not** been installed or created as a personal/public plugin. Review and upload it when ready.

## Testing priorities

Test at minimum:
- PostgreSQL ranking/window query;
- SQL Server duplicate-join debugging;
- Snowflake destructive-write preview;
- BigQuery BI/incremental query;
- Databricks query-profile tuning;
- unrelated non-SQL prompt;
- request to falsely claim query execution.
