---
name: edit-contact
description: Use when the user wants to change something about a person or company already saved in their Nexusplus contacts: a new phone number or email, a new job or employer, a spelling or name correction, a birthday, notes, or tags ("Sheila's new number is...", "she moved to Acme", "fix the spelling of his name"). Not for adding a brand-new contact.
---

Changes a saved contact with `submit_contact_revision`, which either replaces a field's value or adds one new item beside the existing ones, and says plainly what stays, what changes, and what goes out to the user's accounts.

Input to expect: "Sheila's new number is...", "she moved to Acme", "fix the spelling of his name", "add a work email for him", "tag her as a client".

Steps:

1. Find the contact with `search_contacts`, then read `get_contact_dossier` for its `masterId` and current values. If several people fit, show them with something that tells them apart (company, email) and ask which; never pick one silently. If the person is not saved, use the capture-with-reason skill instead.
2. Choose the input that matches what the user said:
   - `fields` REPLACES the value of each field you pass: the name parts (`firstName`, `lastName`, `middleName`, `prefix`, `suffix`, `nickname`), `companyName`, `primaryCompany` (the employer shown on a person), `primaryTitle`, `birthday`, `anniversary` and `notes`. Use it for a spelling fix, a changed employer or title, or a birthday. Passing `null` for a field clears it. `fields.notes` replaces ALL existing notes, so read the current notes first and send the full new text, only what the user asked to record, never conversation text.
   - `addAttribute` only ever ADDS one new email, phone, address, role (`orgRole`) or web address per call; a social profile is a `url` with the matching `urlType`. It never replaces or removes anything: a new phone number or email sits beside the old one, and an item that is already there is skipped silently. If the user means "replace the old number", say that the new number will be added next to the old one and that the old one cannot be removed through the assistant; it has to be removed in the Nexusplus app.
   - `tags` adds and removes tags: `add` and `remove` are case-insensitive, adding a tag that is already there or removing one that is not changes nothing, and a tag named in both is removed.
   For "she moved to Acme", set `fields.primaryCompany` to Acme (and `primaryTitle` if the user gave a title). Tell the user exactly that: the employer shown on the contact changed; the assistant cannot end or remove other recorded roles, so if they want an old role removed or ended, that is done in the Nexusplus app.
3. Publishing rule (the same in every Nexusplus skill). By default the revision is published: it is sent to the user's connected Outlook and iCloud accounts and overwrites the matching fields of the record there, unless the contact list is set to hold changes for review or you pass `disposition: stage_for_review` (which holds the change for the user's review instead). Before the call, say in one sentence what will leave Nexusplus and to which connected accounts (`list_integrations` names them; `get_contact_dossier` shows where this contact goes). Wait for a yes only if the user has not already asked for this edit to go to their accounts: "fix his name and sync it to my phone" is such a request, a plain "fix his name" is not. A send can also delete extra cards for the same contact in an account (see the publish-and-destinations skill).
4. Call `submit_contact_revision` with the `masterId`, the change (`fields`, `addAttribute` and/or `tags`) and a one-sentence `reason` in the user's own words ("new job at Acme"). One call carries at most one `addAttribute`; make a separate call for each further email or phone.
5. A successful call returns `accepted: true`. The change is applied within a few seconds, so re-read `get_contact_dossier` and report what it shows; do not say it is done until the dossier shows it. Read `disposition`: `accept_now` is published to the connected accounts, `stage_for_review` waits as an unpublished change for the user's review, and `degradedFromAcceptNow` means the user's access does not allow publishing, so it was held for review.
6. Undo: earlier values stay in version history (`get_contact_versions`), so a wrong replaced field or tag change is corrected by revising again. An item added by mistake with `addAttribute` cannot yet be removed through the assistant; say so and send the user to the Nexusplus app.

Output: a plain confirmation naming the contact, what was changed or added, what stayed as it was, and whether it was sent to the connected accounts or is waiting for review.

Stop and ask when the contact is not clearly one person, when the user has more than one contact list and has not said which, when the new value would replace several existing values, or before replacing notes the user did not ask to overwrite.
