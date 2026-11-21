# Output formats

## Quick extraction

Study/design; population and analyzed N; intervention/comparator; primary outcome and timepoint; key result with effect measure/CI/p-value; author conclusion; author limitations. Mark unavailable fields `NR`.

## Field table

| Field | Extracted value | Source location | Confidence | Notes |
|---|---|---|---|---|

Use one row per field/value. For result matrices use one row per distinct outcome, timepoint, group/contrast, population, and adjustment status.

## Multi-paper evidence table

Suggested columns: Study ID; authors/year; country; design; population; sample size; intervention/exposure; comparator; primary outcome; follow-up; main numerical result; effect estimate; CI; p-value; adverse events; author conclusion; limitations; funding; bias-related evidence; source locations; uncertainty. Keep identical columns across studies, use `NR` consistently, and put study-specific detail in cells without implying comparability.

## JSON

Return valid JSON when requested: double-quoted keys/strings, correct null/number/boolean types where the schema calls for them, no comments, no trailing commas, and missingness codes as strings if the schema requires them. Do not coerce a reported string-formatted statistic into a number if doing so would lose precision or symbols. Include provenance and uncertainty fields when the schema permits.

## CSV-ready output

Use a stable header row and quote cells containing commas, quotes, or newlines. Escape embedded double quotes by doubling them. Keep units in a dedicated field or exactly as reported; do not create a new column set per paper. For nested data, offer one flat row per result and include Study ID.

## Large documents

State scope and progress. Work in coherent sections/tables; maintain the same schema and stable study identifiers across continuation. At the end reconcile coverage and clearly list any inaccessible or unreadable pages.
