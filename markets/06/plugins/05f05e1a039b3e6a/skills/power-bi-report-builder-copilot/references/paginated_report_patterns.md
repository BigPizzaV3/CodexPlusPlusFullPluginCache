# Paginated Report Patterns

## Purpose

Use this file for Power BI Report Builder / RDL design, troubleshooting, datasets, parameters, tablix, expressions, filters, grouping, and layout.

# 1. Data flow

A useful mental model:

`data source → dataset query → dataset fields → report parameter/filter/group → tablix/chart/map → renderer`

Diagnose the earliest layer where behavior becomes incorrect.

# 2. Dataset design

Prefer datasets that return the grain needed by the report.

Good defaults:
- select explicit columns;
- filter early when appropriate;
- aggregate at source/model when reused or expensive;
- keep parameter datasets small;
- order values deterministically.

Avoid pulling a huge dataset only to remove most rows with a report filter unless there is a specific reason.

# 3. Parameter map

For every parameter record:

- report parameter name;
- type;
- single/multi-value;
- available values source;
- default source;
- nullable/blank behavior;
- dataset/query parameter mapping;
- downstream dependencies.

Do not assume Report Builder parameter names automatically match source placeholders after manual edits.

# 4. Cascading parameters

Pattern:

`Region → Country → Site`

Each downstream available-values dataset should filter using upstream selections.

Guardrails:
- keep lookup datasets narrow;
- sort deterministically;
- avoid circular dependencies;
- handle default values carefully;
- validate empty selections;
- test multi-value upstream behavior separately.

# 5. Multi-value parameters

The report parameter may contain multiple values, but the source/provider determines how those values must be passed.

Possible patterns:
- provider-native array/list binding;
- joined delimited string + source-side split;
- table-valued/staging input;
- dataset filter when data volume is small enough.

Do not prescribe one universal SQL pattern across SQL Server, Oracle, semantic models, and other providers.

# 6. Expression scope

Common scopes:
- current row;
- current group;
- parent group;
- dataset;
- report.

When using aggregates, name scope when ambiguity can change the result.

Examples:

```vb
=Sum(Fields!Amount.Value)
```

```vb
=Sum(Fields!Amount.Value, "RegionGroup")
```

```vb
=First(Fields!ReportDate.Value, "HeaderDataset")
```

Use dataset-scoped header/footer expressions only when that dataset is appropriate for the value.

# 7. Tablix diagnosis

Check:
1. dataset grain;
2. row/column group hierarchy;
3. Details group;
4. group expression;
5. filters;
6. sorting;
7. static/dynamic members;
8. aggregate scope;
9. visibility/toggle;
10. page-break settings.

Duplicate-looking rows may be a grain/grouping problem rather than a display problem.

# 8. Filter order

Remember:
- source query filtering reduces retrieved data;
- dataset/report-region/group filters are applied within report processing;
- group filters act at their scope.

Choose the layer based on correctness and performance.

# 9. Sorting

If pagination, ranking, or export order matters, use deterministic sorting with tie-breakers.

Do not rely on incidental source order.

# 10. Headers and footers

Page headers/footers cannot freely reference detail rows without appropriate aggregate/scope patterns.

For report metadata, prefer:
- parameters;
- built-in globals;
- dedicated small dataset when needed.

# 11. Page breaks

Use group page breaks when the report needs logical sections.

Page breaks do not imply separate output files.

Page names can improve Excel worksheet naming and navigation.

# 12. RDL expressions

Expressions are VB-based and begin with `=`.

Useful built-ins include:
- `Parameters!Name.Value`
- `Fields!Name.Value`
- `Globals!PageNumber`
- `Globals!TotalPages`
- `User!UserID`

Keep complex reusable business rules outside RDL when possible.

# 13. Debug order

When a report is wrong:

1. run dataset/query independently;
2. verify parameter values/mapping;
3. verify dataset fields/types;
4. inspect filters;
5. inspect tablix groups/scope;
6. inspect expression;
7. inspect renderer/export behavior.

Do not start by rewriting the entire report.
