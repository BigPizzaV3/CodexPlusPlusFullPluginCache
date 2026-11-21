# Eurostat statistics

`eurostat_query(question)` turns one plain-language question into a filtered
Eurostat table. It picks a dataset, validates every filter against the
dataset's catalogue and returns at most 30 rows. It takes 10–25 s; tell the
user before calling.

## Ask well

- One indicator per call: "Unemployment rate in Croatia, quarterly, last 8
  quarters", not "unemployment and inflation in Croatia and Slovenia".
- Name the geography (Eurostat codes: `HR`, `EL` for Greece, `EU27_2020`,
  `EA`), the frequency (annual, quarterly, monthly) and the period.
- Non-EU countries such as `RS`, `BA`, `ME` are covered by many datasets.

## Check before using the numbers

1. `available` — false means no data; read `error` and `attempted_filters`.
   It is not an error envelope.
2. `dataset_code` / `dataset_title` match the question. The tool can return a
   related but different dataset, especially for vague questions.
3. `applied_filters` describe the rows actually returned. Compare `geo`,
   `unit` and the period with the question; `filter_adjustments` lists every
   substitution (for example seasonal adjustment SA → NSA).
4. `time_coverage` — `periods_shown`, `last_fetched`, `staleness_months` and
   `note` say how recent the data is.

If the table does not answer the question (wrong dataset, a requested region
or country missing), say so instead of presenting it as the answer.

## Report

Give the figures with unit, period and geography from `applied_filters`, the
dataset code and title, and `source_url`. `related_legislation` is an
unverified suggestion — check it with `get_article` before citing it.
Eurostat has no enforcement or regulator statistics.
