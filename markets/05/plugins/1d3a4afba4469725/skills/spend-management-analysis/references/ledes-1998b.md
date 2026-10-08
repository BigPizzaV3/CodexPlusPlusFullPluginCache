# LEDES 1998B input

Read this reference only when the input begins with `LEDES1998B[]`.

## Convert the file

Run the bundled parser from the skill directory:

```bash
python3 scripts/parse_ledes.py <input.txt> <normalized-output.csv>
```

The parser keeps fee, expense, and adjustment rows, and produces normalized fields for entity, matter, timekeeper, hours, rate, billed amount, descriptions, codes, dates, invoice number, and line type.

## Required limitations

- LEDES 1998B contains `LAW_FIRM_ID`, not a reliable firm name. Use the ID unless the user supplies the mapping; never guess a firm name.
- It has no native matter-type field. The parser labels recognized UTBMS Litigation task-code families as an approximation and otherwise states that the matter type is not specified.
- It has no budget or estimate field. Budget-variance analysis requires a separately supplied budget.
- Expense rows do not have timekeeper hours. Include them in spend totals, but exclude them from staffing-mix calculations.
- The parser requires the standard 24-column LEDES 1998B header in its defined order, `[]` record terminators, recognized line types, exact row field counts, and finite required numeric values. It rejects files with no valid rows. Individual malformed rows may be skipped when other valid rows remain. Report the parser’s skipped-row count when nonzero and do not analyze a rejected file as if it parsed successfully.

State these limitations in the final report so readers do not infer completeness the format cannot provide.
