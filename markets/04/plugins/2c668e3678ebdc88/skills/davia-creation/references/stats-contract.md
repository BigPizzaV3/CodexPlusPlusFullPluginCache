# Stats contract

Stats are remembered questions about the world: who controls a cell, how loyal
an entity is, whether a landmark is intact, or how tense the whole game has
become. Define only information that can affect interpretation or simulation.

## Definition shape

Every entry in `stats.json` exposes:

- `stat_id`: immutable engine identity;
- `label`: creator-facing name;
- `value_kind`: `categorical`, `ordinal`, `scalar`, or `text`;
- `applies_to`: one or more of `world`, `cell`, `entity`, `landmark`;
- `domain`: the allowed value structure;
- `value_colors`: map colors for named categorical or ordinal values;
- `default_value`: optional inherited value;
- `allow_dynamic_values`: whether a categorical stat may accept new values;
- `description`: what the stat means and when it changes.

Existing ids are read-only and may use a legacy format such as
`superpower alignment`. Preserve them exactly. A new definition must be appended
as a complete object and its `stat_id` must use lowercase snake_case with at
most 64 characters, matching the Creation Hub's generated-id format. Search by
label and meaning before creating it to avoid semantic duplicates. Existing
definitions cannot be removed or reordered through the MCP.

## Domains

- Categorical and ordinal domains are ordered arrays of `{ "key", "value" }`.
  Keys are stored values; values are display labels. Keys must be unique.
- Scalar domains contain numeric `min` and `max`, plus an optional `unit`.
- Text domains are `{}`.

For categorical and ordinal stats, use a domain key as the starting value.
Categorical values may fall outside the listed domain only when
`allow_dynamic_values` is true. Scalar values must be numeric and within the
bounds. `null` means no explicit value.

All values in the virtual files are strings or `null`, including scalar
numbers. Do not change a stat's kind merely to make one value fit.

## Subjects and defaults

A value may appear only on a subject listed in `applies_to`. The database uses
different internal names, but the virtual files always use `world`, `cell`,
`entity`, and `landmark`.

An omitted override inherits the stat's default when one exists. An explicit
`null` expresses no value. Before removing or nulling a value, inspect the
definition so the effective state is clear.

Only validate values changed by the current edit. Existing games may contain
unchanged legacy values from an older contract; those must not block an
unrelated rename, description change, placement change, or stat update.

## Design guidance

Use one stat across several subjects only when it asks exactly the same
question with the same domain everywhere. Keep different concepts separate:
country is not stability, allegiance is not military control, and wealth is
not legitimacy.

The current Creation Hub budgets are ten world stats, three cell stats, ten
entity stats, and four landmark stats. Respect them when creating a definition,
but do not delete or rewrite an existing game merely because legacy content
exceeds a current budget.

Colors are six-digit hex values such as `#3b82f6`. Use distinct colors for
named values that should be visualized. Scalar and text stats have no value
color map.
