# AvaTax: import

Navigation: Transactions > Import transactions. A legacy import path also exists. Check
results at Transactions > Transaction import history.

Requires account administrator permission. Account Viewers cannot import, though they can
view import history, so a Viewer can confirm what an earlier import did.

## Sequence

1. Download or select a template.
2. Populate it, including the process code in column A.
3. Map columns if using a custom template.
4. Verify the batch, automatic commit behavior, and approval before uploading.
5. Check import history, then download the error file for any failed rows.

## When the user supplies their own file

A business-system export may lack process codes or use different column names. Inspect
the actual file and selected template rather than assuming it is ready for import.

Before mapping, establish the following from the request and file; ask only for missing
decisions:

1. **Are these new transactions or changes to existing ones?** This decides odd versus
   even process codes. Creating when the user intended corrections can produce duplicates
   or document-code conflicts rather than changing the intended records.
2. **Does the file identify existing records?** Adjustments need the document code and
   document type of the record being changed. A file lacking them does not fail safely.
   An adjust code with nothing to match against creates a new transaction, so a
   corrections file missing its identifiers produces a duplicate per row and reports
   success.

Map the file into the template and explain the chosen process codes. Validate before
upload. A pilot upload changes records too: use it only when authorized, identify its
complete documents, and exclude successful pilot records from the remaining batch.

## Process codes decide the operation

Column A is not metadata. It determines what the import does to each row:

| Process code | Effect |
|---|---|
| 0 | Void the transaction. Requires document code, document type, and company code. |
| 1 (new) / 2 (adjust) | Override the tax amount. Avalara does not calculate; it back-calculates the taxable amount from the tax you supply. |
| 3 (new) / 4 (adjust) | Calculate tax in AvaTax from the amount. |
| 5 (new) / 6 (adjust) | Accrued consumer use tax override. |

Additional codes vary by template. Use codes such as 9 or 10 only when the selected
template or current official help defines their effect; never infer behavior from parity.

For the paired codes above, odd creates and even adjusts. Verify that the selected
template supports them. Three failures follow from a mismatch:

- **An override where a calculation belonged.** Override codes can change how tax and
  taxable amounts are derived and reported. Verify supplied tax and amount fields against
  the template. Codes 3 and 4 request calculation; 5 and 6 are overrides too, not merely
  reporting labels. Do not choose an override without the user's supplied basis.
- **A create code on corrections.** Rows can create unwanted transactions or conflict with
  existing document codes. Verify document type and identifiers before choosing a code.
- **An adjust code that finds nothing to adjust.** This does not fail. When a code of 2,
  4 or 6 has no matching transaction, AvaTax can add a new one instead. The import
  reports success and you get the same duplicates by the opposite route.

Read the process codes present in the file before importing, and restate them as part of
the approval request.

## Verify before importing

Environment, account, destination company **and every value in the file's company code
column**, file name, row and document counts, document identifiers/types, column mapping,
template, process codes, supplied overrides, validation results, and automatic commit or
filing-period effects. Every destination company must be within the approved batch.

## Traps

- **The file overrides the company selector.** Rows carrying a value in the company code
  column go to the companies named in the file, not the company selected on screen. The
  selector governs only rows where that column is blank. Verifying the on-screen company
  is therefore not sufficient. Open the file and check the column. This is the most
  likely way an import lands in the wrong entity.
- **A tax override needs nexus.** Importing an override for a jurisdiction with no active
  nexus fails, and the transaction date must fall within the nexus start and end dates.
  See [nexus](nexus.md).
- **Keep pilots bounded.** A sandbox validation or explicitly approved subset can reduce
  risk. Approval of a pilot alone does not cover the full batch. Keep all line items for
  each document together; never re-import successful pilot records as part of the full file.
- **File and document limits differ.** Check current row, column, and per-document line
  limits in the selected template or visible help. Do not split a document to evade a limit.
- **Error files can omit source columns.** Reconcile import history, successful records,
  and failed rows back to the original file; an absent error-file column proves nothing.
- **Never re-run an import whose outcome is unknown.** Check import history first, then
  ask.
