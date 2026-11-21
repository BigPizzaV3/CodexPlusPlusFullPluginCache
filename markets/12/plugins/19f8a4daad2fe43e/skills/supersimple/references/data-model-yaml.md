# Models, metrics, and AI configuration

Docs: https://docs.supersimple.io/guides/managing-the-data-model/

For editor completion, start YAML files with:

```yaml
# yaml-language-server: $schema=https://assets.supersimple.io/configuration_schema/1.1.0/supersimple_configuration_schema.json
```

Contents: file structure; models and enums; relations; derived models; metrics; access rules;
AI configuration; exploration locations.

## File structure

| Single entity (ID required) | Map (ID is the key) |
| --- | --- |
| `model` with `model_id` | `models` |
| `metric` with `metric_id` | `metrics` |
| `exploration` with `exploration_id` | `explorations` |
| `agent_skill` with `agent_skill_id` | `agent_skills` |

Other top-level sections are `access_rules` (named access rules) and `ai_instructions` (one object).
The CLI merges YAML files; duplicate entity IDs or access-rule names are errors. `ai_instructions`
may appear in only one input file. Map entries must not repeat their IDs inside the value: the import schema rejects that.
Always set `*_id` in single-entity files; otherwise validate/import prompts and rewrites the file.

## Models and properties

<!-- schema: # -->
```yaml
model:
  model_id: orders
  name: Orders
  table: public.orders
  primary_key: [id]
  description: Customer orders
  properties:
    id: { name: ID, type: Integer }
    customer_id: { name: Customer ID, type: Integer }
    amount: { name: Amount, type: Float, format: usd }
    status:
      name: Status
      type: Enum
      enum_options:
        load: static
        options:
          - { value: pending, label: Pending }
          - { value: completed, label: Completed }
    created_at: { name: Created At, type: Date }
  relations:
    customer:
      model_id: customers
      type: hasOne
      join_strategy:
        join_key_on_base: customer_id
        join_key_on_related: id
  labels:
    section: Sales
  semantics:
    kind: Event
    properties:
      created_at: created_at
```

Base and derived models require `name`. A base model requires `properties` and exactly one source:
`table`, `sql`, or `prql`. Model IDs must not contain dashes. Property display names must be unique
within a model, and `format` must be compatible with the property type.
`connection` optionally names a configured database connection. Declare a real primary key when
available; don't invent one or use a non-unique field just to fill the setting.

Property types: `String`, `Enum`, `Number`, `Integer`, `Float`, `Boolean`, `Date`, `Array`, `Object`,
`Interval`. Properties require `name` and `type`. Optional fields include `description`, `format`,
`access`, and `sql` (a column expression, supported only on table-based models).
`column_type` and `precision` apply only to Date properties; preserve an existing valid value or
consult the schema and database-connection docs before setting them.

`labels.section` groups models in the sidebar. `semantics.kind` can be `Event`, `User`, or `Account`;
all three require a `semantics.properties.created_at` key pointing to a **Date** property.
An Event also needs a `hasOne` or `hasOneThrough` relation to a User or Account semantic model.
The example’s `customers` model must therefore declare User or Account semantics.

### Dynamic enums

<!-- schema: #/definitions/modelProperty select: status -->
```yaml
status:
  name: Status
  type: Enum
  enum_options:
    load: distinct_values
    cache_ttl: 6 hours
```

By default values come from this model and property. Optional `model`, `value_key`, and `label_key`
select a different lookup model/column and friendly labels. Cache durations use integer minutes,
hours, or days (`30 minutes`, `6 hours`, `1 day`); the default is six hours. Results are capped at
1,000 values. `cache_ttl: 0 minutes` disables caching. Static enum values must be strings; quote numeric-looking values such as `"1"`.
Choose enums for useful categorical values, not arbitrary identifiers or free text.

## Relations

Relation types are `hasOne`, `hasMany`, `manyToMany`, and `hasOneThrough`. Cardinality describes the
related records for one base record. Relations across connections are rejected. Confirm it from data and primary keys before choosing a type.

For `hasOne` or `hasMany`, choose one join strategy:

<!-- schema: #/definitions/modelRelationJoinStrategy select: join_strategy -->
```yaml
# Same column name on both models:
join_strategy:
  join_key: customer_id
```

<!-- schema: #/definitions/modelRelationJoinStrategy select: join_strategy -->
```yaml
# Different column names (orders.customer_id -> customers.id):
join_strategy:
  join_key_on_base: customer_id
  join_key_on_related: id
```

<!-- schema: #/definitions/modelRelationJoinStrategy select: join_strategy -->
```yaml
# Custom SQL, using aliases supplied by the engine:
join_strategy:
  sql: "{{base_model}}.customer_id = {{related_model}}.id"
```

A many-to-many join requires endpoint keys. Junction keys are optional and default to the
corresponding endpoint keys; specify them when the junction uses different names:

<!-- schema: #/definitions/modelRelationManyToMany select: products -->
```yaml
products:
  model_id: products
  type: manyToMany
  join_strategy:
    join_key_on_base: id
    join_key_on_related: id
    through:
      model_id: order_items
      join_key_to_base: order_id
      join_key_to_related: product_id
```

Here the path is `orders.id -> order_items.order_id` and
`order_items.product_id -> products.id`. `join_key` is shorthand for identical endpoint key names.
A many-to-many relation can alternatively use a SQL join strategy. Do not omit endpoint keys just
because the junction keys are specified.

A single-record relation through existing relations uses a chain:

<!-- schema: #/definitions/modelRelationHasOneThrough select: customer_country -->
```yaml
customer_country:
  model_id: countries
  type: hasOneThrough
  join_strategy:
    steps:
      - relation_key: customer
      - relation_key: country
```

Add useful reverse relations explicitly. They are not created automatically. `supersimple fix`
only works on `models:` map files (it crashes on single `model:` files) and suggests missing reverse relations it can infer from models within each input file, so it
will miss relationships split across files. Review its output rather than treating it as a full
validation or writing its output over your original files.

## Derived models

A derived model references a base model and applies operations; it inherits the resulting fields.
It does not use the base-model `properties`, `relations`, `labels`, or `semantics` declarations.

<!-- schema: # -->
```yaml
model:
  model_id: completed_orders
  name: Completed Orders
  base_model: orders
  operations:
    - operation: filter
      parameters:
        key: status
        operator: "=="
        value: completed
    - operation: deriveField
      parameters:
        key: order_year
        field_name: Order Year
        value:
          expression: 'year(created_at)'
          version: "1"
```

Operations use snake_case parameter keys. See [explorations-yaml.md](explorations-yaml.md) for
common no-code operations. Exploration-only operations, such as code blocks, are not general
model transformations. Penguino bare identifiers such as `created_at`, or `prop(created_at)`, resolve by property key.
`prop("Created At")` resolves by display name, not key. Prefer bare keys in YAML so renaming a
display name does not break formulas. SQL expression syntax is not Penguino syntax.

## Metrics

A named metric is a reusable aggregation attached to a model:

<!-- schema: # -->
```yaml
metric:
  metric_id: completed_revenue
  name: Completed Revenue
  model_id: orders
  aggregation:
    type: sum
    key: amount
  operations:
    - operation: filter
      parameters:
        key: status
        operator: "=="
        value: completed
```

For ordinary named metrics use `count` (no source key), or `count_distinct`, `sum`, `avg`, `min`,
`max` with a source `key`. The parser also accepts `first`, `last`, `custom`, and `metric` types. Do not copy an exploration aggregation verbatim: named metric YAML has
its own smaller schema (`aggregation.type` and optional `key`), not `property`, `filter`, `sort`,
`value`, or `metric_id` inside the aggregation. In particular, `median` and `array` are supported
in exploration aggregations but not in the named-metric import schema. For unusual existing
metric types, export and validate them rather than assuming exploration options apply.

## Access rules

**Requires CLI ≥2.27.0.** Named rules resolve within the same import only. Include `access_rules.yaml`
when validating/importing a subset (`supersimple validate ./models ./access_rules.yaml`). Export
writes this file alongside entity directories.

Models and properties can have inline `access` rules or reference a named rule from top-level
`access_rules`. Preserve existing access restrictions when editing. For example:

<!-- schema: # -->
```yaml
access_rules:
  finance:
    user_parameters:
      team: [finance, leadership]
```

A model or property can then use `access: finance`. Do not confuse model/field access with SQL
row-level filtering. See https://docs.supersimple.io/guides/managing-the-data-model/model-access-control
for the account's security workflow before changing access rules.

## Workspace AI configuration

These sections configure Supersimple's AI, rather than installing a coding-agent skill. They require
the **Manage AI System Message** permission. Export existing content first:

```bash
supersimple export --agent-skills --ai-instructions -o ./sup-ai-config
```

<!-- schema: # -->
```yaml
agent_skill:
  agent_skill_id: retention-analysis
  name: Retention analysis
  description: Use for customer retention questions.
  instructions: |
    Use completed billing periods when comparing retention cohorts.
  enabled: true
  position: 0
```

`name`, `description`, and `instructions` are required, non-empty strings. `enabled`, `position`
(integer), and `access` are optional. Preserve IDs to update an existing skill.

<!-- schema: # -->
```yaml
ai_instructions:
  general: Use the company's fiscal calendar for quarterly reports.
  sources:
    - connection: warehouse
      instructions: The reporting schema contains the curated business tables.
```

Each source uses exactly one of `connection` or `integration`, and non-empty `instructions`.
Connections match by configured name. Integrations match by lowercase service name (`slack`,
`notion`, `google_drive`, etc.); use an integration ID when multiple integrations share a service. `general` is optional; an empty string explicitly clears it.
Omitted sections remain unchanged. With `--delete-dangling`, including `agent_skills: {}` deletes
all workspace skills; including `ai_instructions.sources: []` deletes per-source instructions.
See [cli-reference.md](cli-reference.md) before using deletion flags.

## Exploration locations

Set an exploration’s location with `folder` and `visibility`:

<!-- schema: #/definitions/exploration -->
```yaml
name: Revenue Overview
folder: Sales
visibility: team
view: { cells: [] }
```

`folder` addresses a folder by name and can create it on import. Missing or null means root.
`visibility` is `team` (the default) or `personal` (the importing user's personal space, including
personal folders).
See [explorations-yaml.md](explorations-yaml.md) for the full notebook structure.

Formula reference: https://docs.supersimple.io/guides/custom-formulas/reference
