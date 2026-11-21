# Dataset intake, quality checks and privacy boundaries

## Data intake
1. Identify allowed data scope, study purpose and provenance. Work on de-identified fictional/educational material or approved aggregate results. Avoid requesting real patient-level identifying data; ask user to mask identifiers first.
2. Declare structure: rows = subjects/visits/sites? columns = variables? Confirm wide vs long, repeated observations and whether unique IDs were pseudonymized.
3. Parse CSV carefully: delimiters comma/semicolon/tab, quoted multiline strings, decimal comma versus decimal point, encoding UTF-8, missing codes (blank, NA, -99), date formats, units, factor levels and the distinction between numeric ID codes and actual numbers.
4. Count n overall and by group; detect duplicate rows and duplicate IDs (which might be legitimate repeated measures); test ranges/plausibility and missingness by variable. Ask whether missing data are structural, censored or truly absent. Do not convert missing to zero.
5. Show planned transformations and new variables before running them. Keep raw dataset unchanged unless explicit permission. Note exclusions with numbers and reasons. Do not fabricate an audit trail or describe tests not executed.
6. For tables in images, transcribe conservatively; signal ambiguous characters and units. Never infer unseen rows from charts.

## De-identification caution
- Do not ask for names, local patient identifiers, phone numbers, addresses, faces, dates of birth, free-text notes, or exact events dates that can identify patients. Children and rare-disease populations can be re-identified from indirect identifiers. Suppress small cells where necessary for public dissemination; the appropriate threshold varies by policy and population.
- Sensitive/restricted dataset sharing must be governed by local research ethics, IRB, data governance, and organizational policies; authorization is the user's responsibility. The plugin cannot make certified anonymization or compliance claims.
- If identifiers are supplied inadvertently: avoid unnecessary repetition; suggest redaction and, if possible, continue with a synthetic/aggregate example. No unauthorized onward sharing. Do not claim platform retention or third-party processing arrangements without verified provider policy.

## Aggregation and common errors
- Percent = numerator / correctly defined denominator × 100; specify missing denominators, n per group, and total vs available-case fractions.
- Excel rounded display may hide underlying precision: do not compute using display-only approximations without mentioning precision limits.
- Check category sums, inconsistent row counts, impossible ages/dates, mixed units, records counted twice, incompatible time windows, unlinked measures, and transposed 2x2 tables.
- If only summaries are given, say which analyses need raw individual data and which can be done from summaries.
