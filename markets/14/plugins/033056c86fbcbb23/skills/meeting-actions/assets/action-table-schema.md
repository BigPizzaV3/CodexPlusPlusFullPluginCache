# Action table schema — Kaus

## Canonical columns

| Column | Required | Rules |
| --- | --- | --- |
| Owner | Yes | Person or team named in the source, or `TBD` |
| Action | Yes | Imperative, concrete, single outcome (one row = one action) |
| Due | Yes | Absolute date if known; else relative phrase from source; else `TBD` |
| Source quote | Yes | Short verbatim span (≤160 chars) supporting the commitment |

## CSV header (when requested)

```csv
Owner,Action,Due,Source quote
```

Escape quotes in CSV normally. Do not add extra columns unless the user asks (e.g. Priority).

## Inclusion rules

Include a row when the source shows a **commitment or clear assignment**.

Exclude or park:

- Brainstorm ideas with no owner
- Already-completed items mentioned only as context (unless user asks for a decisions log)
- Pure informational statements

## Ambiguity checklist

List under **Ambiguities** when any apply:

- No owner
- Multiple possible owners without resolution
- Vague action (“look into X”, “handle it”) with no success criteria
- No deadline and time-sensitivity is implied
- Conflicting statements about the same action
