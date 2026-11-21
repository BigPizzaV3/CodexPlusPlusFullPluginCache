---
name: delivery-notes
description: Track and analyse material deliveries — search records, delivery frequency/patterns
  by supplier or material, reconcile against usage. Not usage/consumption analysis
  alone (use resource-analysis).
---

Read `../../shared/openai-runtime.md` before this workflow; it defines tool discovery, resource paths, output handling and data checks for this OpenAI edition.


# Delivery Notes — Track and Reconcile Material Deliveries

Search, summarise, and reconcile material delivery records. Provides supplier performance analysis, delivery timelines, and reconciliation against actual material usage recorded on site.

Follow the shared patterns: `../../shared/patterns/01-project-resolution.md` (project resolution); `../../shared/patterns/02-date-range-parsing.md` (date parsing); `../../shared/patterns/03-empty-data-handling.md` (empty data handling); `../../shared/patterns/04-pagination-rate-limits.md` (pagination).

---

## Step 1: Resolve Project, Date Range, and Optional Filter

Parse `the user’s request` for three possible components:

1. **Project name** — resolve using **Pattern 1 (Project Resolution)** from `../../shared/patterns/01-project-resolution.md`.
2. **Date range** — parse using **Pattern 2 (Date Range Parsing)** from `../../shared/patterns/02-date-range-parsing.md`. If no date range is specified, default to the last 4 weeks.
3. **Supplier or material filter** — if the user specifies a supplier name (e.g. "Tarmac", "Hanson") or material type (e.g. "concrete", "aggregate", "steel"), store it for filtering in Step 2. This is optional.

Confirm the interpreted parameters with the user:
> "I'll retrieve delivery notes for **[project name]** from **[start date]** to **[end date]**[, filtered to **[supplier/material]**]. Does that look right?"

If the date range is unambiguous (exact dates provided), skip confirmation and proceed.

---

## Step 2: Locate and Retrieve Delivery Data

Delivery notes are **not** a standalone dashboard report. Locate the data in this order:

1. **Check for a delivery-capable report.** Call `getReportSchemas` and inspect the available reports for delivery-related fields (supplier, delivery reference, quantity delivered). If one exists, call `getCachedReport` with that report name, the resolved project UUID, and the parsed from/to dates.
2. **Fall back to shift records.** If no report carries delivery fields, deliveries are recorded inside shift diary records. Follow **Pattern 20 (Evidence Retrieval Fallback)** from `../../shared/patterns/20-evidence-retrieval.md` to mine `getShiftRecords`/`getShiftRecord` for delivery entries in list fields and narratives (delivery ticket photos may be attached as image assets — note their presence).
3. **Do not use `dashboardResourceMaterial` as the delivery source.** That report is material *usage* — it is the comparison side of the reconciliation in Step 4, and using it here would make the reconciliation compare usage against itself.

If no delivery data is found by either path, follow **Pattern 3 (Empty Data Handling)** from `../../shared/patterns/03-empty-data-handling.md`. Specifically suggest:
- Delivery notes may not be recorded in Gather for this project — check whether the site team is logging deliveries
- The date range may not cover any delivery periods
- The supplier/material filter may not match any records — try without the filter

Extract from the response:
- Delivery date
- Supplier name
- Material type / description
- Quantity delivered (with unit)
- Delivery note reference number
- Any associated shift record or supervisor

If a supplier or material filter was specified, apply it using fuzzy matching (e.g. "concrete" should match "Ready Mix Concrete", "Concrete C32/40", etc.).

---

## Step 3: Summarise Deliveries

Present a delivery summary with the following sections:

### Delivery Summary — [Project Name]
**Period:** [start date] to [end date]
**Total deliveries:** [count]

### Deliveries by Date

| Date | Supplier | Material | Quantity | Unit | Reference |
|---|---|---|---|---|---|
| [date] | [supplier] | [material description] | [qty] | [unit] | [delivery note ref or "—"] |

If there are more than 20 deliveries, show the first 20 and offer to show the full list.

### Deliveries by Supplier

| Supplier | Deliveries | Materials Supplied | Total Loads |
|---|---|---|---|
| [supplier] | [count] | [material (×count), material (×count)] | [count] |

### Deliveries by Material Type

| Material Type | Total Quantity | Unit | Deliveries | Suppliers |
|---|---|---|---|---|
| [material type] | [total qty] | [unit] | [count] | [supplier(s)] |

### Delivery Timeline

Show the distribution of deliveries over the period to identify delivery patterns:
- Peak delivery days
- Days with no deliveries
- Delivery frequency (average deliveries per week)

---

## Step 4: Reconciliation (If Requested)

If the user asks for reconciliation, or if they mention "reconcile", "usage", "wastage", "stock", or "consumed":

### 4a: Retrieve Material Usage Data

Call `getCachedReport` with the following parameters:
- **Report name:** `dashboardResourceMaterial`
- **Project:** the resolved project UUID
- **Date range:** the same from/to dates

This returns actual material usage recorded on site — what was consumed/installed.

### 4b: Match Deliveries to Usage

For each material type that appears in **both** the delivery data and the usage data:

1. **Total delivered** — sum of all delivery quantities for this material
2. **Total used** — sum of all usage records for this material
3. **Variance** = delivered - used
4. **Variance %** = (variance / delivered) x 100%. Per the **Pattern 12** divide-by-zero convention, if delivered = 0 (used but no delivery recorded), show "n/a" and flag the row — do not divide by zero.

Note in the output that the reconciliation covers this period only — it excludes opening stock (material delivered in a prior period and used in this one), so period-boundary variances are indicative, not absolute.

### 4c: Present Reconciliation

### Material Reconciliation — [Project Name]
**Period:** [start date] to [end date]

| Material | Unit | Delivered | Used | Variance | Variance % | Status |
|---|---|---|---|---|---|---|
| [material] | [unit] | [qty] | [qty] | [+/- qty] | [X% or "n/a"] | [Stock on site / Usage exceeds delivery / Balanced] |

### Anomaly Flags

Flag the following situations for investigation:

- **Usage exceeds delivery** (negative variance): Material used on site exceeds what was delivered in this period. This may indicate:
  - Prior period stock being consumed
  - Deliveries not recorded
  - Measurement discrepancy between delivery notes and usage records

- **Large positive variance (>25%)**: Significantly more delivered than used. This may indicate:
  - Stock building on site (intentional)
  - Material wastage not recorded
  - Over-ordering
  - Usage recording lag — material delivered but not yet installed

- **Delivered but no usage recorded**: Material was delivered but no corresponding usage appears. Possible explanations:
  - Material stored for future use
  - Usage not being recorded by the site team
  - Wrong material type categorisation between delivery and usage systems

- **Used but no delivery recorded**: Material usage appears with no corresponding delivery. Possible explanations:
  - Delivered in a prior period
  - Delivery note not recorded in Gather
  - Material sourced from elsewhere (transferred from another site)

---

## Step 5: Supplier Delivery Patterns (If Multiple Deliveries Per Supplier)

If any supplier has 5 or more deliveries in the period, provide a brief delivery-pattern summary (note: this shows frequency and cadence only — the data does not support on-time/quality performance ratings):

| Supplier | Total Deliveries | Date Range | Avg Deliveries/Week | Materials |
|---|---|---|---|---|
| [supplier] | [count] | [first – last delivery date] | [X.X] | [materials] |

Note any patterns:
- Regular delivery schedules (e.g. "Tarmac delivers every Monday and Thursday")
- Gaps in expected deliveries
- Concentration of deliveries on specific days

---

## Related Skills

After presenting results, suggest these related skills for deeper analysis:

- `$resource-analysis` — Analyse all resource usage including materials, labour, and plant for a broader picture
- `$narrative-search` — Search shift narratives for mentions of delivery issues, material shortages, or supplier problems
- `$delay-analysis` — Check if any delays were caused by late or missing deliveries
