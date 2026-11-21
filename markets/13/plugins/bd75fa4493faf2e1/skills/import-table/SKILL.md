---
name: import-table
description: Turn a pasted or uploaded table (CSV, spreadsheet excerpt, spec sheet) into a BOLDR form with all of its rows and measurements in one call.
---

# Import a table into BOLDR

Use this when the user provides tabular data — a CSV, a pasted table, a cut
list, a spec sheet — and wants it in BOLDR.

1. Confirm the destination: which project and job (create them with
   `create_project` / `create_job` if the user asks for new ones).
2. Map the table's headers to column types: lengths → `measurement`,
   angles → `angle`, categories with a fixed set of values → `singleSelect`
   (collect the options), yes/no → `boolean`, free text → `text`, counts →
   `number`. Show the user the mapping before writing if anything is
   ambiguous.
3. Call `import_table` once: `columns` from the headers, `rows` with cells
   keyed by column NAME. Measurement cells take the values as written —
   numbers are read in `unit`, strings like `3' 4-1/2"` parse as-is, and
   `{value, label}` attaches a label to the created measurement.
4. More than 50 rows? `import_table` the first 50, then batch the rest with
   `create_groups` using the column ids the first call returned (cells are
   keyed by column ID there, not name).
5. Hand back the section name and row count, and offer a follow-up: lock a
   measurement column's display unit with `set_column_unit_lock`, or set
   tolerances so out-of-spec rows surface in reports.

Never create rows one call at a time with `create_group` +
`create_measurement` when the data is already tabular — the bulk tools are
atomic and far cheaper on the organization's request quota.
