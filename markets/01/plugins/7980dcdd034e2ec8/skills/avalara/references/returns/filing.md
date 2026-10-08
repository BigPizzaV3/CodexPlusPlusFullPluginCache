# Managed Returns: reconcile, approve, file

Liability worksheet reports are available only to Managed Returns subscribers and must be
exported. See [reports](../avatax/reports.md).

## Sequence

The documented order is reconcile, resolve, then approve.

1. Compare totals between Avalara and the user's business records.
2. Isolate variance using progressively more detailed reports, starting from the liability
   worksheet.
3. Explain differences, including dates, filters, refresh delays, and location codes.
   Propose changes only when supported by the user's facts and approved treatment; do
   not alter transactions just to make totals match. Authorized corrections are AvaTax
   operations; see [transactions](../avatax/transactions.md).
4. Approve only once discrepancies are resolved.

Approval exists at more than one granularity: a single region, or all regions at once,
each with a corresponding undo path. Approving all regions is a materially larger action
and must be restated as such, never folded into a single-region approval.

## Traps

- **Leaving a return unapproved may not hold it.** Managed Returns can approve
  automatically at the cutoff. Check the selected account's automation and return status;
  if the user wants to prevent filing, explain the supported hold or support path and
  obtain authorization before changing anything.
- **Read the current cutoff and time zone.** Use the page or current official help,
  not a remembered monthly deadline. Do not promise a hold after the relevant window.
- **Undo is narrower than approve.** The undo window closes before the approval deadline,
  not at it, and only works while Avalara has not started filing that region. Undo also
  applies to a whole region, so undoing one return out of several is not something the
  interface offers. Once that window has passed the route is a support case. Say that
  rather than retrying.
- **The monthly rhythm is mostly outside the portal.** New filings are added before the
  period they cover; changes to scheduled filings, including filing frequency, must land
  before the period closes; review and approval happen early in the following month;
  funds are pulled after the cutoff; filing runs through the rest of the month;
  confirmations arrive the month after. A change requested "now" may be too late for the
  current period and early for the next. Check which period it lands in before promising
  an effect, and check the current deadline with support rather than quoting one.
- **Recalculation temporarily disables approval controls.** When returns for a state are
  being recalculated, approval and undo-approval are unavailable. Manually adding or
  editing transactions for that state is one of the triggers. This is expected behavior,
  not a fault and not a permissions problem. Report and wait rather than retrying or
  looking for another route.
- **Approval can authorize remittance.** Funds are pulled after approval. Restate approval
  and payment as one consequence even though they are separate screens. The pull is a
  scheduled batch in the days after the cutoff, not something the approval click triggers
  on the spot, so do not tell a user money has moved because they approved.
- **Location-code mismatches can produce a $0 return.** Compare transaction location
  codes with the return's expected codes when totals are unexpectedly low. Report the
  evidence and ask the tax owner to verify; do not certify a return as correct or wrong.
- **Credits can explain a missing filing.** Check visible carryover credits and the
  jurisdiction's return treatment before treating an absent filing as an error.

## Funding

Approval decides what gets filed. A separate arrangement decides whether the money can
actually move, and it fails quietly.

Avalara withdraws funds under a funding power of attorney. Only one is active at a time,
it has to be submitted before a dated deadline to cover a given filing period, and it can
stop being valid without anyone doing anything: repeated failed debits expire it, and
Avalara then switches the account to wire transfer until a new one is submitted.

Approval alone does not establish that funding is in place. When the task involves
money moving, check the visible funding arrangement and report its status separately
from the return approval and any eventual payment confirmation.

For requested funding changes, prepare supported steps to review and apply [SKILL.md](../../SKILL.md)'s
confirmation requirements. Signing a power of attorney and entering banking credentials
belong to the user in the browser. Verify current deadlines; when the workflow requires
an account manager or support case, explain that route and draft the request if useful.

## Before approving or submitting

Restate: company, return or transaction identifiers, period, jurisdictions, amount and
currency, destination or masked funding account, scheduled date, and any automatic
downstream consequence visible on the page. Then apply the approval protocol in [SKILL.md](../../SKILL.md).

Do not sign attestations, accept a power of attorney, or make declarations requiring the
user's personal certification. Hand those to the user in the browser.

## Amendments and backfiling

These workflows can require Avalara support rather than a self-service portal action.
The documented path is a request through the user's
account manager, or a support case containing the information Avalara requires for that
request type. The required detail differs by category, including returned or refunded
products, non-taxable products, exemptions, and additional tax due.

The user reviews and approves a funding summary, funds are debited for the approved
remittance, and the amended or backfiled returns become downloadable afterward.

**Traps:**

- **Do not reconstruct an amendment through transaction edits.** Locked transactions
  cannot be edited anyway, and editing around them creates a mismatch between what was
  filed and what the account shows.
- **Drafting does not authorize sending.** Prepare the content for review. Open a support
  case or contact an account manager only with explicit authorization covering that action.
- **An empty amended view is not proof of success or failure.** Check the request history
  and selected company/period; reports can distinguish original and corrected versions.
