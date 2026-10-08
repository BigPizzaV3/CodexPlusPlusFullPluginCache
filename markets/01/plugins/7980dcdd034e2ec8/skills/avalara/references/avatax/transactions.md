# AvaTax: transactions

Navigation: Transactions > Transactions. Import history lives at Transactions >
Transaction import history.

## Status model

Status determines whether a transaction appears in reports and whether it is filed. Four
statuses are visible in the interface:

| Status | In reports | In returns | Notes |
|---|---|---|---|
| **Locked** | Yes | Yes | Finalized for return filing. Cannot be modified. |
| **Committed (unlocked)** | Yes | Yes | Ready for reporting and filing. Becomes Locked once reported on a tax return. |
| **Uncommitted** | Not by default | No | Not finalized. Can be included in some reports. |
| **Voided** | Not by default | No | Equivalent to deleted, retained for audit. Can be included in some reports. |

Further statuses appear only in API responses and display differently in the portal:
**Saved** and **Posted** both show as Uncommitted; **Canceled** shows as Voided;
**Adjusted** describes a modified transaction and can apply to any core status;
**Temporary** covers estimates that are never stored.

**Traps:**

- **Locked is caused by filing, not by the calendar.** A committed transaction becomes
  Locked when it is reported on a tax return. Never tell the user a period locks on a
  date. Read the status off the record.
- **Check document date and filing period before committing.** Today's commit does not
  necessarily put an earlier invoice in the current period. Inspect the document's dates
  and the affected return. Committing does not amend an already filed return; use the
  supported amendment path. Change a date only to correct it to the actual date supplied
  by the user or tax owner, never to move a transaction around a closed period.
- **"Uncommitted" in the portal covers several API states.** If the user is reading API
  data and you are reading the portal, you may be describing one record in two
  vocabularies. Say which you are looking at.
- **Voiding retains the transaction for audit.** It excludes the record; it does not
  erase it or amend a filed return. Certificate and customer deletion can be permanent,
  so do not carry this reassurance across products. See [certificates](../ecm/certificates.md).

## Void one transaction

Requires account administrator permission and consequential approval for the exact
records and filing impact before saving.

1. Transactions > Transactions, filter to the transaction, select it.
2. Select Change status, then VOIDED.
3. Save. After refresh, the document status column shows Voided.

## Update one transaction

1. Transactions > Transactions, open the document code.
2. Inspect the existing fields and apply only the requested changes. For a recalculation,
   use Calculate tax where available and inspect the preview.
3. Before saving, confirm any change to committed or reportable tax under the approval
   protocol. Save once and verify the summary, lines, and resulting document status.

Recalculating in AvaTax does not sync back to a connected business application. If the
user runs an integration, their system still shows the old tax until someone updates it
there. Say so rather than reporting the transaction fixed.

## Update or void many

Both run through the import template using the process code column, and only unlocked
transactions can be changed this way. A second route exports the sales tax document data
report, edits it, and re-imports it as a template.

Bulk void is an import: everything in [import](import.md) applies, including the company code
trap. Load it before proceeding.

## Traps specific to corrections

- Locked transactions cannot be edited. For a filed period the usual path is an
  amendment. See [filing](../returns/filing.md).
- A transaction backdated into a period that is already locked or filed is silently left
  off that return even if it remains editable. Check the filed version before claiming
  the correction was picked up. Explain the supported amendment request and required
  review. Do not move it into a later period merely to get it filed.
  See [filing](../returns/filing.md).
- Voiding to "clean up" test data in production is a real request. Restate exactly which
  document codes are in scope before acting.
- A transaction that calculated zero tax may reflect missing nexus rather than an
  exemption. See [nexus](nexus.md) before concluding anything about the record itself.
