# CE Quotation — Output Template (Step 7)

## Header block

```
CE QUOTATION (CLAUSE 62)
Project: [Name]
Contract: [NEC3/NEC4 Option X]
Ref: QT-[NNN]
CE Reference: [CE-NNN, cross-referenced from prior notification / "notification pending — event details supplied fresh"]
Dividing Date: [date] ([how fixed, per Step 1])
Date: [today]
```

Apply **Pattern 8** for the `QT-[NNN]` sequence (session-local, increments per prior `QT` ref in
this conversation, else `001`).

## Closing summary table and submission timetable

| Item | Value |
|---|---|
| Changes to the Prices | £[X] (Step 3 build-up) |
| Delay to Completion Date | +[X] working days ([date] → [date]) |
| Delay to Key Date(s) | +[X] working days / "no Key Dates affected" |
| Quotation submission deadline (62.3) | [date] — 3 weeks from the PM's instruction to quote (or the agreed longer period) |
| PM reply deadline (62.3) | [date] — 2 weeks from submission |
| Deemed-acceptance route (62.6) | If the PM does not reply by the deadline, the Contractor may notify the failure; a further 2 weeks of silence deems this quotation accepted. Track both deadlines with `$nec-deadlines`. |
