---
name: duplicate-review
description: Use when the user asks whether their Nexusplus contacts contain duplicates, whether two of their contacts are the same person, wants to clean up or merge their saved contacts, wants to dismiss a suggested duplicate, or says a merge of their contacts was wrong and wants it undone or two people separated. Not for deciding whether two public figures or companies are the same.
---

Finds contacts that may be the same person and resolves them, without ever merging on a guess.

Input to expect: "do I have duplicates", "are these two the same person", "merge them", "that merge was wrong".

Steps:

1. To review the queue, call `list_duplicate_candidates` (proposals awaiting review by default). For one named person, find them with `search_contacts`, then call `find_duplicate_candidates` with their `masterId`. Each pair has a match type (email, phone or name) and a confidence. Describe pairs in plain words ("these two share an email address") and show a few at a time.
2. Confidence is never a decision, and merging is always the user's explicit choice. A pair whose reasons include `name_disagreement` shares an identifier but the names plainly differ; treat it as probably two people.
3. If two contacts have in common only a shared address, an office or main phone line, or a surname, say they may well be different people and do not propose a merge. A father and son who share a name and an address (one with a Jr. suffix), and a married couple who share a surname and an address, are different people.
4. For a pair worth considering, call `merge_preview` with both `masterIds` and show what would be combined: the names, company, emails, phones and sources of each, which contact would be kept and which retired into it. Let the user choose which to keep. If `mergeToken` comes back empty, do not merge; relay the note.
5. Merge only after the user says yes to that preview. Call `merge_contacts` with `primaryMasterId` (kept), `secondaryMasterIds`, the preview's `mergeToken` and a one-sentence `reason`. The token lasts about ten minutes and goes stale if either contact changes; if it is refused, preview and confirm again. Merging needs admin access to the contact list; if refused for access, say so.
6. The merge is applied within a few seconds, so re-read with `get_contact_dossier` before saying it is done. A merge changes nothing in the user's connected Outlook or iCloud accounts until the merged contact is published (see the publish-and-destinations skill). Offer to publish; do not publish unasked. Before publishing a merged contact, say this plainly: if a connected account holds a card for each of the two contacts, the absorbed contact's card will be deleted from that account when the surviving contact is sent there (Nexusplus marks it as superseded first), and a later scheduled sync can do the same. The same publishing rule as everywhere applies: say what will leave Nexusplus and to which accounts, and wait for the user's yes.
7. If they are different people, call `dismiss_duplicate_candidate` with both ids and a short `reason` ("father and son, same address") so the pair does not come back. There is no call to undo a dismissal; the pair can still be merged later if the user changes their mind.
8. To undo a merge, call `unmerge_contact` with the survivor's `masterId`. It works only for a clean, recent merge of two contacts with no edits to the survivor since, and refuses anything else with the reasons. If the merge was already published and the absorbed contact's card was deleted from a connected account, say so first: the contact comes back in Nexusplus, but its old card and any edits made to that card are not restored, and it gets a new card the next time it is published (the unmerge is refused if that account does not accept new contacts of that type).
9. For a contact that holds two people's records, call `get_contact_sources`, show which records belong to whom, then call `split_contact` to move one person's records onto an existing, separate contact (every record must be assigned). A split needs that second contact to exist already as the target. If none exists, do not try to create one with `create_contact`: it may refuse because the new person's details match the conflated contact. Say so, and ask the user to create the separate contact in the Nexusplus app first, then continue. Merge, unmerge and split need admin access to the contact list.

Output: what was compared, what you did or did not change, and what the user can do next.

Stop and ask when the user has not confirmed the preview, when the preview shows conflicting identities, or when a pair has only a shared address, line or surname in common.
