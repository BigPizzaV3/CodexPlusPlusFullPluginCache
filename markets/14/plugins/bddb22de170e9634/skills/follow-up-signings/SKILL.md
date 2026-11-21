---
name: follow-up-signings
description: Follow up documents that are out for signature in sajn — who has opened or signed, reminders, deadline extensions, withdrawal, and changing parties on sent documents. Use when the user asks about signing status or wants to nudge or manage an in-flight document.
---

# Follow up in-flight signings

## Workflow

1. **Locate and read status first.** `findDocumentsByParty` (by person) or `findDocuments` / `listDocuments` with status PENDING, then `getPartyActivity` for who has opened, read, and signed. Answer status questions from this — do not guess.
2. **Reminders.** `sendDocumentReminder` targets one party, works only while the document is PENDING, and emails them immediately. Confirm with the user before sending, and never remind a party who has already signed.
3. **Deadlines.** `extendDocumentExpiration` is for sent documents and emails every party about the new date. `setDocumentExpiration` is for drafts only.
4. **Changing parties on a sent document.** `addPartyToSentDocument` and `removePartyFromSentDocument` alter the live signing process and notify people — state the consequence and confirm before calling. A party who has already signed cannot be removed; the document must be withdrawn instead.
5. **Withdrawal.** `withdrawDocument` returns the document to draft and notifies all parties. Use it when content must change after sending — then re-send.
6. **sajn's own suggestions.** `listActions` lists follow-ups sajn already proposes (reminders, extensions, renewals). Prefer acting on an existing card over inventing a parallel action; `dismissAction` is permanent, `snoozeAction` is temporary.

## Validation

After any action, re-read `getPartyActivity` or `getDocumentDetails` and report the new state to the user.
