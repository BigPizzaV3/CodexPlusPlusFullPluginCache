# Query recipes

Prefer focused tools. Use these patterns only when `edu_run_sql` is necessary.

## One accepted point in time

Choose a relation whose name or discovery guidance says `latest_final`. Do not combine it with provisional context. Return the collection cycle, reference period, source release, and release stage alongside every measure.

## Historical change

Choose the matching longitudinal relation. Group and order by the source's collection cycle. Keep release identifiers in the result. Compare like measures and populations.

## Completion totals

Sum `completions_first_major` when the person asks for degrees in a primary field. Do not add second majors unless the question explicitly asks for all major declarations. Filter the award level explicitly.

Use one comparable collection cycle for a latest grouped ranking. Do not sum each college's independently selected latest cycle.

## Counts

Count the entity at its declared grain. Use distinct identifiers only when the relation can contain more than one row for that entity under the applied filters.

## Non-additive measures

Never sum:

- wages or earnings medians;
- rates, shares, percentages, or scores;
- years or codes;
- employment estimates from overlapping geography or industry packages;
- the same broader field outcome repeated across narrower fields.

Use a weighted calculation only when the source supplies a valid weight and the method matches the measure definition.

## Reproducible result

Return:

- readable labels with any necessary identifiers;
- measure value and unit;
- period and source release;
- coverage or suppression reason;
- level of detail and any broader-to-narrower applicability;
- enough rows to support the claim, within the server limit.

The tool's `totals` describe the full query before row limiting. Use that count instead of counting returned rows.
