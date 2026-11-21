---
name: capture-with-reason
description: Use when the user has just met someone and wants to save them to their Nexusplus contacts, or wants to add a new person or company to their contacts, and says why ("met at the conference", "a candidate for the sales role", "a competitor"), or asks you to add someone to their contacts and check that they are not already saved. Not for looking people up elsewhere.
---

Adds a brand-new contact together with the reason the user is adding it, so the record still explains how they know this person later.

Input to expect: a name or company, ideally an email address or phone number, and the reason in the user's own words.

Steps:

1. Collect what `create_contact` needs: at least one identifying signal. Any one of a first or last name, a company name (with `entityType: company` for a company), an email or a phone number is accepted, but a name alone cannot be checked reliably against the user's saved contacts. Ask for an email or phone when the user has one; if they have neither, say the check for an existing copy is weaker and continue only if they still want it. Never guess a missing email, phone, company or title.
2. If the user may already know this person, call `search_contacts` on the email or name first. If they are there, go to step 7 instead of creating.
3. Publishing rule (the same in every Nexusplus skill). `create_contact` publishes the new contact to the user's connected Outlook and iCloud accounts unless the contact list is set to hold changes for review or you pass `disposition: stage_for_review` (which holds it for the user's review instead). Before the call, say in one sentence what will leave Nexusplus and to which connected accounts (`list_integrations` names them). Wait for a yes only if the user has not already asked for it to go to their accounts: "add her and sync it to my phone" is such a request, a plain "add her" is not.
4. Call `create_contact` with the name or `companyName`, the `email` or `phone`, and `title` only together with `companyName`. For the why, pass `intent.kind` as the closest of lead, competitor, partner, vendor, candidate, investor, press or other (use other when none fits; never invent a kind), `intent.source` for where it happened ("conference"), and `intent.note` and `reason` as one short sentence each, at most 200 characters, never the conversation. Pass `destinations` only if the user named where it should go (see the publish-and-destinations skill).
5. A successful call returns `outcome: created` and `pending: true`. The contact appears within a few seconds and `masterId` is still empty. Read `disposition`: `accept_now` will publish to the connected accounts, `stage_for_review` waits as an unpublished change for the user's review, and `degradedFromAcceptNow` means the user's access does not allow publishing, so it was held for review. Find the contact with `search_contacts` and confirm with `get_contact_dossier`: `intents` shows the kind and note, `destinations` shows where it goes. Do not say it is done until the dossier shows it.
6. A weaker match with a saved contact is not visible in the create result: it comes back as `outcome: created` like any other. After a create, call `list_duplicate_candidates` to learn whether the new contact was filed as a possible duplicate. If it was, its publishing is held until the pair is resolved: say so and follow the duplicate-review skill.
7. If the result says `outcome: matched_existing`, no contact was created and nothing was recorded. Tell the user who already matches (`match` has the name, match type and confidence) and that you did not make a second copy. To add the new email, phone or company to that person, use the edit-contact skill (`submit_contact_revision` with the `masterId` and `addAttribute`, one attribute per call); it follows the same publishing rule. This capture's reason cannot be attached to an existing contact; tell the user, and do not put it in `fields.notes`, which replaces the existing notes.

Output: a plain confirmation naming the contact, the reason recorded, and whether it was sent to the connected accounts or is waiting for review.

Stop and ask when neither a name nor an email or phone is available, when several saved contacts could be the match, or when the user has more than one contact list and has not said which.
