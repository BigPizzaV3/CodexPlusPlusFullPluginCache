# Semantic Model and DAX Patterns

## Purpose

Use this file for Power BI Desktop, semantic models, DAX, Power Query, relationships, time intelligence, and model correctness.

# 1. Model first

Before writing complex DAX, confirm the model grain and relationships.

Prefer:
- fact tables for events/measures;
- dimension tables for filtering/grouping;
- one-to-many relationships when appropriate;
- a clear Date dimension;
- stable keys;
- hidden technical columns where useful.

A poor model often produces unnecessarily complex DAX.

# 2. Grain

For each table define:
“one row represents ______.”

Do not join/relate tables before the grain is clear.

# 3. Relationships

Check:
- key uniqueness on the one side;
- cardinality;
- active/inactive;
- filter direction;
- many-to-many necessity.

Use bidirectional filtering intentionally, not as a generic fix for missing results.

# 4. Measures vs calculated columns

Use measures for context-dependent aggregations.

Use calculated columns when a row-level persisted model attribute is actually required.

Do not replace a modeling problem with a large number of calculated columns.

# 5. Filter context

When debugging a measure, identify:
- visual filters;
- slicers;
- page/report filters;
- relationship propagation;
- `CALCULATE` modifiers;
- row context transitions.

Wrong totals are often context problems rather than arithmetic problems.

# 6. DAX debugging

Use:

1. expected grain;
2. current filter context;
3. base measure;
4. intermediate measure/table expression;
5. final logic.

Prefer small helper measures during diagnosis.

# 7. Date/time

Use a proper Date table for standard time intelligence.

Confirm:
- date range;
- unique date key;
- relationship to fact date;
- fiscal/calendar requirement;
- time zone before converting timestamps.

Do not guess whether UTC/local date is intended.

# 8. Power Query

Prefer non-destructive, foldable transformations when possible.

Check:
- source types;
- query folding;
- null behavior;
- locale;
- identifiers;
- duplicate keys.

Do not silently convert identifiers with leading zeros to numbers.

# 9. Star schema

Power BI semantic models generally benefit from clear fact/dimension separation because visuals send filter/group/summarize queries to the model.

For large/complex source transformations, consider doing heavy ETL in the warehouse/lakehouse rather than forcing all shaping into Power Query.

# 10. Current documentation

For new DAX functions, storage-mode behavior, Direct Lake/composite features, or Desktop/service differences, verify current Microsoft documentation.
