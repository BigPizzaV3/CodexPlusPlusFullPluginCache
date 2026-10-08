# Consequential actions

Read this before any write. The approval protocol itself is defined in [SKILL.md](../SKILL.md); this
file only says where it applies.

## The state ladder

AvaTax transaction statuses run:

```
Uncommitted → Committed (unlocked) → Locked
                                       ↑
                    reported on a tax return
```

`Voided` sits outside the ladder: it excludes a transaction from calculation and returns
while retaining it for audit. Some reports can include voided records when filtered by
status. A void does not erase a record or amend a return that was already filed. Do not
carry this retention behavior over to certificate or customer deletion.

Two rules follow:

**Authorization must cover the actual downstream effect.** A routine save request does
not authorize a commit. Committing makes a transaction reportable, and worksheet approval
can authorize filing and remittance together. Explain and obtain approval for that combined
effect before clicking; do not assume a separate filing or payment prompt will follow.

**Locked records require the supported correction path.** Read the actual transaction
and filing status; do not derive editability from the calendar. Do not edit around a lock.
A filed return may require an amendment through Avalara support.

Full status detail, including the API-only statuses that display differently in the
portal, is in [transactions](avatax/transactions.md).

## Actions requiring approval

Apply [SKILL.md](../SKILL.md)'s authorization rule to the actions below. Reuse existing explicit approval
when it covers the same details and consequences. Routine requested edits may use the
authorization already in the request. For an unlisted action, inspect its effect: tax,
filing, funding, destructive, access, or automation changes need approval of that effect.

| Action | What actually changes | Restate before asking |
|---|---|---|
| Commit a transaction | Becomes reportable; can flow into a return | Document IDs, current state, amounts, period, whether it enters an open filing period |
| Adjust a committed transaction | Alters reportable tax; does not itself amend a filed return | Document ID, before and after amounts, period, jurisdictions, filing status of that period |
| Void a transaction | Excludes it from calculation and unfiled returns; retained for audit and some status-filtered reports. Requires admin | Document codes and types, current status, amounts, what depends on it |
| Import a batch | Creates, adjusts, overrides tax on, or voids many records at once depending on process codes | Destination company **and the file's company code column**, file name, row count, column mapping, **the process codes present**, validation errors |
| Override tax on an import | Replaces Avalara's calculation with a supplied figure; verify supported process codes in the selected template | Which rows carry an override, the supplied amounts, and the user's basis for overriding |
| Change a tax code or exemption | Changes calculated tax going forward and sometimes retroactively | Record, current value, proposed value, the user's stated basis for it |
| Clear a certificate's invalid flag | Can make the certificate eligible to exempt transactions, depending on account settings and dates | Customer, certificate, the recorded invalid reason, the user's basis for considering it valid |
| Turn off parent settings inheritance | Detaches a child company from centrally managed settings | Company, parent, which fields become independently editable |
| Add, edit, or end-date nexus | Changes tax calculation; can affect filing obligations and related setup | Jurisdiction, effective date, current setting, visible filing impact; do not assume it registers or schedules a return |
| Change a filing frequency | Changes what gets filed, when, and whether automatically. Users call this the filing calendar | Returns affected, frequency, first filing period, automation settings |
| Approve returns for a region | Authorizes filing, and funds are pulled after approval | Company, region, return IDs, period, total amount and currency, what approval triggers on this screen |
| Approve returns for all regions | Same, across every region at once | Everything above, plus the region count and combined total. Never fold this into a single-region approval |
| Submit, file, or amend a return | Files with a tax authority | Everything above, plus submission date and whether it is an original or amendment |
| Schedule or release a payment | Moves money | Amount, currency, masked funding account, destination, scheduled date |
| Change banking or funding details | Redirects money | Current masked value, proposed value, which filings it affects |
| Change user access or roles | Changes who can do all of the above | User, current role and company scope, proposed role and scope |
| Change integrations or notifications | Changes data flow out of the account | Integration or recipient, current state, proposed state |
| Enable any automation | Removes the human from future consequential actions | What becomes automatic, from which period, how to reverse it |
| Delete a certificate or customer record | Can permanently remove linked data; deleting a primary multijurisdictional certificate can delete the group | Records and linked jurisdictions, current status, visible deletion effect, and recovery limits. For stopping exemption, discuss a supported pause or invalidation instead; it needs its own authorization |
| Change a company's status | An inactive company stops calculating tax, and Returns can neither generate reports nor file for it | Company, current status, proposed status, and that tax and filing stop for that entity |
| Expire a return | Cannot be reversed. Filing again means setting up a new return | Which return, which period it last covers, and that this is one way |

## Actions that do not require approval

Reading, filtering, opening a record, and generating a report within the scope the user
already requested. These still follow the scope rules in [context verification](context-verification.md) and
the handling rules in [data handling](data-handling.md).

A report the user asked for is a read. Emailing it, scheduling recurring delivery, or
uploading it elsewhere is not.

## Labels that mislead

- **"Approve"** on a worksheet or return can start filing and remittance. The word is
  mild; the effect is not.
- **"Save"** on some screens also commits. Check the screen before assuming it is a
  draft operation.
- **"Change status"** is the void control on the transactions page. It reads like a
  filter or a display setting and is neither.
- **"Delete" is product-specific.** Voiding retains a transaction for audit; explain that
  distinction when a user asks to delete one. Certificates and customers can delete
  permanently, including linked jurisdictions. Inspect the product's warning rather than
  assuming transaction retention applies to ECM. See [certificates](ecm/certificates.md).
- **The process code column** in an import template is the most consequential field in
  the file and looks like a reference number. See [import](avatax/import.md).

When a control's effect is not clear from the page, say what is unclear and ask rather
than clicking to find out.

## Inaction as a consequential act

Managed Returns can approve returns automatically at a published cutoff. Verify the
selected account's automation, return status, deadline, and funding arrangement; leaving
a return unapproved may still result in filing and a scheduled funds pull.

Check the following:

- When the user's goal is to prevent or delay a filing, say that this requires positive
  action before the cutoff. Never let "we'll leave it for now" stand as if it holds the
  return.
- Read the current cutoff and its time zone from the page or current official help.
  Do not use a remembered monthly deadline or imply that waiting holds the return.
- Undoing an approval closes earlier than the approval deadline itself, and only works if
  Avalara has not already started filing that region. Undo is also region-wide, so
  "undo just that one return" is not something the interface offers. Once the window has
  passed, the route is a support case, not a retry.

## Locks, closed periods, and filing windows

Locks are real state, not permissions problems, and retrying never clears them:

- **Locked transactions.** Locked records cannot be edited or bulk-updated through the
  ordinary workflow. Read the record and return status rather than deriving a lock from
  the date. A filed return may need an amendment; verify current support requirements
  rather than assuming an unlock is available.
- **Recalculation in progress.** When Avalara is recalculating returns for a state,
  approval and undo-approval are temporarily unavailable. Manually adding or editing
  transactions for that state is one of the triggers. Report the visible processing state.
  It does not establish that the filing deadline is extended; verify the scheduled effect.
- **"Dirty" jurisdiction status.** The jurisdiction is still processing. Inspect the
  current status and deadline rather than retrying the action or assuming a completion time.

Never work around a lock by editing an adjacent record, using a different company,
backdating a document, or reopening a period. Explain what is locked and why, describe
the supported path (an adjustment, an amendment, or a support case), and draft what
would be needed if that helps.

## Failures, timeouts, and retries

Never automatically retry a consequential action whose outcome is unknown. Imports,
filings, and payments can complete server-side after the interface gives up, and a
duplicate filing or double remittance is far worse than a delay.

On failure or ambiguity:

1. Narrowly inspect the affected record or the relevant activity history.
2. Report what is confirmed, what is uncertain, and what evidence you used.
3. Do not retry while the outcome remains uncertain. If noncompletion is established,
   confirm the intended retry and any changed details before repeating a consequential
   operation. A successful partial batch must not be submitted again with its failed rows.
