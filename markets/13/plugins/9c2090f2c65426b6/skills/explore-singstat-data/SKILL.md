---
name: Explore Singstat data
description: Find, retrieve, compare, and explain official Singapore economic, population, household, industry, trade, and social statistics using the SingStat MCP tools. Use when answering questions requiring official Singapore statistics, table metadata, or series discovery from the SingStat Table Builder.
---

# SingStat Skill

Use this skill to answer questions that require official Singapore statistics from the SingStat Table Builder. Follow the continuous execution pipeline below, routing dynamically based on user intent.

## Execution Pipeline

### Step 1: Table Discovery (If Resource ID is not provided)
1. If the user provided a direct `resource_id` matching `M######` (e.g., `M015321`), **skip to Step 2**.
2. Otherwise, call `get_relevant_table_names` with `query_text` (capped at 500 characters).
3. **Intent Check & Decision:**
   - **Table Discovery Only:** If the user only asked to find or list available datasets (e.g., *"What tables exist for CPI?"*), present the matching table names, subjects, frequencies, and resource IDs, then **stop**.
   - **Ambiguous Match:** If multiple candidates fit and no single best match exists that fulfills the query, list top candidate tables with resource IDs and briefly ask the user to select.
   - **Unambiguous Match / General Data Query:** Select the strongest matching table, state which resource ID is chosen, and **continue immediately to Step 2**.

### Step 2: Metadata Inspection
1. Verify `resource_id` matches pattern `M######` (letter M followed by 6 digits). Reject invalid formats prior to tool invocation.
2. Call `get_table_metadata` for the target `resource_id`.
3. **Intent Check & Decision:**
   - **Metadata / Structure Query Only:** If the user only asked about table structure, series numbers, coverage ranges, or definitions (e.g., *"What series are in table M015321?"*), report the metadata details directly and **stop**.
   - **Data Query:** Extract the relevant `seriesNo`, `unit`, `frequency`, and `startPeriod`/`endPeriod` boundaries, and **continue immediately to Step 3**.

### Step 3: Data Retrieval & Pagination
Call `get_table_data` using parameters configured from Step 2:
- `resource_id` (required): `M######` format.
- `seriesNoORrowNo` (optional): Digits, commas, and periods only (e.g., `1` or `1,2,3`). Use `seriesNo` values from metadata `row[]`, not descriptive labels.
- `timeFilter` (optional): `[start, end]` array in `yyyy-mm` format. Both bounds must lie within metadata `startPeriod` and `endPeriod`, with `start` $\le$ `end`.
- `offset` (optional): Digits only for response pagination.

### Step 4: Formatting, Output Presentation & Partial Results
1. **Tables:** Format requested time series or comparative figures as a clean Markdown table. State the table title, resource ID, period, frequency, and unit.
2. **Partial Results & Pagination Disclosures:**
   - The service caps responses at 3,000 rows per request.
   - When the data limit is reached or the tool returns a message indicating a truncated set (e.g., `Set time filter to [start, end] to retrieve next set of data`):
     - Present the partial results retrieved so far immediately rather than omitting them.
     - State clearly that the displayed results are incomplete for the full requested window.
     - Identify the exact coverage retrieved (e.g., date range or series numbers returned).
     - Inform the user how to retrieve the next chunk by specifying the suggested time filter range (e.g., `Set time filter to [start, end]`) or by narrowing `seriesNoORrowNo`.
3. **Footnotes:** Surface any row-level or top-level footnotes that impact data interpretation.
4. **Integrity:** Never silently convert SingStat's `na` or `-` notations to zero. Do not invent or interpolate missing data points.
5. **Calculations:** Mark user-facing derived figures (e.g., growth rates, averages, percentage changes) explicitly as assistant calculations—do not attribute derived math to SingStat.

---

## Tool Input Validation Rules

| Parameter | Validation Rule | Action on Failure |
| --- | --- | --- |
| `resource_id` | Must match `M######` (e.g., `M015321`) | Reject before call |
| `query_text` | String length $\le 500$ characters | Shorten input |
| `seriesNoORrowNo` | Digits, commas, and periods only | Cross-reference against metadata `seriesNo` |
| `timeFilter` | Array `["yyyy-mm", "yyyy-mm"]` within `startPeriod`/`endPeriod` | Re-check bounds from metadata |
| `offset` | Numeric digits only | Omit or correct |

---

## Tool Error & System Messages

| Response Message Pattern | Meaning | Handling Procedure |
| --- | --- | --- |
| `Set time filter to [start, end] to retrieve next set of data` | Response row limit reached; tool returned next suggested date range | Display retrieved partial data, inform user results are partial, and explicitly state the recommended `timeFilter` range to fetch the remaining data |
| `"Invalid Resource ID input."` | `resource_id` format mismatch | Fix string; do not retry unchanged |
| `"Invalid seriesNoORrowNo input."` | Contains illegal characters | Re-verify `seriesNo` from `get_table_metadata` |
| `"Invalid timeFilter input."` | Out of range or invalid date format | Adjust dates to match table metadata bounds |
| `"Search input exceeds character limit."` | `query_text` exceeded 500 chars | Truncate search terms |
| `"Error occured. Please try again later."` | Server exception | Retry once; if persistent, state service is temporarily unavailable |

---

## Resource Links & Connection Info

- **Time-Series Link:** `https://tablebuilder.singstat.gov.sg/table/TS/<resource_id>`
- **Cross-Sectional Link:** `https://tablebuilder.singstat.gov.sg/table/CT/<resource_id>`
- **Official Documentation:** `https://www.singstat.gov.sg/data-tools-services/singstat-mcp`
- **MCP Endpoint:** `https://chatwithsandra.singstat.gov.sg/mcp`