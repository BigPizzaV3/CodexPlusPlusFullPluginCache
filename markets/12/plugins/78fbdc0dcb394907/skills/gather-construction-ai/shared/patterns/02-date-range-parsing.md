# Pattern 2: Date Range Parsing

Users express date ranges in many ways. Normalise these to `from`/`to` parameters for `getCachedReport` and `getShiftRecords`:

| User Input | Parsed As |
|---|---|
| "last week" | Monday to Sunday of previous week |
| "this month" | 1st of current month to today |
| "January" / "January 2026" | 2026-01-01 to 2026-01-31 |
| "Q3 2025" | 2025-07-01 to 2025-09-30 |
| "2026-01-15 to 2026-02-15" | Exact dates as given |
| "last 30 days" | Today minus 30 to today |
| No date specified | Default to **last 4 weeks** — recent enough to be useful, broad enough to show trends |

**Key rule (uniform across all skills):** Confirm the interpreted date range with the user only when the input required non-trivial interpretation (relative phrases with multiple readings, missing year, conflicting hints). Exact dates, named months, and clearly stated periods proceed without confirmation. Never add a confirmation step beyond this rule — inconsistent confirmation behaviour across skills is itself a defect.
