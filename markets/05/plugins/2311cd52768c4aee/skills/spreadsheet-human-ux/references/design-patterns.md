# Spreadsheet UX Design Patterns

Read this file when creating or materially restructuring a human-facing workbook.

## Progressive disclosure

Show what is necessary for the current task. Keep advanced assumptions, technical calculations, audit trails, and evidence on subordinate tabs or clearly separated sections. A dashboard should not be a compressed copy of every other tab.

## Information architecture

Use the smallest number of visible tabs that supports the job. Common patterns include:

1. **START / DASHBOARD** — purpose, active scenario/period/entity, key result, warnings, next action.
2. **INPUTS** — user-editable assumptions and sourced values.
3. **SCENARIOS / DECISION** — alternatives, sensitivities, breakevens, comparisons.
4. **DETAIL / MODEL** — calculation detail that explains outputs.
5. **EVIDENCE / SOURCES** — provenance, dates, references, assumptions.

Keep tab names short, descriptive, and stable. Prefixes are useful only when they improve scanning. Hidden technical tabs must remain reversible and disclosed when material.

## Dashboard / start surface

The first visible surface should answer:

- What is this workbook for?
- What scenario, period, entity, property, project, or case am I viewing?
- What is the main result?
- Is anything incomplete, risky, stale, or outside tolerance?
- What should I do next?

Prefer roughly 3–7 high-signal outputs to KPI clutter.

## Input patterns

Treat input areas like good forms:

- persistent labels;
- visible units and expected formats;
- dropdowns/checkboxes where options are controlled;
- validation for invalid values;
- clear required/optional distinction;
- protected or separated formulas;
- source/status where material;
- short notes near non-obvious inputs.

Use status labels appropriate to the domain, such as SOURCED, CALCULATED, ASSUMPTION, INFERRED, UNKNOWN. Do not style an assumption as confirmed fact.

## Output patterns

For material outputs, show the interpretation context: unit, horizon/period, active scenario, comparison baseline, and relevant caveat.

Avoid isolated numbers whose meaning depends on surrounding cells.

## Visual hierarchy

Use three levels as a practical default:

- Level 1 — sheet title and primary outcome;
- Level 2 — section headings and decision blocks;
- Level 3 — ordinary labels, values, and detail.

Whitespace is functional. Borders should group rather than cage every cell. Prefer restrained palettes, consistent alignment, and spacing before additional color.

## Density

Separate dense audit/detail tables from interactive decision surfaces. Avoid horizontal scrolling for the primary decision block where practical. Prefer one coherent table to several fragmented micro-tables.

## Navigation and resumability

Keep stable tab order and make current scenario/as-of date visible. Add links/navigation only when they reduce search effort. Put explanations near the point of use rather than in a distant manual.

## Small-screen use

Keep critical dashboard content narrow; favor vertical sections; avoid large frozen regions that consume the viewport; keep important labels visible without hover; avoid essential instructions that exist only in comments.

## Accessibility

Use descriptive headers, consistent tables, readable font sizes, adequate contrast, meaningful number formats, text labels in addition to color, minimal merged cells, and clear actionable error messages. Avoid blank spacer rows inside machine-readable data tables when they harm structure.

## Error and exception UX

Design deliberately for:

- missing required inputs;
- zero denominators;
- inconsistent dates;
- invalid percentages/rates;
- stale source dates;
- impossible combinations;
- negative balances or threshold breaches when relevant;
- scenario not selected;
- formula errors.

The best warning prevents the error where feasible; the next best explains recovery precisely.

## Structure vs freedom

Add structure in proportion to complexity, collaboration, and error risk. Do not formalize a tiny one-off sheet like an enterprise application. Preserve reversible freedom for exploratory inputs while strengthening validation and separation as the model grows.
