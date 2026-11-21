---
name: tax1099-payer
description: Create or update Payers in Tax1099 without sending TINs, and check pending Payer status. Use when the user wants to add a Payer, update an existing Payer, or find out whether a pending Payer's TIN has been entered.
---

# Tax1099 Payers

| Task | Tool |
|---|---|
| Create or update one or more Payers (no TIN) | `savePayer` |
| Check whether a pending Payer's TIN has been entered | `getPendingPayer` |

## Creating a Payer

1. Collect name, address, country, phone and `idType` (Business or Individual). Never ask for the TIN.
2. Call `savePayer` without `tpid`. Each Payer comes back pending with an `idEntryUrl`.
3. Show the `idEntryUrl` to the user: they sign in to Tax1099 and enter the TIN there.
4. Later, call `getPendingPayer` with the `pendingPayerKey`. When `idStatus` is `Provided`, the Payer's `id` and `tpid` are returned.

## Updating a Payer

Call `savePayer` with the Payer's `tpid` and `isUpdate: true` plus the fields to change. The TIN on file is kept.

## Handling information

- Never collect or repeat a TIN in the conversation.
- Only supply the fields each tool defines. The tools reject anything else.
- If a call fails, report the error code and request ID to the user.
