# Evidence Schedule — Shared Table Format

Used by `ce-builder` (all three contract formats) and cited from `ce-quotation` Step 6.

```
| Date | Shift Record | Summary |
|------|-------------|---------|
| [date] | [ID] | [brief narrative excerpt] |
```

Rules:
- One row per Gather shift record cited as evidence — the record ID must be traceable back to
  a `getShiftRecords`/`getShiftRecord` result actually retrieved in this run.
- "Summary" is a brief excerpt of the narrative text relevant to the event, not the whole
  narrative — quote what you use.
- Sort by date ascending.
- `ce-quotation` restricts this table to records dated up to the dividing date only (see its
  Step 2/Step 6).
