# Submission test cases

## Positive cases

### 1. Monthly inflation

- Prompt: “Show Singapore's monthly inflation rate for the latest 12 available months.”
- Expected behavior: Search for the best inflation table, inspect metadata, identify the correct monthly series, then retrieve only the requested period.
- Expected result: A concise chronological table with values, unit, table title, resource ID, period, and any provisional-data note.
- Fixture: Public SingStat data; no account required.

### 2. Population comparison

- Prompt: “Compare Singapore's resident population in 2015 and 2025.”
- Expected behavior: Select a resident-population table, verify the series definition and yearly coverage, retrieve both observations, and calculate the absolute and percentage change.
- Expected result: The two official observations plus clearly labeled derived changes, units, source table, and definitions.
- Fixture: Public SingStat data; no account required.

### 3. GDP trend

- Prompt: “What is the latest quarterly Singapore GDP growth trend?”
- Expected behavior: Resolve whether the request is best answered by year-on-year or quarter-on-quarter data using metadata; if both are available, state the selected measure and retrieve recent quarters.
- Expected result: A short trend summary with a compact table, frequency, unit, resource ID, and a note that the narrative is AI analysis.
- Fixture: Public SingStat data; no account required.

### 4. Known resource ID

- Prompt: “For SingStat resource M015631, retrieve the first listed series from January 2024 through October 2025.”
- Expected behavior: Inspect metadata even though the resource ID is supplied, map the first listed series correctly, and use the requested date filter.
- Expected result: Filtered observations with series name, unit, period, and resource ID.
- Fixture: Resource `M015631` remains available in the public service.

### 5. Ambiguous table request

- Prompt: “Show Singapore employment for 2025.”
- Expected behavior: Search the catalog and, when materially different measures are equally plausible, ask whether the user means employed residents, total employment, or another measure; otherwise explain the selected series.
- Expected result: A focused clarification or a clearly scoped result with table and series attribution.
- Fixture: Public SingStat data; no account required.

## Negative cases

### 1. Non-Singapore data

- Prompt: “Give me Canada's unemployment rate for the past five years.”
- Expected behavior: Do not call SingStat. Explain that the plugin covers Singapore official statistics and offer to use an appropriate Canadian official source if available.
- Why not complete: The request is outside SingStat's national data scope.

### 2. Unsupported prediction

- Prompt: “Use SingStat to tell me Singapore's exact CPI next December.”
- Expected behavior: Retrieve historical data only if useful and clearly say SingStat does not provide an exact future observation. Do not fabricate or attribute a forecast to SingStat.
- Why not complete: The official data service retrieves published statistics, not guaranteed future values.

### 3. Excessively broad extraction

- Prompt: “Download every observation from every SingStat table in one response.”
- Expected behavior: Decline the unbounded extraction, explain the 3,000-row response cap, and ask the user to narrow the subjects, tables, series, or periods.
- Why not complete: The request exceeds the documented response constraints and is not a reproducible focused workflow.
