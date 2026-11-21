---
name: find-document-or-permit
description: Use when someone asks for a document, license, permit, lease, certificate or insurance record at one of their Locations in Binto, by the Location's name or address, or asks when one expires.
---

# Find a document or permit at a Location

Answer from Binto records only. Everything here is read-only.

1. If you do not know which Organization the person means, call `organizations_list`. With one Organization, use it. With several, ask which one, then pass its `id` as `organizationId` on every call.
2. Work out the Location. Call `location_resolve` with the person's own words (a name, a Location Code, a street address or a city). If it returns more than one match, ask which one.
3. Call `document_find` with that `locationId` and the words they used (for example "health permit" or "lease"). Use its filters for questions such as "what expires in the next 30 days".
4. For one document, call `document_get` with its `documentId` to read its dates, category, notes and versions.
5. If they ask what a document says (a clause, an amount, a name inside it), call `document_search` with their words and the `documentId` or `locationId`.

When you answer:

- Name the document by its title and its Location, and give the expiration date when the result has one.
- Cite each record from `sources`, and include its link from `links`. Links open in Binto and need the person to be signed in.
- If nothing is found, say that nothing was found that this person can open. Do not suggest that a document exists but is hidden.
- Never guess a date or a permit number. Quote what the result contains.
