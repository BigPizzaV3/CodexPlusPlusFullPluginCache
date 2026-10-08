# Plugin Creator Prompt — Data Engineering Copilot

Create/validate a **skills-only plugin** from the attached archive.

## Identity
- Package: `production-data-engineering-copilot`
- Skill: `data-engineering`
- Public display name: `Data Engineering Copilot`
- Version: `0.1.0`
- Category: `Data & Analytics`

## Architecture
Keep v0.1 skills-only.

Do **not** add:
- MCP;
- external connectors;
- authentication;
- custom UI;
- Databricks/Airflow/database credentials;
- live query execution;
- automatic checkpoint changes;
- automatic replay/backfill execution.

## Required behavior
Preserve the existing production data-engineering workflow:
- reason from supplied architecture, code, SQL, plans, Spark UI metrics, logs, runtime details, and configs;
- never claim live inspection or execution without actual tool/results;
- prioritize data correctness, loss/corruption risk, recovery, SLA, then performance/cost;
- preserve replayability and idempotency;
- use authoritative source sequence/version for CDC when available;
- treat Structured Streaming checkpoints/state as production state;
- require scope, validation, concurrency rules, and rollback/repair for backfills;
- diagnose Spark/Databricks performance from evidence before scaling;
- distinguish reversible incident containment from permanent fixes;
- use current official docs for runtime/version-sensitive Spark, Databricks, Delta, and Airflow behavior.

## Preserve
- `SKILL.md`
- all reference files
- `agents/openai.yaml`
- branding assets
- public listing material
- positive/negative tests

## Validate
1. ZIP root discovery.
2. `plugin.json` and `skills: "./skills/"`.
3. Skill frontmatter.
4. Combined plugin/skill identity <= 64 characters.
5. `agents/openai.yaml`.
6. Asset paths remain inside the package and do not use `..`.
7. Branding files are valid and square.
8. Public listing lengths.
9. Starter prompts.
10. Five positive and three negative tests.

Do not create, install, or submit the plugin unless the user explicitly asks for that action.
