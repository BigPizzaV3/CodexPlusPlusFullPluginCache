---
name: "placement-pipeline-sheet"
description: "Build a spreadsheet of cited pages that do not list the business, with outreach status, cost per citing answer, and answers naming you since go-live."
---

# Placement pipeline sheet

Use this guidance to build a working sheet of the cited pages that do not list the business. The person works one row from first contact to a listing, then sees if AI apps name the business after it.

## Build the sheet

1. Call `get_sources` for the project and the scan in the request. Call it again with `include_branded: false`.
2. Make one row for each page in `pages_to_get_on`. The row key is the page `url`. Never change it.
3. Fill the Frontmost AI columns from the data:

| Column | Value |
|---|---|
| Page | `url` |
| Type | `type` |
| Answers Citing It | `answers` from the first call |
| Non-Branded Answers Citing It | `answers` for the same `url` in the second call, or 0 |
| Rivals Listed | the names in `rivals` where `listed` is true |
| Lists You | `you`: Present, Not present, or Check needed |
| Listing Checked On | `checked_on` |
| Answers Naming You Since Go-Live | empty until the person types a go-live date |

4. Add the columns that the person fills in: Contact, Status, Quote, Paid, Go-Live Date, Note. Leave them empty. Never write in them after the first build.
5. Add two calculated columns:
   - Cost per Citing Answer = Paid ÷ Answers Citing It. Leave it empty when Paid is empty.
   - Answers Naming You Since Go-Live. For a row with a Go-Live Date, copy the row's `answers_filter` into `get_answers`, set `since` to that date, and add `named: true`. Write `total`.
6. Above the table, write the counted period from `counted.window`: the `rule`, then `from` and `to` as dates, then the number of scans in `counted.scans`.
7. Sort by Answers Citing It, largest first.

## Refresh the sheet

Do this when the person asks to refresh or update the sheet.

1. Read the Page column. Call `get_sources` with `page_urls` for those pages, 50 in each call. Do it for both question scopes.
2. Match each returned row to a sheet row by `url`. Rewrite only the Frontmost AI columns and the two calculated columns.
3. Keep every other cell as the person typed it. Keep the row order.
4. A page in `not_found` keeps its row. Write "No current read" in Lists You.
5. Call `get_sources` with no `page_urls`. Add a row for each page in `pages_to_get_on` that the sheet does not have.
6. Rewrite the counted period above the table.

## Rules

- A page with `you` equal to Check needed is not confirmed. Never tell the person to pitch it before a check.
- Report each count with its total, such as "16 of 160 answers".
- Keep the two question scopes in two columns. Never add them.
- "Answers Naming You Since Go-Live" shows what happened after the date. It does not prove that the listing caused it. Say so once below the table.
- Say the date in `checked_on` when it is more than 7 days old.
- Never suggest paid links, fake reviews, fake accounts, or a promised result. A quote for a sponsored listing is the person's decision, and the page must label it as sponsored.
- Ask before you change anything in Frontmost AI. This sheet reads only.

## Output

A spreadsheet file with one table, the counted period above it, and a link to the `url` of the Sources tab. If the AI app cannot make a file, return the same table as CSV.
