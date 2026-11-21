---
name: ownerrez-account
description: Use the connected OwnerRez account to find and manage bookings, guests, properties, and other vacation-rental data, or answer OwnerRez API and support questions.
---

# Work with an OwnerRez account

Every account tool is limited to the account the user authorized. Follow this discovery ladder:

1. For structured lists of bookings, guests, or properties, use `entity_list`. For one known numeric ID, use `entity_get`. Do not guess IDs; find them with `entity_list` or `search`. Ask `schema` for a type's available filters and fields if needed.
2. For a name, email, phone, reservation code, or listing number, use `search`, then `fetch` with a typed ID from its results. Use `entity_get` with selected fields when a fetched document is too large. Up to five spelling variants can be comma-separated in one `search` query.
3. For an OwnerRez API v2 operation, inspect `schema` before `api_get` or `api_write`. `schema` can list tags, show a tag's operations, detail an operation, or show an `entity_list` type. `api_docs_search` can locate an operation by keyword when its name is unknown.
4. Use `api_get` for a `/v2/` read. It changes nothing. Use `api_write` only for an intended POST, PATCH, PUT, or DELETE to `/v2/`. Check the operation and JSON body shape first, explain the specific change, and ask the user to confirm before sending it. `api_write` requires full scope; if the connection is read-only, explain that full scope is needed and stop. Send a write once. If the response is truncated, read the record with `api_get`; never repeat a write to retrieve its response.
5. Use `api_docs_search` for API how-to questions and `support_docs_search` for product setup, behavior, or troubleshooting. Cite the returned documentation links when answering.

Lists default to 20 concise items and can request at most 100. Use `response_format: "detailed"` for the full API payload, `fields` for specific fields, or `count_only` for the filtered count. For booking arrivals, `from` and `to` select overlapping stays in the property's timezone; filter returned arrival dates and omit `is_block` rows. Booking lists require `property_ids` or `since_utc`; guest lists require a query or date filter. Follow tool errors, which state what to change.
