# Tool routing

Use this order. Stop as soon as the focused tool can answer the question.

## Begin discovery

1. Call `edu_describe_data` without a topic for each new data question.
2. Read its routing guidance and available semantic views.
3. Resolve named colleges, fields, or occupations with `edu_resolve_entity`.

Exact identifiers are text:

- UnitID identifies a college.
- CIP-6 identifies a field, such as `11.0701`.
- SOC-6 identifies an occupation, such as `15-1252`.

Never guess an identifier from memory.

## Prefer focused tools

| Intent | Tool | Required preparation |
|---|---|---|
| One college | `edu_get_institution` | Resolve the college to UnitID. |
| One college and field | `edu_get_program` | Resolve the college and field to UnitID and CIP-6. |
| One occupation, including its highest observed AI-use tasks | `edu_get_occupation` | Resolve the occupation to SOC-6. Set `task_limit`; do not write SQL for a top-task request. |
| Several known colleges, fields, or occupations | `edu_compare` | Resolve every entity, then pass ordered identifiers of one type. |
| Grouped totals, counts, or rankings | `edu_aggregate` | Use an approved measure, dimension, filters, and period. |
| Source or release explanation | `edu_get_sources` | Pass release IDs returned by another tool and any relations used. |

`edu_aggregate` supports first-major completion totals and college counts. Its `latest_final` period uses one shared accepted reporting cycle. Use `longitudinal` for change over time.

## Use SQL only as the fallback

Use `edu_run_sql` only when a focused tool cannot express the request.

Before SQL:

1. choose the smallest suitable `marts.*` relation from `edu_describe_data`;
2. call `edu_describe_data` again with `table:marts.<relation>`;
3. write one read-only `SELECT` or `WITH ... SELECT`;
4. include period, release, coverage, and applicability columns when available.

Do not query `marts.semantic_catalog`. Do not use `core.*` unless discovery shows that no semantic relation can answer the question.

## Choose the period correctly

- Use latest-final relations for one accepted point in time.
- Use longitudinal relations for historical comparisons.
- One point describes a state.
- Two comparable points show change.
- Three comparable points can support a trend.
- Five comparable points with consistent direction can support a sustained trend.
