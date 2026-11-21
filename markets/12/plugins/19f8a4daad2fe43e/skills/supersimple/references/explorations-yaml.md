# Explorations YAML Reference

Explorations are notebook-style dashboards composed of cells. Data cells have pipelines; text, variables, metrics, conversations, and apps have their own shapes. Export an existing exploration before editing it.

Schema: `https://assets.supersimple.io/configuration_schema/1.1.0/supersimple_configuration_schema.json`

The API runs this JSON schema first and returns early on failure, before runtime parsing.
The optional exploration `schema_version` is a separate version: keep it literally `"1.0.0"`,
even though the configuration schema URL is 1.1.0.

Related docs: https://docs.supersimple.io/guides/no-code-exploration-steps/ (step semantics) and https://docs.supersimple.io/guides/custom-formulas/reference (expression syntax).

## Contents
- [Exploration structure](#exploration-structure)
- [Cell types](#cell-types)
- [Pipelines](#pipelines)
- [Pipeline operations](#pipeline-operations)
- [Visualisations](#visualisations)
- [Series & chart styling](#series--chart-styling)
- [Big numbers](#big-numbers)
- [Filters](#filters)
- [Tabs & layout](#tabs--layout)

## Exploration structure

<!-- schema: # -->
```yaml
exploration:
  exploration_id: revenue-overview
  schema_version: "1.0.0"
  name: Revenue Overview
  folder: Sales
  visibility: team
  view:
    options:
      layout: notebook
    cells:
      - id: monthly-revenue
        kind: records
        title: Monthly Revenue
        pipeline:
          base_model_id: orders
          pipeline_id: monthly-revenue-pipeline
          operations:
            - operation: filter
              parameters:
                key: status
                operator: "=="
                value: completed
        visualisations:
          - aggregation:
              groups:
                - key: created_at
                  precision: month
              aggregations:
                - type: sum
                  key: amount
                  property: { key: revenue, name: Revenue }
            main_axis_key: created_at
            value_keys: [revenue]
            view_options:
              series:
                revenue: { chart_type: bar }
```

Replace the example IDs with your actual models and fields. Folder names are resolved in the
selected space (`team` or `personal`); omitted/null `folder` moves the exploration to the root, and
omitted `visibility` defaults to team. Preserve these fields when editing existing explorations.
Optional `description` is a string or null; `labels` is a string-to-string map. Layout, tabs, and
canvas examples appear below.

## Cell types

Common cell kinds: `records`, `sql`, `python`, `code`, `metric`, `funnel`, `cohort`, `variable`,
`text`, and `app`. Existing exports may also contain `chat`, `conversation`, or `invalid` cells;
remove `chat`, `conversation`, and `invalid` cells from the import copy: the current import gate
rejects them. Keep the original export as a backup. Also strip app `input_block_ids`,
`view_options.pivot`, and `rollback.original_conditional_formatting` before importing.
Do not import `kind: code` blocks using the generic `code` operation until the API schema fix
ships. For Python imports, use the legacy `kind: python` and `python` operation.

Fragments below illustrate fields or arrays; wrap them in the enclosing exploration before import. Generate unique cell
and pipeline IDs, resolve actual model/property IDs, and use real arrays/objects before validating.
Keys are snake_case in YAML. The Supersimple SDK and GraphQL require camelCase keys instead.

### records (most common)

Query data from a model via pipeline, render as table/chart/big number.

<!-- schema: #/definitions/explorationViewCell[] -->
```yaml
- id: cell-uuid
  kind: records
  title: "My Cell Title"
  pipeline: { base_model_id: orders, pipeline_id: example-pipeline, operations: [] }                     # see Pipelines section
  exclude_properties: [field_to_hide]   # optional, array of property keys or null
  visualisations: []                 # optional, see Visualisations section
  sort:                                 # optional, array or null
    - key: created_at
      direction: DESC                   # ASC | DESC
  view_options: {}                 # optional, see Cell view options
  conversation_id: conv-uuid            # optional, internal
```

### sql

Run raw SQL. Pipeline contains a `sql` operation.

<!-- schema: #/definitions/explorationViewCell[] -->
```yaml
- id: cell-uuid
  kind: sql
  title: "SQL Query"
  pipeline: { base_model_id: orders, pipeline_id: example-pipeline, operations: [] }
  visualisations: []
  view_options: {}
```

### python

Run Python code. Pipeline contains a `python` operation.

<!-- schema: #/definitions/explorationViewCell[] -->
```yaml
- id: cell-uuid
  kind: python
  title: "Python Analysis"
  pipeline: { base_model_id: orders, pipeline_id: example-pipeline, operations: [] }
  view_options: {}
```

### metric

Display a predefined metric. No pipeline -- references a metric by ID.

<!-- schema: #/definitions/explorationViewCell[] -->
```yaml
- id: cell-uuid
  kind: metric
  metric_id: monthly_revenue
  view_options: {}
```

### funnel

Funnel analysis. Pipeline contains a `funnel` operation.

<!-- schema: #/definitions/explorationViewCell[] -->
```yaml
- id: cell-uuid
  kind: funnel
  title: "Signup Funnel"
  pipeline: { base_model_id: orders, pipeline_id: example-pipeline, operations: [] }
  view_options: {}
```

### cohort

Retention/cohort analysis. Pipeline contains a `cohort` operation.

<!-- schema: #/definitions/explorationViewCell[] -->
```yaml
- id: cell-uuid
  kind: cohort
  title: "Weekly Retention"
  pipeline: { base_model_id: orders, pipeline_id: example-pipeline, operations: [] }
  view_options: {}
```

### variable

A variable definition (e.g., a filter control). No pipeline. This is the minimal valid
`string` definition: a key and a string default value. YAML uses `default_value`; the app
uses `defaultValue`. Export a working variable for other kinds.

<!-- schema: #/definitions/explorationViewCell[] -->
```yaml
- id: cell-uuid
  kind: variable
  definition: { kind: string, key: segment, default_value: enterprise }
  view_options: {}
```

### text

Markdown/rich text cell. No pipeline.

<!-- schema: #/definitions/explorationViewCell[] -->
```yaml
- id: cell-uuid
  kind: text
  title: "Section Header"
  content: "Markdown content here"     # optional
  view_options: {}
```

### code and app cells

The app uses `kind: code` with a generic `code` operation, but the current import gate rejects
that operation. Use the legacy Python form for import; TypeScript/Scala have no import workaround.
An app block refers to an already-created app; importing the exploration does not publish its code:

<!-- schema: #/definitions/explorationAppViewCell[] -->
```yaml
- id: app-cell-id
  kind: app
  title: Revenue planner
  app_id: published-app-id
  state:
    selected_metric: revenue
  view_options:
    app:
      size: auto                     # auto | fill
```

App `input_block_ids` is a runtime field rejected by the current import gate. Strip it from the
import copy and retain the original export; check app input behavior after importing. Do not assume
export/import is lossless for these blocks until the API schema is fixed.
An optional `app_version_id` pins a specific version. Without it, the block follows the published
version. Preserve state keys and nested data exactly; they belong to the app. Use the
`supersimple-apps` skill to create or change app code.

### Variables

Variable definitions have runtime-specific shapes even though the exploration import schema is
permissive. The minimal `string` shape is shown above. For other kinds (`date_range`, `enum`,
`multiselect`, etc.), export a working variable instead of inventing its definition. Use a Penguino variable expression in a filter:

<!-- schema: #/definitions/explorationOperation[] -->
```yaml
- operation: filter
  parameters:
    key: created_at
    operator: "=="
    value:
      expression: 'variable("Date range")'
      version: "1"
```

Use the exact variable key (`Date range` above). Date ranges resolve only when the filter value
is exactly `variable("<key>")` with double quotes inside the expression. Keep a dynamic date-range variable as an expression so the engine can
resolve its presets and timezone. Exploration `parameters` are separate from variable cells.

### Cell view options

All cell types share these `view_options`:

<!-- schema: #/definitions/explorationCellViewOptions select: view_options -->
```yaml
view_options:
  table_visibility: hidden           # hidden | visible
  pipeline_preview_visibility: hidden # hidden | visible
  block_title_visibility: visible    # hidden | visible
  view_mode: table                   # cards | table
  collapsed: "yes"                   # "yes" | "no", not boolean or "true"
  row_id: row-uuid                   # up to 3 ADJACENT cells with the same row_id form a row
  height: 400                        # pixel height
  field_order:                       # column ordering
    column_key: 0
    another_key: 1
```

Other supported cell view options include `conditional_formatting`, `auto_run_code`,
`code_visibility`, and `app`. Runtime `pivot` exists but is rejected by the import schema.

## Pipelines

A pipeline defines the data query for a cell. Two forms:

### Base pipeline (starts from a model)

<!-- schema: #/definitions/explorationPipeline select: pipeline -->
```yaml
pipeline:
  base_model_id: orders
  pipeline_id: pipe-uuid              # required, unique identifier
  operations: []                   # array of operations
```

### Child pipeline (extends another cell's pipeline)

Only `records` and `cohort` cells accept child pipelines. SQL, Python, code, and funnel cells
require a base pipeline, even where the JSON schema permits a child pipeline.

<!-- schema: #/definitions/explorationPipeline select: pipeline -->
```yaml
pipeline:
  parent_id: pipe-uuid-of-parent      # references another pipeline_id
  pipeline_id: pipe-uuid
  operations: []                   # additional operations on top of parent
```

## Pipeline operations

Operations transform data sequentially. Each has `operation` (type) and `parameters`. All exploration operations support an optional `disabled: true` flag to skip them without removing.

Use cell/visualisation `sort` for ordering,
`slice` for limits, `exclude_properties` to hide columns, and `field_order` for column ordering.
These are configuration fields, not operations; preserve their nesting from a working export.

### filter

Filter rows by condition(s). Parameters use the composite filter format (see [Filters](#filters)).

<!-- schema: #/definitions/explorationOperation[] -->
```yaml
- operation: filter
  parameters:
    key: status
    operator: "=="
    value: active
```

<!-- schema: #/definitions/explorationOperation[] -->
```yaml
# composite filter with AND/OR
- operation: filter
  parameters:
    operator: and
    operands:
      - key: status
        operator: "=="
        value: active
      - key: amount
        operator: ">"
        value: 100
```

### groupAggregate

Group rows and compute aggregations.

<!-- schema: #/definitions/explorationOperation[] -->
```yaml
- operation: groupAggregate
  parameters:
    groups:
      - key: created_at
        precision: month             # year | quarter | month | week | day_of_week | day | hour
        fill: true                   # fill gaps in time series
      - key: category               # non-time grouping (no precision)
    aggregations:
      - type: count
        property:
          key: total_orders
          name: Total Orders
      - type: sum
        key: amount                  # source field to aggregate
        property:
          key: total_amount
          name: Total Amount
    slice:                           # optional limit/offset
      limit: 10
      offset: 0
      sort:
        - key: total_amount
          direction: DESC
```

Exploration aggregation types: `count`, `count_distinct`, `sum`, `avg`, `min`, `max`, `first`,
`last`, `median`, `array`, `custom`, `metric`. `first` and `last` require a `sort` array; `custom`
requires a Penguino `value: { expression, version }`. All need an output `property: { key, name }`.
Named metric definitions have a separate, more limited import schema; see data-model-yaml.md.

The `metric` type references a predefined metric. Use `metric_id` in CLI YAML and `metricId`
in Supersimple SDK/GraphQL parameters:
<!-- schema: #/definitions/explorationAggregation[] -->
```yaml
- type: metric
  metric_id: monthly_revenue
  property:
    key: revenue
    name: Revenue
```

When consuming grouped results through `sup.query` or GraphQL, grouping dimensions live on
parent rows and aggregate values live in recursive `$children` arrays. Carry parent dimensions
into each leaf when flattening; `$leaves` is a result-row count, not a metric. This is the query
response format; exported YAML contains the configuration shown above. The `supersimple-apps`
skill has a complete SDK query and flattening example. `sup.exploration.fetchBlock` already
returns flattened rows.

Aggregations can have `filter` and `relation`; groups can have `relation`. A `type: metric`
aggregation accepts `metric_id` only for its reference, not an extra `key`.

### addRelatedColumn

Pull columns from a related model.

<!-- schema: #/definitions/explorationOperation[] -->
```yaml
- operation: addRelatedColumn
  parameters:
    relation:
      key: customer               # relation key from the model definition
    columns:
      - key: email                # source column in related model
        property:
          key: customer_email     # output column key
          name: Customer Email
```

### relationAggregate

Aggregate across a relation (e.g., count of related records).

<!-- schema: #/definitions/explorationOperation[] -->
```yaml
- operation: relationAggregate
  parameters:
    relation:
      key: order_items
    aggregations:
      - type: count
        property:
          key: item_count
          name: Item Count
      - type: sum
        key: price
        property:
          key: total_price
          name: Total Price
    filter:                       # optional filter on related records
      key: status
      operator: "=="
      value: active
    slice:                        # optional
      limit: 100
```

### deriveField

Create a computed column.

<!-- schema: #/definitions/explorationOperation[] -->
```yaml
- operation: deriveField
  parameters:
    key: order_year               # output column key
    field_name: Order Year        # display name
    value:
      expression: 'year(created_at)'
      version: "1"
```

`relationAggregate` also accepts `pipeline_id` referencing another pipeline, plus
`join_strategy: {join_key_on_base, join_key_on_related}`, instead of `relation`. Preserve those
references and keys from a working export.

### switchToRelation

Switch the pipeline's base to a related model.

<!-- schema: #/definitions/explorationOperation[] -->
```yaml
- operation: switchToRelation
  parameters:
    relation:
      key: customer
```

### joinPipeline

Join another pipeline's results.

<!-- schema: #/definitions/explorationOperation[] -->
```yaml
- operation: joinPipeline
  parameters:
    steps:
      - step_id: joined-payments
        pipeline:
          base_model_id: payments
          pipeline_id: payments-pipeline
          operations: []
        join_strategy:
          join_key_on_base: id
          join_key_on_related: order_id
```

### histogram

Bucket a numeric column.

<!-- schema: #/definitions/explorationOperation[] -->
```yaml
- operation: histogram
  parameters:
    key: amount
    num_buckets: 20               # optional
```

### funnel

Multi-step funnel analysis (used in `funnel` cells).

<!-- schema: #/definitions/explorationOperation[] -->
```yaml
- operation: funnel
  parameters:
    property:
      key: user_id
      name: User ID
    steps:
      - pipeline:
          base_model_id: signups
          pipeline_id: signups-pipeline
          operations: []
        sort_key: created_at
        fields: [user_id]
      - pipeline:
          base_model_id: activations
          pipeline_id: activations-pipeline
          operations: []
        sort_key: created_at
        fields: [user_id]
    groups:                       # optional breakdown
      - key: plan_type
```

### cohort

Retention cohort analysis (used in `cohort` cells).

<!-- schema: #/definitions/explorationOperation[] -->
```yaml
- operation: cohort
  parameters:
    pipeline:                     # the events pipeline
      base_model_id: events
      pipeline_id: pipe-uuid
      operations: []
    cohort_id: user_id
    cohort_time_key: signed_up_at
    cohort_time_interval: week    # year | month | week | day
    event_time_key: event_time
    event_time_interval: week
```

### sql

Raw SQL operation (used in `sql` cells).

<!-- schema: #/definitions/explorationOperation[] -->
```yaml
- operation: sql
  parameters:
    sql: "SELECT id, amount FROM public.orders WHERE amount > 100"
    # connection_id: <connection-id>  # optional; use an actual configured connection ID
    fields:                       # optional output schema
      - key: id
        type: Integer
      - key: amount
        type: Float
```

### python

Python code operation (used in `python` cells).

<!-- schema: #/definitions/explorationOperation[] -->
```yaml
- operation: python
  parameters:
    code: |
      from supersimple import getBlock
      df = await getBlock("Orders").fetchAll().as_df()
      df.groupby("Category", as_index=False)["Amount"].sum()
    fields:                       # keys match the returned DataFrame columns exactly
      - key: Category
        type: String
      - key: Amount
        type: Float
```

Fetch the desired block/model with `getBlock`, using an
actual title and its returned **display names** (`Category`, `Amount`), not property keys. The last expression is the output; assigning `result`
alone does not display it. Preserve the output column names in `fields[].key`, including case
and spaces; if you rename DataFrame columns, declare the renamed keys instead. The app copies
the runtime result field keys into the Python operation without normalizing them.
SQL uses actual warehouse tables.
SQL accepts `{{variables.<name>}}` (date-range endpoints use `.from`/`.to`) and reserved placeholders
`{{account_id}}`, `{{user_email}}`, `{{namespace}}`, `{{timezone}}`,
`{{single_quote_char}}`, `{{double_quote_char}}`, `{{backslash}}`, and `{{user_parameters.<key>}}`. Other `{{x}}` placeholders are errors. Use a real base model on the intended connection;
SQL runs on that connection unless `connection_id` is set.

### code

The runtime supports generic Python, TypeScript, and Scala code operations, but the current
configuration import schema rejects the `code` operation. Do not author this form for imports until
the API schema fix is deployed. Use the `python` operation above for Python imports. Code runtime
APIs differ by language; do not translate Python APIs literally.

## Visualisations

Each cell can have an array of `visualisations`. There are two forms:

### Simple visualisation (chart over pipeline output)

Uses the existing pipeline output without adding another aggregation. If the pipeline already
has a usable `groupAggregate`, the chart inherits its groupings (including subcharts).

<!-- schema: #/definitions/explorationVisualisation[] select: visualisations -->
```yaml
visualisations:
  - value_keys: [amount, quantity]  # columns to plot (required)
    main_axis_key: created_at       # category/time axis column (optional)
    sort:                           # optional
      - key: created_at
        direction: ASC
    view_options: {}           # see below
```

### Aggregated visualisation (chart with its own aggregation)

Adds a visual-level aggregation on top of the pipeline output. This is the most common form.

<!-- schema: #/definitions/explorationVisualisation[] select: visualisations -->
```yaml
visualisations:
  - aggregation:
      groups:
        - key: created_at
          precision: month
          fill: true
      aggregations:
        - type: count
          property:
            key: count
            name: count
        - type: sum
          key: amount
          property:
            key: total
            name: Total
    main_axis_key: created_at       # category/time axis
    value_keys: [count, total]      # numeric measures to plot
    sort:
      - key: created_at
        direction: ASC
    view_options: {}
```

### How groupings become charts

Group order controls layout, not just query granularity. For an aggregated chart, use the
groupings in `aggregation.groups`; for a simple chart, use the inherited pipeline groupings.
Date groupings with `precision` are moved after other groupings, preserving order within each
set. The following rules use that resulting order:

| Groupings | Normal layout |
|---|---|
| One: `[status]` | Status on the category axis; one series per `value_keys` measure. |
| Two: `[plan, status]` | Status on the axis; one colored legend series per plan × measure. |
| Three: `[region, plan, status]` | Separate, vertically arranged subcharts per region; each has status on the axis and plan × measure as series. |
| More than three | Earlier groupings add nested subchart divisions; the last two still select series and axis. |

Keep `main_axis_key` aligned with the **last grouping's output key** (`property.key` for a
relation grouping, otherwise `key`). The app normally derives this axis from the groups, so changing
`main_axis_key` alone is not a way to swap grouping roles. Reorder the groups instead.

**Stacking:** `stacked: false` (the default) places bar series side by side. `stacked: true`
adds series at each axis value within each subchart; it does not normalize to percentages.
Bar, area, and line series stack separately by chart type and value axis. Stack only measures
whose sum is meaningful. `show_totals: true` labels stack totals; use `show_values` for individual
values. Stacking normally leaves the subchart divisions intact.

**Time-series exception:** with three groupings such as `[region, plan, created_at]`, where
`created_at` has `precision: month`, setting `stacked: true` and explicitly setting
`chart_type: bar` on **every measure** produces one plot: each month has side-by-side region
bars, each stacked by plan × measure. With stacking off, or area/line series, regions remain
separate subcharts. With more groupings, this exception applies to the last three; earlier
groupings still create subcharts.

Categorical charts default to horizontal bars (categories on the y-axis). Set
`orientation: vertical` for categories on the x-axis or for line/area styling; horizontal charts
always render bars. Date axes default to vertical area charts, so explicitly choose `bar` or
`line` when wanted. `precision: day_of_week` is categorical, not a time-series axis.

### Visualisation view options

<!-- schema: #/definitions/explorationVisualisationViewOptions select: view_options -->
```yaml
view_options:
  stacked: false                    # stack series as described above
  show_totals: true                 # show stack total labels
  orientation: vertical             # vertical | horizontal (bar direction)
  big_number_field_key: count       # render as big number instead of chart
  series: {}                   # per-series styling, see below
  axes:
    right:
      keys: [total]                 # measures on the secondary value axis
```

## Series & chart styling

Customize series inside `visualisations[].view_options.series`. Without a breakdown grouping,
keys are the measure keys from `value_keys` (the aggregation's output `property.key`).

<!-- schema: #/definitions/explorationVisualisationViewOptions select: view_options -->
```yaml
view_options:
  series:
    revenue:
      color: '#FF1493'             # any hex color string
      chart_type: area             # area | line | bar
      show_values: true            # show data labels on points/bars
    users:
      color: '#FFD700'
      chart_type: bar
  axes:
    right:
      keys: [revenue]              # put the revenue measure on the secondary axis
```

With a breakdown, `series.<measure_key>.chart_type` and `show_values` apply across its series,
but colors use individual combined keys such as `plan:Pro:revenue`
(`group key:group value:measure key`). Preserve exported combined keys when editing individual
legend series. Use `axes.right.keys` for whole-measure axis assignment; `axis` inside a series
override only works for combined series. All styling fields are optional.

## Big numbers

Render a cell as a prominent single number. Three shapes: legacy `big_number_field_key`,
`big_number: {key: total_count}`, or `big_number` with comparison below.

### Simple big number

<!-- schema: #/definitions/explorationVisualisationViewOptions select: view_options -->
```yaml
view_options:
  big_number_field_key: total_count   # just point to the field
```

### Big number with comparison

<!-- schema: #/definitions/explorationVisualisationViewOptions select: view_options -->
```yaml
view_options:
  big_number:
    key: current_revenue              # main value
    comparison_key: previous_revenue  # comparison value
    comparison_type: percentage       # absolute | percentage
    comparison_direction: higher      # higher | lower (which direction is "good")
    show_comparison_label: true
    comparison_mode: value            # value | period_to_date
# Place sorting on the visualisation alongside view_options, not inside big_number:
sort:
  - key: period
    direction: DESC
```

All big-number forms belong under `visualisations[].view_options`, not the cell's view_options.
`hide_chart: true` may be set inside `big_number` to suppress the accompanying chart.

## Filters

Filters appear in pipeline `filter` operations and in `relationAggregate` filter parameters.

### Single condition

<!-- schema: #/definitions/explorationCompositeFilterCondition -->
```yaml
key: status
operator: "=="
value: active
```

### With relation (filter on a related model's field)

<!-- schema: #/definitions/explorationCompositeFilterCondition -->
```yaml
key: plan_name
operator: icontains
value: enterprise
relation:
  key: subscription
  model_id: accounts                # optional BASE model owning this relation, not subscriptions
```

A filter `relation` can also be an array for a multi-hop relation path.

### Composite (AND/OR)

<!-- schema: #/definitions/explorationCompositeFilterCondition -->
```yaml
operator: and
operands:
  - key: status
    operator: "=="
    value: active
  - operator: or
    operands:
      - key: amount
        operator: ">"
        value: 100
      - key: priority
        operator: "=="
        value: high
```

### Filter operators

| Operator | Description | Requires value |
|----------|-------------|----------------|
| `==` | equals | yes |
| `!=` | not equals | yes |
| `<` `>` `<=` `>=` | comparisons | yes |
| `in` | in list | yes (array) |
| `notin` | not in list | yes (array) |
| `icontains` | case-insensitive contains | yes |
| `noticontains` | case-insensitive not contains | yes |
| `arrcontains` | array contains | yes |
| `between` | range | yes (`{from, to}`) |
| `isnull` | is null | no |
| `isnotnull` | is not null | no |
| `isempty` | is empty | no |
| `isnotempty` | is not empty | no |

### Expression values

Penguino bare keys (`created_at`, `prop(created_at)`) resolve by key; `prop("Created At")`
resolves by display name. Prefer bare keys in YAML. Dynamic filter values using expressions:

<!-- schema: #/definitions/expressionValue select: value -->
```yaml
value:
  expression: 'sub(now(), interval(30, "day"))'
  version: "1"
```

## Tabs & layout

### Tabs

Group cells into tabs:

<!-- schema: #/definitions/exploration/properties/view select: view -->
```yaml
view:
  cells: []                      # all cells listed here
  tabs:
    groups:
      - tabs:
          - tab_id: tab-1
            label: Overview
            cell_ids: [cell-id-1, cell-id-2]
          - tab_id: tab-2
            label: Details
            cell_ids: [cell-id-3]
```

### Canvas layout

For `layout: canvas`, position cells on a freeform canvas:

<!-- schema: #/definitions/exploration/properties/view select: view -->
```yaml
view:
  options:
    layout: canvas
  cells: []
  canvas:
    nodes:
      - id: cell-id-1
        position: { x: 0, y: 0 }
        measured: { width: 400, height: 300 }
    edges:
      - id: edge-1
        source: cell-id-1
        target: cell-id-2
        source_handle: handle-id      # optional
        target_handle: handle-id      # optional
```

### Time intervals

Used in grouping `precision`, cohort intervals:

`year` | `quarter` | `month` | `week` | `day_of_week` | `day` | `hour`

Cohort-specific intervals: `year` | `month` | `week` | `day`
