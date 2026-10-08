# Data Engineering Copilot Plugin

Version: 0.1.0

A skills-only production data-engineering copilot for architecture, debugging, recovery, Spark/Databricks tuning, CDC, Structured Streaming, Airflow, backfills, data quality, and observability.

## Architecture

```text
Data Engineering Copilot
└── data-engineering
    ├── production debugging
    ├── data architecture
    ├── implementation templates
    ├── Spark/Databricks tuning
    ├── streaming / CDC / recovery
    └── data quality / observability
```

No MCP server is required for v0.1.

This package cannot inspect live clusters, execute jobs/queries, trigger Airflow, modify checkpoints, or run backfills by itself.

## Package structure

```text
plugin.json
assets/
  icon.svg
  logo.svg
skills/
  data-engineering/
    SKILL.md
    agents/
      openai.yaml
    assets/
      icon.svg
    references/
      production_debug_playbooks.md
      production_architecture_patterns.md
      data_engineering_implementation_templates.md
      spark_databricks_tuning_guide.md
      streaming_cdc_recovery_patterns.md
      data_quality_observability_runbook.md
      official_source_registry.md
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

Review the ZIP and submission files. Upload it to the OpenAI plugin submission flow only when you are ready.

This package has deliberately **not** been created, installed, or submitted as a plugin.
