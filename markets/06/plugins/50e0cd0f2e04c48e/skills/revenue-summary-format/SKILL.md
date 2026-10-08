---
name: revenue-summary-format
description: Apply the standard summary-table formatting and structure (navy header band, min/max highlighting, total row, % of total, helper block + clustered column and doughnut charts) to a category-by-period data set in Excel.
---

# Summary Table & Chart Format

Reusable layout + formatting standard for a "categories down, periods across" summary table with a total column, share-of-total column, and charts. Derived from the `Revenue Summary` pattern.

## When to use

Use when the user asks to build, reformat, or standardize a summary table where:

- Row labels are categories (revenue streams, cost lines, products, departments)
- Columns are periods (months, quarters, years)
- They want totals, % of total, min/max callouts, and/or charts

Also use when they say "format this like my revenue summary", "apply my standard table format", or invoke `/revenue-summary-format`.

## Layout

Assume the block starts at A1. Adjust anchors if the user specifies a different origin.

| Location                                                    | Content                                                                                                           |
| ----------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| A1                                                          | Title: `<Metric> by <Dimension> — <First Period> to <Last Period> (<Units>)`                                      |
| Row 2                                                       | Blank spacer                                                                                                      |
| Row 3                                                       | Header row: A3 = dimension name (e.g. "Revenue Category"), B3:N3 = period dates, then Total column, then % column |
| Rows 4..n                                                   | One row per category, **sorted descending by the Total column**                                                   |
| Row n+1                                                     | Grand Total row, label bold in column A                                                                           |
| Row n+3 onward                                              | Callout block: "Largest contributor" / "Smallest contributor"                                                     |
| Two columns right of the % column (gap of one blank column) | Helper block for charts                                                                                           |

Freeze panes: `freezeRows(3)` and `freezeColumns(1)`.

**Done when:** table occupies a contiguous block, categories are sorted descending by total, and panes are frozen at row 3 / column 1.

## Formulas (never hardcode derived numbers)

- Period total per category: `=SUM(B4:N4)` in the Total column
- Grand total: `=SUM(<Total col>4:<Total col>n)` and `=SUM(B4:B12)` per period column
- % of Total: `=O4/$O$13` (absolute grand-total ref), total row `=SUM(P4:P12)` → should render 100.0%
- Largest contributor: `=INDEX($A$4:$A$12,MATCH(MAX($O$4:$O$12),$O$4:$O$12,0))`
- Smallest contributor: `=INDEX($A$4:$A$12,MATCH(MIN($O$4:$O$12),$O$4:$O$12,0))`
- Callout value: `=MAX($O$4:$O$12)` / `=MIN($O$4:$O$12)`; callout share: `=C15/$O$13`
- Helper block: `=A4` for labels, `=O4` for values — never retype the numbers

Adapt the example row and column references to the actual table size and origin. Do not hardcode the example O/P columns or row 13 if the source table has a different width or category count.

**Done when:** every number outside the raw period grid is a formula, and the % total row reads exactly 100.0%.

## Formatting spec

Font throughout: **Aptos Narrow, 11pt** (title 14pt bold, black).

Header band (A3, period headers, Total and % headers):

- Bold, font `#FFFFFF`, fill `#1F3864`, centered
- Period header number format: `d-mmm`

Body:

- Value cells: `#,##0`
- % column: `0.0%`
- Largest-total category row (across labels, values, total, %): fill `#C6EFCE` (green)
- Smallest-total category row: fill `#FFC7CE` (red), thin solid black bottom border
- Grand Total row: bold, `#,##0` / `0.0%`, **thin solid black top border + thick double black bottom border**
- Callout labels (column A) bold; callout name cells fill `#FFF2CC` (light amber)
- Callout block separator: thin solid border under the row above the callouts

Column widths: uniform across period columns; autofit column A only.

**Done when:** a read-back with `get_cell_ranges(includeStyles: true)` shows the navy header fill, the green/red category rows, and the double bottom border on the total row.

## Helper block for charts

Charts need one contiguous range, so build a two-column helper block to the right of the table (leave one blank column between):

- Header row: dimension name | `<Metric> (<Units>)`, both bold black (no fill)
- Rows link to the table: `=A4` and `=O4`, values formatted `#,##0`

## Charts

Build with `execute_office_js` off the helper block range.

**Clustered column** — magnitude by category:

- `chartType: "ColumnClustered"`, size `525 × 294.75`
- Title = the A1 table title; font Aptos Narrow **14pt, not bold, color `#595959`**
- Legend **hidden** (single series)
- Data labels **on**, number format `#,##0`
- `series.gapWidth = 219`

**Doughnut** — share of total:

- `chartType: "Doughnut"`, size `456.75 × 294.75`
- Title: `Share of Total <Metric> by <Dimension>`, same 14pt / not bold / `#595959`
- Legend **visible, position Bottom**; data labels off

Place charts below the table, side by side, left-aligned to column A.

**Done when:** both charts exist, titles use the 14pt `#595959` style, the column chart has no legend and visible data labels, and the doughnut has a bottom legend.

## Provenance

If the underlying data came from another file, query, connector, or upload, put one source note on the top-left header cell (A3) in the format:
`Source: <file/system>, <sheet/object>, <row range>, <period covered>.`
Do not add per-cell notes on the value grid.

## Verify before reporting

1. Re-read the table with `get_cell_ranges(includeStyles: true)` — confirm fills, borders, number formats.
2. Confirm no `#REF!`, `#VALUE!`, `#NAME?` and that the % column totals 100.0%.
3. Confirm green/red fills are on the actual max/min rows after sorting.
4. Name the ranges you verified in your reply.
