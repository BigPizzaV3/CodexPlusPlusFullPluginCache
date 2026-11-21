---
name: get-started
description: Use when the user has just connected Nexusplus, asks what Nexusplus can do with their contacts, or asks about a person or company in their own Nexusplus contacts, a possible duplicate among those contacts, or a change to one of those contacts, for the first time in a conversation. Do not use for general questions about people or companies that are not about the user's own contacts.
---

Nexusplus holds the user's own contact lists, built from their connected Outlook, iCloud and CSV sources, with one record per person and a full history of every change.

Input to expect: a question about a person or company in the user's own contacts ("who do I know at Acme", "what is Sheila's current number"), a request to add a new contact with a reason, to fix a duplicate, to change a saved contact, or to add an email or phone to someone already saved.

Steps:

1. Call `list_my_lists` once to learn the user's contact lists. If there is exactly one, every other tool may omit `listId`.
2. To answer a question, use `search_contacts` or `list_contacts`, then `get_contact_dossier` for the full record. Report only what the tools return; never infer a phone number, email or employer that is not in the record.
3. Before any change, find the contact and read its dossier. A write records the change and Nexusplus applies it within a few seconds; re-read the dossier to confirm the result instead of assuming it. Only `set_contact_destinations` takes effect immediately.
4. Pick the skill for the job: `capture-with-reason` to add a new contact, `edit-contact` to change a saved one, `duplicate-review` for duplicates, merges and splits, `publish-and-destinations` for what goes to the user's Outlook and iCloud accounts, and `lookup` for questions.
5. Publishing rule (the same in every Nexusplus skill). `publish_contact` sends changes to the user's connected Outlook and iCloud accounts, and so do `create_contact` and `submit_contact_revision` unless the contact list is set to hold changes for review or you pass `disposition: stage_for_review` (which holds the change for the user's review instead). Before any call that will publish, say in one sentence what will leave Nexusplus and to which connected accounts (`list_integrations` names them). Wait for a yes only if the user has not already asked for this add or edit to go to their accounts: "add her and sync it to my phone" is such a request, a plain "add her" is not. Ask before publishing more than a few contacts at once.
6. When a tool accepts `reason`, pass one short sentence in the user's own words about this action ("met at the conference"), never the conversation.

Output: a plain answer grounded in the tool results, naming the contact list and the contact, and for a change, what was recorded and whether it will be sent to the user's accounts.

Stop and ask when a search returns several plausible people, when a merge preview shows conflicting identities, or when the user's request would publish to accounts they have not named.
