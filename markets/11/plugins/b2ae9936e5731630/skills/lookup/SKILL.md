---
name: lookup
description: Use when the user asks, about their own Nexusplus contacts, who they know at a company, what a saved contact's phone number, email, address or employer is, how two of their contacts are connected, when one of their contacts last changed or where its details came from, or which accounts are connected to Nexusplus. Do not use for general questions about public figures or companies (for example who someone works for) that are not about the user's own contacts.
---

Answers questions about the user's own saved contacts from tool results only.

Input to expect: "who do I know at Acme", "what's Sheila's number", "when did we last change this contact", "where did this email come from", "what accounts are connected".

Steps:

1. Call `list_my_lists` once. If there is more than one contact list, ask which one, or search each, and pass `listId`.
2. To find a person or company, call `search_contacts` with a name or email fragment; `entityType` (person or company) narrows it. To browse or filter, call `list_contacts` with `search`, `entityType`, or `needsReview` for contacts the system flagged for review. Only active contacts are listed unless `statuses` says otherwise. When `hasMore` is true, say there are more than you showed.
3. If more than one person fits, show them with something that tells them apart (company, email) and ask which. Never pick one silently.
4. For details, call `get_contact_dossier` and answer only from it: emails, phones, addresses, roles and links as labeled, and `intents` for why the user added the person. If a field is not there, say it is not recorded. Never infer or fill in a number, email or employer from memory or from a similar contact.
5. "Who do I know at a company": find the company with `search_contacts` (`entityType: company`), then call `get_relationship_network` with its `masterId` as `entityId`. The people connected to it by an employment relationship are the answer. For how two people are connected, run it on one of them and look for the other. Former links are left out unless `includeRetired` is true; say which you used. Say the answer reflects the relationships recorded in Nexusplus, not everyone who may work there.
6. "When did this change": call `get_contact_versions`, which gives published and earlier versions with a state, `publishedAt` and `createdAt`; add `includeAllRevisions` to include unpublished changes. "Where did this come from": call `get_contact_sources`, which shows the Outlook, iCloud or CSV records behind the contact and their sync status.
7. "What is connected": call `list_integrations` for each connected account's name, type, status and last sync. Credentials are never shown.
8. If the dossier reports a mixed-identity diagnostic, tell the user the record may combine two people and offer the duplicate-review skill.

Output: a short plain answer naming the contact list and the contact, quoting values exactly as recorded, and saying when something is not recorded.

Stop and ask when a search returns several plausible people, when the user has several contact lists, or when the question needs data the tools do not return.
