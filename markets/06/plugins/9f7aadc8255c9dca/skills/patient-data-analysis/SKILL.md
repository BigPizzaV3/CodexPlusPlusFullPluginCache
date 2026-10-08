---
name: patient-data-analysis
description: Combine patient records from multiple city/location sheets into one source, build a pivot table counting HIV-positive patients with blood group O by location, and add a linked column chart with a city slicer filter.
---

## When to use
Use when the workbook has one patient-register sheet per city/location (e.g. Ibadan, Lagos, Abuja), all with the same headers, including **HIV Status** and **Blood Group**, and the user wants:
- a pivot table built from **all** location sheets together, and/or
- a chart of HIV-positive patients with blood group O (O+ and O−) that can be filtered by city.

Also use it when the user asks for the same analysis with a different criterion (e.g. "HIV negative and blood group A"). Change the flag formula in Step 2 to match.

## Expected sheet layout (input)
Each location sheet has a header row in row 1 and one patient per row, for example:
`Patient Name | Age | Occupation | Gender | HIV Status | Blood Group | Date of Test`
- HIV Status values: `Positive` / `Negative`
- Blood Group values: `O+`, `O-`, `A+`, `B-`, `AB+`, etc.

## Step 1: Discover the location sheets
- Use execute_office_js to list the worksheets. For each one, load the used range and row 1.
- Treat a sheet as a location sheet if its headers include both "HIV Status" and "Blood Group". Skip "All Patients", "HIV Pivot", "Data Sources" and any sheet without those headers.
- Record each sheet's name, last data row (from `getUsedRange().rowCount`) and the column letter of every header. **Don't assume column positions**: find "HIV Status" and "Blood Group" by header text.
- If the sheets' headers differ, stop and tell the user which sheet is different.
- Done when: you have a list of {sheetName, lastRow, headerMap} for every location sheet.

## Step 2: Build the combined "All Patients" source sheet
A pivot table can only use one contiguous range, so combine the location sheets onto one sheet with links. Don't paste static values.
- If "All Patients" already exists, ask before replacing it. Otherwise create it with `worksheets.add("All Patients")`.
- Header row: `Location`, then every source header in order, then a flag column `HIV+ & Blood Group O (1=Yes)`.
- For each location sheet, for rows 2..lastRow write:
  - Column A: the sheet name as text (e.g. `Ibadan`).
  - Columns B onwards: link formulas to the source cell, e.g. `=Ibadan!A2`, `=Ibadan!B2`, …
  - Flag column: `=IF(AND(<HIV col><r>="Positive",LEFT(<Blood col><r>,1)="O"),1,0)`, where `<r>` is the row on All Patients (e.g. `=IF(AND(F2="Positive",LEFT(G2,1)="O"),1,0)`).
- Write all formulas in one `range.formulas = [...]` call. Build the 2D array in JS.
- Formatting: header row bold, white text on navy `#1F3864`, wrap text. Linked columns in green `#008000` (cross-sheet links). Date column `dd-mmm-yyyy`. Centre the numeric/code columns. Autofit columns A to the last linked column, set the flag column width to about 110. Freeze row 1.
- Done when: the row count on All Patients equals the sum of all location data rows, and a spot-check of the first and last rows shows the right names and 0/1 flags.

## Step 3: Create the pivot table
- Create (or reuse) a sheet named "HIV Pivot". Put a bold 13pt title in A1: `HIV-Positive Patients with Blood Group O (O+ / O-) — all locations`.
- `pivotTables.add("HIV_O_Pivot", <All Patients A1:lastCol lastRow>, "HIV Pivot"!A3)`
- Row field: **Location**.
- Data field: the flag column, `summarizeBy = sum`, renamed `HIV+ & Blood Group O`.
- Don't add a "Total Patients" count to this pivot. A second series on the chart dwarfs the HIV+ O bars. If the user wants totals, build a separate pivot.
- After `context.sync()`, **re-read `pt.rowHierarchies`** and confirm it is `["Location"]`. The row field has been seen to change to another field (e.g. Age). If it isn't Location, remove the wrong field and add Location.
- Done when: `pt.layout.getRange()` shows one row per city plus Grand Total.

## Step 4: Cross-check the count
- In a temporary cell on All Patients, write `=COUNTIFS(<HIV col>2:<HIV col><last>,"Positive",<Blood col>2:<Blood col><last>,"O*")`, read the value, then clear the cell.
- Done when: it equals the pivot's Grand Total. If not, investigate before continuing.

## Step 5: Create the chart linked to the pivot
- On "HIV Pivot", add a chart from the pivot's body range (header + city rows, **excluding the Grand Total row**, e.g. `A3:B6`):
  `ws.charts.add(Excel.ChartType.columnClustered, range, Excel.ChartSeriesBy.columns)`
  Because the source is a pivot range, Excel makes it a PivotChart that follows the pivot's filters.
- Settings:
  - name `HIV_O_Chart`, title `HIV-Positive Patients with Blood Group O by City`
  - legend hidden
  - series fill `#1F3864`, data labels on
  - value axis title `No. of Patients`, minimum 0, majorUnit 1
  - category axis title `City`
  - position: `top = 45, left = 330, width = 420, height = 280`, to the right of the pivot so they don't overlap.
- Done when: the chart has exactly one series, and its category values are the city names.

## Step 6: Add the city filter (slicer)
- `context.workbook.slicers.add(pt, "Location", ws)`: name `City_Slicer`, caption `Filter by City`, `left = 760, top = 45, width = 150, height = 150`.
- The PivotChart's own **Location** field button also filters. Mention both to the user.
- Test it: `slicer.selectItems(["<one city>"])`, read the chart series values and the pivot layout, and confirm they show only that city. Then run `slicer.clearFilters()`.
- Done when: filtering changes both the pivot and the chart, and the slicer is cleared again.

## Step 7: Visual check and report
- Render `HIV Pivot!A1:P22` with `getImage()` + `attachImage` and confirm that the pivot, chart and slicer don't overlap, that the bars are labelled, and that no second series is present.
- Report to the user:
  - the per-city counts and the grand total
  - where each thing lives: All Patients, and HIV Pivot for the pivot, chart and slicer
  - how to filter
  - that edits to existing rows show up after right-clicking the pivot and choosing **Refresh**, but new patients added below a sheet's current last row need All Patients extended (re-run Steps 1–2)

## Conventions
- Follow the user's hardcoded-input preference: numeric inputs are written with a leading `=` (e.g. `=34`, `=DATE(2026,1,14)`).
- Never compute the counts in JS and paste them. The counts must come from the pivot and the flag formulas.
